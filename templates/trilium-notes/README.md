# Trilium Notes / TriliumNext

Das frühere Trilium wird als TriliumNext weiterentwickelt. Das aktuelle Upstream-Projekt veröffentlicht `triliumnext/trilium` selbst auf Docker Hub. Die Datenbank und Notizen bleiben im Volume `trilium-data`.

## Start

Deployen und `http://<Docker-Host-IP>:8080` öffnen. Beim ersten Aufruf den Serverzugang einrichten. Trilium ist für eine einzelne Person mit synchronisierten Geräten gedacht, nicht für gleichzeitiges Multi-User-Editing. Die Datenbank nicht auf einen Netzwerk-Mount legen.

Port und Zeitzone lassen sich über die Projekt-`.env` anpassen.

Quellen: [TriliumNext](https://triliumnotes.org/), [Projekt-Repository](https://github.com/TriliumNext/Trilium), [Docker Hub](https://hub.docker.com/r/triliumnext/trilium).
