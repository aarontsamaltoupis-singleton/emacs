---
id: Addition
aliases: []
tags: []
---

#Peano_Axioms
#Tao_Analysis1 
# Definition 2.2.1: Addition of natural numbers

Let $m$ be a natural number. 
We define: 
$0+m:=m$

**Defining addition inductevely:**
Suppose $n+m$ is defined.

$(n++)+m:=(n+m)++$
## [[Recursive Definitions|recursive]] definition: 
base case: $a_{0} = 0+m =  m$
$a_{n}=n+m$
$S(n)+m=a_{S(n)}=f_{n}(a_{n})=S(a_{n})=S(a+m)$


# Lemma 2.2.2.
$\forall n\in N:n+0 = n$

# Lemma 2.2.3 
$\forall n,m\in N n+S(m) = S(n+m)$

# Proposition 2.2.4 (Addition is commutative)
$\forall n,m\in N: n+m=m+n$

# Proposittion 2.2.5 (Addition is associative)

# Proposition 2.2.6 (Cancellation law)
$\forall a,b,c\in N: a+b=a+c\implies b=c$

