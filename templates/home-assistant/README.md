# Home Assistant

Container image `homeassistant/home-assistant` wird vom Home Assistant-Projekt auf Docker Hub veröffentlicht. Die Vorlage nutzt Bridge-Netzwerk und veröffentlicht die Weboberfläche auf Port 8123.

## Start

Deployen und anschließend `http://<Docker-Host-IP>:8123` öffnen. Beim ersten Aufruf wird das Benutzerkonto eingerichtet.

Die Konfiguration bleibt im Docker-Volume `home-assistant-config`. Diese schlichte Bridge-Konfiguration benötigt weder privileged mode noch Host-Netzwerk. Geräteerkennung über mDNS/SSDP, Bluetooth, USB-Dongles oder andere Integrationen kann zusätzliche Netzwerk-/Gerätefreigaben benötigen. Solche Freigaben sind absichtlich nicht pauschal aktiviert. Bei Bedarf lässt sich der Host-Port über `HOME_ASSISTANT_PORT` ändern.

Quellen: [Home Assistant](https://www.home-assistant.io/), [Container-Installation](https://www.home-assistant.io/installation/linux/#install-home-assistant-container), [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant).
