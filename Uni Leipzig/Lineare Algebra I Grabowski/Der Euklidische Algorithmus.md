Sei $n_{0},m_{0}\in \mathbb{N}.$


$$
\begin{aligned}
n_{0}>m_{0}
(n_{0},m_{0})\to(n_{1},m_{1})\to\dots\to(r_{-1},r)\to(r,0) \\ 
n_{0} = k\cdot m_{0}+m_{1}, 0<m_{1}<m_{0} \\
m_{1} = n_{0}-k\cdot m_{0}
\\n_{1} = m_{0}
 \\
 \\ 
\end{aligned}
$$Informaler Beweis, dass das r aus dem letzten Tupel $(r,0)$ des Alogrithmus
der $ggT(m_{0},n_{0})$ ist:
$$
\begin{align}

\text{Sei } t\in \mathbb{N}, \ t|n_{0},\ t|m_{0}.\\
t|n_{1},\text{da } n_{1} = m_{0}\\
t|m_{1}, \text{da}\ m_{1} = n_{0} - k\cdot  m_{0} \text{ und } t| n_{0} \land t|m_{0} 
\\
\\
t|n_{0},m_{0} \implies t|n_{1},m_{1}
\\
\end{align}
$$

Jedes Tupel hat also dieselben Teiler, wie die vorherigen Tupel. Deshalb haben auch $r,0$ dieselben Teiler wie $(n_{0},m_{0})$}.
Da der größte gemeinsame Teiler von $r$ und $\hspace{0pt}0$ $r$ ist, gilt: $$
ggT(m_{0},n_{0}) = r
$$
Allgemeiner gilt: 
$t|a \land t|b \implies t|ggT(a,b)$

# Erweiterter Euklidischer Algorithmus
Lösung **Diophantischer Gleichungen**: 




Eine Diophantische Gleichung $ax+by=c$ kann nur eine Lösung haben, wenn $ggT(a,b)|c$.
Also insbesondere in dem Fall, wenn $a$ und $b$ Teilerfremd sind.


Bsp: 
$99x+35y=1$
$\iff \underbrace{ (2\cdot35+29) }_{ 99 }x+35y =1$
$\iff 35(\underbrace{ y+2x) }_{ y_{1} }+29x =1$
$\iff 35y_{1}+29x=1$

$\iff (29+6)y_{1}+29x=1$

$\iff 29(y_{1}+x)+6y_{1}=1$

...

$\iff 5x_{2}+y_{2}=1$


$5x_{2}+y_{2}=1$
Sei $x_{2}$
$\implies y_{2}=1$




Weitere Lösungen der diophantischen Gleichung: 
