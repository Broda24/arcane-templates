# ntfy

Der ntfy-Maintainer veröffentlicht `binwiederhier/ntfy` auf Docker Hub. Die Vorlage startet den HTTP-Server und hält den Nachrichten-Cache im Docker-Volume `ntfy-cache`.

## Start und Zugriff

Deployen und `http://<Docker-Host-IP>:8085` öffnen. Für LAN-Tests kann ntfy direkt verwendet werden. **Nicht ungeschützt ins öffentliche Internet weiterleiten:** vor externer Veröffentlichung Authentifizierung/Zugriffsregeln und HTTPS konfigurieren. Port und Zeitzone sind in `.env` anpassbar.

Quellen: [ntfy](https://ntfy.sh/), [Docker-Installationshinweise](https://docs.ntfy.sh/install/#docker), [Docker Hub](https://hub.docker.com/r/binwiederhier/ntfy).

## English

The ntfy maintainer publishes `binwiederhier/ntfy` on Docker Hub. This template starts the HTTP server and stores its message cache in the `ntfy-cache` Docker volume.

### Start and access

Deploy the project and open `http://<Docker-host-IP>:8085`. You can test ntfy on your LAN. **Do not expose it to the public Internet without protection:** configure authentication/access rules and HTTPS first. Change the port and timezone in `.env` if needed.

Sources: [ntfy](https://ntfy.sh/), [Docker installation guide](https://docs.ntfy.sh/install/#docker), [Docker Hub](https://hub.docker.com/r/binwiederhier/ntfy).
