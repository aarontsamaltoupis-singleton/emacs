# Alphabet
Ein Alphabet ist eine endliche Menge von Symbolen. 
$\Sigma = \{ a_{1},a_{2},..,a_{n} \}$
Bspw:

$\Sigma_{4}= \{ \text{program, const, var, label, procedure, function, ...}\}$
	$\Sigma_{4}$ ist das Alphabet aller Schlüsselwörter der Programmiersprache Pascal

# Wort
Ein Wort ist eine **endliche Folge** an Symbolen. Ein Wort   mit $w= a_{1}a_{2}\dots a_{n}$ mit $a_{i}\in{\Sigma}$ heiß$t$ Wort **über dem Alphabet $\Sigma$.

$\Sigma^{*} := \{ w|w\text{ ist ein Wort über dem Alphabet } \Sigma \}$
$\Sigma^{*}$ beschreibt die Menge aller Wörter, die nur Symbole aus diesem Alphabet nutzen, also alle Wörter über dem Alphabet $\Sigma$

$\Sigma^{+} := \Sigma^{*}\backslash\{ \varepsilon \}$

Bspw: 
Jedes Pascal-**Programm** kann als **Wort** über $\Sigma_{4}$ betrachtet werden. $\Sigma^{*}$ enthält dabei aber auch sehr viele "sinnlose" Wörter, also Programme, die von keinem Compiler akzeptiert werden würden.

# Formale Sprache
Eine (formale) **Sprache** ist eine **Menge von Wörtern.**
Eine Sprache $L\subseteq \Sigma^{*}$ heiß$t$ *Sprache über dem Alphabet $\Sigma$.*

Sowohl $\Sigma^{*}$, als auch $\Sigma^{+}$ sind unendliche Sprachen

# Operationen auf Sprachen und Wörtern

## Präfix
$u$ ist Präfix von $v$, wenn $v=uw$ mit $u$,$w$ $\in \Sigma^{*}$
## Suffix
$u$ ist Suffix von $v$, wenn $v=wu$, mit $u,w\in\Sigma^{*}$.
## Infix
$u$ ist **Infix** von $v$, wenn $v = w_{1}uw_{2}$ mit $u,w_{1},w_{2}\in\Sigma^{*}$.

## Konkatenation
- Operation, **die sowohl auf Wörter, sowie auf Sprachen** angewandt werden kann.
### Anwendung auf Wörter
Sei $u$,$v$ Wörter. 
$u\cdot v = uv$ 
$u\cdot v$ bezeichnet das Wort $uv$.

Bsp: 
$abb\cdot ab = abbab$

### Anwendung auf Sprachen
$L_{1}\cdot L_{2} = \{ u\cdot v\ | u\in L_{1} \text{ und } v\in L_{2} \}$

Bsp: 
$\{ aa,a \} \cdot \{ ab,b,aba \} = \{ aaab,aab,aaaba,aab,ab,aaba \}$

$\varnothing \cdot L = L\cdot \varnothing =  \varnothing$, da $\neg \exists v\in \varnothing( w = uv, u\in L )$

Konkatenation ist nicht kommutativ: 

## Boolsche Operationen
Vereinigung:   $L_{1} \cup L_{2} := \{ w| w\in L_{1} \lor w\in L_{2} \}$
Schnitt:            $L_{1} \cap L_{2} := \{ w| w\in L_{1} \land w\in L_{2}\}$
Komplement:   $\overline{L_{1}} := \{ w|w\in \Sigma^{*}\land w \not\in L_{1} \}$

## Kleene-Stern

$L^{0} := \{ \varepsilon \}$
$L^{n+1} := L^{n} \cdot L$
$L^{*} := \bigcup\limits_{n\geq{0}}L^{n}$
$L^{+} := \bigcup\limits_{n\geq_{1}} L^{n}= L^{*}\backslash\{ \varepsilon \}$
