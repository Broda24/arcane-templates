# Eclipse Mosquitto

## English

MQTT broker using the official Eclipse Mosquitto Docker image. Set a unique `MQTT_PASSWORD` before deployment. The template creates a password file from the configured user and password and disables anonymous access. Docker administrators can inspect environment values. The default host binding publishes the authenticated broker on all interfaces; restrict it with `MOSQUITTO_BIND` or the host firewall and do not expose it to the public Internet. Back up `mosquitto-data`.

Sources: [Eclipse Mosquitto](https://mosquitto.org/), [official Docker image](https://hub.docker.com/_/eclipse-mosquitto).

## Deutsch

MQTT-Broker mit dem offiziellen Eclipse-Mosquitto-Docker-Image. Vor dem Deploy ein individuelles `MQTT_PASSWORD` setzen. Die Vorlage erzeugt aus Benutzer und Passwort eine Passwortdatei und deaktiviert anonymen Zugriff. Docker-Admins können Umgebungsvariablen einsehen. Standardmäßig wird der authentifizierte Broker auf allen Host-Schnittstellen veröffentlicht; `MOSQUITTO_BIND` oder Host-Firewall einschränken und den Broker nicht öffentlich ins Internet stellen. `mosquitto-data` sichern.

Quellen: [Eclipse Mosquitto](https://mosquitto.org/), [offizielles Docker-Image](https://hub.docker.com/_/eclipse-mosquitto).
