---
aliases:
  - Linearkombinationen
  - linear unabhaengig
  - Basis
  - Standartbasis
---
#Grabowski 
Sei $\mathbb{K}$ ein [[Körper]]. Ein Vektorraum über K ist ein Tupel $(V,+,\mu)$, wobei $+:V\times V\to V$ und $\mu :K\times V\to V$ mit folgenden Eigenschaften:

- + ist kommutativ, assotiativ und hat neutrales, inverses Element
- $\mu$ ist assotiativ, distr gegenüber + in K und gegenüber + in V und $\forall v\in V: 1\cdot v=v$
# Linearkombinationen
Sei V ein Vektorraum und seien $v_{1},v_{2},\dots v_{p}\in V$ Vektoren.
Eine Linearkombination dieser Vektoren ist eine Summe der Form
$a_{1}v_{1}+a_{2}v_{2}+\dots+a_{p}v_{p} = \sum\limits^{ p}_{k=1}a_{k}v_{k}$
, wobei $a_{i}\in \mathbb{K}$

# Basis
die Vektoren $v_{1},..,v_{n}\in V$ sind eine **Basis** von V, wenn jeder Vektor $v\in V$ eine **eindeutige** Darstellung als Linearkombination der Basisvektoren hat.
- Die Koeffizienten $a_{1},\dots,a_{n}$ sind die **Koordinaten** von $V$ i nder Basis $v_{1},..,v_{n}$.

Beispiel:
Sei $V=\mathbb{K}^{n}$
$e_{1}:=(1,0\dots0)^{T}$
$e_{2}:=(0,1,0,\dots,0)^{T}$
...
$e_{n}:=(0,0\dots{0},1)^{T}$
-->**Standardbasis**


## Bemerkung
Sei $v_{1},\dots,v_{n}$ eine Basis von V.
Es gibt eine [[bijektiv|Bijektion]] $f:\mathbb{K}^{n}\to V$, da jeder Vektor eindeutige Linearkombination der Basis ist.
Diese Eigenschaft ist in Zukunft wichtig um Eigenschaften von $\mathbb{K}^{n}$ auf $V$  zu verallgemeinern.

Eine Basis hat folgende zwei Eigenschaften: 
Sie ist ein
[[Erzeugendensystem]]
und
[[Linear unabhängig]]

