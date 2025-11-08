# Def. 1.2
Sei $P^{*}$ die [[Partition]], sodass $\forall a,b\in P^{*}(a\neq b\implies g(a)\neq g(b))$

Sei $P_{i} = \{ \{ a1,a2 \},\{ a3,a4 \}, \dots, \{ a_{n-1},an \} \}$ eine Partition.
Sei $Sum(P_{i}) = \sum^{n-1}_{k=1}g(a_{k},a_{k+1})$ 

Es gilt $Sum(P_{0}) = n$
Es gilt $Sum(P^{*}) =\frac{n(n+1)}{2}$


Für jedes n Sei: 

A(n) iff $\exists P^{*}$($P^{*}$ ist eine Partition und es gilt $\forall a,b\in P^{*}(g(a) = g(b)\implies a=b)$)


# Lemma1: 
Seien alle möglichen Partitionen für eine Menge $[2n]$ Vertices eines [[Graph theory|Graphen]].
Seien zwei Partitionen $P_{1}, P_{2}$ benachbart, wenn $P_{2}$ durch eine einzige Tauschoperation erreicht werden kann.


Es gilt dabei: 
## Lemma 1.1: 
- Es gibt einen [[Graph theory#walk|walk]] von einer belieebigen Partition zu jeder anderen belibigen Partition (Graph ist [[Graph theory#Connected Graph|connected]])
	Insbesondere: 
	Es gibt einen walk von $P_{0}$ zu $P^{*}$, sollte es $P^{*}$ geben. 

## Lemma 1.2:
- sei zwei benachbarte Partitionen $P1,P2$. 
	- Es gilt: $Sum(P_{1})\equiv Sum(P_{2}) \mod2$ 



Es soll nun bewiesen werden, dass: 
1.
$n\not\equiv \frac{n(n+1)}{2} \mod2\implies \neg A(n)$
äquivalent zu: 
$A(n) \implies n\equiv \frac{n(n+1)}{2} \mod2$
Beweis: 
Sei $A(n)$
Demnach gibt es eine Partition $P^{*}$ von $[2n]$, sodass $\forall a,b\in P^{*}(g(a)=g(b)\implies a=b)$
Nach [[#Lemma1.1]] gibt es einen Walk von  $P_{0}$ nach $P^{*}$. 
Nach [[#Lemma 1.2]] gilt dabei $Sum(P_{0}) = n \equiv \frac{n(n+1)}{2} = Sum(P^{*})$
$\square$
2.
$\neg A(n) \implies n\not\equiv \frac{n(n+1)}{2}\mod2$
ist äquivalent zu: 
$n\equiv \frac{n(n+1)}{2}\mod2 m\implies A(n)$

Also zu zeigen: 
wenn n kongruent zu $\frac{n(n+1)}{2}$ modulo 2, dann gibt es eine Partition $P^{*}$von $[n]$, sodass $\forall a,b\in P^{*}(g(a) = g(b) \implies a=b)$













Sei n kongruent
Es gilt dann: 




Für welche n gilt $n\equiv \frac{n(n+1)}{2}\mod2$?
Für alle n, für die das gilt, muss auch gelten: 

$n=2k\implies 4|n(n+1) \land n=2k+1 \implies \neg4|n(n+1)$
$\iff$
$n=4k\lor n=4k+1$




# Hinreichende Bedingung
1. Es soll gezeigt werden, dass wenn n=4k, es für jede länge l element [n], eine Partition gibt, in der alle tupel die länge l haben
2. Es soll gezeigt werden, dass wenn es eine Partition gibt, in der die Summen der strecken n/2(n+1) beträgt, es auch die endpartition gibt.