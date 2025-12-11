---
id: Zeichenketten
aliases:
  - Regulaere Ausdruecke
  - String
  - Stringbuilder
  - Escape Sequenzen
  - regular expression
tags:
  - Javaspezifisch
---
- zeichen können hinzugefügt und entfernt werden

# String
- unveränderlich
## methoden
### Suche
▶ int indexOf( String str )
▶ int lastIndexOf( String str )
▶ int indexOf( String str, int fromIndex )
▶ int lastIndexOf( String str, int fromIndex )
### Vergleiche 
▶ int compareTo(String str)
- 0: beide gleich
- größer /kleiner 0: zahlen unterschiedlich groß
▶ int compareToIgnoreCase(String str)
▶ boolean equals(String str)
▶ boolean equalsIgnoreCase(String str)
▶ boolean startsWith(String str)
▶ boolean endsWith(String str)
### andere Methoden
▶ String toLowerCase()
▶ String toUpperCase()
▶ String trim()
- entfernt leerzeichen am anfang und ende des Strings
▶ String replace(char oldChar, char newChar)
- ersetze alle vorkommen eines symbols mit einem anderen symbol

# Stringbuilder
- veränderlich
- für Veränderung, Konstruktion von Zeichenketten
## wichtige methoden:
### Veränderung
▶ StringBuilder append(.)
▶ StringBuilder insert(int offset, .)
▶ StringBuilder delete(int start, int end)
▶ StringBuilder replace(int start, int end, String str)

- startposition inklusive, endposition exklusive
### Länge
`int length()`

### Suche

### Sonstige
▶ StringBuilder reverse()
▶ String toString()
▶ String subString(int start, int end)
▶ String subString(int start)



# Escape Sequenzen
Zeichen
`"\\":\`
"\t": Springe n Leerzeichen nach rechte (Tabulator)
"\n": neue Zeile 
"\r": zu beginn der Zeile
`"\\d"` :genau eine Ziffer

Gehe in eine neue Zeile (line feed)
Springe zum Beginn der Zeile (carriage return)
# Reguläre Ausdrücke
"?" 1 oder 0
"+" mindestens 1
`"*" ` beliebig viele (auch 0)

`"[.]"` Punkt
`"."` beliebiges Zeichen
`"\\s"` white space
`"\\w"` Wort-Buchstabe (Ziffer, Buchstabe oder ` "_"`) 

**Beispiele**
`[2,3]` 2 oder 3
`[2-9]` von 2 bis 9
`"\\d.\\d"` zahl der Form ziffer, symbol, ziffer
`"\\d.\\d+"` zahl der Form ziffer, symbol, beliebig viele Ziffern (aber mindestens eine)
`"\\d[.]?\\d*"` zahl, Punkt oder kein PUnkt, beliebig viele Ziffern (auch keine Ziffern möglich)
`"\\d*[.]?\\d*"` beliebige Dezimalzahl


