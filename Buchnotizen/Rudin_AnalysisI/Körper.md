**Definition**
Ein Körper ist eine Menge $K$ mit zwei Operationen: [[#Addition]] und [[#Multiplikation]], die durch folgende **Körperaxiome** definiert sind:

# Addition
- A1) Ist $x\in K$ und $y\in K$, dann gilt $(x+y)\in K$
- A2) Kommutativität: $\forall x,y\in K: x+y = y+x$
- A3) Assoziativität: $\forall x,y,z\in K: (x+y)+z = x+(y+z)$ 
- A4) $K$ enthält ein Element $\hspace{0pt}0$, sodass $\forall x\in K: 0+x = x$
- A5) $\forall x\in K: \exists -x\in K\text{,sodass } x+(-x) = 0$

# Multiplikation
- M1) Ist $x\in K$ und $y\in K$, dann gilt $xy\in K$.
- M2) Kommutativität: $\forall x,y\in K: xy = yx$
- M3) Assoziativität: $\forall x,y,z\in K:(xy) z=x(yz)$
- M4) $K$ enthält ein Element $1\ne0$, sodass $\forall x\in K: 1x=x$
- M5) Zu jedem $x\in K, x\ne 0$ exisitert ein Element $\frac{1}{x}\in K$, sodass $x(\cdot \frac{1}{x})=1$

# Distributivgesetz
$\forall x,y,z\in K: x(y+z) = xy+xz$



**Satz**
Die Axiome der Addition implizieren die folgenden Regeln:
a)  $x+y =x+ z \implies y = z$
b) $x+y=x \implies y=0$
c) $x+y =0 \implies y=-x$
d) $-(-x)  =x$
**Satz**
Die Axiome der multiplikation führuen zu den folgenden Regeln:
a) $(x\ne 0 \land xy=xz) \implies y=z$
b) $x\ne 0 \land xy=x \implies y=1$
c) $x\neq 0\land xy=1 \implies y=\frac{1}{x}$
d) $x\ne 0 \implies \frac{1}{(\frac{1}{x})}=x$


**Satz** 
Aus den Körperaxiomen resultieren die folgenden Aussagen fü$r$ alle $x,y,z\in K$
a) $0x = x$
b) $x\neq 0 \land y\neq 0 \implies xy\neq {0}$
c) $(-x)y = -(xy) = x(-y)$
d) $(-x)(-y)= xy$

**Satz 1.16**
a) $0x=0$
b) $x\neq 0$ und $y\ne 0$, dann $xy\ne 0$
c) $(-x)y = -(xy) = x(-y)$
d) $(-x)(-y) = xy$

# geordnete Körper
Ein **geordneter Körper** ist ein Körper $K$, der zugleich eine [[Geordnete Menge|geordnete Menge]] ist, auf folgende Weise:

i) $x+y <x+z, \text{falls } x,y,z\in K\text{und } y<z$
ii) $xy<0$, falls $x,y\in K$ und $x>0$ und $y>0$

Ist $x>0$, so ist $x$ **positiv**, ist $x<0$, so ist $x$ **negativ**.


Die folgenden Behauptungen gelten in jedem geordneten Körper:
a) $x<0 \iff -x<0$
b) $x>0 \land y<z \implies xy<xz$
c) $x<0 \land y<z \implies xy>xz$
d) $x \ne 0 \implies x^2>0$ Insbesondere gilt $1>0$.
e) $0<x<y \implies 0< \frac{1}{y}< \frac{1}{x}$
