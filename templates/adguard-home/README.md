# AdGuard Home

## English

Network-wide DNS filtering using the upstream `adguard/adguardhome` image.

1. Check that host ports 53 TCP/UDP are free; an existing resolver may already use them.
2. Open `http://<host-ip>:3000` for first-time setup. After setup, the admin UI is available on host port 3001 (container port 80).
3. Configure clients or your router to use this host for DNS. DHCP is not enabled or published by this template.
4. Back up both persistent volumes. Do not publish the admin UI to the Internet.

Sources: [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome), [official Docker instructions](https://github.com/AdguardTeam/AdGuardHome/wiki/Docker).

## Deutsch

Netzwerkweiter DNS-Filter mit dem Upstream-Image `adguard/adguardhome`.

1. Prüfen, dass TCP/UDP-Port 53 auf dem Host frei ist; oft belegt ihn bereits ein DNS-Dienst.
2. Die Ersteinrichtung unter `http://<Host-IP>:3000` öffnen. Danach ist die Admin-Oberfläche über Host-Port 3001 (Container-Port 80) erreichbar.
3. Clients oder Router so konfigurieren, dass sie diesen Host als DNS-Server verwenden. DHCP ist in dieser Vorlage weder aktiviert noch veröffentlicht.
4. Beide persistenten Volumes sichern. Die Admin-Oberfläche nicht im Internet veröffentlichen.

Quellen: [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome), [offizielle Docker-Anleitung](https://github.com/AdguardTeam/AdGuardHome/wiki/Docker).
