#!/usr/bin/env python3
"""Validate registry metadata, template paths, and approved upstream image refs."""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_REGISTRY_FIELDS = {
    "$schema", "name", "description", "version", "author", "url", "templates"
}
REQUIRED_TEMPLATE_FIELDS = {
    "id", "name", "description", "version", "author", "compose_url",
    "env_url", "documentation_url", "tags"
}
IMAGE_REFERENCE = re.compile(
    r"^(?:(docker\.io|ghcr\.io)/)?([a-z0-9][a-z0-9._/-]*):"
    r"([A-Za-z0-9_][A-Za-z0-9_.-]*)(?:@sha256:[a-f0-9]{64})?$"
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    registry_path = ROOT / "registry.json"
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"registry.json kann nicht gelesen werden: {exc}")

    if not isinstance(registry, dict) or set(registry) != REQUIRED_REGISTRY_FIELDS:
        fail("registry.json hat nicht exakt die von Arcane erwarteten Felder.")
    templates = registry.get("templates")
    if not isinstance(templates, list) or not templates:
        fail("Die Registry muss mindestens eine Vorlage enthalten.")

    approved_images = {
        line.strip()
        for line in (ROOT / "approved-images.txt").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }

    seen_ids = set()
    for template in templates:
        if not isinstance(template, dict) or set(template) != REQUIRED_TEMPLATE_FIELDS:
            fail("Ein Template-Eintrag hat nicht exakt die erwarteten Arcane-Felder.")
        template_id = template["id"]
        if not isinstance(template_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", template_id):
            fail(f"Ungültige Template-ID: {template_id!r}")
        if template_id in seen_ids:
            fail(f"Doppelte Template-ID: {template_id}")
        seen_ids.add(template_id)
        if not isinstance(template["tags"], list) or not template["tags"]:
            fail(f"{template_id}: tags muss eine nichtleere Liste sein.")

        compose_path = ROOT / "templates" / template_id / "docker-compose.yml"
        env_path = ROOT / "templates" / template_id / ".env.example"
        readme_path = ROOT / "templates" / template_id / "README.md"
        for path in (compose_path, env_path, readme_path):
            if not path.is_file():
                fail(f"{template_id}: Datei fehlt: {path.relative_to(ROOT)}")

        expected_compose_url = f"/templates/{template_id}/docker-compose.yml"
        expected_env_url = f"/templates/{template_id}/.env.example"
        if not template["compose_url"].endswith(expected_compose_url):
            fail(f"{template_id}: compose_url zeigt nicht auf die Compose-Datei dieser Vorlage.")
        if not template["env_url"].endswith(expected_env_url):
            fail(f"{template_id}: env_url zeigt nicht auf die .env.example dieser Vorlage.")

        compose_text = compose_path.read_text(encoding="utf-8")
        if not re.search(r"^x-arcane:\s*$", compose_text, flags=re.MULTILINE):
            fail(f"{template_id}: projektweite x-arcane-Metadaten fehlen.")
        if not re.search(r"^  icon:\s+https://", compose_text, flags=re.MULTILINE):
            fail(f"{template_id}: x-arcane.icon muss eine HTTPS-URL sein.")
        if not re.search(r"^  urls:\s*$", compose_text, flags=re.MULTILINE) or len(
            re.findall(r"^    - https://", compose_text, flags=re.MULTILINE)
        ) < 2:
            fail(f"{template_id}: x-arcane.urls braucht mindestens zwei HTTPS-Links.")

        images = re.findall(r"^\s*image:\s*([^\s#]+)", compose_text, flags=re.MULTILINE)
        if not images:
            fail(f"{template_id}: keine expliziten Image-Referenzen gefunden.")
        for image in images:
            match = IMAGE_REFERENCE.fullmatch(image)
            if not match:
                fail(f"{template_id}: Image {image!r} muss ein unterstütztes Registry-Image mit festem Tag sein.")
            registry, image_path, _tag = match.groups()
            if registry is None:
                registry = "docker.io"
                if "/" not in image_path:
                    image_path = f"library/{image_path}"
            canonical_image = f"{registry}/{image_path}"
            if canonical_image not in approved_images:
                fail(f"{template_id}: Upstream-Image {canonical_image!r} fehlt in approved-images.txt.")

    print(f"OK: Registry und {len(templates)} Template(s) geprüft.")


if __name__ == "__main__":
    main()
