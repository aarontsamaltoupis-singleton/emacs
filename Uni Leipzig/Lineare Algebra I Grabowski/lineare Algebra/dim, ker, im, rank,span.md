---
id: dim, ker, im, rank,span
aliases: []
tags: []
---

# Span
seien $v_{1},\dots,v_{n}\in V$  
Der lineare Span dieser Vektoren ist die Menge
$span(v_{1},\dots,v_{n})$ aller [[Vektorraum|Linearkombinationen]] der Form 
$a_{1}v_{1},\dots a_{r}v_{r}$, wobei $a_{i}\in \mathbb{K}$

$span(v_{1},\dots,v_{n})$ ist ein  [[Untervektorraum]] von $V$ 

## Berechnung der Basis des Span
- Sei die Matrix

# Kern
$\ker(A):=\{ v\in V:A(v)=0 \}$

- Wenn A eine [[Matrix|Matrix]], dann $ker(A)$ sind die Lösungen des Systems $AX=0$
- ker(A) ist ein [[Untervektorraum]] von V


# Bild
$im(A)=A(V)=\{ A(v):v\in V \}$

- im(A) ist ein Untervektorraum von W
- 
Sei $A$ eine Matrix, mit $[v_{1},\dots,v_{n}]$ als Spaltenvektoren.
$span[v_{1},\dots,v_{n}]=im(A)$

# Rang
rank(A):= dim(im(A))=dim span(v1,...,v_n), wenn $A = [v1,...,v_n]$
