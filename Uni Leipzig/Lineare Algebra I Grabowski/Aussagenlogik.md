Aussage: 
Äußerung, die entweder wahr oder falsch ist. Sie hat genau einen Wahrheitswert, dieser darf unbekannt sein. 

Keine Aussage: 
'Dieser Satz ist falsch.' 
	- Kann kein Wahrheitswert haben, führt immer zu Widerspruch


## Definition (informell): Atome & Formeln
Atome= primitive Aussagen wie $A,B$.
	Wahrheitswert von Atom = Gültigkeit fachlicher "Aussage". 
Formeln= Kombinationen von Atomen, $z$.$B$.: $(A\land B)\lor C$
		Wahrheitswert von Formel = ergibt sich aus Wahrheitswerten der vorkommenden Atome unter Anwendung der oben genannten Regeln 

**Rangfolge logischer Operationen:** 
- Negationen
- Konjunktionen
- Disjunktionen
- Implikationen
- Äquivalenz

## Definitionen: verschiedene Arten an Formeln

- **Tautologie**: 
	- Formel ist unabhängig von der Belegung der Atome immer wahr
		- "Tautologien sind immer wahr"
- **Widerspruch, unerfüllbar**: 
	- Formel ist unabhängig von der Belegung der Atome immer falsch
		- "Kontradiktionen sind immer falsch"
- **erfüllbar**: 
	- Formel ist kein Widerspruch: es gibt eine Belegung der Atome, sodass die Formel wahr ist.
- **widerlegbar**:
	- Formel ist keine Tautologie: es gibt eine Belegung der Atome, sodass die Formel falsch ist.
# Gesetze der Logik

|                      |                                   |                               |
| -------------------- | --------------------------------- | ----------------------------- |
| $A\land B$           | $B\land A$                        | Kommutativitä$t$ von $\land$  |
| $A\lor B$            | $B\lor A$                         | Kommutativitä$t$ von $\lor$   |
| $(A\land B) \land C$ | $A\land (B\land C)$               | Assoziativitä$t$ von $\land$  |
| $(A\lor B)\lor C$    | $A\lor(B\lor C)$                  | Assoziativitä$t$ von $\lor$   |
| $A\land(B\lor C)$    | $(A\land B)\lor(A\land C)$        | Distributivitä$t$ von $\land$ |
| $A\lor(B\land C)$    | $(A\lor B)\land(A\lor C)$         | Distributivitä$t$ von $\lor$  |
| $A\land A$           | $A$                               | Idempotenz von $\land$        |
| $A\lor A$            | $A$                               | Idempotenz von $\lor$         |
| $\neg \neg A$        | $A$                               | Involution $\neg$             |
| $A\lor \neg A$       | $1$                               | Ausgeschlossenes Drittes      |
| $\neg (A\land B)$    | $\neg A \lor \neg B$              | De-Morgan Gesetz für $\land$  |
| $\neg(A\lor B)$      | $\neg A\land \neg B$              | De-Morgan Gesetz für $\lor$   |
| $A\land(A\lor B)$    | $A$                               | Absorptionsgesetz für $\land$ |
| $A\lor (A\land B$    | $A$                               | Absorptionsgesetz für $\lor$  |
| $A\implies B$        | $\neg A\lor B$                    | Elimination von $\implies$    |
| $A\iff B$            | $(A\implies B)\land(B\implies A)$ | Elimination von $\iff$        |
