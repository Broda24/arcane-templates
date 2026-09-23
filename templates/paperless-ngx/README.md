# Paperless-ngx

## English

Paperless-ngx is a document archive with OCR and full-text search. The application upstream publishes `paperlessngx/paperless-ngx` on Docker Hub. The template also starts PostgreSQL, Valkey, Apache Tika, and Gotenberg; Tika/Gotenberg add Office-document import support.

### Before deploying

1. Set unique values for `PAPERLESS_DB_PASSWORD` and `PAPERLESS_SECRET_KEY` in the project `.env`. Do not deploy with either value empty. Generate the secret key with Python, for example: `python3 -c "import secrets; print(secrets.token_urlsafe(64))"`.
2. Deploy the project and open `http://<Docker-host-IP>:8010`.
3. Create the first admin account from the Paperless container with `createsuperuser` (Arcane's project/container console can be used).
4. Put files to import into the project's `consume` directory, or add a suitable host folder mount. Stored documents persist in Docker volumes.

Paperless stores documents unencrypted on disk, so use it only on a trusted host and ensure the data and database volumes are backed up. Never expose it publicly without HTTPS and appropriate access protection. Change `PAPERLESS_PORT`, timezone, and OCR languages in `.env` as needed.

Sources: [Paperless-ngx documentation](https://docs.paperless-ngx.com/), [upstream Compose configuration](https://github.com/paperless-ngx/paperless-ngx/tree/main/docker/compose), [Docker Hub image](https://hub.docker.com/r/paperlessngx/paperless-ngx).

## Deutsch

Paperless-ngx ist ein Dokumentenarchiv mit OCR und Volltextsuche. Der Upstream veröffentlicht `paperlessngx/paperless-ngx` auf Docker Hub. Die Vorlage startet außerdem PostgreSQL, Valkey, Apache Tika und Gotenberg; Tika/Gotenberg ergänzen den Import von Office-Dokumenten.

### Vor dem Deploy

1. In der Projekt-`.env` individuelle Werte für `PAPERLESS_DB_PASSWORD` und `PAPERLESS_SECRET_KEY` setzen. Nicht deployen, solange einer der Werte leer ist. Den Secret Key kann man z. B. mit Python erzeugen: `python3 -c "import secrets; print(secrets.token_urlsafe(64))"`.
2. Projekt deployen und `http://<Docker-Host-IP>:8010` öffnen.
3. Das erste Admin-Konto im Paperless-Container mit `createsuperuser` erstellen (z. B. über die Arcane-Projekt-/Container-Konsole).
4. Zu importierende Dateien in das `consume`-Verzeichnis des Projekts legen oder einen passenden Host-Ordner mounten. Archiv und Datenbank liegen persistent in Docker-Volumes.

Paperless speichert Dokumente unverschlüsselt auf dem Datenträger. Daher nur auf einem vertrauenswürdigen Host betreiben und Daten-/Datenbank-Volumes sichern. Nicht ohne HTTPS und passenden Zugriffsschutz öffentlich bereitstellen. Port, Zeitzone und OCR-Sprachen lassen sich in `.env` anpassen.

Quellen: [Paperless-ngx-Dokumentation](https://docs.paperless-ngx.com/), [Compose-Konfiguration des Upstreams](https://github.com/paperless-ngx/paperless-ngx/tree/main/docker/compose), [Docker-Hub-Image](https://hub.docker.com/r/paperlessngx/paperless-ngx).
