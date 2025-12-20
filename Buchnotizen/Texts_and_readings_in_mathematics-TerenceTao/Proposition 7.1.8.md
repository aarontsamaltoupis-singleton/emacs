Sei $f: X\to \mathbb{R}$

Seien zwei Bijektionen $g,h: \{1,\dots ,|X|\}\to X$

Zu zeigen ist, dass 
$$
    \sum_{i=1}^{n}f(h(i))=\sum_{i=1}^{n}f(g(i))
$$

Sei $|X|=n$.
Sei  $\sum_{i=1}^{n}f(h(i))=\sum_{i=1}^{n}f(g(i))$, für **alle** Bijektionen h,g **(Induktionshypothese)**

Sei  $|X|=n+1$
$g,h: \{1,\dots ,n+1\}\to X$

Sei $g(n+1)=x$
Sei $h(j)=x$

$$

    \begin{align}
        &\sum_{i=1}^{n+1}f(g(i))=\sum_{i=1}^{n}f(g(i))+f(x)\\
    \end{align}
$$
$$
    \begin{align}
        \sum_{i=1}^{n+1}f(h(i))=& \sum_{i=1}^{j-1}f(h(i))+f(h(j))+\sum_{i=j+1}^{n+1}f(h(i))\\
        =& \sum_{i=1}^{j-1}f(h(i))+\sum_{i=j}^{n}f(h(i+1))+f(x)
    \end{align}
$$

Definiere eine neue Funktion

$\tilde{h}:\{1,\dots ,n\}\to X\backslash \{x\}$

$$
\tilde{h}(i)=
\begin{cases}
        h(i), \textnormal{falls i<j}\\
        h(i+1), \textnormal{falls } i\geq j
    \end{cases}
$$

$\tilde{h}$ ist wohldefiniert:
$\tilde{h}(i)\in X\backslash \{x\}$:
$\tilde{h}(i)$ ist niemals gleich $h(j+1)=x$
$h(i+1)$ ist wohldefiniert: 
$i+1<n+1\implies i+1\in def(h)$

$\tilde{h}$ ist surjektiv:
Ansonsten wird jeder Funktionswert von $h(i)$ angenommen und $h$ ist surjektiv. 

$\tilde{h}$ ist injektiv:
$h(i)\neq h(i+1)$


Somit gilt:
$$
    \begin{align}
     
      \sum_{i=1}^{n+1}f(h(i))  &=\sum_{i=1}^{j-1}f(h(i))+\sum_{i=j}^{n}f(h(i+1))+f(x)\\
        &= \sum_{i=1}^{j-1}f(\tilde{h}(i))+\sum_{j}^{n}f(\tilde{h}(i))+f(x)\\
        &=\sum_{i=1}^{n}f(\tilde{h}(i))+f(x)\\
        &\overset{IH}{=} \sum_{i=1}^{n}f(g(i))+f(x)=\sum_{i=1}^{n+1}f(g(i))
    \end{align}

$$
