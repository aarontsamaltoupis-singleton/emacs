- Für einen gegebenen Zustand und ein gelesenes Symbo *mehr als ein möglicher Übergang* erlaubt.
- Die Übergangs[[Funktionen|funktion]] wird durch eine Übergangs[[Relation|relation]] ersetzt.
- Es werden die Wörter akzeptiert, für die es zumindest eine Möglichkeit gibt zu einem akzeptierten Zustand zu gelangen.

# Definition NEA
Ein nichtdeterministischer endlicher Automat (NEA) ist analog zum [[Deterministische endliche Automaten (DEA)]]
ein Tupel $\mathcal{A} = (Q,\Sigma,q_{0},\Delta,F)$, wobei

- $Q=\{ q_{0},q_{1},\dots, q_{n}\}$ eine endliche Menge von **Zuständen** ist
- $\Sigma$ ein Eingabealphabet ist
- $q_{0}\in Q$ der Anfangszustand ist
- $\Delta \subseteq Q\times\Sigma \times Q$ die **Übergangsrelation ist**
- $F\subseteq Q$ eine Menge von **akzeptierten Zuständen** ist


# Definition 1.11 (Akzeptierte Wort, erkannte Sprache)
Der NEA  $\mathcal{A} = (Q,\Sigma,q_{0},\Delta,F)$ **akzeptiert** das Wort $w\in\Sigma^{*}$, wenn es einen Pfad gibt mit der Beschriftung $w$ von $q_{0}$: $\ q_{0}\stackrel{w}{\implies}_{\mathcal{A}}q_{f}$, sodass $q_{f}\in F$.

Also: 
Der NEA akzeptiert ein Wort $w$, wenn es zumindest einen [[Pfad]] von dem Anfangszustand $q_{0}$ zu einem akzeptierten Zustand $q_{f}\in F$ gibt, der die Beschriftung $w$ hat.

# Satz 1.12
Zu jedem NEA kann man einen äquivalenten [[Deterministische endliche Automaten (DEA)|DEA]] konstruieren.

[[AequivalenzNEA_DEA|Beweis]].







