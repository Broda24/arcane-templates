# Actual Budget

## English

Private budgeting application using the official `actualbudget/actual-server` image. Open `http://localhost:5006` by default and follow the first-run setup. The port is bound to localhost to avoid exposing financial data; use an authenticated HTTPS reverse proxy if remote access is required. Back up the `actual-data` volume regularly.

Sources: [Actual Budget](https://github.com/actualbudget/actual), [official Docker guide](https://actualbudget.org/docs/install/docker/).

## Deutsch

Private Haushaltsbuch-Anwendung mit dem offiziellen Image `actualbudget/actual-server`. Standardmäßig unter `http://localhost:5006` öffnen und die Ersteinrichtung durchführen. Der Port ist zum Schutz der Finanzdaten nur an localhost gebunden; für Fernzugriff einen authentifizierten HTTPS-Reverse-Proxy verwenden. Das Volume `actual-data` regelmäßig sichern.

Quellen: [Actual Budget](https://github.com/actualbudget/actual), [offizielle Docker-Anleitung](https://actualbudget.org/docs/install/docker/).
