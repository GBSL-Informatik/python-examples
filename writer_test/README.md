# Schreibmaschinen Test

[Schreibgeschiwndigkeit 10-Fingersystem](https://de.wikipedia.org/wiki/Zehnfingersystem#Schreibgeschwindigkeit)

>> Die erreichbare Schreibgeschwindigkeit ist von der Trainingszeit sowie der persönlichen Fähigkeit abhängig. Geübte ZehnfingerschreiberInnen erreichen bei einem 10-Minuten-Test 200 bis 400 Anschläge pro Minute. Auf internationalen Wettbewerben werden derzeit bis zu 900 Anschläge pro Minute erreicht. Dabei zählt auch das Anschlagen der Umschalttaste und jeder anderen Taste mit, z. B. Akzente bei französischen Texten.
>> Im Training können SpitzenschreiberInnen Ergebnisse von mehr als 1200 Anschläge/min leisten. Selbst damit liegt ihre Datenerfassungsrate noch immer deutlich niedriger als dies mit der Stenografie erreichbar ist.

Gibt in der Kommandozeile die aktuellen Tastenanschläge / Minute aus.

## Voraussetzungen

PIP3 Pakete:
- `pynput` (Text zu Sprache umwandeln)


```sh
pip3 install --user pynput
```

!! Unter OSX muss nach dem ersten Start dem Terminal die Berechtigung fürs Abfragen der Tastenanschläge gegeben werden: `Systemeinstellungen > Sicherheit > Datenschutz > Input-Monitoring` das Häkchen bei `Terminal` setzen.