# Snowman Meltdown

Ein kleines Python-Lernprojekt rund um Spiel-Logik, Modulstruktur und Versionskontrolle mit Git.

## Projektidee

**Snowman Meltdown** ist ein einfaches Wortspiel im Stil von Hangman: Ein geheimes Wort wird zufällig gewählt, der Spieler errät Buchstaben, und bei jeder falschen Eingabe schmilzt die ASCII-Figur ein Stück weiter.

Das Projekt eignet sich gut, um folgende Grundlagen praktisch zu üben:

- Arbeiten mit Python-Funktionen und Modulen
- Eingabevalidierung in der Konsole
- Schleifen und Zustandslogik
- Trennung von Daten und Spiellogik
- Git-Workflows mit add, commit und push

## Dateistruktur

```text
Snowman-Meltdown/
├── ascii_art.py
├── game_logic.py
├── snowman.py
└── README.md
```

### ascii_art.py

Enthält die visuellen Spielphasen als ASCII-Art. Jede Phase steht für einen Fehlerstand. Je mehr Fehler gemacht werden, desto weiter schmilzt die Figur.

### game_logic.py

Enthält die Kernlogik des Spiels:

- Auswahl eines Zufallsworts
- Anzeige des aktuellen Spielzustands
- Prüfung von Eingaben
- Zählen von Fehlern
- Gewinn- und Verlustbedingungen
- Optionale Wiederholung einer Runde

### snowman.py

Startdatei des Spiels. Diese Datei importiert die Spiel-Funktion und startet die Anwendung.

## Spiellogik

Die Spiellogik folgt einem einfachen, gut nachvollziehbaren Ablauf:

1. Das Spiel wählt zufällig ein geheimes Wort aus einer Wortliste.
2. Eine leere Sammlung für geratene Buchstaben wird angelegt.
3. Der Fehlerzähler startet bei 0.
4. In jeder Runde wird der aktuelle Zustand angezeigt:
   - ASCII-Art passend zur Anzahl der Fehler
   - das Wort mit Unterstrichen für unbekannte Buchstaben
   - bereits geratene Buchstaben
   - aktueller Fehlerstand
5. Der Spieler gibt einen Buchstaben ein.
6. Die Eingabe wird geprüft:
   - nur ein einzelner Buchstabe ist erlaubt
   - keine Zahlen oder Sonderzeichen
   - bereits geratene Buchstaben werden erkannt
7. Wenn der Buchstabe im Wort vorkommt, wird er gespeichert.
8. Wenn der Buchstabe nicht vorkommt, wird der Fehlerzähler erhöht.
9. Das Spiel endet, wenn:
   - alle Buchstaben im Wort erraten wurden, oder
   - die maximale Anzahl an Fehlern erreicht ist.
10. Optional kann danach eine neue Runde gestartet werden.

## Beispiel für den Spielzustand

```text
==============================
  ___
 /___\\
 (o o)
 ( : )
 ( : )

Word: _ _ _ _ _ _ _
Guessed letters: a e
Mistakes: 1/6
==============================
```

## ASCII-Art: Snowman, Snowwoman und Snowsomething

Die ASCII-Art ist nicht nur Deko, sondern ein Teil des Feedback-Systems. Sie zeigt direkt, wie nah das Spiel am Verlust ist.

### Klassischer Snowman

```text
  ___
 /___\\
 (o o)
 ( : )
 ( : )
```

### Snowwoman

```text
  ___
 /___\\
 (^ ^)
 ( : )
 /( : )\\
   " "
```

### Snowsomething

Für alle Fälle, in denen sich der Schneekörper nicht auf binäre Winterrollen festlegen möchte:

```text
   ___
 _/???\\_
 (o_O)
 <( : )>
  /   \\
```

### Humorvolle Idee für spätere Erweiterung

Statt nur eine Figur schmelzen zu lassen, könnte das Spiel künftig unterschiedliche Charaktere anbieten:

