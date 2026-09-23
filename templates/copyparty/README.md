# Copyparty

## English

Copyparty is an upstream-maintained Docker Hub file server. This template creates one authenticated read/write account and stores shared files in the persistent `copyparty-files` volume. The recommended upstream image is `copyparty/ac`.

### Before deploying

1. Set a long, unique `COPYPARTY_PASSWORD` in the project `.env`; deployment is intentionally blocked while it is empty. Keep the `.env` private. Docker administrators can inspect container configuration, including command arguments.
2. Deploy and open `http://<Docker-host-IP>:3923`; sign in with username `share` (or your chosen `COPYPARTY_USER`) and the password you set.
3. Do not expose the HTTP service directly to the public Internet. Use a properly secured HTTPS reverse proxy if external access is needed.

Files persist in `copyparty-files`; configuration can be placed in the `copyparty-config` volume. Only HTTP is enabled; FTP, SMB, and other optional protocols are not exposed. Change the host port and username in `.env` if needed.

Sources: [Copyparty](https://github.com/9001/copyparty), [official Docker guide](https://github.com/9001/copyparty/blob/hovudstraum/scripts/docker/README.md), [Docker Hub](https://hub.docker.com/r/copyparty/ac).

## Deutsch

Copyparty ist ein Dateiserver mit einem vom Upstream gepflegten Docker-Hub-Image. Die Vorlage richtet ein angemeldetes Konto mit Lese-/Schreibzugriff ein; Dateien bleiben im persistenten Volume `copyparty-files`. Der Upstream empfiehlt das Image `copyparty/ac`.

### Vor dem Deploy

1. Ein langes, individuelles `COPYPARTY_PASSWORD` in der Projekt-`.env` setzen; ohne Passwort blockiert Compose absichtlich den Deploy. Die `.env` privat halten. Docker-Admins können die Container-Konfiguration einschließlich Kommandozeilen-Argumenten einsehen.
2. Deployen und `http://<Docker-Host-IP>:3923` öffnen. Mit Benutzer `share` (oder dem gesetzten `COPYPARTY_USER`) und dem eigenen Passwort anmelden.
3. Den HTTP-Dienst nicht direkt öffentlich ins Internet stellen. Für externen Zugriff einen gesicherten HTTPS-Reverse-Proxy verwenden.

Dateien liegen dauerhaft im Volume `copyparty-files`; Konfiguration kann im Volume `copyparty-config` abgelegt werden. Nur HTTP ist aktiviert; FTP, SMB und andere optionale Protokolle sind nicht veröffentlicht. Host-Port und Benutzer lassen sich in `.env` ändern.

Quellen: [Copyparty](https://github.com/9001/copyparty), [offizielle Docker-Anleitung](https://github.com/9001/copyparty/blob/hovudstraum/scripts/docker/README.md), [Docker Hub](https://hub.docker.com/r/copyparty/ac).
