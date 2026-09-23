# Jellyfin

Jellyfin veröffentlicht und dokumentiert sein eigenes Docker-Hub-Image `jellyfin/jellyfin`. Die Vorlage verwendet Bridge-Netzwerk, persistente Konfigurations-/Cache-Volumes und ein leeres, zunächst read-only eingebundenes Medien-Volume.

## Start

Deployen und `http://<Docker-Host-IP>:8096` öffnen. Der Einrichtungsassistent führt durch die Ersteinrichtung. Das Volume `jellyfin-media` ist an `/media` eingebunden, enthält nach der Installation aber noch keine Dateien.

Für bereits vorhandene Medien die Vorlage an den eigenen Medienpfad anpassen oder in Arcane einen passenden Ordner als Mount auf `/media` einbinden. Hardware-Transkodierung ist nicht voreingestellt und benötigt passende Gerätefreigaben. DLNA-Erkennung erfordert laut Jellyfin Host-Netzwerk; diese Vorlage veröffentlicht stattdessen die normalen Web-/Streaming-Ports im Bridge-Netz.

Quellen: [Jellyfin](https://jellyfin.org/), [offizielle Container-Dokumentation](https://jellyfin.org/docs/general/installation/container/), [Docker Hub](https://hub.docker.com/r/jellyfin/jellyfin).
