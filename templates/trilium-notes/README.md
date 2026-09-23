# Trilium Notes / TriliumNext

Das frühere Trilium wird als TriliumNext weiterentwickelt. Das aktuelle Upstream-Projekt veröffentlicht `triliumnext/trilium` selbst auf Docker Hub. Die Datenbank und Notizen bleiben im Volume `trilium-data`.

## Start

Deployen und `http://<Docker-Host-IP>:8080` öffnen. Beim ersten Aufruf den Serverzugang einrichten. Trilium ist für eine einzelne Person mit synchronisierten Geräten gedacht, nicht für gleichzeitiges Multi-User-Editing. Die Datenbank nicht auf einen Netzwerk-Mount legen.

Port und Zeitzone lassen sich über die Projekt-`.env` anpassen.

Quellen: [TriliumNext](https://triliumnotes.org/), [Projekt-Repository](https://github.com/TriliumNext/Trilium), [Docker Hub](https://hub.docker.com/r/triliumnext/trilium).

## English

The original Trilium project continues as TriliumNext. The current upstream project publishes `triliumnext/trilium` on Docker Hub. The database and notes persist in the `trilium-data` volume.

### Start

Deploy the project and open `http://<Docker-host-IP>:8080`. Set up server access on first launch. Trilium is designed for one person syncing across devices, not simultaneous multi-user editing. Do not place its database on a network mount.

Change the port and timezone in the project `.env` if needed.

Sources: [TriliumNext](https://triliumnotes.org/), [project repository](https://github.com/TriliumNext/Trilium), [Docker Hub](https://hub.docker.com/r/triliumnext/trilium).
