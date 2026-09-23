# Homebox

## English

Home inventory and asset tracker using the upstream GHCR image. Generate a unique pepper (for example, `openssl rand -base64 48`) and set `HOMEBOX_API_KEY_PEPPER` before deployment. The web UI is bound to localhost by default; use an authenticated HTTPS reverse proxy before allowing remote access. Persistent application data is stored in `homebox-data`.

Sources: [Homebox](https://github.com/sysadminsmedia/homebox), [project website](https://homebox.software/).

## Deutsch

Inventar- und Geräteverwaltung für den Haushalt mit dem Upstream-Image auf GHCR. Vor dem Deploy einen individuellen Pepper erzeugen (z. B. `openssl rand -base64 48`) und als `HOMEBOX_API_KEY_PEPPER` setzen. Die Weboberfläche ist standardmäßig nur an localhost gebunden; vor Fernzugriff einen authentifizierten HTTPS-Reverse-Proxy verwenden. Anwendungsdaten liegen persistent in `homebox-data`.

Quellen: [Homebox](https://github.com/sysadminsmedia/homebox), [Projektseite](https://homebox.software/).
