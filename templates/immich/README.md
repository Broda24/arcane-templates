# Immich

Immich publishes its official server, machine-learning and PostgreSQL images on **GHCR**, not Docker Hub. The `valkey/valkey` dependency is the upstream Valkey image on Docker Hub. All four image repositories are individually allowlisted and validated in CI.

## Before deploying

1. In the project `.env`, replace `DB_PASSWORD` with a unique random alphanumeric password. Do not deploy with the example placeholder.
2. Check that the Arcane project storage has enough room for photos and videos. By default uploads use `./library` and PostgreSQL uses `./postgres` below the project directory. Keep the database on local storage, not a network share.
3. Deploy, then open `http://<Docker-Host-IP>:2283` and complete the Immich onboarding.

The project contains four services and is more resource-intensive than a single-container template. Hardware acceleration is not enabled by default. The `IMMICH_PORT`, `UPLOAD_LOCATION` and `DB_DATA_LOCATION` settings can be changed in the project `.env` before deployment.

Sources: [Immich](https://immich.app/), [recommended Docker Compose install](https://docs.immich.app/install/docker-compose/), [upstream Compose file](https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml).
