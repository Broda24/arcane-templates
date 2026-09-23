# Zigbee2MQTT

## English

Bridge Zigbee devices to an MQTT broker using the upstream GHCR image.

1. Connect a supported Zigbee coordinator and set `ZIGBEE_ADAPTER` to its host device path before deployment.
2. Deploy an MQTT broker first (the Mosquitto template is provided separately); set `ZIGBEE_MQTT_SERVER`, `ZIGBEE_MQTT_USER`, and `ZIGBEE_MQTT_PASSWORD` to match it. Use the Docker host's LAN IP and broker port when the services are separate projects.
3. The frontend is bound to localhost by default because it has no authentication configured here. Use a protected reverse proxy for remote access.
4. Back up `zigbee2mqtt-data` and keep a copy of the coordinator's IEEE address and network key.

Sources: [Zigbee2MQTT](https://github.com/Koenkk/zigbee2mqtt), [official Docker installation guide](https://www.zigbee2mqtt.io/guide/installation/).

## Deutsch

Verbindet Zigbee-Geräte über das Upstream-Image auf GHCR mit einem MQTT-Broker.

1. Einen unterstützten Zigbee-Koordinator anschließen und `ZIGBEE_ADAPTER` vor dem Deploy auf dessen Host-Gerätepfad setzen.
2. Zuerst einen MQTT-Broker bereitstellen (die Mosquitto-Vorlage ist separat vorhanden); `ZIGBEE_MQTT_SERVER`, `ZIGBEE_MQTT_USER` und `ZIGBEE_MQTT_PASSWORD` passend konfigurieren. Bei getrennten Projekten die LAN-IP des Docker-Hosts und den Broker-Port verwenden.
3. Das Frontend ist mangels vorkonfigurierter Anmeldung standardmäßig nur an localhost gebunden. Für Fernzugriff einen geschützten Reverse-Proxy verwenden.
4. `zigbee2mqtt-data` sichern und IEEE-Adresse sowie Netzwerkschlüssel des Koordinators aufbewahren.

Quellen: [Zigbee2MQTT](https://github.com/Koenkk/zigbee2mqtt), [offizielle Docker-Installationsanleitung](https://www.zigbee2mqtt.io/guide/installation/).
