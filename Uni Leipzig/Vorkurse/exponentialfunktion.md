

Die Folge $(x_1,x_2,...)$ mit $x_n = (1+\frac{x}{n})^n$ ist [[streng monoton wachsend]] und [[beschränkte mengen|nach oben beschränkt]] von dem Grenzwert  $e^x:= lim_{n\to\infty}(1+\frac{x}{n})^n$.

- $\lim \limits_{n\to\infty} x_n = e^x$
- $e = \lim\limits_{n\to\infty}(1+\frac{1}{n})^n$

Definition der $exp$ funktion: 

$exp : \mathbb{R} \to \mathbb{R}, exp(x) := \Bigl\{^{\lim \limits_{n\to \infty}(1+\frac{x}{n})^n, x\geq 0}_{\frac{1}{exp(|x|)},falls \ x<0}$
**
Es folgt aus dieser Definition:
$exp(0) = 1$
$exp(1) = e$

Die Exponentialfunktion $exp$ hat die folgenden Eigenschaften, die aus der Definition abgeleitet werden können: 

1. $x\to exp(x)$ ist streng monoton wachsend
2. $\forall y>0 (!\exists x\in\mathbb{R}(y = exp(x)))$ : 
	- Die Exponentialfunktion ist [[injektiv_injective_one-to-one]]
3. $\forall x,y\in\mathbb{R}(exp(x+y) = exp(x)\cdot exp(y))$
	- erste Rechenregel der [[potenzen|Potenzen]]	
	- $exp(x)\cdot exp(y) = \lim\limits_{n\to\infty}\left( 1+\frac{x}{n}  \right)^n \cdot \lim\limits_{n\to\infty}\left( 1+\frac{y}{n}  \right)^n =\lim\limits_{n\to\infty}( \left( 1+\frac{x}{n} \right)(1+\frac{y}{n}))^n =$
4. Die Funktion $x\to \exp(x)$ ist differenzierbbar mit $\frac{d}{dx} \exp(x) = \exp(x)$
	- **Beweis für x>0:**
	- Frage: warum gilt $\lim\limits_{ n \to \infty } \left(1+\frac{x}{n}\right)^{n} \cdot (1+\frac{x}{n})^{-1} = \exp(x)$? 
-

# Umkehrfunktion log von exp


Aus diesen Eigenschaften folgt: $\exp: \mathbb{R}\to \mathbb{R}_{+}$ ist [[bijektiv]].
Deshalb kann eine Umkehrfunktion von $\exp$ $$
\log:\mathbb{R}_{+}\to \mathbb{R}
$$
Es gilt: $$
\exp(\log(x)) = \log(\exp(x)) = x
$$
## Logarithmusgesetze:

Es folgen die  Logarithumusgesetze:

$$
\log(x\cdot y) = \log x +\log y
$$
$$
\log (\frac{x}{y}) = \log x - \log y
$$
$$
\log(x^{t}) = t \log y
$$

# Exponentialfunktion zur Basis a
**Definition:** Sei $a\in \mathbb{R}_{+}$. Dann heißt $$
f_{a}: \mathbb{R}\to \mathbb{R} , \ x\mapsto  a^{x}:= \exp(x\log a)
$$
	die **Exponentialfunktion zur Basis $a$.




