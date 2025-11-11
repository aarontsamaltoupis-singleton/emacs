[[DEA, Turingmaschinen|Unterschiede DEI, Turingmaschinen]]


Ein deterministischer endlicher Automat (DEA) ist ein **Tupel** $$\mathcal{A}=(Q,\Sigma,q_{0},\delta,F)$$, wobei:
- $Q$: eine **endliche** Menge an Zuständen
- $\Sigma$: Ein [[Grundlegende Begriffe#Alphabet.|Eingabealphabet]]
- $q_{0}\in Q$: der **Anfangszustand**
- $\delta :Q\times\Sigma \to Q$: die **Übergangsfunktion**
- $F\subseteq Q$: die Menge an **akzeptierten Zuständen**


Die Übergangsfunktion $\delta$ muss **vollständig definiert** sein.
Übergangsfunktion $\delta$ ordnet einzelnen Symbolen und Zuständen neue Zustände zu. 

# Definition 1.3(kanonische Fortsetzung von delta)

Die Funktion $$
\hat{\delta}: Q\times \Sigma^{*}\to Q
$$ ist eine *kanonische Fortsetzung* von $\delta: Q\times \Sigma\to Q$.

$\delta$: Teilt Zuständen und einzelnen Symbolen $(q_{1},a)$ den neuen Zustand $q_{2}$ zu.
$\hat{\delta}$: Teilt Wörtern und ihren Anfagszuständen $(w,q_{0})$ den Endzustand des Wortes $q_{m}$ zu.

$\hat{\delta}$ ist dabei folgendermaßen rekursiv definiert: 

- $\hat{\delta}(q_{0},\varepsilon):=q_{0}$
	- Die Endzustand des leeren Wortes in jedem Automaten ist der Anfangszustand $q_{0}$
- $\hat{\delta}(q_{0},wa):= \delta(\hat{\delta}(q,w),a)$
	- Der Endzustandes eines beliebigen Wortes, ist der Wert der Übergangsfunktion des Endzustand des "vorherigen Wortes", sowie des neuen Buchstabens des beliebigen Wortes.

# Definition 1.4(Akzeptiertes Wort, erkannte Sprache)
Ein DEA $\mathcal{A} = (Q,\Sigma, q_{0}, \delta, F)$ *akzeptiert* das Wort $w\in \Sigma^{*}$, wenn $\hat{\delta}(q_{0}, w) \in F$.
Der Zustand, in dem sich der Automat nach Abarbeitung des Wortes befindet ist also unter den akzeptierten Zuständen. 

Die von $\mathcal{A}$ **erkannte Sprache** ist $L(\mathcal{A}) = \{ w\in \Sigma^{*} |\mathcal{A}\text{ akzeptiert } w\}$


# Definition 1.5  (Erkennbarkeit einer Sprache)
Eine Sprache $L \subseteq \Sigma^{*}$ heiß$t$ *erkennbar*, wenn es einen DEA $\mathcal{A}$ gibt mit $L = L(\mathcal{A})$. 


