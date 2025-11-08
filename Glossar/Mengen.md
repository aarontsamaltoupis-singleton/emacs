---
id: Mengen
aliases: []
tags: []
---
[


Alle mathematischen Strukuren können mithilfe von Mengen definiert werden.


Sei $I$ eine Menge und Sei $M_{i}$ eine Menge für jedes $i\in I$.

Wir definieren: 

$\underset{i\in N}{\bigcup }M_{i}:=\{x: \exists i\in I(x\in M_{i})\}$
$\underset{i\in N}{\bigcap }M_{i}:=\{x: \forall i\in I(x\in M_{i})\}$

$I$ ist die **Indexmenge**.


# Komplemente
Es seien $A,B\subset X$.
$A \textbackslash B :=\{ x\in X;(x\in A)\land (x\not\in B) \}$
Die Menge $A \textbackslash B$ ist das **relative Komplement von $B$ in A.

Ist aus dem Zusammenhang klar, vo welcher Obermenge $X$ die Rede ist, setzen wir:
$A^{c} := X\backslash A$

$A^{c}$ ist das **Komplement** von A.
Es gilt: $A\backslash B= A\cap B^{c}$


# Tao
#Tao_Analysis1 
## Axiom 3.1 (Sets are objects)
If A is a set, then A is also an object.
In particual given two sets A and B, it is meaningful to ask whether A is also an element of B.


## Axiom 3.2 (Empty set)
There exists a set $\emptyset$ known as the *emtpy set* which contains no elements, i.e. for every object x we have $x\not\in \emptyset$

## Axiom 3.3 (singleton sets and pair sets)
Ifa is an object, then there exists a set $\{ a \}$ whose only element is a.
Also: For every object y we have $y\in \{ a \}\iff y=a$
$\{ a \}$ is the singleton set whose element is $a$.

If a and b are objects, then there exists a set $\{ a,b \}$whose only elements are a and b.
this is the pair set formed by a and b.

## Axiom 3.4 (Pairwise union)
Given any two sets A,B there exists a set $A\cup B$, called the *union* of A and B whose elements consist of all the elements which belong to A or B or both.

### Definition 3.1.15 (Subsets)

## Axiom 3.5 (Axiom of specification, Axiom of seperation)
Let A be a set, and for each $x\in A$ let $P(x)$ be a property pertaining to $x$.
Then there exists a set $\{ x\in A:P(x) \}$ whose elements are precisely the elements $x\in A$ for which $P(x)$ is true.
In other words for any object $y$:
$y\in \{ x\in A:P(x) \}\iff(y\in A\land P(y))$

### Definition 3.1.23 (Intersections)
## Axiom 3.6 (Replacement)


## Axiom 3.10 (Power set axiom)
Let $X$ and $Y$ be sets. Then there exists a set,  denoted $Y^{X}$ which consists of all the [[Funktion_Abbildung|functions]] from $X$ to $Y$, thus
$f\in Y^{X}\iff$($f$ is a function with domain $X$ and range $Y$)

### Remark 3.4.10 (Power set)
The set $\{ Y: Y \subseteq X \}$
