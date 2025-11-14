#Rudin
# Definition 3.1: Konvergenz
Eine Folge $\{ p_{n} \}$ in einem [[metrische Raeume|metrischen Raum]]  X konvergiert, wenn ein Punkt $p\in X$ mit der Folgenden Eigenschaft existiert: 

$\forall \varepsilon>0:  \exists N\in \mathbb{N}(n\geq N\implies d(p_{n},p)<\varepsilon)$

$d$ bezeichnet hier den Abstand in X.


# Satz 3.2
- Wenn $\{ p_{n} \}$ konvergiert, dann ist $\{ p_{n} \}$ [[beschränkte mengen|beschränkt]].


# Definition 3.5 Teilfolgen
Gegeben sei eine Folge $\{ p_{n} \}$. 
Man betrachte eine Folge $\{ n_{k} \}$ positiver ganzer Zahlen $(n_{1},n_{2},\dots)$ , mit $n_{1}<n_{2}<\dots$.
Die Folge $\{ p_{n_{i}} \}$ heißt eine Teilfolge von $\{ p_n \}$.
Konvergiert $\{ p_{n_{i}} \}$, so wird ihr Grenzwert ein **Teilfolgengrenzwert** von $\{ p_{n} \}$ genannt.

$\{ p_{n} \}$ konvergiert gegen p g.d.w jede Teilfolge von $\{ p_{n} \}$ gegen $p$ konvergiert. 

# Definition 3.15 
Vergleiche: [[4.3 Monotone Folgen und bestimmte Divergenz#Definition 4.11 (bestimmt divergent)|Hirsch: bestimmt divergent]]

Wir schreiben dann:
$s_{n}\to +\infty$
$s_{n}\to -\infty$


# Definition 3.16: lim sup, inf sup
Vergleiche: [[4.3 Monotone Folgen und bestimmte Divergenz#Definition 4.15 lim sup, inf sup|Hirsch: lim sup, inf sup]]

Sei $E$ eine Teilmenge der [[Die erweiterte reelle Zahlengerade|erweiterten reellen Zahlengeraden.]]
Sei eine Folge $\{ s_{n} \}$

Sei  $E=\{ x: \text{Eine Teilfolge von } \{ s_{n} \text{ konvergiert gegen }x\} \}$.
- $x$ kann dabei auch $\pm \infty sein$
- 
Sei 
$s^{*}=\sup E$ (Limes superior)
$s_{*}=\inf E$ (Limes inferior)
