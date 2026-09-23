# Contributing / Mitwirken

## English

1. Create a directory under `templates/<slug>/`.
2. Add `docker-compose.yml`, `.env.example`, and `README.md`. Document the app in English and German, including ports, setup requirements, persistent data, and links.
3. Add project-level `x-arcane.icon` and `x-arcane.urls` metadata to Compose. Use a working HTTPS icon URL plus the upstream homepage and source repository.
4. Add the template to `registry.json`. URLs must point to files on the `main` branch.
5. Verify that every image is published by its application upstream. Add its exact repository to `approved-images.txt`. Prefer Docker Hub; allow GHCR or an official vendor registry only when the upstream publishes there and has no suitable official Docker Hub image.
6. Check the Compose configuration against upstream documentation. Never commit real secrets or insecure default passwords.
7. Open a pull request and make sure the GitHub Actions checks pass.
8. Do not mount the Docker socket directly into an app container. Ask for review before proposing privileged mode or other host-level access.
9. Keep third-party licenses and notices separate. Do not copy upstream application code or full Compose files unless their license and required notices are preserved.

### Instructions for an AI

> Add the requested application as an Arcane Compose template. Prefer images published by the app's upstream project on Docker Hub; allow GHCR or an official vendor registry only when the upstream publishes its official image there and no suitable official Docker Hub image exists. Verify publisher and configuration against upstream documentation. Add `docker-compose.yml`, `.env.example`, and bilingual `README.md` under `templates/<slug>/`; include project-level `x-arcane.icon` and `x-arcane.urls`; add exact image repositories to `approved-images.txt`; and add the template to `registry.json`. Never commit real secrets or insecure default passwords. Make ports configurable and persist app data in named volumes or documented persistent paths. Do not mount the Docker socket directly or enable privileged/host-network access without explicit owner approval. Keep third-party licenses and notices separate. Run CI and submit a pull request instead of writing directly to `main`. If upstream image provenance or setup requirements cannot be verified, stop and report what is unknown.

## Deutsch

1. Ein Verzeichnis unter `templates/<slug>/` anlegen.
2. `docker-compose.yml`, `.env.example` und `README.md` ergänzen. Die App auf Deutsch und Englisch dokumentieren, einschließlich Ports, Setup-Anforderungen, persistenter Daten und Links.
3. Projektweite `x-arcane.icon`- und `x-arcane.urls`-Metadaten in Compose eintragen. Ein funktionierendes HTTPS-Icon sowie Homepage und Quellcode-Repository des Upstreams verlinken.
4. Die Vorlage in `registry.json` eintragen. URLs müssen auf Dateien im Branch `main` zeigen.
5. Prüfen, dass jedes Image vom jeweiligen App-Upstream veröffentlicht wird. Das exakte Repository in `approved-images.txt` freigeben. Docker Hub bevorzugen; GHCR oder eine offizielle Hersteller-Registry nur nutzen, wenn der Upstream sein offizielles Image dort veröffentlicht und kein passendes offizielles Docker-Hub-Image anbietet.
6. Compose-Konfiguration anhand der Upstream-Dokumentation prüfen. Keine echten Secrets oder unsicheren Standardpasswörter einchecken.
7. Pull Request erstellen und sicherstellen, dass die GitHub-Action erfolgreich durchläuft.
8. Den Docker-Socket nicht direkt in einen App-Container mounten. Privileged mode und andere Host-Zugriffe vorher zur Prüfung vorlegen.
9. Lizenzen und Hinweise Dritter getrennt beachten. Keinen Upstream-App-Code oder vollständige Compose-Dateien kopieren, ohne Lizenz und erforderliche Hinweise zu erhalten.

### Arbeitsanweisung für eine KI

> Ergänze die gewünschte Anwendung als Arcane-Compose-Vorlage. Docker-Hub-Images vom App-Upstream bevorzugen; GHCR oder offizielle Hersteller-Registries nur nutzen, wenn der Upstream sein offizielles Image dort veröffentlicht und kein passendes offizielles Docker-Hub-Image anbietet. Publisher und Konfiguration anhand der Upstream-Dokumentation prüfen. `docker-compose.yml`, `.env.example` und eine zweisprachige `README.md` unter `templates/<slug>/` anlegen; projektweite `x-arcane.icon`- und `x-arcane.urls`-Metadaten ergänzen; exakte Image-Repositories in `approved-images.txt` freigeben; und `registry.json` ergänzen. Keine echten Secrets oder unsicheren Standardpasswörter einchecken. Ports konfigurierbar machen und App-Daten in benannten Volumes oder dokumentierten persistenten Pfaden speichern. Docker-Socket nicht direkt mounten und privileged/Host-Netzwerk nicht ohne ausdrückliche Freigabe aktivieren. Lizenzen und Hinweise Dritter beachten. CI ausführen und Pull Request statt direktem Push auf `main` liefern. Wenn Image-Herkunft oder Setup-Anforderungen nicht verifizierbar sind, stoppen und offene Punkte benennen.
