# Nginx – Test-Webserver

Ein möglichst einfacher Funktionstest für die Arcane-Registry. Das Projekt nutzt das Docker Official Image `nginx` von Docker Hub und zeigt nach dem Start die Nginx-Willkommensseite.

## Starten

1. In Arcane **Customization → Templates** öffnen und diese Vorlage auswählen.
2. **Create Project** klicken.
3. Das Projekt deployen/starten.
4. Im Browser `http://<IP-Adresse-des-Docker-Hosts>:8080` öffnen.

Wenn Port 8080 bereits belegt ist, den Host-Port in der Projekt-`.env` über `NGINX_PORT` ändern. Der Port muss außerdem in der Host-/Proxmox-Firewall erreichbar sein, wenn du von einem anderen Gerät darauf zugreifen möchtest.

Die Vorlage startet einen Webserver, aber keine eigene Anwendung mit Login oder persistenten Nutzdaten. Sie eignet sich deshalb als erster Registry-Test.
