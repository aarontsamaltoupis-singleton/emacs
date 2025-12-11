---
id: Datenstruktur Trie
aliases: []
tags: []
---
#Datenstruktur
Vergleiche [[/Uni Leipzig/Automaten und Sprachen/Grundlegende Begriffe]]

- effiziente Speicherung von wörtern
- 
knoten, kanten folgen aufeinander
- kanten legen fest, wie wort aussieht
- jede Kante hat genau einen Knoten 
- 
vollständige wörter repräsentiert durch das ende der knoten

vergleiche: [[Grundlegende Begriffe#Präfix]]:


# TrieTreeNode, TrieTreeEdge
Klassen
TrieTreeNode
TrieTreeEDdge
- jeder Knoten gehört zu genau einer, oder keiner (Wurzel) Kante
- Es gibt zwischen 0 und 26 Kanten in TrieTreeNode gespeichert

# TrieNode
komprimieren der Klasse in eine Klasse: 
**TrieNode**
 - Klasse wird in sich selbst [[Aggregation|aggregiert]]: [[Rekursion]]

# Trie
**Klasse Trie** baut sich rekursiv aus Instanzen von  der Klasse **TrieNodes** auf
- jedem Buchstaben (Character) wird dabei eine TrieNode in einer [[TreeMap]] zugeordnet
- 

## rekursivität: 
- in der Trie Klasse wird **root** als erste Instanz von **TrieNode** deklariert.
- 


	![[Pasted image 20251203154448.png]]
	- Suchanfrage sind immer max. so lange wie das Wort
		- vergleiche Wörterbuch: 
	- ob ein wort im Trie ist oder nicht, ist ersichtlich am wordcount


# Ablauf der Methoden
## successor map
- speichert für jeden Buchstaben die dazugehörige Instanz einer TrieNode, wenn sie denn existiert

##  +add(word:String):void
- prefix count wird um 1 erhöht
 	- ein neues Wort wird hinzugefügt: selbst wenn die Node für den geraden betrachteten Buchstaben bereits vorhanden ist, wird das Teilwort bis zu diesem Buchstaben schlussendlich Präfix eines neuen Wortes sein.
	  	- *Frage: Was wenn exakt dasselbe Wort hinzugefügt wird, dass bereits enthalten ist, ist es nicht falsch, wenn auch dann jedes Mal der Prefix Count erhöht wird*
- wenn word keine buchstaben  enthält  muss die Methode ncihts machen, der wordcount wird um 1 erhöht
- Sei das word enthält Buchstaben, ist nciht leer.
	- es wird nur der erste Buchstabe (index 0)  betrachtet
	- es wird überprüft, ob dieser Buchstabe bereits eine TrieNode hat
	- wenn er noch keine TrieNode hat, wird eine neue Instanz von TrieNode erstellt und zusammen mit diesem Buchstaben in die TrieMap getan
	- wenn er bereits eine TrieNode hat muss nichts getan werden
	- es wird dann das word ohne den ersten buchstaben betrachtet
		- **rekursivität**




+getWordCount(word:String):int
- gibt aus, wie oft ein wort im Trie vorhanden ist

+getPrefixCount()

