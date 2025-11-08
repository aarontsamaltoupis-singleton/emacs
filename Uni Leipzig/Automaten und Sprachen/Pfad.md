---
aliases:
---
Ein **Pfad** in einem [[Nichtdeterministische endliche Automaten (NEA)|NEA]] $\mathcal{A} = (Q,\Sigma,q_{0},\Delta,F)$ von einem Zustand $p_{1}\in Q$ zu einem Zustand $p_{n}\in Q$ ist **eine Folge**: 
$\pi = p_{0}\stackrel{a_{1}}{\to}_{\mathcal{A}} \ p_{1} \stackrel{a^{2}}{\to}_{\mathcal{A}} \dots \stackrel{a_{n}}{\to}_{\mathcal{A}}\ p_{n}$
, sodass  $(p_{i},a_{i+1}, p_{i+1})\in\Delta$ für $i\in \{ 0,1,\dots,n-1 \}$

	Jedes Tripel an Zustand,symbol,Zustand muss Teil der Übergangsrelation sein. 
	Jeder Übergang von Zustand p0 zu Zustand pn muss also definiert sein.
	Die Symbole, die bei diesen Übergängen benutzt werden sind die **Beschriftung** des Pfades:
# Beschriftung
Der Pfad hat die **Beschriftung** $w:= a_{1}a_{2}\dots a_{n}$

Wenn es in einem NEA $\mathcal{A}$ einen Pfad von $p$ nach $q$ **mit der Beschriftung $w$ gibt**, so schreiben wir: 
$p \stackrel{w}{\implies}_{\mathcal{A}}q$



