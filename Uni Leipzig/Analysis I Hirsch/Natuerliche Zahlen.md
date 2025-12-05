# Definition 3.1: induktive Mengen 
$M\subseteq R$ heißt **induktiv**, falls: 
	- $1\in M$
- $\forall n\in M(n+1\in M)$

# Satz 3.2: kleinste induktive Menge
Es existiert eine kleinste induktive Menge. Diese kennzeichnen wir mit $\mathbb{N}$.
Sie ist charaktierisiert durch: 
$M\subseteq \mathbb{R}$ [[#Definition 3.1|induktiv]] und $M\subseteq \mathbb{N}\implies M=\mathbb{N}$

**Beweis:**
1. Behauptung: Es existiert eine induktive Menge
		Sei  $M = \{ x\in \mathbb{R}: x\geq1 \}$
		$a\in M \implies a+1\geq1\implies a\in M$
		$\implies$ M ist induktiv
	Sei $\mathbb{N}$ der **Durchschnitt aller induktiven Teilmengen von $\mathbb{R}$**.
2. $\mathbb{N}$ ist induktiv 
		zz: $1\in \mathbb{N}$
		Da $1\in M\ \forall M(\text{M ist induktiv})$ gilt $1\in \mathbb{N}$.
		zz: $n\in M\implies n+1\in M(\text{für alle M induktiv})$ 
		Sei $n\in M$. Da $n\in M$ gilt $n+1\in M$. Da $M$ beliebig war, muss $n+1$ sich auch im Durchschnitt aller induktiven Mengen befinden und somit in $\mathbb{N}$.
3. $\mathbb{N}$ ist die kleinste Induktive Menge
		Sei $M\subseteq \mathbb{R}, M$ ist induktiv. Sei $M$ kleiner als $\mathbb{N}$. Da $\mathbb{N}$ der Durchschnitt aller induktiven Mengen, gilt $\mathbb{N}\subseteq M$ 
		Nach Annahme gilt $M\subseteq \mathbb{N}$.
		Damit gilt $\mathbb{N}=M$.
		$\square$


# Korollar 3.3: Schwaches Induktionsprinzip
Zu jeder natürlichen Zahl $n\in \mathbb{N}$ sei eine Aussage $A(n)$ gegeben und es gelte: 
- (a1) $A(1)$ ist wahr
- (a2) aus $A(n)$ wahr folgt $A(n+1)$ wahr
Dann ist $A(m)$ wahr für alle $n\in \mathbb{N}$.

### Beweis 3.3:
$M=\{ m:A(m) \text{ ist wahr} \}$
Nach $(a1)$ und $(a2)$ st M [[#Definition 3.1 induktive Mengen|induktiv]].
Demnach gilt: $\mathbb{N}\subseteq M$ d.h. $A(m)$ ist wahr $\forall m\in \mathbb{N}$



# Satz 3.4
- i) $n\geq1 \forall n\in \mathbb{N}$
- ii) $n+m\in \mathbb{N} \ \forall n\in \mathbb{N}$
- iii) $nm\in \mathbb{N}\ \forall n\in \mathbb{N}$
- iv) $\forall n\in \mathbb{N}$ gilt entweder $n=1$, oder $n-1\in \mathbb{N}$
- v) $n-m\in \mathbb{N}\forall n\in \mathbb{N}\text{ mit }m<n$ 

### Beweise Satz 3.4


# Korollar 3.5
- i) $\nexists n\in \mathbb{N}\text{ mit }0<n<1$
- ii) für $m\in \mathbb{N}: \nexists n\in \mathbb{N}$ mit $m<n<m+1$

-Nach Korollar 3.5: natürlichen Zahlen können abgezählt werden
### Beweise 3.5



# Notation
Sei $n,m\in \mathbb{N}$ mit $m\geq n$.
$\{ 1,2,\dots,n \}\stackrel{Kor.3.5}{=}\{ x\in \mathbb{N}: x\leq n \}$
$\{ n,n+1,\dots m\}=\{ x\in \mathbb{N}: n\leq x\leq m \}$

