# Arcane Template Registry

Homelab-Sammlung von Compose-Vorlagen für Arcane. Erlaubt sind Images, die vom jeweiligen App-Projekt gepflegt und in `approved-images.txt` freigegeben sind. Die Images kommen von Docker Hub; Immich nutzt seine offiziellen Upstream-Images von GHCR, da es kein offizielles Immich-Image auf Docker Hub gibt. Neue Vorlagen werden als Pull Request geprüft, bevor sie in Arcane erscheinen.

## In Arcane einbinden

GitHub-Repository: [`Broda24/arcane-templates`](https://github.com/Broda24/arcane-templates)

1. In Arcane **Customization → Templates → Add Registry** öffnen.
2. Diese Registry-URL hinzufügen:

   ```text
   https://raw.githubusercontent.com/Broda24/arcane-templates/main/registry.json
   ```

3. Eine Vorlage wählen, **Create Project** klicken und das Projekt deployen.
4. Die jeweilige Weboberfläche unter Host-IP und Port aus der Vorlagen-README öffnen.

**Create Project** erstellt in Arcane das Compose-Projekt. Zum tatsächlichen Starten ist danach noch der Deploy-/Start-Schritt nötig. Einige Apps benötigen vor dem Deploy noch Secrets oder Medien-/Geräte-Mounts; das steht in der jeweiligen README.

## Repository vorbereiten

`main` ist der in den Registry-URLs verwendete Branch.

## Regeln für Vorlagen

- Nur vom jeweiligen App-Projekt gepflegte Upstream-Images aus Docker Hub oder GHCR verwenden. Kein Image eines Drittanbieters und keine selbst gebauten Images.
- In `approved-images.txt` sind die konkret freigegebenen vollständigen Image-Repositories allowgelistet. Vor Ergänzung den Publisher, die Upstream-Dokumentation und das zugehörige Projekt-Repository prüfen; CI weist alle nicht freigegebenen Images zurück.
- Image und Compose-Konfiguration vor Aufnahme anhand der Container-Dokumentation des Upstreams prüfen. GHCR ist nur für Immich zugelassen, weil Immich dort seine offiziellen Images veröffentlicht.
- Keine Passwörter, Tokens oder sonstige echten Secrets einchecken. `.env.example` enthält nur harmlose Beispielwerte; erforderliche Secrets müssen vor dem Deploy gesetzt werden.
- Bevorzugt stabile Versions-Tags statt `latest` einsetzen. Tags bei einem Update prüfen und die Änderung als PR einreichen.
- Jede Vorlage hat `docker-compose.yml`, `.env.example` und eine kurze README mit Ports, Setup-Schritten und Besonderheiten.
- Jede Vorlage soll projektweite Arcane-Metadaten (`x-arcane.icon` und `x-arcane.urls`) mit Icon, Projekt-Homepage und Upstream-Repository oder Docker-Hub-Seite setzen.
- Keine unnötigen privilegierten Container, Docker-Socket-Mounts oder Host-Netzwerkmodi.

## Enthaltene Vorlagen

- Home Assistant, Jellyfin, Immich, Syncthing, Uptime Kuma, ntfy und Trilium Notes.
- Nginx bleibt die kleinste Testvorlage und zeigt nach dem Deploy sofort die Willkommensseite.

## Wöchentliche Pflege

Arcane kann Image-Updates für installierte Projekte selbst prüfen. Das ist unabhängig von Änderungen an dieser Registry. Für Vorlagen sollte eine wöchentliche KI-Prüfung zunächst nur einen Pull Request mit geprüften Änderungen erzeugen; automatische Veröffentlichung ungeprüfter Compose- oder Image-Änderungen ist nicht aktiviert.
