# Immich

## English

Immich publishes its official server, machine-learning, and PostgreSQL images on **GHCR**, not Docker Hub. The `valkey/valkey` dependency is the upstream Valkey image on Docker Hub. All four image repositories are individually allowlisted and validated in CI.

## Before deploying

1. In the project `.env`, replace `DB_PASSWORD` with a unique random alphanumeric password. Do not deploy with the example placeholder.
2. Check that the Arcane project storage has enough room for photos and videos. By default uploads use `./library` and PostgreSQL uses `./postgres` below the project directory. Keep the database on local storage, not a network share.
3. Deploy, then open `http://<Docker-Host-IP>:2283` and complete the Immich onboarding.

The project contains four services and is more resource-intensive than a single-container template. Hardware acceleration is not enabled by default. The `IMMICH_PORT`, `UPLOAD_LOCATION` and `DB_DATA_LOCATION` settings can be changed in the project `.env` before deployment.

Sources: [Immich](https://immich.app/), [recommended Docker Compose install](https://docs.immich.app/install/docker-compose/), [upstream Compose file](https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml).

## Deutsch

Immich veröffentlicht seine offiziellen Server-, Machine-Learning- und PostgreSQL-Images auf **GHCR**, nicht auf Docker Hub. Die Abhängigkeit `valkey/valkey` ist das Valkey-Upstream-Image auf Docker Hub. Alle vier Image-Repositories sind einzeln freigegeben und werden von CI geprüft.

### Vor dem Deploy

1. In der Projekt-`.env` ein eigenes zufälliges alphanumerisches Passwort für `DB_PASSWORD` setzen. Nicht mit dem leeren Beispielwert deployen.
2. Prüfen, dass im Arcane-Projektspeicher genug Platz für Fotos und Videos ist. Standardmäßig liegen Uploads in `./library` und PostgreSQL-Daten in `./postgres` unterhalb des Projektverzeichnisses. Die Datenbank auf lokalem Speicher und nicht auf einem Netzwerk-Mount ablegen.
3. Deployen, `http://<Docker-Host-IP>:2283` öffnen und die Immich-Ersteinrichtung abschließen.

Das Projekt enthält vier Services und benötigt mehr Ressourcen als eine Einzelcontainer-App. Hardwarebeschleunigung ist standardmäßig deaktiviert. `IMMICH_PORT`, `UPLOAD_LOCATION` und `DB_DATA_LOCATION` lassen sich vor dem Deploy in der Projekt-`.env` ändern.

Quellen: [Immich](https://immich.app/), [empfohlene Docker-Compose-Installation](https://docs.immich.app/install/docker-compose/), [Compose-Datei des Upstreams](https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml).
