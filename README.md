# Arcane Template Registry

[English](#english) · [Deutsch](#deutsch)

Community-curated Arcane Compose templates for popular self-hosted apps. Templates use images published by their upstream projects, include persistent storage and `x-arcane` metadata, and are validated with GitHub Actions. Contributions are welcome through pull requests.

## English

### Add this registry to Arcane

In Arcane, open **Customization → Templates → Add Registry** and add:

```text
https://raw.githubusercontent.com/Broda24/arcane-templates/main/registry.json
```

Choose a template and select **Create Project**. Arcane creates a Compose project; deploy/start it to run the containers. Open the app at the host address and port documented in that template's README.

Some apps need a setting before deployment or additional mounts after deployment. For example, Immich requires a unique database password, and Jellyfin needs a media folder mounted to access your media library.

### Templates

- Home Assistant — local smart-home hub
- Jellyfin — media server
- Immich — photo and video library
- Syncthing — peer-to-peer file synchronization
- Uptime Kuma — uptime monitoring
- ntfy — self-hosted push notifications
- Trilium Notes — personal knowledge base
- Nginx — simple first-deployment test

### Image and security policy

- Use only container images published by the app's upstream project. No third-party repackaged images or locally built images.
- Approved image repositories are listed in [`approved-images.txt`](approved-images.txt); CI rejects anything not on that list.
- Images come from Docker Hub, except Immich, whose upstream publishes its official images on GHCR and has no official Docker Hub image.
- Never commit real passwords or tokens. Set required secrets before deploying. Keep ntfy behind trusted access controls; do not expose an unauthenticated server to the public Internet.
- Review ports, storage, device access, and backup needs in each template README before deployment.

### Updates and contributions

Arcane can check and apply image updates for deployed projects. This is separate from updates to the templates in this repository. Compose, storage, configuration, or dependency changes should be submitted here as a pull request. GitHub Actions validate the registry and run `docker compose config` against every template.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contributor and AI instructions. Registry entries point to the `main` branch.

Contributors without repository write access can fork the project and open a pull request. The `main` branch requires a pull request and a passing `validate` check for normal merges. Repository admins can bypass branch protection; currently the owner account (also used by the authorized AI) is the only admin.

## Deutsch

Community-gepflegte Arcane-Compose-Vorlagen für beliebte Self-Hosting-Apps. Die Vorlagen verwenden Images, die vom jeweiligen Upstream-Projekt veröffentlicht werden, enthalten persistente Datenablagen und `x-arcane`-Metadaten und werden per GitHub Actions geprüft. Beiträge sind als Pull Request willkommen.

### Registry in Arcane hinzufügen

In Arcane **Customization → Templates → Add Registry** öffnen und diese URL hinzufügen:

```text
https://raw.githubusercontent.com/Broda24/arcane-templates/main/registry.json
```

Eine Vorlage auswählen und **Create Project** klicken. Arcane erstellt ein Compose-Projekt; zum Starten der Container muss es anschließend deployed/gestartet werden. Adresse und Port der App stehen in der README der jeweiligen Vorlage.

Einige Apps brauchen vor dem Deploy eine Einstellung oder danach zusätzliche Mounts. Immich erfordert zum Beispiel ein eigenes Datenbankpasswort; Jellyfin benötigt einen Medienordner-Mount, um auf die eigene Mediathek zuzugreifen.

### Vorlagen

- Home Assistant — lokale Smart-Home-Zentrale
- Jellyfin — Medienserver
- Immich — Foto- und Videosammlung
- Syncthing — Peer-to-Peer-Dateisynchronisierung
- Uptime Kuma — Verfügbarkeitsüberwachung
- ntfy — eigener Push-Benachrichtigungsserver
- Trilium Notes — persönliche Wissensdatenbank
- Nginx — einfacher Test für den ersten Deploy

### Image- und Sicherheitsregeln

- Nur Images verwenden, die vom jeweiligen App-Upstream veröffentlicht werden. Keine fremden neu verpackten oder lokal gebauten Images.
- Die freigegebenen Image-Repositories stehen in [`approved-images.txt`](approved-images.txt); CI weist nicht freigegebene Images zurück.
- Die Images kommen von Docker Hub. Ausnahme ist Immich: Das Upstream-Projekt veröffentlicht seine offiziellen Images auf GHCR und bietet kein offizielles Docker-Hub-Image an.
- Keine echten Passwörter oder Tokens einchecken. Erforderliche Secrets vor dem Deploy setzen. ntfy nur mit vertrauenswürdigen Zugriffskontrollen betreiben und nicht ungeschützt öffentlich bereitstellen.
- Vor dem Deploy die README der Vorlage zu Ports, Speicherung, Gerätezugriff und Backups beachten.

### Updates und Beiträge

Arcane kann Image-Updates laufender Projekte prüfen und einspielen. Das ist unabhängig von Änderungen der Vorlagen in diesem Repository. Änderungen an Compose, Storage, Konfiguration oder Abhängigkeiten bitte als Pull Request einreichen. GitHub Actions prüfen die Registry und führen `docker compose config` für jede Vorlage aus.

Hinweise für Beiträge und KI stehen in [CONTRIBUTING.md](CONTRIBUTING.md). Die Registry-Einträge verweisen auf den Branch `main`.

Mitwirkende ohne Schreibrechte können das Repo forken und einen Pull Request erstellen. Für normale Merges verlangt der Branch `main` einen Pull Request und einen erfolgreichen `validate`-Check. Repository-Admins können den Schutz umgehen; aktuell ist nur das Owner-Konto (auch vom autorisierten KI-Zugang verwendet) Admin.
