# StreckenRadar

Kompakte Web-App (PWA) für iPhone im Hochformat, außerdem im Browser am PC nutzbar.

## Funktionen
- Amtliche Verkehrshinweise für GPS-Position oder einen manuell eingegebenen Startpunkt.
- Strecke zur Arbeit, Strecke nach Hause oder Umgebung.
- Wohn- und Startadresse werden nicht in GitHub gespeichert. Persönliche Ziele werden erst auf dem Gerät im Browser eingegeben und dort lokal gespeichert.
- Stationäre Blitzermessstellen können **nur auf ausdrücklichen Knopfdruck vor Fahrtbeginn** aus OpenStreetMap abgefragt werden.
- Für aktuelle **mobile** Blitzer steht ein Link zu einer externen Meldeseite bereit. Die App selbst hat **keine** verlässliche Live-Datenquelle für mobile Blitzer.

## GitHub Pages einmalig aktivieren
Repository → **Settings** → **Pages** → **Build and deployment** → Source: **Deploy from a branch** → Branch: **main**, Folder: **/(root)** → **Save**.

Adresse nach der Veröffentlichung: https://bernd72.github.io/StreckenRadar/

## Verkehrssicherheit und Datenschutz
Nach § 23 Abs. 1c StVO darf die Blitzerwarnfunktion beim Führen eines Fahrzeugs nicht benutzt werden. Die Messstellenabfrage ist deswegen nur für die Information **vor** der Fahrt vorgesehen.

Die App übermittelt notwendige Koordinaten an den Routing-Dienst und beim manuellen Abruf stationärer Blitzer an einen OpenStreetMap-Datendienst. Adresssuchen senden die Suchanfrage an externe Geocoding-Dienste. Gespeicherte Angaben bleiben ansonsten lokal im Browser.

Hinweise zu Verkehrsstörungen und Messstellen sind nicht vollständig oder garantiert aktuell. Es wird kein zuverlässiges Live-Stauradar angeboten.

Quellen: MobiData BW, Verkehrsservice Hessen, Autobahn GmbH, © OpenStreetMap-Mitwirkende (ODbL).
