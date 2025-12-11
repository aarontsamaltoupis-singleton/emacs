---
id: Rekursion
aliases: []
tags: []
---

- langsamer als Iterativ, ist aber möglichkeit bestimmte Funktionen, wie Ackermann- Funktion zu berechnen

Beispiel Fakultät: (funktionale rekursion)
```
public static final fakultaetRecursive(final long n){
	if (n>1){
		// rekursiver Aufruf
		return n*fakultaetRecursive(n-1);
	}
	else{
		//Basisfall
		return 1;
	}
}
```
- Basisfall im else
	- Werte kleiner 1 springen somit auch in den Basisfall


Beispiel odd even
$\text{odd}(n)=\begin{cases} \text{true}: n=1 \\\text{even}(n-1): n>1 \\ \end{cases}$

$\text{even}(n)=\begin{cases} \text{false}: n=1 \\\text{odd}(n-1): n>1 \\ \end{cases}$

```
public static boolean odd(final int n){
	if (n>1){
		return even(n-1);
	}
	else{
		return true
	}
}

public static boolean even(final int n){
	if (n>1){
		return odd(n-1);
	}
	else{
		return false
	}
}
```

# funktionale rekursion (Übung)
- methoden, die sich selber aufrufen

1. Abbruchbedingung
- 
2. Rekursiver schritt

## beispiel


# iteration
- jedes rekursive problem kann auch iterativ gelöst werden
- problem wird über wiederholge Schleifen gelöst
- schnell unübersichtlich

# rekursive datentypen
bspw [[Datenstruktur Trie]]

- Datentyp, die sich selbst/eine Instanz von sich als Attribut enthält
- benötigt keine Abbruchbedingung
- 

## Beispiel verkettete Liste
- jeder knoten enthält daten und verweis auf den nächsten knoten
- kette geht so lange, bis ein knoten auf den WErt null verweist
- es gibt hier kein äquivalent zu einem 'root' Knoten. Der erste Knoten verweist einfach auf einen Knoten, der noch nicht initialisiert wurde, also den Wert null hat.
