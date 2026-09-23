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

| Template | Description |
| --- | --- |
| [Home Assistant](templates/home-assistant/) | Local smart-home hub |
| [Jellyfin](templates/jellyfin/) | Media server |
| [Immich](templates/immich/) | Photo and video library |
| [Syncthing](templates/syncthing/) | Peer-to-peer file synchronization |
| [Uptime Kuma](templates/uptime-kuma/) | Uptime monitoring |
| [ntfy](templates/ntfy/) | Self-hosted push notifications |
| [Trilium Notes](templates/trilium-notes/) | Personal knowledge base |
| [Paperless-ngx](templates/paperless-ngx/) | Document archive with OCR |
| [Copyparty](templates/copyparty/) | Authenticated file server |
| [Vaultwarden](templates/vaultwarden/) | Bitwarden-compatible password server |
| [AdGuard Home](templates/adguard-home/) | Network-wide DNS filtering |
| [Nextcloud](templates/nextcloud/) | File sync and collaboration platform |
| [Mealie](templates/mealie/) | Recipe manager and meal planner |
| [Actual Budget](templates/actual-budget/) | Personal finance and budgeting |
| [Gitea](templates/gitea/) | Self-hosted Git service |
| [Audiobookshelf](templates/audiobookshelf/) | Audiobook and podcast server |
| [Navidrome](templates/navidrome/) | Personal music streaming |
| [Node-RED](templates/node-red/) | Visual automation flows |
| [n8n](templates/n8n/) | Workflow automation |
| [SearXNG](templates/searxng/) | Privacy-respecting metasearch |
| [Ollama](templates/ollama/) | Local model runner |
| [Homebox](templates/homebox/) | Home inventory |
| [Zigbee2MQTT](templates/zigbee2mqtt/) | Zigbee-to-MQTT bridge |
| [Eclipse Mosquitto](templates/mosquitto/) | MQTT broker |
| [Nginx](templates/nginx-welcome/) | Simple first-deployment test |

### Image and security policy

- Use only container images published by the app's upstream project. No third-party repackaged images or locally built images.
- Approved image repositories are listed in [`approved-images.txt`](approved-images.txt); CI rejects anything not on that list.
- Docker Hub is preferred. GHCR and official vendor registries are used only where the upstream publishes its official image there and no suitable official Docker Hub image exists.
- Never commit real passwords or tokens. Set required secrets before deploying. Keep ntfy behind trusted access controls; do not expose an unauthenticated server to the public Internet.
- Keep sensitive or unauthenticated services (including Vaultwarden, Node-RED, n8n, SearXNG, Ollama, Homebox, and Zigbee2MQTT) on trusted networks or behind an authenticated HTTPS reverse proxy.
- Review ports, storage, device access, and backup needs in each template README before deployment.
- Dozzle is intentionally not included yet: its standard setup requires Docker API access, which is root-equivalent. The registry does not mount the Docker socket into application containers.

### Updates and contributions

Arcane can check and apply image updates for deployed projects. This is separate from updates to the templates in this repository. Compose, storage, configuration, or dependency changes should be submitted here as a pull request. GitHub Actions validate the registry and run `docker compose config` against every template.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contributor and AI instructions. Registry entries point to the `main` branch.

Contributors without repository write access can fork the project and open a pull request. The `main` branch requires a pull request and a passing `validate` check for normal merges. Repository admins can bypass branch protection; currently the owner account (also used by the authorized AI) is the only admin.

### License and attribution

