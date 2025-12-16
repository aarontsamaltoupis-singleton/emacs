
# Zusammenhang matrix lin. abb
## lin abb aus Matrix
Sei $A$ eine $m\times n$ Matrix.
Die Abbildung $A:\mathbb{K}^{n}\to \mathbb{K}^m$, die durch $v\mapsto A\cdot v$ gegeben ist ist eine lineare Abbildung

**Jede $m\times n$ Matrix $A$ gibt uns eine lineare Abbildung $\mathbb{K}^{n}\to \mathbb{K}^{m}$ und jede lineare Abbildung $\mathbb{K}^{n}\to \mathbb{K}^{m}$ ist von dieser Form.

## Matrix aus lin abb
- Lineare Abbildung $T:V\to W$ ist definiert durch die Werte in den Basen von $V$ und $W$.
- Sei die Basis von $V$ $e_{1},\dots,e_{n}$ gewählt.
- die Basis von $W$ ist $T(e_{1}),T(e_{2}),\dots,T(e_{n})$
- $A$ muss so gewählt sein, dass $A\cdot e_{i}=T(e_{i})$
	- siehe [[Matrix#Multiplikation Vektor Matrix|Multiplikation vektor Matrix]]
(siehe folie 13, folie 14 wiederholung)

#
Falls $A\in M_{m\times n}$ [[Lineare Abbildung#Isomorph|Isomorphismus]], also $A:\mathbb{K}^{n}\to \mathbb{K}^{m}$ dann $m=n$.

$A\in M_{n\times n}$
A injektiv gdw A surjektiv


# 3
## 2.1
Sei $AX=0$  ein homogenes lineares Gleichungsystem von $m$ Gleichungen mit $n$ Variablen
-->$A\in M_{m\times n}$
$X:=(X_{1},\dots,X_{n})^{T}$
$L\subset \mathbb{K}^{n}$ ist die Menge aller $X$, die eine Lösung des Gleichungssystems sind

**L ist dann ein Untervektorraum**

Sei $S\cdot X=0$ eine Zeilenstufenform des Systems

Seien $X_{2(1)},\dots,X_{s(d)}$ die freien Variablen.
$X_{s(1)}=1,X_{s(2)}=0,\dots,X_{s(d)}=0$ ist eine Lösung $f_{1}\in L$

- $f_{i}$ sind eine Basis von $S$
- Demnach gibt es $d$ Basisvektoren gleich der Anzahl der freien Variablen, oder der Anzahl der Spalten ohne Pivots
- $dim(S)=dim(A)=d$
- dieser Satz wird benötigt im [[ranksatz.pdf|Ranksatz]]

## 2.2
- sei $b\in \mathbb{K}^{m}$ nicht 0
	- kein Untervektorraum, da $\vec{0}\not\in L$ und somit kein Vektoraum
		- denn $A\cdot  \vec{0} =\vec{0}\neq b$


# 4
Sei $A\in M_{m\times n}$
$A=[v_{1},\dots,v_{n}]$
**Dann: $im(A)=span(v_{1},\dots,v_{n})$**

--A stellt alle linearekombinationen der Basis dar. Diese basis ist aber genau $v_{1},\dots,v_{n}$ 
-- vergleiche: A ist vollständig durch die Werte auf der Basis definiert



# 5
Sei $T:V\to W$ ein Isomorphismus und sei $U\subset V$ ein Untervektorraum.
Dan $U$ und $T(U)$ isomorph.
INsb. $dim(U)=dim(T(U))$


