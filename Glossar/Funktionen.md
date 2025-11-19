---
aliases:
  - mapping
  - function
  - Abbildung
---
[[injektiv_injective_one-to-one|injektive Funktionen]]
[[bijektiv|bijektive Funktionen]]
[[surjektiv_onto_functions|surjektive Funktionen]]



# Tao, Analysis I
#Tao_Analysis1
## Definition 3.3.1
Let $X,Y$ be [[Mengen|sets]].

Let P(x,y) be a property pertaining to an object $x\in X$ and an object $y\in Y$
For every $x\in X$ there is exactly one $y\in Y$ for which $P(x,y)$ is true.

A function can be associated and defined to this property: 
The function $f:X\to Y$ *defined by P on the domain X and the range Y* is defined to be the **object** which assigns to any **input** $x\in X$ an output $f(x)\in Y$, which is the **unique** object for which $P(x,f(x))$ is true.

$y=f(x)\iff P(x,y)$ is true

### explicit, implicit definitions
**explicit:**
Bsp:$f$ has domain and [[Wertebereich|range]] $N$ and $f(x):=S(x), \forall x\in N$
**implicit**: 
- specifying what property P(x,y) links the input x with the output f(x)
- this is only valid if we know that for every input there is exactly one output obeying the implicit relation

## Definition 3.3.7 (equality of functions)
suppose $f:X\to Y, g:X\to Y$
$f=g\iff f(x)=g(x)\forall x\in X$

[[Komposition_composition|composition of functions]]
