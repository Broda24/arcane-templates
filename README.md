# Arcane Template Registry

Homelab-Sammlung von Compose-Vorlagen für Arcane. Als Image-Quelle sind Docker Official Images auf Docker Hub vorgesehen. Neue Vorlagen werden als Pull Request geprüft, bevor sie in Arcane erscheinen.

## In Arcane einbinden

GitHub-Repository: [`Broda24/arcane-templates`](https://github.com/Broda24/arcane-templates)

1. In Arcane **Customization → Templates → Add Registry** öffnen.
2. Diese Registry-URL hinzufügen:

   ```text
   https://raw.githubusercontent.com/Broda24/arcane-templates/main/registry.json
   ```

3. Vorlage **Nginx – Test-Webserver** wählen, **Create Project** klicken und das Projekt deployen.
4. Im Browser `http://<Docker-Host-IP>:8080` öffnen.

**Create Project** erstellt in Arcane das Compose-Projekt. Zum tatsächlichen Starten ist danach noch der Deploy-/Start-Schritt nötig; bei dieser Nginx-Vorlage sind keine Zugangsdaten oder weiteren Dienste erforderlich. Für produktive Erreichbarkeit müssen Port und Firewall passend konfiguriert sein.

## Repository vorbereiten

`main` ist der in den Registry-URLs verwendete Branch.

## Regeln für Vorlagen

- Nur Docker Official Images aus dem impliziten Docker-Hub-Namespace `library` verwenden (z. B. `nginx:alpine`, `wordpress:...`, `mariadb:...`). Keine fremden Namespaces, GHCR-Images oder selbst gebauten Images.
- In `official-images.txt` sind die konkret freigegebenen Image-Namen allowgelistet. Neue Namen erst nach Prüfung ihres Docker-Official-Status ergänzen; CI weist alle anderen Images zurück.
- Image und Compose-Konfiguration vor Aufnahme anhand der offiziellen Docker-Hub-Seite und Upstream-Dokumentation prüfen.
- Keine Passwörter, Tokens oder sonstige echten Secrets einchecken. `.env.example` enthält nur harmlose Beispielwerte; erforderliche Secrets müssen vor dem Deploy gesetzt werden.
- Bevorzugt stabile Versions-Tags statt `latest` einsetzen. Tags bei einem Update prüfen und die Änderung als PR einreichen.
- Jede Vorlage hat `docker-compose.yml`, `.env.example` und eine kurze README mit Ports, Setup-Schritten und Besonderheiten.
- Keine unnötigen privilegierten Container, Docker-Socket-Mounts oder Host-Netzwerkmodi.

## Geplante nächste Tests

- **WordPress + MariaDB**: praxisnaher Mehr-Container-Test. Benötigt vor dem Start sichere, individuell gesetzte Datenbank-Passwörter und anschließend die WordPress-Ersteinrichtung im Browser; nicht komplett ohne Eingaben.
- **PostgreSQL**: nützlicher Test für persistente Volumes und Secret-Variablen, aber ohne eigene Weboberfläche.
- **Nginx** bleibt der erste Test, weil er nach dem Deploy unmittelbar im Browser erreichbar ist und keine Secrets benötigt.

## Wöchentliche Pflege

Arcane kann Image-Updates für installierte Projekte selbst prüfen. Das ist unabhängig von Änderungen an dieser Registry. Für Vorlagen sollte eine wöchentliche KI-Prüfung zunächst nur einen Pull Request mit geprüften Änderungen erzeugen; automatische Veröffentlichung ungeprüfter Compose- oder Image-Änderungen ist nicht aktiviert.