- **Snowman** – der Klassiker, stoisch und rund
- **Snowwoman** – elegant, gelassen, leicht genervt von falschen Buchstaben
- **Snowsomething** – avantgardistisch, geheimnisvoll und definitiv zu cool für lineare Wortlisten

Jede Figur könnte eigene ASCII-Phasen, Siegtexte und Niederlagen-Sprüche erhalten.

## Mögliche Erweiterungen

### 1. Erweitertes Menü

Ein Startmenü könnte vor dem Spiel folgende Optionen anbieten:

- Spiel starten
- Charakter wählen
- Wortkategorie wählen
- Schwierigkeit wählen
- Hilfe anzeigen
- Spiel beenden

### 2. Optionale Charaktere

Geplante Auswahl:

- Snowman
- Snowwoman
- Snowsomething

Technisch könnte jeder Charakter eine eigene Liste von `STAGES` bekommen, zum Beispiel in separaten Dateien oder in einem verschachtelten Dictionary.

### 3. Wortlisten aus verschiedenen Bereichen

Statt nur einer kleinen Standardliste könnte das Spiel mehrere Kategorien unterstützen, zum Beispiel:

- Python und Programmierung
- Git und GitHub
- Winter und Wetter
- Tiere
- Filme und Popkultur
- Zufallsauswahl über alle Kategorien

Beispielstruktur:

```python
WORDS = {
    "python": ["function", "module", "variable"],
    "git": ["commit", "branch", "remote"],
    "winter": ["snow", "icicle", "blizzard"]
}
```

### 4. Web-App-Version

Eine lauffähige Web-App wäre ein sehr guter nächster Entwicklungsschritt. Dafür könnte das Spiel mit HTML, CSS und JavaScript oder mit Python plus Flask umgesetzt werden.

Mögliche Web-App-Features:

- Schöne visuelle Darstellung statt reiner Konsole
- Buttons für Buchstaben statt Texteingabe
- Auswahl von Charakteren und Kategorien
- Highscore oder Statistik
- Mobile Darstellung
- Teilen eines Spiels per Link

## Vermarktungsidee

Falls aus dem Lernprojekt ein kleines Portfolio- oder Showcase-Projekt werden soll, könnte die Web-App so positioniert werden:

### Zielgruppen

- Python-Einsteiger
- Lehrkräfte und Coaches
- Coding-Bootcamps
- Eltern mit Kindern
- Fans kleiner Browser-Games

### Mögliche Positionierung

- "Spielerisch Python und Logik lernen"
- "Ein charmantes Lernspiel mit Git- und Python-Fokus"
- "Ein humorvolles Open-Source-Miniprojekt für Unterricht, Portfolio und Web"

### Denkbare Marketing-Bausteine

- README mit Screenshots und GIFs
- GitHub Pages oder kleines Hosting für die Web-App
- Kurzes Demo-Video
- LinkedIn-Post oder Mastodon-Post zum Lernfortschritt
- Portfolio-Eintrag mit Roadmap und Lessons Learned

## ToDos

- Erweiterte Menüführung implementieren
- Charakterauswahl für Snowman, Snowwoman und Snowsomething einbauen
- Eigene ASCII-Phasen für alle Charaktere ergänzen
- Wortlisten nach Kategorien strukturieren
- Zufallsauswahl für Kategorien ergänzen
- Schwierigkeitssystem einbauen
- Web-App-Version entwickeln
- UI/UX für Browser und Mobilgeräte gestalten
- Projekt mit Screenshots und Demo besser dokumentieren
- Deployment und Vermarktung vorbereiten

## Spiel starten

Wenn die Python-Dateien vorhanden sind, kann das Spiel im Projektordner gestartet werden mit:

```bash
python snowman.py
```

## Entwicklungshinweis

Dieses Projekt ist bewusst klein gehalten, damit der Fokus auf Lernfortschritt, sauberer Struktur und iterativer Verbesserung liegt. Gerade dadurch eignet es sich gut als Basis für Refactoring, Modularisierung und spätere Erweiterungen.