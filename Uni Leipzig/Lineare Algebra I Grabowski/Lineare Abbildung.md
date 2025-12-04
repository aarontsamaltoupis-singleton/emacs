---
aliases:
  - isomorph
---
# Def lineare Abbildung
Sei $\mathbb{K}$ ein Körper und $V,W$ [[Vektorraum|Vektorräume]] über $\mathbb{K}$.
Eine **lineare Abbildung**  von $V$ nach $W$ ist eine [[Funktionen|Funktion]] $T:V\to W$ mit den folgenden zwei Eigenschaften:
$T(av)=aT(v)$
$T(v+w)=T(v)+T(w)$
- äquivalent dazu die folgende eine Eigenschaft: 
- $\forall a,b\in \mathbb{K},v,w\in V:T(av+bw)=aT(v)+bT(w)$


# Bemerkung 1
Eine lineare Abbildung $T:\mathbb{K}^{n}\to \mathbb{K}^{m}$ ist durch ihre Werte auf der Standartbasis bestimmt, d.h. $T(e_{1,}),\dots,T(e_{n})$

# Bemerkung 2
Eine lin Abb $T:\mathbb{K}^{n}\to \mathbb{K}^{m}$ ist durch die Auswahl der Vektoren $a_{i}\in \mathbb{K}$ definiert, auf die die Vektoren $e_{i}$ abgebildet werden sollen.



# Isomorph

# Übungsblatt 6.4
Der Nullvektor $\vec{0}$ eines [[Vektorraum|vektorraums]] $V$ ist eindeutig.
Sei $T:V\to W$
$T(\vec{0})=\vec{0}$

# Lemma
Sei $T:V\to W$ eine lineare Abbildung
Sei $T$ [[injektiv_injective_one-to-one|injektiv]] Falls $\vec{v_{1}},\dots,\vec{v_{n}}$ lin. abhängig, dann auch $T(\vec{v_{1}}), \dots,T(\vec{v_{n}})$ lin. abhängig

