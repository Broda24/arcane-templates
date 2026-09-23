# ntfy

Der ntfy-Maintainer veröffentlicht `binwiederhier/ntfy` auf Docker Hub. Die Vorlage startet den HTTP-Server und hält den Nachrichten-Cache im Docker-Volume `ntfy-cache`.

## Start und Zugriff

Deployen und `http://<Docker-Host-IP>:8085` öffnen. Für LAN-Tests kann ntfy direkt verwendet werden. **Nicht ungeschützt ins öffentliche Internet weiterleiten:** vor externer Veröffentlichung Authentifizierung/Zugriffsregeln und HTTPS konfigurieren. Port und Zeitzone sind in `.env` anpassbar.

Quellen: [ntfy](https://ntfy.sh/), [Docker-Installationshinweise](https://docs.ntfy.sh/install/#docker), [Docker Hub](https://hub.docker.com/r/binwiederhier/ntfy).
