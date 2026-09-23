# Vaultwarden

## English

Vaultwarden is an unofficial, lightweight server compatible with Bitwarden clients. The official upstream image is `vaultwarden/server`.

### Setup and security

- The web vault requires HTTPS (except on localhost). The default host bind is localhost; use a trusted HTTPS reverse proxy for remote access.
- Signups are disabled by default. To create the first account, temporarily set `VAULTWARDEN_SIGNUPS_ALLOWED=true`, register, then set it back to `false` and redeploy.
- Back up the `vaultwarden-data` volume. Never expose its admin interface or data without suitable access controls.

Sources: [Vaultwarden](https://github.com/dani-garcia/vaultwarden), [image and deployment guide](https://github.com/dani-garcia/vaultwarden/wiki).

## Deutsch

Vaultwarden ist ein inoffizieller, ressourcenschonender Server, der mit Bitwarden-Clients kompatibel ist. Das offizielle Upstream-Image ist `vaultwarden/server`.

### Einrichtung und Sicherheit

- Das Web-Vault benötigt HTTPS (außer auf localhost). Standardmäßig ist der Port nur an localhost gebunden; für Fernzugriff einen vertrauenswürdigen HTTPS-Reverse-Proxy verwenden.
- Registrierungen sind standardmäßig deaktiviert. Für das erste Konto `VAULTWARDEN_SIGNUPS_ALLOWED=true` setzen, registrieren und danach wieder auf `false` stellen und redeployen.
- Das Volume `vaultwarden-data` sichern. Admin-Oberfläche und Daten nie ungeschützt erreichbar machen.

Quellen: [Vaultwarden](https://github.com/dani-garcia/vaultwarden), [Image- und Installationsanleitung](https://github.com/dani-garcia/vaultwarden/wiki).
