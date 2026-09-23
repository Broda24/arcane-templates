# Nginx – Test-Webserver

Ein möglichst einfacher Funktionstest für die Arcane-Registry. Das Projekt nutzt das Docker Official Image `nginx` von Docker Hub und zeigt nach dem Start die Nginx-Willkommensseite.

## Starten

1. In Arcane **Customization → Templates** öffnen und diese Vorlage auswählen.
2. **Create Project** klicken.
3. Das Projekt deployen/starten.
4. Im Browser `http://<IP-Adresse-des-Docker-Hosts>:8080` öffnen.

Wenn Port 8080 bereits belegt ist, den Host-Port in der Projekt-`.env` über `NGINX_PORT` ändern. Der Port muss außerdem in der Host-/Proxmox-Firewall erreichbar sein, wenn du von einem anderen Gerät darauf zugreifen möchtest.

Die Vorlage startet einen Webserver, aber keine eigene Anwendung mit Login oder persistenten Nutzdaten. Sie eignet sich deshalb als erster Registry-Test.

## English

This is a minimal smoke test for the Arcane registry. It uses the Docker Official Image `nginx` from Docker Hub and displays the default Nginx welcome page.

### Start

1. In Arcane, open **Customization → Templates** and select this template.
2. Click **Create Project**.
3. Deploy/start the project.
4. Open `http://<Docker-host-IP>:8080` in a browser.

If port 8080 is already in use, change `NGINX_PORT` in the project `.env`. The port must also be allowed by the host/Proxmox firewall for access from another device. This template starts only a web server, with no login or persistent application data, making it a good first registry test.
