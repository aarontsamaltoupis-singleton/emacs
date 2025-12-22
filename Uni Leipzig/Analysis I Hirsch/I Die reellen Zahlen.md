---
id: I Die reellen Zahlen
aliases:
  - anordnungsaxiome
  - Koerperaxiome
  - Vollstaendigkeitsaxiom
  - Rechnen mit Betrag
tags: []
---


Literaturempfehlungen: 
Konstruktion der reellen Zahlen: 
	Dedekind Schnitte: [[Dedekind Schnitte|Kapitel 1c in Escher]]
Rudin: [[Körper]]

Wir bezeichnen mit $\mathbb{R}$  eine Menge, die (I- III) erfüllt: 

# I Körperaxiome K1-K5
Vergleiche: [[Körper|Körperaxiome, Rudin]]

Das Tripel $(\mathbb{R}, +, \cdot)$  ist ein Körper , wenn es folgende Eigenschaften hat: 
	$\mathbb{R}$ ist dabei die Menge auf der gerechnet wird
	$+, \cdot$ sind [[Operatoren]] auf der Menge $\mathbb{R}$.
	Da gilt $+,\cdot: \mathbb{R}^{2}\to \mathbb{R}$ ist der Körper $\mathbb{R}$ abgeschlossen.

### K1 Assotiativgesetz: 
$$
\begin{align}
(a+b)+c = a+(b+c) \\
(ab)c = a(bc)
\end{align}
$$
### K2 Kommutativgesetz: 
$$
\begin{align}
b+a = a+b \\
b\cdot a=a\cdot b
\end{align}
$$
### K3 Neutrales Element:
$$
\begin{align}
\exists 0 \in \mathbb{R}\text{, sodass }0+a = a \\
\exists 1\in \mathbb{R}\text{, sodass }1\cdot a = a
\end{align}
$$
### K4 Inverses Element: 
$$
\begin{align}
\forall a\in \mathbb{R}:\exists 0\in \mathbb{R}(a+0=0) \\
\forall a\in \mathbb{R}\setminus \{ 0 \}: \exists b\in \mathbb{R}(a\cdot  (-a)=1)
\end{align}
$$
### K5 Distributivgesetz:
$$
(a+b)+c = ac+bc
$$
## Bemerkung 2.1
- $\hspace{0pt}0$ ist eindeutig
	- Beweis: 
		Sei $0'$ ein weiteres neutrales Element. 
		- $0'\stackrel{K 3}{=}0 +0' \stackrel{K 2}{=}0'+0 = 0$
- $\hspace{0pt}1$ ist eindeutig
		- Beweis wie für die 0
		- 
- Das inverse  Element $-a$ ist eindeutig
	- Beweis: 
		- Sei $a\in \mathbb{R}$ mit zwei Inversen $b,b'$.
		- $b' \stackrel{K3}{=}0+b' \stackrel{K 4}{=} (b+a) +b' \stackrel{K 1}{=} b+ (a+b') \stackrel{K2, K4}{=} b+0 \stackrel{K 3}{=} b$

- Das inverse  Element $a^{-1}$ ist eindeutig
	- Beweis: 
		- Sei 

## Satz 2.1 (Rechnen in R)
### i) 
$$
\ a = -(-a),  \forall a\in \mathbb{R}
$$
Beweis: 
$$
(-a) +(-b) = -(a+b), \forall a,b,\in \mathbb{R}
$$
Beweis: 

### ii) 
$$
a = (a^{-1})^{-1}, \forall a\in \mathbb{R}\setminus\{ 0 \}
$$
$$
a^{-1} \cdot b^{-1} = (ab)^{-1}, \forall a, b\in \mathbb{R}\setminus \{ 0 \}
$$
Beweis: 
### iii) 
$$
a\cdot  0 = 0, \forall a\in \mathbb{R}
$$
$$
a\cdot (-b) = -(ab), \forall a,b\in \mathbb{R}
$$
Beweis: 
$$
(-a)(-b) = ab, \forall a,b,\in \mathbb{R}
$$
Beweis: 

