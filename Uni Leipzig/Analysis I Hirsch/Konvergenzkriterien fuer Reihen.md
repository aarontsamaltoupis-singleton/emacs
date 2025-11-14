---
tags:
  - hirsch
---
# Bemerkung 4.22
$(s_{n})$ ist eine Cauchyfolge $\iff$ 
$\forall\varepsilon>0: \exists N\in \mathbb{N}:|a_{n+1}+a_{n+2}+\dots+a_{m}| = \sum^{m}_{k=n+1}a_{k}=|s_{m}-s_{n}|<\varepsilon, \forall m\geq n>N$
# Korollar 4.23
$\sum_{n}a_{n}$ konvergiert $\implies (a_{n})_{n}$ ist eine Nullfolge

Beweis: 
Wähle in [[#Bemerkung 4.22]] $m=n+1$.
$\sum \limits^{n+1}_{k=n+1}a_{k}=a_{n}<\varepsilon$

# Satz 4.24 (Majorantenkriterium)
Seien $\sum\limits^{ }_{n}a_{n},\sum\limits^{ }_{n}b_{n}$ Reihen mit $|a_{n}|\leq b_{n}$ und $\sum\limits^{ }_{n}b_{n}$ konvergent.
Dann ist $\sum\limits^{ }_{n}a_{n}$ konvergent. (mit $|\sum\limits^{ }_{n}a_{n}| \leq \sum\limits^{ }_{n}b_{n}$)
	