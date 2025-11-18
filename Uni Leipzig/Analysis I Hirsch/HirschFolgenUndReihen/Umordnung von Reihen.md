# Definition Umordnung
Eine Reihe $\sum\limits^{ }_{n}b_{n}$ ist eine Umordnung der Reihe $\sum\limits^{ }_{n}a_{n}$, falls eine [[bijektiv|Bijektion]] $\tau:\mathbb{N}\to \mathbb{N}$ existiert, mit der Eigenschaft, dass $b_{n} = a_{\tau(n)}$


# Bemerkung/Lemma
Sei $\tau:\mathbb{N}\to \mathbb{N}$ eine [[bijektiv|Bijektion]], dann gilt: 
$\forall N\in \mathbb{N}: \exists M\in \mathbb{N}:\{1,\dots,N  \}\subseteq \{ \tau(1),\dots,\tau(M) \}$.

**Beweis der Behauptung:**
Wähle $M=max\{ \tau^{-1}(1),\dots,\tau^{-1}(N) \}$

# Satz 4.27
Die folgenden Aussagen sind  äquivalent: 
1) $\sum\limits^{ }_{n}a_{n}$ konvergiert [[Konvergenzkriterien fuer Reihen|absolut]] 
2) $\sum\limits^{ }_{n}a_{\tau(n)}$ ist konvergent für jede [[bijektiv|Bijektion]], d.h. jede Umordnung von $a_{n}$ ist konvergent

