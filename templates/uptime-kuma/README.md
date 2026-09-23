# Uptime Kuma

Uptime Kuma veröffentlicht das eigene Image `louislam/uptime-kuma` auf Docker Hub. Die Datenbank und Monitore bleiben im Volume `uptime-kuma-data` erhalten.

## Start

Deployen und `http://<Docker-Host-IP>:3001` öffnen. Beim ersten Start ein Administratorkonto anlegen. Falls Port 3001 belegt ist, `UPTIME_KUMA_PORT` im Projekt `.env` ändern.

Quellen: [Uptime Kuma](https://uptime.kuma.pet/), [GitHub](https://github.com/louislam/uptime-kuma), [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma).

## English

Uptime Kuma publishes its own `louislam/uptime-kuma` image on Docker Hub. The database and monitors persist in the `uptime-kuma-data` volume.

### Start

Deploy the project and open `http://<Docker-host-IP>:3001`. Create an administrator account on first launch. If port 3001 is already in use, change `UPTIME_KUMA_PORT` in the project `.env`.

Sources: [Uptime Kuma](https://uptime.kuma.pet/), [GitHub](https://github.com/louislam/uptime-kuma), [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma).
