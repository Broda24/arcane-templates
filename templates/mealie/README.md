# Mealie

## English

Self-hosted recipe manager and meal planner using the upstream Mealie image on GHCR.

Open `http://<host-ip>:9925` and create the first administrator account. New-account signup is enabled by default for initial setup; disable `MEALIE_ALLOW_SIGNUP` after creating accounts if public registration is not wanted. Back up the `mealie-data` volume.

Sources: [Mealie](https://github.com/mealie-recipes/mealie), [installation documentation](https://docs.mealie.io/documentation/getting-started/installation/).

## Deutsch

Selbst gehostete Rezeptverwaltung und Essensplanung mit dem offiziellen Mealie-Image auf GHCR.

`http://<Host-IP>:9925` öffnen und das erste Administratorkonto erstellen. Für die Ersteinrichtung ist die Registrierung standardmäßig aktiviert; danach `MEALIE_ALLOW_SIGNUP` deaktivieren, falls keine offene Registrierung gewünscht ist. Das Volume `mealie-data` sichern.

Quellen: [Mealie](https://github.com/mealie-recipes/mealie), [Installationsdokumentation](https://docs.mealie.io/documentation/getting-started/installation/).