--> Denn aus [[#Korollar 3.5]] folgt, dass eine Teilmenge aus $\mathbb{N}$ abgezählt werden kann
# Satz 3.6 (Prinzip der kleinsten natürlichen Zahl)
Vergleiche: [[well-ordering principle]]

Jede nicht-leere Menge $M\subseteq \mathbb{N}$ hat ein kleinstes Element.

### Beweis 3.6
Sei $M\subseteq \mathbb{N}, M\neq \varnothing$ und sei $M$ hat kein kleinstes Element.

zz: $A(n)= "\ \{ 1,2,3,\dots,n \}\cap M=\varnothing \ "$

zz: $A(1):$
Es muss gelten $\{ 1 \}\cap M=\varnothing$, da wenn $1\in M$ aus [[#Satz 3.2 kleinste induktive Menge|Satz 3.2]] folgt, dass $1$ das kleinste Element aus $\mathbb{N}$ ist.

zz: $A(n)\implies A(n+1)$
Sei $A(n)$: $\{ 1,..,n \}\cap M =\varnothing$ ist wahr.
zz: $\{ 1,\dots,n+1 \}\cap M=\varnothing$ ist wahr $\iff$ $n+1\not\in M$

Falls  $n+1\in \mathbb{N}$, dann $\stackrel{Kor. 3.5}{\implies}$ $n+1$ ist das kleinste Element in $M$.

Demnach gilt nach [[#Korollar 3.3 Schwaches Induktionsprinzip]]: $A(n)$ ist wahr für alle $n\in \mathbb{N}$.
Widerspruch.


# Korollar 3.7 (starkes Induktionsprinzip)
Erweiterung von [[#Korollar 3.3 Schwaches Induktionsprinzip]]

$\forall n\in \mathbb{N}:$ Sei eine Aussage $A(n)$ gegeben. 
$A(n)$ habe die Eigenschaften: 
- i) $A(1)$ ist wahr.
- ii) falls $\forall k\leq n:A(k)$ wahr $\implies A(n+1)$ wahr 
Dann ist $A(n)$ wahr $\forall n\in \mathbb{N}$.
## Beweis 3.7
Sei i)  und ii).
Sei $M:=\{ m\in \mathbb{N}:A(m)\text{ist wahr.} \}\neq \mathbb{N}\text{(Da A(1)wahr)}$
Falls $M\neq \varnothing$, dann $\exists!$ kleinstes Element $m_{0}$ von $M$ (da $M\subseteq \mathbb{N}$, siehe [[#Satz 3.6 (Prinzip der kleinsten natürlichen Zahl)|Satz 3.6]])

--> $A(k)$ ist wahr $\forall k\leq m_{0}-1\stackrel{(ii)}{\implies}A(m_{0})$ wahr.
Nach Satz 3.6 muss also gelten $M=\varnothing$.


# Satz 3.8 (Bernoulli Ungleichung)
Sei $x>-1$ dann glit: $(1+x)^{n}\geq 1+nx$ 
mit $(1+x)^{n} =1$ gdw $n=1$ oder $x=0$.


# Beweis Satz 3.8
Sei $x\neq0$.
zz: $(1+x)^{n}\geq1+nx$

$A(1): (1+x)^{1}= 1+x\geq1+x$

$A(n)\implies A(n+1)$
$(1+x)^{n+1}=(1+x)^{n}\underbrace{ (1+x) }_{ >0 }\stackrel{IH:A(n)}{\geq}(1+nx)(1+x)=1+nx+x+nx^{2}=1+(n+1)x+\underbrace{ nx^{2} }_{ >0 }>1+(n+1)x$
$\implies A(n)$ wahr $\forall n\in \mathbb{N}$


# Korollar 3.9
Sei $a_{n} = (1+\frac{1}{n})^{n}$
Sei $b_{n}=\left( 1+ \frac{1}{n} \right)^{n+1}$
Es gilt:
$a_{n}<a_{n+1}$
$b_{n}>b_{n+1}$
$a_{n}<b_{n}$

### Beweis 3.9



# Definition 3.10
Wir definieren $\mathbb{N}_{0} =\mathbb{N}\cup \{ 0 \}$.
Die ganzen Zahlen: $\mathbb{Z}=\{ -a:a\in \mathbb{N} \}\cup \mathbb{N}_{0}$
Die rationalen Zahlen: $\mathbb{Q}=\left\{  \frac{p}{q}:p,q\in \mathbb{Z},q\neq0  \right\}$
Die irrationalen Zahlen: $\mathbb{R}\backslash\mathbb{Q}$

# Satz 3.11
1) Sei $a,b\in \mathbb{Z}$, dann gilt: 
	1)  $-a\in \mathbb{Z}$
	2) $a+b\in \mathbb{Z}$
	3) $ab \in \mathbb{Z}$
2)$(\mathbb{Q},+,\cdot)$ ist ein Körper 

Beweis als Übung (nutz [[#Satz 3.4]] und $-(-a)=a$, sowie $a>0\iff-a<0$


# Proposition 3.12
Sei $n\in \mathbb{N}$ mit $n>1$, dann gilt entweder, dass $n=2k$ ("n ist gerade"), oder $n=2k$ ("n ist ungerade") für ein $k\in \mathbb{N}$

## Beweis 3.12
Sei $M=\{ k\in \mathbb{N}:2k\geq n \}$
$M\neq \varnothing$, da $n\in M$ und $2n>n$.
Nach [[#Satz 3.6 (Prinzip der kleinsten natürlichen Zahl)]] existiert dann ein kleinstes Element $k_{0}$ von $M$.
$2k_{0}\geq n$

Sei $2k_{0}=n$. Dann sind wir fertig. (Da $n=2k$)

Sei $2k_{0}>n$. 
Sei $k_{1}= k_{0}-1$. 
D.h. $k_{1}\not\in M$, also $2k_{1}<n<2k_{1}+2=2k_{0}$
Demnach:
$n-2k_{1}>0$
und
$n-2k_{1}<2$
Also: 
$0<n-2k<2$
Also: 
$1\leq n-2k<2$
Es gilt $n-2k=1$, da es keine andere natürliche Zahl zwischen 0 und 1 gibt. 
Also $n=2k+{1}$ 

$\square$

# Folgerung 3.13

Jedes $n\in \mathbb{N}$ lässt sich eindeutig zerlegen in $n=2^{k}\cdot u$, mit $k\in N_{0}$ und $u$ ungerade. 

## Beweis 3.13
**Existenz** der Zerlegung mittels Induktion über n.
Induktionsanfang: 
$A(1)=2^{0}\cdot1=2^{k}\cdot u$

Induktionshypothese: 
$\forall m\leq n: A(m)$.
Induktionsbehauptung: 
$A(n+1)$.

Nach [[#Proposition 3.12]] gilt: 
$(n+1=2k+1=2^{0}+u)$ ==> nichts mehr zu beweisen
oder
$(n+1)=2k$

Sei $(n+1) =2k$
$k<n$
d.h. $A(k)$ wahr
$k=2^{l}\cdot u$
==> $n+1 = 2^{l+1}\cdot u$
$\square$
**Eindeutigkeit** der Zerlegung 
Sei $n=2^{k}\cdot u=2^{l}\cdot u$, mit $v,u$ ungerade. 
OBdA: Sei $k\geq l$.
==> $2^{k-l}\cdot u=v$
da $v$ ungerade muss gelten:
$k-l=0$
==> $u=v,k=l$
$\square$


# Satz 3.14
$\nexists q\in \mathbb{Q}(q^{2}=2)$

## Beweis 3.14




# Satz 3.15 (Satz von Archimedes)
Vergleiche Rudin: [[Der Körper der reellen Zahlen#a) Archimedische Eigenschaft von R|Archimedische Eigenschaft]], Tao: [[5.4 Ordering the reals#Corollary 5.4.13 (Archimedean property)]]
$\forall a\in \mathbb{R}:  \exists n\in \mathbb{N}$, mit $n>a$
## Beweis 3.15
Sei $a\in \mathbb{R}$, sodass $n<a,\forall n\in \mathbb{N}$.
Also: $a$ ist eine [[I Die reellen Zahlen#Definition 2.9 Obere Schranke|obere Schranke]] von $\mathbb{N}$.

Nach dem [[I Die reellen Zahlen#III Das Vollständigkeitsaxiom|Vollständigkeitsaxiom]] gilt: 
$\exists Sup\mathbb{N}=S<\infty$, mit $S\leq a$
Da $S-1<S$  und $S-1$ keine obere Schranke $\mathbb{N}$: 
$\exists n\in \mathbb{N}:S-1<n$ 
--> $S<n+1\in \mathbb{N}$
Damit ist $S$ keine obere Schranke.
Widerspruch.
# Bemerkung 3.16
Satz 3.15 ist äquivalent zu der Aussage
$\forall\varepsilon>0:\exists n\in \mathbb{N}$ mit $\frac{0<1}{}$

# Kor. 3.17: Q ist dicht in R
Vergleiche Rudin: [[Der Körper der reellen Zahlen#b) Q ist eine dichte Teilmenge von R|Q dichte Teilmenge R]].
$\forall a,b\in \mathbb{R}$, mit $a<b$: $\exists q\in \mathbb{Q}(a<q<b)$

--> Jede reelle Zahl kann beliebig nah durch rationale Zahlen approximiert werden.

## Beweis 3.17


# Satz 3.18:
$\forall c\in \mathbb{R}$ mit $c\geq0,n\in \mathbb{N}:\exists! x\in \mathbb{R}$ mit $x\geq0$, sodass $x^{n}=c$.

Wir bezeichnen x mit der n-ten Wurzel von c: $x=\sqrt[n]{ c }$

## Beweis 3.13: Fall n=2
Der Fall $c=0$ ist trivial mit $x=0$.
### 1. Eindeutigkeit
Sei $x_{1},x_{2}>0$, mit $x_{1}^{2}=c=x_{2}^{2}$
$0=x_{1}^{2}-x_{2}^{2}=(x_{1}-x_{2})\underbrace{ (x_{1}+x_{2}) }_{ >0}\implies(x_{1}-x_{2})=0$


### 2. Existenz
Sei $M:=\{ x\in \mathbb{R}: x^{2}\leq c \}$



## Beweis 3.13: Allgemeiner Fall
