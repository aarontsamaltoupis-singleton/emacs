
# Endliche Automaten mit Wortübergängen, epsilon- NEA

## Definition 1.14
Ein NEA *mit Wortübergängen* hat die Form $\mathcal{A}= (Q,\Sigma,q_{0},\Delta,F)$,
wobei $Q,\Sigma,q_{0},F$ wie beim normalen NEA definiert sind 
und $\Delta \subseteq Q\times\Sigma^{*}\times Q$  eine endliche Menge an *Wortübergängen* ist.

Ein $\varepsilon$-NEA ist ein [[Nichtdeterministische endliche Automaten (NEA)|NEA]] mit Wortübergängen der Form $(q,\varepsilon,q')$ und $(q,a,q')$ mit $a\in\Sigma$.


Pfade, Pfadbeschriftungen und erkannte Sprachen sind entsprechend wie bei [[Nichtdeterministische endliche Automaten (NEA)|NEAs]] definiert.
So hat der Pfad  $q_{0}\stackrel{ab}{\to}_{A}q_{1}\stackrel{\varepsilon}{\to}_{A}q_{2}\stackrel{bb}{\to}_{A}q_{3}$ die Beschriftung $ab\cdot\varepsilon \cdot bb=abbb$

Unterschied $q\stackrel{a}{\implies}p$ und $a\stackrel{a}{\to}p$:
$q\stackrel{a}{\implies}p$ erlaubt auch für beliebig viele $\varepsilon$-Übergänge, nur ein $a$ Übergang muss vorhanden sein


# Satz 1.15
Zu jedem [[Nichtdeterministische endliche Automaten (NEA)|NEA]] mit Wortübergängen kann man einen äquivalenten NEA konstruieren.


# Lemma 1.16
Zu jedem NEA mit Wortübergängen kann man einen äquivalenten $\varepsilon-$NEA konstruieren.

# Lemma 1.17 
Zu jedem $\varepsilon$-NEA kann man einen äquivalenten NEA konstruieren.
