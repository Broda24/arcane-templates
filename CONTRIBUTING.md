# Neue Vorlage hinzufügen

1. Einen Ordner unter `templates/<slug>/` anlegen.
2. `docker-compose.yml`, `.env.example` und `README.md` hinzufügen. Im Compose-Root `x-arcane.icon` und `x-arcane.urls` mit Selfh.st-Icon, Homepage und Upstream-Repository hinterlegen.
3. Einen Eintrag in `registry.json` ergänzen. Die URLs müssen auf die Dateien im `main`-Branch zeigen.
4. Prüfen, dass jedes Image vom App-Upstream veröffentlicht wird. Die vollständige Image-Referenz anschließend in `approved-images.txt` freigeben. GHCR-Images nur aufnehmen, wenn das Projekt selbst sie dort veröffentlicht und Docker Hub keine offizielle Alternative anbietet.
5. Compose-Konfiguration anhand der offiziellen Image-Dokumentation prüfen. Für Secrets keine schwachen, festen Default-Passwörter hinterlegen.
6. Pull Request erstellen und die GitHub-Action erfolgreich durchlaufen lassen.

## Arbeitsanweisung für eine KI

> Ergänze die gewünschte Anwendung als neue Arcane-Compose-Vorlage. Verwende nur vom Projekt-Upstream gepflegte Images auf Docker Hub oder – falls das Projekt dort seine offiziellen Images veröffentlicht – GHCR. Prüfe Publisher und Konfiguration anhand der Upstream-Dokumentation. Lege `docker-compose.yml`, `.env.example` und `README.md` unter `templates/<slug>/` an, setze projektweite `x-arcane.icon`- und `x-arcane.urls`-Metadaten, ergänze die exakten Image-Repositories in `approved-images.txt` und trage die Vorlage in `registry.json` ein. Checke keine echten Secrets ein und verwende keine unsicheren Standardpasswörter. Stelle sicher, dass Ports konfigurierbar sind und persistente Daten in benannten Volumes liegen. Führe die CI-Prüfungen aus und liefere die Änderung als Pull Request statt direkt auf `main` zu schreiben. Wenn das Upstream-Image oder notwendige Einrichtung nicht verifiziert werden kann, stoppe und nenne die offenen Punkte statt zu raten.
