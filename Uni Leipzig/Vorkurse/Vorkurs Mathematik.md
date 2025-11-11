
# Tag 1
## Rechengesetze der rationalen Zahlen
$a,b,c,d \in\mathbb{Z},b,d\neq 0$
$\frac{a}{b} + \frac{c}{d} = \frac{ad+cb}{bd}$

$
## Das Schubfachprinzip (Pidgeon-hole-principle) 
Seien $m$ Objekte in $n$ **Kategorien** ("Schubfaecher") aufgeteilt. Wenn $m>n$, dann gibt es mindestens eine Kategorie, die mindestens zwei Objekte enthaelt. 

## Anwendungen des Schubfachprinzips
Unter je $n+1$ Zahlen der Menge $\{1,2,3,.....,2n\}$ gibt es stets zwei Zahlen, von denen die eine die andere teilt.

Jede Zahl der Menge kann umgeschrieben werden und so $n$ Kategorien zugeordnet werden: 
Es sein $n+1$ Zahlen $a_i$ augewaehlt: 

Jede Zahl ist ein Vielfaches einer zweier Potenz: 

$a_i = 2^{l_{i}}\cdot u_{i},u_i \in \{1,3,5,\dots,2n - 1\}$

Es gibt $n$ natuerliche Zahlen zwischen 1 und 2n, es werden aber $n+1$ $a_i$ ausgewaehlt. Demnach werden zwei $a_i,a_k$ mit demselben $u_i = u_k$, allerdings unterschiedlichen zweierpotenzen $2^{l_i}, 2^{l_{k}}$ gebildet. 

## Uebung 1

Nr 8

Gegeben seien 10 natuerliche Zahlen. Begruenden Sie, das es darunter zwei gibt, deren Differenz durch 9 teilbar ist. 

Jede der 10 natuerlichen Zahlen $a_i$ wird einer von 9 Kategorien zugeordnet, je nachdem welchen *Rest* der Bruch $\frac{a_i}{9}$ hat.

Nach dem [[#Das Schubfachprinzip (Pidgeon-hole-principle)|Schubfachprinzip]] haben demnach zwei Zahln $a_i, a_k$ bei der Division durch 9 denselben Bruch.
Es gilt: 

$a_i = k \cdot 9 +r$
$a_k = j \cdot 9 +r$

$a_i - a_k = (k-j)\cdot 9$



# Tag 2

# Tag 7
## Primfaktorzerlegung
**Definition:** 
Sei $n\in \mathbb{N}.$ Dann heißen Primzahlen $p_{1},p_{2},\dots,p_{m}$ *Primfaktorzerlegungen* von $n$, falls $n=p_{1}\cdot p_{2}\cdot\dots p_{m}$.

**Satz:** (Existenz und Eindeutigkeit der Primfaktorzerlegung)
	- Jede natürliche Zahl hat eine eindeutige Primfaktorzerlegung

**Beweis:**
**Existenz**
	Ist $n$ prim, so 
	$n$ kann keine Primzahl sein:
	Somit gibt es ein $k,l\in \mathbb{N}(1<k,l<n)$	mit $n=k\cdot l$.
**Eindeutigkeit**
1) Sei es gibt natürliche Zahlen, für die Primfaktorzerlegung nicht eindeutig ist. 
2) Es sei die kleinste solche Zahl $n$ ausgewählt. 
i) Da $n$ keine Primzahl sein kann, gibt es Primzahlen $$
p_{1}\leq p_{2}\leq \dots \leq pm
$$und Primzahlen$$ q_{1}\leq q_{2}\leq\dots\leq q_{l}

$$ sodass 
$$ n=p_{1}\cdot p_{2}\cdot  ..\cdot p_{m} = q_{1}\cdot q_{2}\cdot \dots q_{l}
	$$
