#Rudin 
# Definition 2.15
Eine Menge X, in der allen zwei beliebigen verschiedenen Elementen (Punkte) $p,q\in X$ eine reelle  Zahl $d(p,q)$ (Abstand der Punkte p und q) zugeordnet ist, sodass gilt:

- $d(p,q)>0$, wenn $q\neq p$
- $d(p,q)=d(q,p)$
- $d(p,q)\leq d(p,r)+d(r,q)$, für alle $r\in X$ ( #Dreiecksungleichung)

Eine Funktion $d$, die diese drei Eigenschaften hat wird Distanzfunktion, oder Metrik genannt



# Definition 2.18
Sei $X$ ein metrischer Raum.

1) Eine **Umgebung** eines Punktes $p\in X$ ist eine Menge $U_{r}(p)$, bestehend aus allen Punkten q, sodass $d(p,q)<r$. Die Zahl $r$ heißt **Radius** von $U_{r}(p)$.
	1) Vergleiche [[4 Folgen, Reihen und Potenzwerte#Bemerkung 4.3 epsilon-Ball|epsilon Ball]]
2) Ein Pukt $p$ ist ein **Häufungspunkt** der Menge $E$, wenn in jeder **Umgebung** von $p$ ein Punkt $q\in E$ mit $q\neq p$ liegt.
3) Wenn $p\in E$ und $p$ **kein** Häufungspunkt von E, dann ist $p$ ein **isolierter** PUnkt von $E$.

