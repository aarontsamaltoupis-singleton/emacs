---
id: 4 Folgen, Reihen und Potenzwerte
aliases:
  - Konvergenz
  - Sandwich Satz
  - Monotonie der Grenzwerte
  - epsilon Ball
  - Eindeutigkeit der Grenzwerte
tags: []
---

# Definition 4.1: Folge
Einne Folge von reellen Zahlen ist eine [[Funktion_Abbildung|Abbildung]] $N\to \mathbb{R}$ 
d. h. wir ordnen jedem $n\in \mathbb{N}$ ein $a_{n}\in \mathbb{R}$ zu.

Wir schreiben $(a_{n})_{n\in \mathbb{N}}$.


## Beispiele
- B1) $n_{n\in N}$
- B2) $a_{n}=(-1)^{n}$
- B3) $a_{n}=\frac{1}{n}$ ([[harmonische Folge]])
- B4) $\forall n\in \mathbb{R}$, sei $a_{n}=a^{n}$, oder $(a^{n})_{n\in \mathbb{N}}$
- B5) $a>0$: $a_{n}=\sqrt[n]{ a }$, 
- B5*) $\sqrt[n]{ n }$

## zu den Beispielen
### zu B4)
zu zeigen: $(a^{n})_{n\in \mathbb{N}}$ konvergiert nicht, falls $|a|>1$.
zu zeigen: Folge hat keine obere Schranke. Nach [[#Satz 4.5 Jede konvergente Folge ist beschränkt|Satz 4.5]]  ist die Folge demnach nicht konvergent.

Sei ein beliebiges $A>0$.

# Rekursive Definition 
Mithilfe der vollständigen Induktion können wir Folgen rekursiv definieren.

i) $a_{1},\dots,a_{0}$ werden explizit angegeben.
ii) $a_{n}$ lässt sich mittels einer Vorschrift $V(n)$ aus der Menge aller vorigen Elemente $\{ a_{l}: l\leq n-1 \}$ berechnen, $\forall n>n_{0}$.

- B6) Fibonacci Zahlen: 
	- $f_{0}=0,f_{1}=1$
	- $V(n): f_{n}=f_{n-2}+f_{n+2},\forall n\geq2$


# Definition 4.2: Konvergenz
Eine Folge $(a_{n})_{n\in \mathbb{N}}$ heißt **konvergent** gegen eine reelle Zahl $a\in \mathbb{R}$, falls gilt: 

$\forall\varepsilon>0:\exists N\in \mathbb{N}\ (\forall n>N: |a_{n}-a|<\varepsilon)$

Die Zahl $a$ heißt Grenzwert, oder Limes der folge $(a_{n})_{n\in \mathbb{N}}$.

Wir schreiben $\underset{n\to \infty}{\lim}a_{n}=a$
i
# Bemerkung 4.3: epsilon-Ball
Der $\varepsilon$- Ball **um a** ist definiert als 

$B_{\varepsilon}(a)=\{ x\in \mathbb{R} : |x-a|<\varepsilon\}=(a-\varepsilon,a+\varepsilon)$

Er wird auch als $\varepsilon$-Umgebung von $a$ bezeichnet.

[[#Definition 4.2 Konvergenz|Def 4.2]] besagt geometrisch: 
--> Sei eine folge $(a_{n})_{n\in \mathbb{N}}$ konvergiert gegen $a$ , dann
$\forall\varepsilon>0:\exists N\in \mathbb{N}(\forall n>N:a_{n}\in B_{\varepsilon}(a))$
# Satz 4.4: Eindeutigkeit des Grenzwertes
Der Grenzwert einer folge ist eindeutig.
Wenn also eine Folge $(a_{n})_{n\in \mathbb{N}}$ gegen $a$ und $b$ konvergiert, so gilt $a=b$.

## Beweis 4.4
Sei $a\neq b$.
--> $|a-b| >0$

wähle $0<\varepsilon< \frac{1}{4}|a-b|$ und sei $\exists N\in \mathbb{N}$.
Es gilt:
$|a_{n}-a|<\varepsilon, \forall n>N$

Aber: ([[I Die reellen Zahlen#Satz 2.5 (Rechnen mit Ungleichungen)|Dreiecksungleichung]])
$|a-b|=|a+a_{n}-a_{n}-b|\leq |a-a_{n}|+|a_{n}-b|=|a_{n}-a|+|a_{n}-b|=2\varepsilon=\frac{1}{2} |a-b|$ 

--> Widerspruch, da $|a-b|\neq0$

Intuitiv: 
Wenn $b\neq a$  kann ein Epsilon klein genug gewählt werden, sodass $B_{\varepsilon}(a)\cap B_{\varepsilon}(b)=\emptyset$
Kein $a_{n}$ kann sich dann in beiden dieser Mengen befinden.


# Satz 4.5: Jede konvergente Folge ist beschränkt
Jede konvergente Folge ist beschränkt.
Also: Die Menge der Beträge aller Elemente der Folge ist  [[I Die reellen Zahlen#Definition 2.9 Obere Schranke|nach oben beschränkt]].

d.h.: $\{ a_{n}:n\in \mathbb{N} \}\subseteq \mathbb{R}$ hat eine obere Schranke (nach unten ist die Menge durch 0 beschränkt)

Oder:
$\exists A\in \mathbb{R}(a_{n}<A, \forall n\in \mathbb{N})$
$a_{n}\in B_{A}(0), \forall n\in \mathbb{N}$

## Beweis 4.5
Sei $(a_n)_{n}$ eine konvergente Folge

Es gilt: 
$\exists N\in \mathbb{N}:|a_{n}-a|<1$
(denn es kann $\varepsilon=1$ gewählt werden)

Es folgt: 
$|a_{n}| \leq |a_{}|+\varepsilon= a+|a_{n}-a|\leq |a|+1$ 

Sei $A=\max\{ |a_{1}|,\dots,|a_{N}|,|a|+1 \}$
Demnach: 
$|a_{n}|\leq A, \forall n\in \mathbb{N}$
# Satz 4.6: Rechenregeln für konvergente Folgen
Seien $(a)_{n}$ und $(b_{n})_{n}$ zwei konvergente Folgen, mit
$\lim \limits_{n\to \infty}a_{n}=a$
$\lim \limits_{n\to \infty}b_{n}=b$
Dann gelten folgende Aussagen:
1) $\lim\limits_{n\to \infty}$ 


# Satz 4.7: Monotonie der Grenzwerte
Seien $(a_{n})_{n}$, $(b_{n})_{n}$ zwei konvergente Folgen mit $\lim\limits_{n\to \infty}a_{n}=a$,  $\lim\limits_{n\to \infty}b_{n}=b$ und $a_{n}\leq b_{n}, \forall n\in \mathbb{N}$
Dann folgt $a\leq b$



# Satz 4.8 (Sandwich satz)
Seien $(a_{n})_{n}, (b_{n})_{n}$ zwei konvergente Folgen mit $\lim\limits_{ n \to \infty }a_{n}=a=\lim\limits_{ n \to \infty }b_{n}$ und 
$(c_{n})_{n}$ mit $a_{n}\leq c_{n}\leq b_{n}$.

Dann folgt $\lim\limits_{ n \to \infty }c_{n}=a$

	
