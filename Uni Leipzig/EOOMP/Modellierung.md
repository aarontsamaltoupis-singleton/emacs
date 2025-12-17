---
id: Modellierung
aliases:
  - aggregation
  - multiplizitaeten
tags: []
---

[[UML]]: Universal Modelling Language
**Graphische Darstellung des Modells**

# Klassen 

![[Pasted image 20251204132333.png]]

# Vererbung

![[Pasted image 20251204132518.png]]
# Interface
![[Pasted image 20251204132638.png]]
# Aggregation
- **Achtung**: Aggregation hat kein Schlüsselkonzept zur Implementierung in Java
- "Teil-Ganzes Beziehung"
- Ein Objekt kann aus anderen Objekten bestehen, diese Objekte, aus denen das Originalobjekt besteht, können aber auch für sich bestehen

**Beispiel**

![[Pasted image 20251204133027.png]]
- keine gemeinsamen Methoden, gehören aber trotzdem zusammen
- kann bspw durch [[ArrayList]] implementiert werden

## Multiplizitäten

| n    | Interpretation |
| ---- | -------------- |
| n    | genau n        |
| n..m | n bis m        |
| 0..m | höchstens n    |
| n..* | mindestens n   |
| *    | beliebig viele |

Bsp: 
![[Pasted image 20251204133323.png]]
- müssen immer angegeben werden

# Exceptions
- eine selbstgeschriebene Exception kann als Erweiterung der Klasse "Exception" dargestellt werden
- sie hat aber keine Verbindung zu der Methode, die sie aufruft


