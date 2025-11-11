ALLES_GROß
alles_klein
lowerCamelCase
UpperCamelCase

| Objekt                          | Konvention     |             |
| ------------------------------- | -------------- | ----------- |
| Klassen                         | UpperCamelCase | Substantive |
| Methoden                        | lowerCamelCase | Verben      |
| Konstanten                      | ALLES_GROß     |             |
| Attribute, Variablen, Parameter | lowerCamelCase |             |
| package                         | lowerCamelCase |             |

keine Sonderzeichen (Umlaute), auch nicht in den Kommentaren

# Formatierungen
eine "Funktionalität": eine Zeile

## Methoden
jede Methode nur eine Funktionalität

## Packages
- starke Kopplung innerhalb einer package
- schwache kopplung zwischen zwei packages

## Klassen
- Innerhalb einer Klassen starke Kopplung
- zwischen zwei Klassen schwache Kopplung

# Restrukturierung (Refactoring)
- Untermethoden, wenn Methoden zu groß werden
- 