ii) Es muss gelten $\{ p_{1},p_{2}\dots p_{m} \}\cap \{ q_{1},q_{2},\dots,q_{l} \} = \{  \}$.
	Hätten beide Mengen ein gemeinsames Element $k$, wäre $\frac{n}{k}$ eine kleinere Zahl als $n$, die ebenfalls keine eindeutige Primzahlzerlegung hätte.
	Dies ist ein Widerspruch zu Annahme 2).
	
iii)Aus i) folgt $p_{1}^{2} \leq n$ und $q_{1}^{2}\leq n$. Daraus folgt $p_{1}q_{1} = \sqrt{p_{1}q_{1}}\leq \sqrt{n^{2}} = n$.

Sei eine Zahl $k:= n-p_{1}q_{1}\geq{0}$. 
iv) Es gilt $p_{1}|k$ und $q_{1}|k$.
v) Somit gilt $p_{1}q_{1}|k$.	
	Es gilt auch	$p_{1}|n \land q_{1}|n$. Da $n$ aber keine eindeutige Primfaktorzerlegung hat folgt daraus nicht unbedingt $p_{1}\cdot q_{1}|n$.
	Tatsächlich würde daraus sogar folgen, dass $p_{1}\cdot q_{1}\not{|}n$, da nach ii) die beiden Faktoren nicht in derselben Primfaktorzerlegung enthalten sein können.
	Da $k$ kleiner ist als $n$, hat $k$ nach 2) eine eindeutige Primfaktorzerlegung. Somit muss $q_{1}$ ein Faktor von $\frac{k}{p_{1}}$ sein, da $q_{1}$ $k$ ansonsten nicht teilen würde.
vi)Somit gilt auch $p_{1}q_{1}|(k+p_{1}q_{1}) = n$, also gilt auch $p_{1}q_{1}|n$.
Da $n$ durch $p_{1}$ und $q_{1}$ teilbar ist, gilt $q_{1}| \frac{n}{p_{1}}$.
Da $\frac{n}{q_{1}}>n$, hat $\frac{n}{q_{1}}$ nach 2) eine eindeutige Primfaktorzerlegung, nämlich $\frac{n}{q_{1}}=q_{2}\cdot q_{3}\cdot\dots \cdot q_{m}$.
Da $q_{1}| \frac{n}{p_{1}}$ gibt es $r_{1},r_{2},..,r_{s}$, sodass $\frac{n}{p_{1}} = q_{1}\cdot r_{1}\cdot r_{2}\cdot..\cdot r_{2} = q_{2}\cdot q_{3}\cdot\dots \cdot q_{m}$. Dies ist ein Widerspruch zu Annahme 2), nach der alle natürlichen Zahlen kleiner $n$ eine eindeutige Primfaktorzerlegung haben müssen. $\square$




 

			
			

		
		

# Tag 10: Komplexe Zahlen

Die Gleichung $$
x^{2}+1 = 0
$$
hat keine Lösungen in $\mathbb{R}$. 
Der Zahlenbereich soll erweitert werden, sodass die Gleichung eine Lösung besitzt.

$$
\mathbb{C} := \{ z = a+ib|a,b\in \mathbb{R} \land i^{2} = -1 \}
$$
$a$: Realteil von $z$, $a = \mathrm{Re}(z)$ 
$b$: Imaginärteil von $z$, $b=\mathrm{Im}(z)$

Die Rechenoperationen sind auf die komplexen Zahlen so definiert, dass die üblichen Rechenregeln weiter gelten: 

$$
z_{1}+z_{2} = (a_{1}+ib_{1})+(a_{2}+ib_{2}) = (a_{1}+a_{2})+i(b_{1}+b_{2})
$$
$$
z_{1}\cdot z_{2} = (a_{1}+ib_{1})\cdot (a_{2}+ib_{2})=(a_{1}a_{2}-b_{1}b_{2})+i(a_{1}b_{2}+b_{1}a_{2})
$$

## Das Modell der Gaußschen Zahlenebene




