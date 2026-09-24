# Backrest

## English

Backrest is a web UI and orchestrator for [restic](https://restic.net/) backups. This template uses the upstream-published `garethgeorge/backrest` Docker Hub image.

### Setup and security

- Before deployment, set `BACKREST_SOURCE_PATH` to the host directory you want to back up. It is mounted read-only at `/userdata`. The default `./backup-source` is relative to the Compose project directory; replace it with a path that contains your data. Add more read-only mounts in Compose if you need to back up multiple directories.
- Set `BACKREST_RESTORE_PATH` to a host directory for restored files. It is mounted writable at `/restore`, separate from the read-only backup source.
- `BACKREST_REPOSITORY_PATH` selects a persistent host directory for local Restic repositories, mounted at `/repos`. It is optional when using a remote repository such as S3 or SFTP.
- Open `http://127.0.0.1:9898` after deployment. On first run, Backrest asks you to create a username and password.
- The published web port binds to localhost by default. For remote access, use an authenticated HTTPS reverse proxy and restrict network access; do not expose the unauthenticated setup or plain HTTP service to the public Internet. `BACKREST_BIND_ADDRESS` and `BACKREST_HOST_PORT` configure the host-side port mapping.
- The `backrest-config` volume contains the login and repository configuration; keep it backed up and protected. `backrest-data` stores Backrest data including its managed Restic binary, `backrest-cache` stores the Restic cache, and `backrest-rclone` can hold rclone configuration for rclone remotes. The local repository path contains backup data and should also be included in your backup plan.

Sources: [Backrest documentation](https://garethgeorge.github.io/backrest/), [Backrest source and Docker instructions](https://github.com/garethgeorge/backrest).

## Deutsch

Backrest ist eine Weboberfläche und Orchestrierung für Restic-Backups. Diese Vorlage verwendet das vom Upstream veröffentlichte Docker-Hub-Image `garethgeorge/backrest`.

### Einrichtung und Sicherheit

- Vor dem Deploy `BACKREST_SOURCE_PATH` auf das Host-Verzeichnis setzen, das gesichert werden soll. Es wird schreibgeschützt unter `/userdata` eingebunden. Der Standard `./backup-source` ist relativ zum Compose-Projektverzeichnis; den Pfad durch ein Verzeichnis mit den eigenen Daten ersetzen. Für mehrere Verzeichnisse zusätzliche schreibgeschützte Mounts in Compose ergänzen.
- `BACKREST_RESTORE_PATH` auf ein Host-Verzeichnis für wiederhergestellte Dateien setzen. Dieses wird getrennt von der schreibgeschützten Quelle unter `/restore` eingebunden und ist beschreibbar.
- `BACKREST_REPOSITORY_PATH` bestimmt ein dauerhaftes Host-Verzeichnis für lokale Restic-Repositories, eingebunden unter `/repos`. Bei einem Remote-Repository wie S3 oder SFTP ist es optional.
- Nach dem Deploy `http://127.0.0.1:9898` öffnen. Beim ersten Start fordert Backrest zur Einrichtung von Benutzername und Passwort auf.
- Der veröffentlichte Web-Port ist standardmäßig nur an localhost gebunden. Für Fernzugriff einen authentifizierten HTTPS-Reverse-Proxy verwenden und den Netzwerkzugriff beschränken; weder die ungeschützte Ersteinrichtung noch den HTTP-Dienst öffentlich bereitstellen. `BACKREST_BIND_ADDRESS` und `BACKREST_HOST_PORT` konfigurieren das Host-Port-Mapping.
- Das Volume `backrest-config` enthält Login- und Repository-Konfiguration und muss geschützt und gesichert werden. `backrest-data` enthält Backrest-Daten einschließlich des verwalteten Restic-Binaries, `backrest-cache` den Restic-Cache und `backrest-rclone` kann die rclone-Konfiguration für rclone-Remotes enthalten. Der lokale Repository-Pfad enthält Backup-Daten und gehört ebenfalls in den Sicherungsplan.

Quellen: [Backrest-Dokumentation](https://garethgeorge.github.io/backrest/), [Backrest-Quellcode und Docker-Anleitung](https://github.com/garethgeorge/backrest).