### iv)
$$
a(b-c) = ab-ac, \forall a,b,c\in \mathbb{R}
$$
Beweis: 
### iv)
$$
ab = 0 \implies a=0 \lor b=0
$$
Beweis: 

## Folgerung 2.2 
$a,b,c,d\in \mathbb{R}$
$c,d \ne 0$

ii)$\frac{a}{c} \cdot \frac{b}{d} = \frac{a\cdot b}{c\cdot d}$

iii) $\frac{\left( \frac{a}{c} \right)}{\left( \frac{b}{d} \right) }= \frac{a\cdot d}{c \cdot b}\text{, mit } d\ne 0$


# II Anordnungsaxiome
Durch die Körperaxiome sind die reellen Zahlen noch nicht eindeutig festgelegt.
	Siehe [[Hörsaalübung]]
Anordnung auf dem **Zahlenstrahl** ist noch notwendig.

Vergleiche: [[Körper#geordnete Körper|Axiome des geordneten Körpers, Rudin]].
### A1: positive und negative Zahlen
$\forall x\in \mathbb{R}$ gilt genau eine der drei Relationen: 
i) $a<0$
ii) $a=0$
iii) $a>0$
	
### A2: Invarianz der positiven Zahlen
Wenn $a>0,  b>0$, dann $a+b>0 \land ab>0$.
$a>0$  ist **invariant unter Rechenoperationen $+,\cdot$

Anschaulich: 

## Bemerkung: 2.3

$a>0\iff -a<0$
Beweis: 


Damit hätten wir anstelle von [[#A1 positive und negative Zahlen|A1]] auch forder können, dass: 

$(\tilde{A})$: $\forall a\in \mathbb{R}$ gilt genau eine der Relationen: 
- $a=0$ 
- $a>0$
- $-a>0$


## Definition 2.4: Relationen von Zahlen ungleich 0
$$
a>b \iff a-b>0
$$


## Satz 2.5 (Rechnen mit Ungleichungen)
1) Für $a,b,\in \mathbb{R}$ gilt genau eine der Relationen: 
	1) $a>b$
	2) $a=b$
	3) $a<b$
2) $a>b, b>c \implies a>c$
3) Sei $a>b$
	1) $a+c > b+c, \forall c\in \mathbb{R}$
	2) $ac> bc$, falls $c>0$
	3) $ac< bc$, falls $c<0$
4) Sei $a>b, c>d$.
	1) $a+c > b+d$, $\forall c\in \mathbb{R}$
	2) $ac> bd$, falls $b,d >0$
5) $a\ne 0 \implies a^{2} >0$ (Damit gilt  insbesondere: $1>0$)
6) $a>0 \implies a^{-1} >0$
7) $a>b > 0 \implies \frac{1}{b} > \frac{1}{a}$

### Beweise Satz 2.5


## Definition 2.4 Teil 2
[[Funktionen|Abbildungen]] max/min: 

**Definition des Maximum:**
$$
\max\{ a,b \} = \begin{cases}
a, \text{falls } a\geq b\\ \\
b, \text{falls } b\geq a
\end{cases}
$$
**Defnition ds Minimums:**
$$
\min\{ a,b \} = \begin{cases}
b, \text{falls } a\geq b\\ \\
a, \text{falls } b\geq   a
\end{cases}
$$
## Definition 2.6: Betrag
Der Betrag einer Zahl $a\in \mathbb{R}$ ist definiert als:
$$
|a| = \max \{ a,-a \} = \begin{cases}
a \text{ falls } a>0\\ \\
-a \text{ sonst}
\end{cases}
$$

