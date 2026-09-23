# Home Assistant

Container image `homeassistant/home-assistant` wird vom Home Assistant-Projekt auf Docker Hub veröffentlicht. Die Vorlage nutzt Bridge-Netzwerk und veröffentlicht die Weboberfläche auf Port 8123.

## Start

Deployen und anschließend `http://<Docker-Host-IP>:8123` öffnen. Beim ersten Aufruf wird das Benutzerkonto eingerichtet.

Die Konfiguration bleibt im Docker-Volume `home-assistant-config`. Diese schlichte Bridge-Konfiguration benötigt weder privileged mode noch Host-Netzwerk. Geräteerkennung über mDNS/SSDP, Bluetooth, USB-Dongles oder andere Integrationen kann zusätzliche Netzwerk-/Gerätefreigaben benötigen. Solche Freigaben sind absichtlich nicht pauschal aktiviert. Bei Bedarf lässt sich der Host-Port über `HOME_ASSISTANT_PORT` ändern.

Quellen: [Home Assistant](https://www.home-assistant.io/), [Container-Installation](https://www.home-assistant.io/installation/linux/#install-home-assistant-container), [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant).

## English

The Home Assistant project publishes `homeassistant/home-assistant` on Docker Hub. This template uses bridge networking and exposes the web UI on port 8123.

### Start

Deploy the project, then open `http://<Docker-host-IP>:8123`. Create your Home Assistant account on first launch.

Configuration persists in the `home-assistant-config` Docker volume. This simple bridge-mode setup needs neither privileged mode nor host networking. Device discovery through mDNS/SSDP, Bluetooth, USB dongles, and some other integrations may need extra network or device access; these permissions are not enabled by default. Change the host port with `HOME_ASSISTANT_PORT` if needed.

Sources: [Home Assistant](https://www.home-assistant.io/), [container installation](https://www.home-assistant.io/installation/linux/#install-home-assistant-container), [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant).
