---
id: 5 Komplexe Zahlen
aliases: []
tags: []
---
# 5.1 Definition von C

# Definition 5.1 (a) (1.Definition der komplexen Zahlen)
Für $a,b\in\mathbb{R}$ sein $a+bi\in\mathbb{C}$ und wir definieren
die Summe: 
$(a+bi)+(c+di)=(a+c)+(b+d)i$
das Produkt: 
$(a+bi) \cdot (c+di)=(ac-bd)(ad+bc)i$

# Definition 5.2 (kartesische Produkt)
Seien $A,B$ zwei Mengen. 
Die Menge $A\times B = \{(a,b): \in A, b\in B\}$
heißt das kartesische Produkt von $A,B$.

# Definition 5.1(b) (2. Definition der komplexen Zahlen)
$\mathbb{C} =\mathbb{R} \times \mathbb{R}$ mit den Verknüpfungen $+,\cdot$ definiert durch: 
"+": $(a,b)+(c,d)=(a+c,b+d)$
"$\cdot$": $(a,b)\cdot(c,d)=(ac-bd,ad+bc)$

## Bemerkung:
Es gilt $\mathbb{R}\cong \{ (a,0): a\in \mathbb{R}^{2} \}\subseteq \mathbb{C}$

- $\mathbb{R}$ [[Lineare Abbildung#Isomorph|isomorph]] zu $R:=\{ (a,0):a\in \mathbb{R} \}$
	- also Summe und Produkt sind "gleich":
	- $(a,0)+(b,0)=(a+b,0)$
	- $(a,0)\cdot(b,0)=(a\cdot b,0)$

# Satz 5.1
Die [[Körper]]axiome gelten auch für $\mathbb{C}$.

**Bemerkng**:
  $\mathbb{C}$ ist ein Körper, aber **nicht angeordnet**. I Die reellen Zahlen#II Anordnungsaxiome gelten nicht.



# Definition 5.2
Sei $z=x+y\cdot i\in \mathbb{C}$, dann heißt:

a) x der Realteil von $z$ (Notation $\mathrm{Re}(z)=x$)
b) y der Imaginäteil von z
c) $\bar{z}=x-yi$ die **konjugierte Zahl** (Notation $\bar{z}$)
d) $|z|=\sqrt[]{x^{2}+y^{2}}$  der **Betrag** von z





# Satz 5
.3:
$\forall a,b\in \mathbb{C}:$
0) $\bar{\bar{a}}=a$


1) $\overline{a+b}=\bar{a}+\bar{b}$
2) $\mathrm{Re}(a)=\frac{1}{2}(a+\bar{a})$
3) $\mathrm{Im}(a)i=\frac{1}{2}(a-\bar{a})$
4) $a=\bar{a}\iff a\in \mathbb{R}$
5) $a\bar{a}=|a^{2}|=\mathrm{Re}(a)+\mathrm{Im}(a)^{2}\geq{0}, |a|^2\iff a=0$
6) $|a|\geq |\mathrm{Re}(a)|, |a|\geq |\mathrm{Im}(a)|, |a|=|\bar{a}|$



# Proposition 5.4
Für jedes $c\in \mathbb{C}/\{ 0 \}$ hat die Gleichung $z^{2}=c$ genau die beiden Lösungen $\{ z, -z\}$ mit 
$z=\sqrt[]{ \frac{|c|+\mathrm{Re}(c)}{2} }+i\cdot\text{sign}(\mathrm{Im}(c))\cdot \sqrt[]{\frac{|c|-\mathrm{Re}(c)}{2}  }$

, wobei $\text{sign}(y)=\begin{cases}+1 , \text{falls }y>0\\-1, \text{falls }y<0\\0, \text{falls y=0} \end{cases}$


# Korollar: 
Für jedes $u,v$
