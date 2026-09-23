# Contributing / Mitwirken

## English

1. Create a directory under `templates/<slug>/`.
2. Add `docker-compose.yml`, `.env.example`, and `README.md`. Document the app in English and German, including ports, setup requirements, persistent data, and links.
3. Add project-level `x-arcane.icon` and `x-arcane.urls` metadata to Compose. Use a working HTTPS icon URL plus the upstream homepage and source repository.
4. Add the template to `registry.json`. URLs must point to files on the `main` branch.
5. Verify that every image is published by its application upstream. Add its exact repository to `approved-images.txt`. GHCR images are allowed only when the upstream publishes there and has no official Docker Hub image.
6. Check the Compose configuration against upstream documentation. Never commit real secrets or insecure default passwords.
7. Open a pull request and make sure the GitHub Actions checks pass.

### Instructions for an AI

> Add the requested application as an Arcane Compose template. Use only images published by the app's upstream project on Docker Hub, or on GHCR when the upstream publishes its official image there and no official Docker Hub image exists. Verify the publisher and configuration against upstream documentation. Add `docker-compose.yml`, `.env.example`, and bilingual `README.md` under `templates/<slug>/`; include project-level `x-arcane.icon` and `x-arcane.urls`; add exact image repositories to `approved-images.txt`; and add the template to `registry.json`. Never commit real secrets or insecure default passwords. Make ports configurable and persist app data in named volumes or documented persistent paths. Run CI and submit a pull request instead of writing directly to `main`. If upstream image provenance or setup requirements cannot be verified, stop and report what is unknown.

## Deutsch

1. Ein Verzeichnis unter `templates/<slug>/` anlegen.
2. `docker-compose.yml`, `.env.example` und `README.md` ergänzen. Die App auf Deutsch und Englisch dokumentieren, einschließlich Ports, Setup-Anforderungen, persistenter Daten und Links.
3. Projektweite `x-arcane.icon`- und `x-arcane.urls`-Metadaten in Compose eintragen. Ein funktionierendes HTTPS-Icon sowie Homepage und Quellcode-Repository des Upstreams verlinken.
4. Die Vorlage in `registry.json` eintragen. URLs müssen auf Dateien im Branch `main` zeigen.
5. Prüfen, dass jedes Image vom jeweiligen App-Upstream veröffentlicht wird. Das exakte Repository in `approved-images.txt` freigeben. GHCR-Images nur aufnehmen, wenn der Upstream sie dort veröffentlicht und kein offizielles Docker-Hub-Image anbietet.
6. Compose-Konfiguration anhand der Upstream-Dokumentation prüfen. Keine echten Secrets oder unsicheren Standardpasswörter einchecken.
7. Pull Request erstellen und sicherstellen, dass die GitHub-Action erfolgreich durchläuft.

### Arbeitsanweisung für eine KI

> Ergänze die gewünschte Anwendung als Arcane-Compose-Vorlage. Verwende nur Images, die vom App-Upstream auf Docker Hub veröffentlicht werden, oder auf GHCR, wenn der Upstream dort sein offizielles Image veröffentlicht und kein offizielles Docker-Hub-Image anbietet. Prüfe Publisher und Konfiguration anhand der Upstream-Dokumentation. Lege `docker-compose.yml`, `.env.example` und eine zweisprachige `README.md` unter `templates/<slug>/` an; ergänze projektweite `x-arcane.icon`- und `x-arcane.urls`-Metadaten; gib die exakten Image-Repositories in `approved-images.txt` frei; und ergänze `registry.json`. Checke keine echten Secrets oder unsicheren Standardpasswörter ein. Mache Ports konfigurierbar und speichere App-Daten in benannten Volumes oder dokumentierten persistenten Pfaden. Führe CI aus und liefere einen Pull Request statt direkt auf `main` zu schreiben. Wenn Image-Herkunft oder Setup-Anforderungen nicht verifizierbar sind, stoppe und benenne die offenen Punkte.
