
	
# Beweisidee
Beweis durch [[Potenzmengenkonstruktion]].

# Definitionen
Sei $\mathcal{A} = (Q,\Sigma,q_{0},\Delta,F)$ ein [[Nichtdeterministische endliche Automaten (NEA)|NEA]].

Es gilt nach [[Nichtdeterministische endliche Automaten (NEA)#Definition 1.11 (Akzeptierte Wort, erkannte Sprache)|Definition]]: 
$w\in L(A)$ gdw $\exists q_{f}\in F$, mit  $q_{f}\in\{ q: q_{0}\stackrel{w}{\implies}_{A}q\}$
Also: 
$w\in L(\mathcal{A})$ genau dann, wenn die Menge aller Zustände, die von $q_{0}$ aus mit Pfaden der Beschriftung $w$ zu erreichen sind, zumindest einen akzeptierten Zustand enthält.

Es soll ein äquivalenter [[Deterministische endliche Automaten (DEA)|DEA]] zu $\mathcal{A}$ konstruiert werden. 
$\mathcal{A'}=(2^{Q}, \Sigma, \{ q_{0} \}, \delta, F')$

## Zustände, Alphabet von A'
Die Menge aller Zustände, die in $\mathcal{A'}$ verwendet werden ist die Menge aller Teilmengen der Zustände $Q$ von $\mathcal{A}$

$\mathcal{A'}$ soll die selben Wörter wie $\mathcal{A}$ erkennen ,deshalb bleibt das Eingabealphabet dasselbe

## Übergangsfunktion von A'
Die [[Deterministische endliche Automaten (DEA)#Definition 1.3(kanonische Fortsetzung von delta)|Übergangsfunktion]] $\delta$ und $F'$ sind folgendermaßen definiert:
**Definition $\delta$**
$\hat{\delta}(\{ q_{0} \},w)=\{ q\in Q: q_{0}\stackrel{w}{\implies}_{\mathcal{A}} q\}$

Der Endzustand eines Wortes $w$ im DEA $\mathcal{A'}$ ist also die Menge aller Zustände $q\in Q$, sodass es einen Pfad von $q_{0}$ zu $q$ mit der Beschriftung $w$ gibt.

Der eine deterministische Lauf von $\mathcal{A'}$ bei der Eingabe $w$ enthält also alle möglichen Läufe, die eintreten könnten, wenn $w$ in $\mathcal{A}$ eingegeben wird.

Sei $P\subseteq Q, a\in\Sigma$. 
$\delta(P,a)= \underset{p\in P\subseteq Q}{\bigcup}\{ p':(p,a,p')\in\Delta \}$

Die nächste Menge an  Zuständen, die einem Tupel an einer  Menge an Zuständen und einem Symbol zugeteilt wird, ist also die Menge aller jener Zustände  $p'$ sodass in $\mathcal{A}$ das Symbol $a$ von einem der Zustände in $P$ zu $p'$ führt.


## Akzeptierte Zustände von A'
**Definition F'**
Ein Zustand $\{ q\in Q: q_{0}\stackrel{w}{\implies}_{\mathcal{A}\ q}\}$ von $\mathcal{A'}$ ist dann ein **akzeptierter** Zustand von $\mathcal{A'}$, wenn er mindestens einen akzeptierten Zustand von $\mathcal{A}$ enthält.

$F'=\{ P\in2^{Q}:P\cap F\neq \varnothing \}$

### Beispiel: 
$\delta(\{ q_{n},q_{m} \},a)$ wären die Menge all jener Zustände $q_{i}$, sodass man in $\mathcal{A}$ durch das Symbol $a$ von $q_{n}$, oder $q_{m}$ nach $q_{i}$ gelangt.
$\delta( \{\{ q_{n},q_{m}\},a \})$ ist ein akzeptierter Zustand, wenn unter den Zuständen $q_{i}$, zu denen man über $a$ von $q_{n}$, oder $q_{m}$ gelangt, mindestens einen akzeptierten Zustand in $\mathcal{A}$ $q_{f}\in F$ gibt.


# Beweis

## Hilfsaussage
$q'\in \hat{\delta}(\{ q_{0} \},w)$ gdw. $q_{0}\stackrel{w}{\implies}_{A}q'$

zz: 
Wenn es einen Zustand $q'\in Q$ gibt, zu dem es einen Pfad von $q_{0}\in Q$ mit der Beschriftung $w$ gibt, dann gibt es auch einen Pfad von $q_{0}$

## Beweis Hilfsaussage





Sei ein $\mathcal{A}$ akzeptiert ein Wort. 
[[Nichtdeterministische endliche Automaten (NEA)#Definition 1.11 (Akzeptierte Wort, erkannte Sprache)|Laut Definition]] bedeutet dies: 
Es gibt einen Pfad $q_{0}\stackrel{w}{\implies}_{A}q_{f}$, wobei $q_{f}\in F$.


Per Definition gilt dann $q_{f}\in \hat{\delta}(\{ q_{0} ,w\})$.
Offensichtlich enhält dann die Menge aller Zustände, zu denen $w$ von $q_0$ aus führt einen Zustand, der von $\mathcal{A}$ akzeptiert wird.
Somit wird $w$ auch von $\mathcal{A'}$akzeptiert.


