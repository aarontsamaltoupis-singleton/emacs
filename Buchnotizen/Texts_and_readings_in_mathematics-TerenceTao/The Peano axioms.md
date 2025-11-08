#Tao_Analysis1
# Definition 2.1.1 (Informal): natural number
#Peano_Axioms
A *natural number* is any element of the set
$\mathbb{N} :=\{ 0,1,2,3,4,\dots \}$

which is the set of all the numbers created by starting with 0 and then counting forward indefinitely.

**N conists of 0 and everything which can be obtained from 0 by incementing**


# Axiom  2.1:
 **0 is a natural number**
# Axiom 2.2: 
**If n is a  natural number, then n++ is also a natural number.**

From [[#Axiom 2.1]] and 

A set like $\{ 0,1,2,3,4 \}$ could obey these Axioms.

# Axiom 2.3:
**0 is not the successor of any natural number**
$\forall_{n\in \mathbb{N}}\ n++\neq0$

# Axiom 2.4:
**Different natural numbers mut have different successors**
$\forall n,m\in \mathbb{N}(n\neq m\implies n++\neq m++)$
$\forall n,m\in \mathbb{N}(n++=m++\implies n=m)$



# Axiom 2.5 (principle of mathematical Induction)
Let P(n) be any property pertaining to a natural number n. 
Suppose P(0) is true and suppose that whenever P(n) is true, P(n++) is also true.
Then P(n) is true for every natural number n.


# Assumption 2.6
There exists a number system $\mathbb{N}$, whose elements we will call **natural numbers**, for which Axioms 2.1 - 2.5 are true.


