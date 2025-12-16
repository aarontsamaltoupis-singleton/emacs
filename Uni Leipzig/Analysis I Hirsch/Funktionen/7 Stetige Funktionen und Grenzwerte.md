---
aliases:
  - unstetigkeitsstelle
  - lipschitz
  - folgenkriterium
  - zwischenwertsatz
  - gleichmaessige stetigkeit
---
# Definition 7.1 (stetige Funktionen)
$f:D\to \mathbb{R}^{n}$
$f$ heißt **stetig** in $x_{0}$ falls:

$\forall\varepsilon>0 : \exists\delta>0:\forall x\in D: |x-x_{0}|<\delta\implies |f(x)-f(x_{0})|<\varepsilon$

$f$ heißt stetig in $D$ falls $f$ stetig in jedem Punkt $x_{0}\in D$


$x_{0}$ ist eine Unstetigkeitstelle von $f$,falls:

$\exists \varepsilon>0: \forall\delta>0:|x-x_{0}|<\delta: \exists x_{\delta}\in D:|x_{\delta}-x_{0}|<\delta ,\text{aber } |f(x_{\delta})-f(x_{0})|\geq\varepsilon$


# Definition 7.2 Lipschitz stetig
$\exists L>0: |f(x)-f(y)|\leq L|x-y|, \forall x,y\in D$

# Definition 7.4.1 (gleichmäßige stetigkeit)
Eine Funktion $f:D\to \mathbb{R}^{n}$ heißt **gleichmäßig stetig** (auf D), falls: 

$\forall\varepsilon >0: \exists\delta>0:\forall x,y\in D: |x-y|<\delta \implies|f(x)-f(y)|<\varepsilon$

- für jedes $\varepsilon>0$ gibt es ein $\delta>0$ für alle Paare $x,y\in D$
	- in der normalen Stetigkeit kann es für jedes $x$ ein "eigenes" $\delta$ geben.

Sei $f$ nicht gleichmäßig stetig.
$\exists\varepsilon>0: \forall\delta>0: \exists x_{\delta},y_{\delta}\in D:|x_{\delta}-y_\delta|<\delta,\text{aber }|f(x_{\delta})-f(y_{\delta})|\geq\varepsilon$

# Satz 7.3 Folgenkriterium für die Stetigkeit

# Satz 7.1.3
[[5.1.3.pdf]]
# Zwischenwertsatz

# Korollar 7.2.2 (Fixpunkt)

# Existenz von Maximum, Minimum
[[Maxima_Minima_stetiger_funktionen.pdf]]
# Definition 7.3.2 (kompakte Mengen)


# Satz 7.4.2
Sei $f:E\to \mathbb{R}^{n}$ stetig und $E$ kompakt, so ist $f$ gleichmäßig stetig.
[[gleichmaessigeStetigkeitKompakteDefinitionsBereich.pdf]]]
