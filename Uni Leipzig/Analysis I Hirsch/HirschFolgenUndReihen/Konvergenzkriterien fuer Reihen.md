---
tags:
  - hirsch
aliases:
  - Majorantenkriterium
  - Wurzelkriterium
  - Quotientenkriterium
  - Absolute Konvergenz
  - Cauchy-Verdichtungskriterium
  - Leipnizkriterium
---

# Bemerkung 4.22
$(s_{n})_{n}$ konvergiert $\iff(s_{n})$ ist eine Cauchyfolge $\iff$ 
$\forall\varepsilon>0: \exists N\in \mathbb{N}:|a_{n+1}+a_{n+2}+\dots+a_{m}| = \sum^{m}_{k=n+1}a_{k}=|s_{m}-s_{n}|<\varepsilon, \forall m\geq n>N$
# Korollar 4.23(Notwendige Bedingung)
$\sum_{n}a_{n}$ konvergiert $\implies (a_{n})_{n}$ ist eine Nullfolge

Dass $(a_{n})_{n}$ eine Nullfolge ist, ist eine [[Notwendige Bedingung, Hinreichende Bedingung|notwendige Bedinung]] dafür, dass $\sum\limits^{ }_{n}$  konvergiert.

Beweis: 
Wähle in [[#Bemerkung 4.22]] $m=n+1$.
$\sum \limits^{n+1}_{k=n+1}a_{k}=a_{n}<\varepsilon$


# Absolute Konvergenz
-  Summe der Beträge einer Reihe konvergiert

# Satz 4.24 (Majorantenkriterium)
Seien $\sum\limits^{ }_{n}a_{n},\sum\limits^{ }_{n}b_{n}$ Reihen mit $|a_{n}|\leq b_{n}$ und $\sum\limits^{ }_{n}b_{n}$ konvergent.
Dann ist $\sum\limits^{ }_{n}a_{n}$ konvergent. (mit $|\sum\limits^{ }_{n}a_{n}| \leq \sum\limits^{ }_{n}b_{n}$)


# Cauchy Verdichtungskriterium
Sei eine Folge $a_{n}$ eine monoton fallende Folge. 

$\sum\limits^{ }_{n}a_{n}$ konvergent gdw $\sum\limits^{ }_{n}2^{n}a_{2^{n}}$ konvergent

# Leipniz Kriterium
Sei $(a_{n})_{n}$ eine monoton fallende reelle Nullfolge
Dann konvergiert die Reihe
$\sum\limits^{ \infty}_{n=0}(-1)^{n}a_{n}$


# Wurzelkriterium
Sei $(a_{n})_{n}$ eine Folge
w1)  $\exists N\in \mathbb{N}:\sqrt[n]{ |a_{n}| }\leq \theta <1, \forall n>N$, **dann** $\sum\limits^{ }_{n}a_n$ ist [[Konvergenzkriterien fuer Reihen|absolut konvergent]].
w2) $\exists N\in \mathbb{N}: \sqrt[n]{ |a_{n}| }\geq\lambda>1, \forall n>N$ **dann** $\sum\limits^{ }_{n}a_{n}$ ist nicht konvergent.
# Quotientenkriterium
Sei $(a_{n})_{n}$ eine Folge
q1) $\exists N\in \mathbb{N}: |a_{n}|>0,  \forall n>N$ und $\frac{|a_{n+1}|}{|a_{n}|}\leq\theta<1, \forall n>N$, **dann** $\sum\limits^{ }_{n}a_{n}$ ist absolut konvergent
q2) $\exists N\in \mathbb{N}: |a_{n}|>0,  \forall n>N$ und $\frac{|a_{n+1}|}{|a_{n}|}\geq\lambda>1, \forall n>N$, **dann** $\sum\limits^{ }_{n}a_{n}$ ist nicht konvergent
# Bemerkung
$(w1) \iff (w1)^*:$ 
$(q1) \iff (q1)^*:$ 




Das Wurzelkriterium und das Quotientenkriterium beschreiben nicht alle Reihen. Beispielsweise Reihen wie $\sum\limits^{ }_{n}\frac{1}{n}$, in denen $\sqrt[n]{ \frac{1}{n} }$ gegen 1 konvergiert. Dieser Fall ist weder von q1, noch q2, noch w1, noch w2 abgedeckt.


# Übung: 
Wenn eine Folge konvergiert, konvergieren auch alle Potenzen der Folge gegen denselben Wert
