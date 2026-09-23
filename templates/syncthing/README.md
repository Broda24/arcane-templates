# Syncthing

Syncthing veröffentlicht das Image `syncthing/syncthing` selbst auf Docker Hub. Die Konfiguration und Sync-Daten liegen persistent im Volume `syncthing-data`.

## Start

Deployen und die Weboberfläche unter `http://<Docker-Host-IP>:8384` öffnen. Auf jedem weiteren Gerät Syncthing installieren und die Geräte in der Oberfläche gegenseitig freigeben.

Die offiziellen Docker-Hinweise empfehlen Host-Netzwerk für automatische LAN-Erkennung. Diese Vorlage bleibt im Bridge-Netz und veröffentlicht GUI-, Synchronisierungs- und Discovery-Ports; je nach Netzwerk kann die automatische LAN-Erkennung eingeschränkt sein. Geräte können dann manuell über Adresse/Port verbunden werden. Beim externen Zugriff auf die Weboberfläche Zugangsschutz und HTTPS einrichten. Ports lassen sich in `.env` ändern.

Quellen: [Syncthing](https://syncthing.net/), [Docker-README des Upstreams](https://github.com/syncthing/syncthing/blob/main/README-Docker.md), [Docker Hub](https://hub.docker.com/r/syncthing/syncthing).
