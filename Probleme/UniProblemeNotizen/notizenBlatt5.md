# gegeben: 
$n(a_{n+1} - a_n)<\varepsilon$



# Nr 3.5
Ein Weg, wie der Durschnitt einer Folge gegen einen Wert konvergieren könnte, ohne dass die Folge selbst gegen einen WErt konvergiert, ist analog zu der Sinusfunktion
Abschnitte der Folge konvergieren dabei gegen den Wert

Dies bedeutet, dass die Folge nicht gegen den Wert a konvergiert, sondern der Wert a einfach ihr Durschnitt ist.

zu beweisen ist, dass ab einem gewissen Punkt der Durchschnitt jedes folgenden Teilsummanden naeher zu dem Grenzwert a ist als der Durschnitt des vorherigen Teilsummanden.




Eine **Teilfolge** der Folge konvergiert dabei gegen den Wert, aber nicht ide Folge selber
a ist ein **[[Lineare Algebra I Grabowski/Teilfolgen und der Satz von Bolzano-Weinstrauss|Haeufungspunkt]]** der folge a_n.


Inwieweit würde dies in konflikt mit der zweiten Bedinung stehen? 

Zu zeigen ist, dass wenn eine Teilfolge von a  gegen a konvergiert, dann ist limsup an = liminf an


# Fakten
Die Folge a ist beschränkt (beweis nötig)


# Ansatz
folgere zunaechst aus der zweiten Bedingung die cauchy bedingung.

an konvergiert dann garantiert gegen einen Wert b.
Sei $b\neq a$.
Folgere daraus einen Widerspruch. Genauer: Finde ein 

Sei ein $\varepsilon < \frac{b-a}{4}$ gewaehlt.
Da $b_n$ gegen a konvergiert, gibt es ein $N\in\mathbb{N}$, sodass $\forall n>N: |b_n-a|<\frac{\varepsilon}{2}$.
Sei spezifisch ein $n>N$ gewaehlt, sodass $|a_{n_0}-b|<\frac{\varepsilon}{2}, \forall n_0>n$

Sei nun $2n>n$ gewaehlt.

$b_{2n} =$

Es gilt 