Der Zahlenstrahl ist ein anschauliches Modell für $\mathbb{R}$.
	$d$.$h$.: $a>b \implies \text{"a rechts von b, mit Abstand |a-b|"}$
	$|a|$ ist der Abstand von a zur $0$.

## Satz 2.7: Rechnen mit Betrag
1) $|-a| = |a|$ und $a\leq|a|$
2) $|a|\geq 0$ und $|a| = 0\iff a=0$
3) $|a\cdot b| = |a|\cdot|b|$
4) $|a+b|\leq|a|+|b|$ (Dreiecksungleichung)
5) $||a|-|b||\leq|a\pm b|\leq|a|+|b|$ (umgekehrte Dreiecksungleichung)
### Beweise zu 2.7: 
1) 
	1) $$|-a| = \begin{cases}
-a, falls -a\geq0\\ \\
a, falls\ a>0
\end{cases} \stackrel{Def. 2.6}{=} |a|$$
	2)$$|a|-a =\begin{cases}
a-a=0,\text{falls }a\geq0\\ \\
a-a=-2a=2\cdot (-a), \text{falls }a<0
\end{cases} $$		
		
2) $|a|\geq0$ folgt direkt aus [[#Definition 2.6 Betrag|Def 2.6]] und $|a|=0\iff a=|0|$ folgt aus $-a\neq0$ (Eindeutigkeit des [[#K4 Inverses Element|inversen Elements]]), falls $a\neq0$.
3) 
## Bemerkung 2.8: betrag,max funktion

$$
\max\{ a,b \} = \frac{a+b}{2} + \frac{|a-b|}{2}
$$
$$
\min\{ a,b \} = \frac{a+b}{2} - \frac{|a-b|}{2}
$$




## Definition 2.9: Obere Schranke
Sei $M\subseteq  \mathbb{R}$.
1) $k\in$ ist eine **obere Schranke von M**, Vergleiche: [[beschränkte mengen#Obere Schranken|obere Schranken einer Menge EcM]]
2) M ist **nach oben beschränkt**.
	1) zu 2): M heißt **beschränkt**, wenn M nach oben **und** nach unten beschränkt ist, d.h. $\exists k\in \mathbb{R}(-k\leq a\leq k, \forall a\in M)$
		1) Erklärung: 
			Sei $k_{1}\leq a\leq k_{2}$
			OBdA: $k_{2}\geq0,k_{2}\leq0$, ansonsten gilt $0=k_{2}\lor0=k_{1}$
			Sei $k= \max \{ k_{2},-k_{1} \}$
			$-k \leq k_{1}$
			$-k\leq k_{1}\leq a\leq k_{2}\leq k, \forall a$
			
4) d
5) Wir schreiben $\sup M =+\infty$, falls $M$ nicht von oben beschränkt ist und $\inf M= -\infty$, falls $M$ nicht von unten beschränkt ist.


## Bemerkung: 
Nach [[#Definition 2.4 Teil 2|Def. 2.4]] haben wir nun max und min zweier und damit auch das Maximum von endlich vielen Zahlen:

$\max\{ a,b,c \}=\max\{ a,\max\{ b,c \} \}$
$\implies$ insbesondere $\max\{ a_{i}: i=1,2,3,\dots,n \} = a_{i_{0}}$ mit $a_{i_{0}}\geq a_{i}\forall i$

**Problem**: Die Menge $\{ x\in \mathbb{R}:x<1 \}$ hat kein Maximum
# III Das Vollständigkeitsaxiom
Falls $M\subseteq \mathbb{R}$ nach oben (unten) beschränkt und nicht leer, dann existiert $\sup M(\inf M)$
Vergleiche: [[beschränkte mengen#Supremums Eigenschaft einer Menge M|Supremumseigenschaft(Rudin)]]


$\mathbb{Q}$ erfüllt das Vollständigkeitsaxiom nicht. Siehe [[beschränkte mengen#Supremums Eigenschaft einer Menge M]](Rudin)
	
