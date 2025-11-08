
# Informatikbbiber - Castor informaticus:
spezielle [[Turingmaschinen]] mit folgenden Eingenschaften:

- Eingabe besteht immer aus leerem Turingband
- Bandalphabet besteht aus zwei Zeichen:
	- $\Sigma = {1}$
	- $A = \{ \#,1 \}$
- Die Turingtafeln der Biber sind vollständig
	- Sie terminieren demnach nur aufgrund des Stopp-Signals


Wenn eine Untergattung $\hat{T}$ an Bibern **maximal** bezüglich einer gewissen Eigenschaft ist, bedeutet dies, dass jede andere **terminierende** Turingmaschine $T$ mit **der gleichen Anzahl an Zuständen** diesen Biber in dieser Eigeinschaft nicht übertrifft:

Eine dieser Untergattungen an Biber ist die Gattung der **fleißigen Bieber**:
# Fleißige Bieber - Castor industrius
- Biber, die maximal in der Eigenschaft sind nach dem Halten möglichst viele Einsen auf das Band geschrieben zu haben. 

Bei n Zuständen gibt es $(6n)^{2n}$ verschiedene vollständig definierte Turingmaschinen.
# Konstruktion von fleißigen Biebern
- Jeder Biber ist eine Turingmaschine mit:
	- n Zustände, aus denen eine Aktion ausgeführt wird
	- 2 Zeichen, die gelesen werden können
	- 3 Bewegungen, die ausgeführt werden können
	- 2 Zeichen, die geschrieben werden können
	- n Zustände, in die nach der Aktion übergegangen wird

Die Biber unterscheiden sich dabei in den Zeichen, die geschrieben werden, die Bewegungen, die ausgeführt werden und in die Zustände, in die übergegangen wird. 

Pro Element des Definitionsbereiches der Überführungsfunktion gibt es $3\cdot2\cdot n$ Unterschiedliche Mögliche Anweisungen. 
Da der Definitionsbereich der Überführungsfunktion bei einer vollständigen Turingmaschine $2\cdot n$ Elemente hat und Anweisungen sich auch doppeln können, gibt es insgesamt $(6n)^{2n}$ Turingmaschinen, die sich in mindestens einer Anweisung unterscheiden. 


Von allen möglichen $(6n)^{2n}$ Turingmaschinen sind folgende garantiert keine fleissigen Biber: 

- Maschinen, die kein Stoppsignal enthalten
- enthält Kombination $(Q_0,n\in A, S ,Q_{n} \in Z)$
	- Maschine würde stoppen, sobald erstes Leeres Zeichen gelesen wird