Original Compose templates and documentation in this repository are licensed under the [MIT License](LICENSE). The repository is an independent community project and is not affiliated with Arcane or the listed application projects. App names and marks remain with their respective owners; referenced container images are fetched from their upstream registries and are not redistributed here. Icons are referenced from [selfh.st/icons](https://github.com/selfhst/icons), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); this is the attribution for the icon collection, while individual marks remain with their owners.

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

| Vorlage | Beschreibung |
| --- | --- |
| [Home Assistant](templates/home-assistant/) | Lokale Smart-Home-Zentrale |
| [Jellyfin](templates/jellyfin/) | Medienserver |
| [Immich](templates/immich/) | Foto- und Videosammlung |
| [Syncthing](templates/syncthing/) | Peer-to-Peer-Dateisynchronisierung |
| [Uptime Kuma](templates/uptime-kuma/) | Verfügbarkeitsüberwachung |
| [ntfy](templates/ntfy/) | Eigener Push-Benachrichtigungsserver |
| [Trilium Notes](templates/trilium-notes/) | Persönliche Wissensdatenbank |
| [Paperless-ngx](templates/paperless-ngx/) | Dokumentenarchiv mit OCR |
| [Copyparty](templates/copyparty/) | Dateiserver mit Anmeldung |
| [Vaultwarden](templates/vaultwarden/) | Bitwarden-kompatibler Passwortserver |
| [AdGuard Home](templates/adguard-home/) | DNS-Filter fürs Heimnetz |
| [Nextcloud](templates/nextcloud/) | Dateiablage und Zusammenarbeit |
| [Mealie](templates/mealie/) | Rezeptverwaltung und Essensplanung |
| [Actual Budget](templates/actual-budget/) | Haushaltsbudget und Finanzplanung |
| [Gitea](templates/gitea/) | Eigener Git-Dienst |
| [Audiobookshelf](templates/audiobookshelf/) | Hörbuch- und Podcastserver |
| [Navidrome](templates/navidrome/) | Musikstreaming aus der eigenen Sammlung |
| [Node-RED](templates/node-red/) | Visuelle Automatisierungen |
| [n8n](templates/n8n/) | Workflow-Automatisierung |
| [SearXNG](templates/searxng/) | Datenschutzfreundliche Metasuche |
| [Ollama](templates/ollama/) | Lokale Sprachmodelle |
| [Homebox](templates/homebox/) | Inventar für Haushalt und Geräte |
| [Zigbee2MQTT](templates/zigbee2mqtt/) | Zigbee-zu-MQTT-Bridge |
| [Eclipse Mosquitto](templates/mosquitto/) | MQTT-Broker |
| [Nginx](templates/nginx-welcome/) | Einfacher Test für den ersten Deploy |

### Image- und Sicherheitsregeln

- Nur Images verwenden, die vom jeweiligen App-Upstream veröffentlicht werden. Keine fremden neu verpackten oder lokal gebauten Images.
- Die freigegebenen Image-Repositories stehen in [`approved-images.txt`](approved-images.txt); CI weist nicht freigegebene Images zurück.
- Docker Hub wird bevorzugt. GHCR und offizielle Hersteller-Registries sind nur zugelassen, wenn der Upstream sein offizielles Image dort veröffentlicht und kein passendes offizielles Docker-Hub-Image anbietet.
- Keine echten Passwörter oder Tokens einchecken. Erforderliche Secrets vor dem Deploy setzen. ntfy nur mit vertrauenswürdigen Zugriffskontrollen betreiben und nicht ungeschützt öffentlich bereitstellen.
- Sensible oder nicht standardmäßig geschützte Dienste (u. a. Vaultwarden, Node-RED, n8n, SearXNG, Ollama, Homebox und Zigbee2MQTT) nur in vertrauenswürdigen Netzen oder hinter einem authentifizierten HTTPS-Reverse-Proxy betreiben.
- Vor dem Deploy die README der Vorlage zu Ports, Speicherung, Gerätezugriff und Backups beachten.
- Dozzle ist vorerst nicht enthalten: Die Standardkonfiguration benötigt Docker-API-Zugriff, der root-äquivalent ist. Diese Registry mountet den Docker-Socket nicht direkt in App-Container.

### Updates und Beiträge

Arcane kann Image-Updates laufender Projekte prüfen und einspielen. Das ist unabhängig von Änderungen der Vorlagen in diesem Repository. Änderungen an Compose, Storage, Konfiguration oder Abhängigkeiten bitte als Pull Request einreichen. GitHub Actions prüfen die Registry und führen `docker compose config` für jede Vorlage aus.

Hinweise für Beiträge und KI stehen in [CONTRIBUTING.md](CONTRIBUTING.md). Die Registry-Einträge verweisen auf den Branch `main`.

Mitwirkende ohne Schreibrechte können das Repo forken und einen Pull Request erstellen. Für normale Merges verlangt der Branch `main` einen Pull Request und einen erfolgreichen `validate`-Check. Repository-Admins können den Schutz umgehen; aktuell ist nur das Owner-Konto (auch vom autorisierten KI-Zugang verwendet) Admin.

### Lizenz und Namensnennung

Die originalen Compose-Vorlagen und Dokumentation in diesem Repository stehen unter der [MIT-Lizenz](LICENSE). Das Repo ist ein unabhängiges Community-Projekt und nicht mit Arcane oder den gelisteten App-Projekten verbunden. App-Namen und Marken verbleiben bei ihren jeweiligen Eigentümern; referenzierte Container-Images werden beim Upstream bezogen und hier nicht weiterverteilt. Icons werden von [selfh.st/icons](https://github.com/selfhst/icons) eingebunden und stehen unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); diese Namensnennung gilt der Icon-Sammlung, einzelne Marken verbleiben bei ihren Eigentümern.
