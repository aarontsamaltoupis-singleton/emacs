schlüssel ncht sortiert gespeichert

Hinzufügen:
put(Schlüssel,Wert)

```
HasMap<String,Integer> map = new HasMap<>();
map.put("Apfel",5);
int wert = map.get("Apfel"); //liefert 5
```


- wird versucht zwei mal derselbe Schlüssel hinzuzufügen, wird der erste eintrag überschrieben
- wert null ist sowohl als wert, wie als schlüssel erlaubt