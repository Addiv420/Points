# Punkte

Ein textbasiertes Abenteuer-Spiel, bei dem der Spieler tief in ein Dungeon vordringt, um Gegner zu besiegen und Herausforderungen zu meistern. Das Spiel bietet ein einfaches Level-Up-System, Kämpfe gegen Gegner und Bosse sowie die Möglichkeit, das Spiel jederzeit zu beenden oder neu zu starten.

## Installation

### Voraussetzungen

- Python 3.x
- msvcrt (für Windows-Nutzer)

### Installation und Ausführung

1. **Klonen des Repositories**:
    ```bash
    git clone https://github.com/dein-benutzername/dungeon-adventure-game.git
    cd Punkte
    ```

2. **Spiel starten**:
    Nach dem Klonen des Repositories, einfach das Skript ausführen:
    ```bash
    python Punkte.py
    ```

### Hinweis für Windows-Nutzer:
Das Spiel nutzt die `msvcrt`-Bibliothek für Tastatureingaben. Dies bedeutet, dass es auf Windows-Plattformen ausgeführt werden muss. Auf Linux und macOS könnte eine alternative Lösung erforderlich sein.

## Spielprinzip

Das Spiel ist ein textbasiertes Dungeon-Crawler-Abenteuer, bei dem der Spieler auf verschiedene Gegner trifft, die bekämpft werden müssen, um im Dungeon tiefer vorzudringen und Erfahrungen zu sammeln.

**Ziel:**  
- Gehe so tief wie möglich in das Dungeon.
- Besiege Gegner und Bosse, um Erfahrungspunkte zu erhalten.
- Steige im Level auf und verbessere deine Fähigkeiten.
- Vermeide Fehlschläge und steige bei Bedarf neu ein.

## Steuerung

- **[W]**: Gehe vorwärts in das Dungeon.
- **[S]**: Gehe zurück.
- **[Quit]**: Beendet das Spiel.
- **[J]**: Startet das Spiel neu, wenn du verloren hast.
- **[N]**: Beendet das Spiel, wenn du verloren hast.
- **Angriff**: Wähle eine Angriffstaste aus den verfügbaren (z.B. [Y], [X], [C], etc.).
- **Ausweichen**: Wähle eine der vier möglichen Ausweich-Tasten aus ([Q], [E], [A], [D]).

## Spielablauf

1. **Dungeon-Tiefe und Gegner**:  
   Du beginnst auf Ebene 0 des Dungeons. Jede Ebene ist mit einem zufälligen Gegner oder einem Boss versehen.

2. **Kämpfe gegen Gegner**:  
   Wenn du einen Gegner triffst, musst du die richtige Angriffstaste drücken, um den Gegner zu besiegen. Bei Fehlschlag verlierst du das Spiel und musst entscheiden, ob du einen neuen Versuch starten möchtest.

3. **Bosskämpfe**:  
   Wenn du das Ende des Dungeons erreichst, trittst du gegen einen Boss an. Du musst Angriffstasten korrekt drücken und gleichzeitig den Angriffen des Bosses ausweichen, um zu überleben.

4. **Level-Up**:  
   Wenn du genug Erfahrungspunkte sammelst, steigerst du dein Level und erhältst mehr Kraft, um tiefere Ebenen zu erreichen.

5. **Verlieren und Neustart**:  
   Wenn du stirbst, kannst du das Spiel neu starten oder aufhören. Es gibt auch einen Cheat-Code, den du mit der Eingabe „nuh uh“ aktivieren kannst.

## Farben

Das Spiel nutzt Farben, um den Text hervorzuheben:

- **Grün**: Zeigt positive Ereignisse wie Level-Up oder Angriffserfolge an.
- **Rot**: Zeigt Fehlschläge oder Gegner an.
- **Gelb**: Wird für Hinweise und Statusanzeigen verwendet.

## Funktionen

- **Punkte**: Dein Fortschritt im Dungeon wird in Punkten gemessen.
- **Level**: Dein Charakter steigt im Level auf und wird stärker.
- **Erfahrung**: Du sammelst Erfahrungspunkte, indem du Gegner besiegst und Herausforderungen meisterst.
- **Bosskämpfe**: Am Ende jeder Dungeon-Tiefe kämpfst du gegen einen Boss, um weitere Punkte und Erfahrung zu sammeln.
- **Tasteneingaben**: Um das Spiel zu steuern, drücke Tasten für Bewegung, Angriff und Ausweichen.

## Beispiel für das Spiel:

