# ASCII Art


[Wikipedia: ASCII Art](https://de.wikipedia.org/wiki/ASCII-Art)

>> ASCII-Art (englisch für ASCII-Kunst) ist eine Kunstrichtung, die mit Buchstaben, Ziffern und Sonderzeichen einer nichtproportionalen Schrift kleine Piktogramme oder ganze Bilder darzustellen versucht. 

Mit [ascii_text.py](./ascii_text.py) kann z.b. folgender Schriftzug (Schriftart `univers`) erzeugt werden:

```
  ,ad8888ba,  88888888ba   ad88888ba  88           
 d8"'    `"8b 88      "8b d8"     "8b 88           
d8'           88      ,8P Y8,         88           
88            88aaaaaa8P' `Y8aaaaa,   88           
88      88888 88""""""8b,   `"""""8b, 88           
Y8,        88 88      `8b         `8b 88           
 Y8a.    .a88 88      a8P Y8a     a8P 88           
  `"Y88888P"  88888888P"   "Y88888P"  88888888888
```

Mit [cowsay_text.py](./cowsay_text.py) kann z.b. folgende Ausgabe erzeugt werden:

(Charakter `deamon`)

```
  ____
< GBSL >
  ====
         \
          \
           \
            \  
             /- _  `-/  '
            (/\/ \ \   /\
            / /   | `    \
            O O   ) /    |
            `-^--'`<     '
           (_.)  _  )   /
            `.___/`    /
              `-----' /
 <----.     __ / __   \
 <----|====O)))==) \) /====
 <----'    `--' `.__,' \
              |        |
               \       /
         ______( (_  / \______
       ,'  ,-----'   |        \
       `--{__________)        \/
```

## Voraussetzungen

PIP3 Pakete:
- `pyfiglet` (für ASCII Schriftzüge)
- `cowsay` (für sprechende ASCII Charaktere)
- `inquirer` (für Benutzerabfragen)

```sh
pip3 install pyfiglet cowsay inquirer
```