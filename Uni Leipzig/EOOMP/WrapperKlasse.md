
| primitiv | Wrapper Klasse (java.lang) |
| -------- | -------------------------- |
| byte     | Byte                       |
| short    | Short                      |
| int      | Integer                    |
| long     | Long                       |
| boolean  | Boolean                    |
| char     | Character                  |
| -        | String                     |
[[java primitive datentypen|Primitive Datentypen]] sind keine objekte.
Wrapper Klassen sind eine Möglichkeit die Werte der Primitiven Datentypen in Form von Instanzen von Klassen und somit Objekten zu speichern.
 
 Alle Wrapper Klassen für primitive Datentypen sind **immutable** (unveränderlich)
 Änderung eines Wertes nur durch neue instanz möglich

[[Generics|generische Klassen]] können nur mit [[object klasse|Objekten]] arbeiten.

- Objekt kann `null` sein, ein primitiver Datentyp nicht
	- methoden die fehlende werte erlauben benötigen somit ebenfalls wrapperklassen anstelle primitiver Datentypen


