# Navidrome

## English

Personal music streaming server. Place music in the project `music` directory; it is mounted read-only. The container runs as the configured `PUID:PGID`, so ensure it can write its data volume and read the music directory. Open `http://<host-ip>:4533`; back up `navidrome-data`.

Sources: [Navidrome](https://github.com/navidrome/navidrome), [official Docker instructions](https://www.navidrome.org/docs/installation/docker/).

## Deutsch

Eigener Musikstreaming-Server. Musik in das Projektverzeichnis `music` legen; es wird schreibgeschützt eingebunden. Der Container läuft als `PUID:PGID`; dieser Benutzer muss ins Daten-Volume schreiben und das Musikverzeichnis lesen können. `http://<Host-IP>:4533` öffnen und `navidrome-data` sichern.

Quellen: [Navidrome](https://github.com/navidrome/navidrome), [offizielle Docker-Anleitung](https://www.navidrome.org/docs/installation/docker/).
