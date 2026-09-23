# Nextcloud

## English

Personal file sync and collaboration using the official Nextcloud Docker image, MariaDB, and Redis.

1. Set unique values for `NEXTCLOUD_DB_PASSWORD`, `NEXTCLOUD_DB_ROOT_PASSWORD`, and `NEXTCLOUD_ADMIN_PASSWORD` in the project `.env` before deployment.
2. Set `NEXTCLOUD_TRUSTED_DOMAINS` to the hostname or IP used to access the service (space-separated for multiple names).
3. Open `http://<host-ip>:8089`. Use HTTPS and a trusted reverse proxy for external access.
4. Back up the Nextcloud and MariaDB volumes together. Upgrade one major Nextcloud version at a time.

Sources: [Nextcloud](https://nextcloud.com/), [official Docker image documentation](https://github.com/nextcloud/docker).

## Deutsch

Eigene Dateiablage und Zusammenarbeit mit dem offiziellen Nextcloud-Docker-Image, MariaDB und Redis.

1. Vor dem Deploy individuelle Werte für `NEXTCLOUD_DB_PASSWORD`, `NEXTCLOUD_DB_ROOT_PASSWORD` und `NEXTCLOUD_ADMIN_PASSWORD` in der Projekt-`.env` setzen.
2. `NEXTCLOUD_TRUSTED_DOMAINS` auf den verwendeten Hostnamen oder die IP setzen (mehrere Namen durch Leerzeichen trennen).
3. `http://<Host-IP>:8089` öffnen. Für externen Zugriff HTTPS und einen vertrauenswürdigen Reverse-Proxy verwenden.
4. Nextcloud- und MariaDB-Volumes gemeinsam sichern. Nextcloud immer nur um eine Hauptversion auf einmal aktualisieren.

Quellen: [Nextcloud](https://nextcloud.com/), [Dokumentation des offiziellen Docker-Images](https://github.com/nextcloud/docker).
