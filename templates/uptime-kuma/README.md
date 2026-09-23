# Uptime Kuma

Uptime Kuma veröffentlicht das eigene Image `louislam/uptime-kuma` auf Docker Hub. Die Datenbank und Monitore bleiben im Volume `uptime-kuma-data` erhalten.

## Start

Deployen und `http://<Docker-Host-IP>:3001` öffnen. Beim ersten Start ein Administratorkonto anlegen. Falls Port 3001 belegt ist, `UPTIME_KUMA_PORT` im Projekt `.env` ändern.

Quellen: [Uptime Kuma](https://uptime.kuma.pet/), [GitHub](https://github.com/louislam/uptime-kuma), [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma).
