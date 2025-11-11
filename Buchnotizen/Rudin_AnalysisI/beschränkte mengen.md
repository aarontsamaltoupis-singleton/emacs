#Rudin 
**Definition**
Sei $M$ eine [[Geordnete Menge|geordnete menge]] und sei $E\subset M$.

# Obere Schranken
$E$ ist **nach oben beschränkt** $\iff$ $\exists \beta \in M(\forall x\in E(x \leq\beta))$
Es gibt ein $\beta$ aus $M$, dass größer als alle Elemente aus  $E$ ist.
$\beta$ ist eine **obere Schranke** von $E$.
## Supremum von E
**Definition**
Sei $M$  eine geordnete Menge und sei  $E$ eine **nach oben beschränkte**  Teilmenge von $M$.
i) $\alpha$ ist **eine** obere Schranke von $E$.
ii) Ist $\gamma < \alpha$, so ist $\gamma$ keine obere Schranke von $E$.

$\alpha$ ist die **kleinste obere Schranke** von $E$, oder das **Supremum vom E**.
$\alpha = \sup E$
Es gibt nur ein Supremum, dies folgt aus ii).
# Untere Schranken
$E$ ist **nach unten beschränkt** $\iff$ $\exists \beta \in M(\forall x\in E(x \geq\beta))$
Es gibt ein $\beta$ aus $M$, dass **kleiner** als alle Elemente aus   $E$ ist.
$\beta$ ist eine **untere Schranke** von $E$.

Es kann mehrere obere Schranken einer Teilmenge geben, die nicht unbedingt Element dieser Menge sein müssen.

# Infimum von E
Definition analog zu dem [[#Supremum von E]].


# Supremums Eigenschaft einer Menge M
**Definition**
Eine [[Geordnete Menge|geordnete Menge]] $M$ hat die Supremums-Eigenschaft, wenn fü$r$ alle Teilmengen $E$ gilt:

- $(E\subset M\neq \varnothing \land \text{E ist nach oben beschränkt})\implies \text{sup E existiert in M}$

- Fü$r$ jede beschränkte Teilmenge $M$ gibt es also immer eine eindeutige kleinste Schranke

$\mathbb{Q}$ hat die Supremums- Eigenschaft nicht:
Beispiel:

Sei $A:=\{ x\in \mathbb{Q}^{+}|p^{2}<2 \}$
A ist nach oben beschränkt von genau den Elementen der Menge $B:=\{ x\in\mathbb{Q}^{+}|p^{2}>2\}$. Da $B$ kein kleinstes Element hat und es kein eindeutiges Element gibt, sodass $p^{2} = 2$, hat $A$ keine kleinste Schranke und somit kein Supremum.

