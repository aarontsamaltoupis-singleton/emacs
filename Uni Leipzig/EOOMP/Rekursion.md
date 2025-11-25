Beispiel Fakultät:
```
public static final fakultaetRecursive(final long n){
	if (n>1){
		return n*fakultaetRecursive(n-1);
	}
	else{
		return 1;
	}
}
```