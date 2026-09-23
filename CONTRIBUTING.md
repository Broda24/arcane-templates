# Neue Vorlage hinzufügen

1. Einen Ordner unter `templates/<slug>/` anlegen.
2. `docker-compose.yml`, `.env.example` und `README.md` hinzufügen.
3. Einen Eintrag in `registry.json` ergänzen. Die URLs müssen auf die Dateien im `main`-Branch zeigen.
4. Prüfen, dass sämtliche Images Docker Official Images aus Docker Hub sind. In Compose wird dafür der implizite `library`-Namespace ohne Slash verwendet, z. B. `nginx:alpine`. Den geprüften Image-Namen anschließend in `official-images.txt` freigeben.
5. Compose-Konfiguration anhand der offiziellen Image-Dokumentation prüfen. Für Secrets keine schwachen, festen Default-Passwörter hinterlegen.
6. Pull Request erstellen und die GitHub-Action erfolgreich durchlaufen lassen.

## Arbeitsanweisung für eine KI

> Ergänze die gewünschte Anwendung als neue Arcane-Compose-Vorlage. Verwende ausschließlich Docker Official Images aus Docker Hub (impliziter `library`-Namespace; keine anderen Registries oder Namespaces). Verifiziere jedes Image und seine Konfiguration anhand der offiziellen Docker-Hub-Seite und der Upstream-Dokumentation. Lege `docker-compose.yml`, `.env.example` und `README.md` im Ordner `templates/<slug>/` an und ergänze `registry.json` exakt nach dem bestehenden Muster. Checke keine echten Secrets ein und verwende keine unsicheren Standardpasswörter. Stelle sicher, dass Ports konfigurierbar sind und persistente Daten in benannten Volumes liegen. Führe die CI-Prüfungen aus und liefere die Änderung als Pull Request statt direkt auf `main` zu schreiben. Wenn Docker-Official-Status, notwendige Einrichtung oder ein sicherer Start nicht verifiziert werden können, stoppe und nenne die offenen Punkte statt zu raten.
