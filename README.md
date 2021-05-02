# Uvod v programiranje v Python-u 
KŠOK - Uvod v programiranje v programskem jeziku Python. 

V naslednjih nekaj tednih bo potekalo 6 eno in pou urnih predavanj. Soočli se bomo z vsemi potrebnimi osnovami programiranja v Pythonu, pri zadnjem predavanju 
pa bomo poskušali naučeno uporabiti v lastnem programu. 

**Kontakt predavatelja ter Zoom:**  
Liam Mislej  
  liammislej@gmail.com  
  zoom: coming soon  
  
V kolikor imate kakršnakoli vprašanja ali rabite pomoč pri programiranju izven ur predavanj, mi lahko pišete na e-naslov in vam bom z veseljem pomagal.  

---

## Novice
Novice bodo objavljene tukaj.

---

## Potek 

Predavanja bodo potekala v dveh delih. V prvem delu bodo predavanja v drugem pa vaje, približno tako kot na faksu. 
Pri predavanjih bom predaval snov(Powerpoint), povedal vse osnove in se v določene stvari poglobil. Pri vajah bomo skupaj predavano uporabili v dejanskem programu, torej bomo pisali kodo in vadili na konkretnih primerih. 

Približen potek posameznih predavanj je prikazan spodaj. Spotoma bom dodajal vse potrebne vire in osnutke. Nekatere stvari se bodo pojavle pred posameznimi predavanji nekatere pa kasneje. 

Na koncu bodo spodnji sklopi služili kot "plonk" listki, kjer bodo na kratko napisane in prikazane vse osnove s katerimi smo se soočli.

Tečaj bo sledil sklopom iz spodnjega vira, s tem da bomo sklope podrobneje predelali. 

[W3schools Python Tutorial](https://www.w3schools.com/python/default.asp)

Vsi uporabljeni oz. napisani programi se nahajajo v mapi Koda.

---

### Torek 4.5.2021 - Uvod v programiranje, osnovni pojmi, števila, nizi in ostale osnove

##### Python

Python je interpretni visokoravni večnamenski programski jezik. Interpretni (interpreted) pomeni, da se napisana koda izvaja postopoma brez potrebe po kompilaciji programa. Pomembno je vedeti, da se koda izvaja zaporedoma po vrsticah (prvo se izvede prva vrstica, nato druga, tretja, ...)



Nekateri programski jeziki uporabljajo razne znake (<code>{ }, ;, ...</code>) za ločevanje blokov kode. Pri Pythonu to ni tako; uporablja se indentacijo (indente) za ločevanje blokov. Indent je le niz, ki ga (ponavadi) sestavljajo štirje presledki, Krajše napišemo oz. natipkamo z tipko <code>Tab</code>, primer: 

Python  
```python
# To ni indentirano in vrne napako
if True:
print("Hello world")
```

```python
# To je pravilno indentirano
if True:
  print("Hello world")
```

Primer iste kode v programskem jeziku Java kjer se bloke deli z uporabo (<code>{}</code>):

```java
class HelloWorld {
    public static void main(String[] args) {
        if (True) {
            System.out.println("Hello, World!"); 
        }
    }
}
```

Seveda bo vse bolj jasno, ko se bomo s tem soočili pri predavanjih in vajah, ko bomo pisali kodo. 

##### Komentiranje (comments)

V Pythonu komentarje označimo na naslednja dva načina: 
- Z znakom <code>#</code> na začetku vrstice, uporabljamo za enovrstične komentarje
- Z uporabo treh dvojnih narekovajev <code>"""</code> na začetku in koncu komentarja, uporabljamo za večvrstične komentarje 

```python
# To je enovrstični komentar 

""" To je večvrstični komentar.
    Še ena vrstica!  """
```
##### Spremenljivke (variables)

Spremenljivke so lahko kateri koli niz ali pa ena sama črka. V spremenljivkah hranimo vse podatke kot so števila, nizi, seznami in celo funkcije. Spremenljivko definiramo z enačajem. 
Pišemo jih kot navadne besede. Ne smejo vsebovati presledkov ali se začeti z številom. V Pythonu se držimo ne napisanega pravila, da kadar spremenljivka vsebuje več besed jih povežemo z podčrtaji. 

Primer:
```python
a = 10 
to_je_spremenljivka = "Niz"
```

##### Podatkovni tipi (data types)

Podatke ločimo na več tipov, vse hranimo v spremenljivkah in vsakemu posameznemu tipu pripadajo določene metode in lastnosti.
 
- int = cela števila 1, 2, 0, -1, -2300 ...  
  ```python
    a = 10 
    b = 0
    c = 6
  ```
- float = decimalna števila 2.13, 1.5, 0.75, -2.33 ...  
  ```python
    a = 10.4 
    b = 0.5
    c = 6.123
  ```
- str = nizi in črke "a", "To je niz", "0.24"
  ```python
    a = 'a' 
    b = "beseda"
    c = "Celoten stavek."
    d = "24"  # To ni število vendar niz
  ```
- list = seznam [1, 3, 4], [[1, 2, 3], [4, 5, 6]]
  ```python
    a = [1, 2, 3]
    b = [1, 1, 1, 1, 0]
  ```
- tuple = n-terka (1, 2), (3, 4, 5)
  ```python
    a = (1, 2)
    b = (1, 2, 3, 4)
    c = (,1)
  ```
- set = množica {3, "b", "c"}
  ```python
    a = {3, 4, 10, "neki"} 
  ```
- dict = slovar {"ključ": podatek}
  ```python
    a = {"ključ 1": 5, "ključ 2": 7}
  ```
  
- bool = binarna vrednost True, False
  ```python
    a = True = 1
    b = False = 0
  ```




- Print in Input
- Števila (numbers)
- Pretvorbe podatkovnih tipov (casting)
- Nizi (strings)
- Logične vrednosti (booleans)
- Operaterji (operators)



### Torek 11.5.2021 - Podatkovni tipi in zanke

- Seznami (lists/arrays)
- Tupli (tuples)
- Množice (sets)
- Slovarji (dictionaries)
- Uporabne integrirane metode in funkcije 
- While zanka (while loop)
- For zanka (for loop)

### Četrtek 13.5.2021 - Funkcije

- Funkcije (functions)
- Lambda funkcije (lambdas)


### Torek 18.5.2021 - Objektno programiranje 

- Razredi (classes)
- Dedovanje (inheritence)

### Četrtek 20.5.2021 - Uvod v knjižnice in njihovo uporabo

- Iteratorji (iterators)
- Obseg v pythonu, funkcije v funkcijah, globalne spremenljivke (scope)
- Moduli in uvažanje (modules and imports)
- PIP 
- Nekaj integriranih knjižnjic: Date, Math, JSON, OS
- Urejanje datotek (file handling)


### Torek 25.5.2021 - Uporaba zunanjih knjižnjic, prvi celotni program


