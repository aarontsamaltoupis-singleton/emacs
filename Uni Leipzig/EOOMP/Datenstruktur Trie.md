---
aliases:
---
#Datenstruktur
Vergleiche [[Grundlegende Begriffe]]

- effiziente Speicherung von wörtern
- 
knoten, kanten folgen aufeinander
- kanten legen fest, wie wort aussieht
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
Trie baut sich rekursiv aus Instanzen von  TrieNodes auf
Klasse: 
Trie 
	- root des Trie


![[Pasted image 20251203154448.png]]
- Suchanfrage sind immer max. so lange wie das Wort
	- vergleiche Wörterbuch: 
- ob ein wort im Trie ist oder nicht, ist ersichtlich am wordcount

+add(word:String):void
- fügt ein Wort dem Trie hinzu

+getWordCount(word:String):int
- gibt aus, wie oft ein wort im Trie vorhanden ist

+getPrefixCount()

