# 4. Wprowadzenie do typów obiektów

W Pythonie dane przybierają postać obiektów — albo wbudowanych, które udostępnia Python, albo tworzonych za pomocą klas
Pythona lub innych narzędzi zewnętrznych, takich jak biblioteki rozszerzeń języka C. Można przyjąć, że są one na
ogół obszarami pamięci zawierającymi określone wartości i posiadającymi zbiory powiązanych operacji. W skryptach Pythona
wszystko jest obiektem; dotyczy to nawet zwykłych liczb (np. 99) i obsługiwanych operacji (dodawanie, odejmowanie itd.).

## Hierarchia pojęć

Programy napisane w tym języku można rozłożyć na moduły, instrukcje, wyrażenia i obiekty w następujący sposób:

1. Programy składają się z modułów.
2. Moduły zawierają instrukcje i polecenia.
3. Instrukcje i polecenia zawierają wyrażenia.
4. *Wyrażenia tworzą i przetwarzają obiekty.*

W tym rozdziale zajmiemy najniższym poziomem tej hierarchii tzn. obiektami wbudowanymi oraz wyrażeniami, które
tworzą i przetwarzają obiekty.

Instrukcje i polecenia w dużej mierze są używane do zarządzania obiektami, które spotkamy tutaj. Klasy pozwalają na
definiowanie nowych, własnych typów obiektów, zarówno poprzez korzystanie z, jak i emulowanie obiektów, które będziemy
tutaj omawiać. Z tego względu zagadnienia związane ze wbudowanymi obiektami Pythona są bardzo ważne z punktu widzenia
każdego użytkownika pragnącego programować w tym języku.

> We wprowadzeniach do programowania często mówi się o trzech kategoriach:
>
> 1. sekwencje („zrób najpierw to, potem tamto”),
> 2. wybory („zrób to, jeżeli tamto jest prawdziwe”)
> 3. powtarzanie („zrób to wiele razy”).
>
> Python oprócz tego posiada jeszcze narzędzia z kategorii definiowania pozwalające na tworzenie funkcji i klas.
> Niektóre wyrażenia stosowane w Pythonie możemy zakwalifikować zarówno jako powtórzenia, jak i wybory; niektóre z tych
> kategorii mają zupełnie inne znaczenia w Pythonie, a wiele pojęć, które poznasz nieco później, w ogóle nie pasuje do
> takiej formy podziału. W języku Python znacznie mocniej jednoczącym pojęciem są obiekty, i to, co możemy z nimi
> zrobić.

## Dlaczego korzystamy z typów wbudowanych?

W językach niższego poziomu np. w C, czy C++, programista musi wykonać wiele żmudnych, a zatem podatnych na błędy
zadań takich jak rozplanowanie pamięci i jej przydziałem czy implementowanie procedur wyszukiwania i dostępu, aby
zaimplementować obiekty (struktury danych) tak, żeby składały się na komponenty aplikacji. Zazwyczaj odwracają one uwagę
programisty od prawdziwych celów programu.

W typowych programach napisanych w Pythonie wykonywanie większości tych niewdzięcznych zadań jest całkowicie zbędne.
Ponieważ Python udostępnia wiele typów obiektów jako nieodłączną część samego języka, zazwyczaj nie ma potrzeby
dodatkowego implementowania obiektów przed rozpoczęciem rozwiązywania prawdziwych problemów.

* **Obiekty wbudowane sprawiają, że programy łatwo się pisze.** W przypadku prostych zadań obiekty wbudowane są często
  wszystkim, czego potrzebujesz do utworzenia struktur niezbędnych do działania programu. Od ręki otrzymujesz narzędzia
  o ogromnych możliwościach, takie jak kolekcje (listy) czy tabele, które można przeszukiwać (słowniki). Bardzo wiele
  zadań można wykonać, korzystając wyłącznie z samych obiektów wbudowanych.
* **Obiekty wbudowane są komponentami rozszerzeń.** W przypadku bardziej zaawansowanych zadań być może nadal konieczne
  będzie udostępnianie własnych obiektów, wykorzystywanie klas Pythona czy interfejsów języka C. Obiekty implementowane
  ręcznie są często zbudowane na bazie typów wbudowanych, takich jak listy czy słowniki. Na przykład strukturę danych
  stosu można zaimplementować jako klasę zarządzającą wbudowaną listą lub dostosowującą ją do własnych potrzeb.
* **Obiekty wbudowane są bardziej wydajne od własnych struktur danych.** Wbudowane obiekty Pythona wykorzystują
  zoptymalizowane algorytmy struktur danych, które zostały zaimplementowane w języku C w celu zwiększenia szybkości ich
  działania.
* **Obiekty wbudowane są standardową częścią języka.**  Choć w Pythonie można implementować własne, unikatowe typy
  obiektów, nie musisz tego robić, by zacząć programować w tym języku. Co więcej, ponieważ obiekty wbudowane są
  standardem, zawsze pozostają takie same; własnościowe rozwiązania stosowane w wielu frameworkach zazwyczaj mają
  tendencję do zmian wraz z upływem czasu.

## Najważniejsze typy danych w Pythonie

Tabela **Przegląd wbudowanych obiektów Pythona**

| Typ obiektu                    | Przykładowe literały ( tworzenie)                           |
|:-------------------------------|:------------------------------------------------------------|
| Liczby                         | 1234, 3.1415, 3 + 4j, 0b111, Decimal(), Fraction()          |
| Łańcuchy znaków                | 'napis', John", b'a\x01c', u'sp\xc4m'                       |
| Listy                          | [1, [2, 'trzy'], 4.5], list(range(10))                      |
| Słowniki                       | {'jedzenie': 'mielonka', 'picie': 'kawa'}, dict(godziny=10) |
| Krotki                         | (1, 'mielonka', 4, 'U'), tuple('mielonka'), namedtuple      |
| Pliki                          | open('eggs.txt'), open(r'C:\ham.bin', 'wb')                 |
| Zbiory                         | set('abc'), {'a', 'b', 'c'}                                 |
| Inne typy podstawowe           | Wartości Boolean, typy, None                                |
| Typy jednostek programu        | Funkcje, moduły, klasy                                      |
| Typy powiązane z implementacją | Kod skompilowany, ślady stosu                               |

Listy i słowniki mają ogromne możliwości reprezentowania danych, które zwalniają programistę z konieczności wykonywania
większości zadań niezbędnych zazwyczaj do zaimplementowania obsługi kolekcji i wyszukiwania w językach niższego poziomu.
Listy udostępniają uporządkowane zbiory innych obiektów, natomiast słowniki przechowują obiekty według określonego
klucza. Zarówno listy, jak i słowniki mogą być zagnieżdżane, mogą rosnąć i kurczyć się na życzenie oraz zawierać
obiekty dowolnego typu.

Jednostki programów, takie jak funkcje, moduły i klasy, w języku Python są obiektami, tworzonymi za pomocą instrukcji
oraz wyrażeń takich jak `def, class, import czy lambda`, i można je swobodnie przekazywać w skryptach bądź przechowywać
w innych obiektach. Python udostępnia również zbiór typów powiązanych z implementacją, takich jak obiekty skompilowanego
kodu, które są zazwyczaj bardziej przedmiotem zainteresowania programistów tworzących narzędzia niż twórców aplikacji.

Wszystko, co przetwarzamy w programach Pythona, jest takimi czy innymi obiektami. Na przykład, kiedy w Pythonie
wykonujemy dopasowywanie tekstu do wzorca, tworzymy obiekty wzorców, a gdy skrypty sieciowe, używamy obiektów
reprezentujących gniazda sieciowe. Te pozostałe typy obiektów tworzone są głównie poprzez importowanie i używanie
funkcji z modułów bibliotecznych (na przykład `re` dla wzorców tekstu czy `socket` dla gniazd sieciowych) i z reguły
mają swoje własne, niestandardowe typy zachowania.

Pozostałe typy obiektów z tabeli nazywane są zazwyczaj podstawowymi, ponieważ są one wbudowane w język, co znaczy, że
istnieje odpowiednia składnia wyrażeń do generowania większości z nich. Na przykład, kiedy uruchomimy następujący kod
zawierający ciąg znaków ujęty w apostrofy:

```commandline
>>> 'mielonka'
```

Z technicznego punktu widzenia wykonujemy wyrażenie z literałem, które generuje i zwraca nowy obiekt typu `string`. W
Pythonie istnieje specyficzna składnia wyrażenia, która tworzy ten obiekt. Podobnie, wyrażenie umieszczone w nawiasach
kwadratowych tworzy listę, a w klamrowych — słownik.

W Pythonie nie używamy deklarowania typów, składnia wykonywanego wyrażenia określa typy tworzonych i wykorzystywanych
obiektów.

Wyrażenia generujące obiekty, jak te z tabeli, to właśnie miejsca, z których pochodzą typy obiektów.

Kiedy tworzymy obiekt, wiążemy go z określonym zbiorem operacji. Na łańcuchach znaków można wykonywać tylko operacje
dostępne dla łańcuchów znaków, a na listach — tylko operacje przeznaczone dla list. Oznacza to, że Python jest językiem
z typami dynamicznymi (co znaczy, że automatycznie przechowuje informacje o typach, zamiast wymagać kodu z deklaracją
typu), ale jednocześnie jego typy są silne (to znaczy na obiekcie można wykonać tylko te operacje, które są poprawne dla
określonego typu).

Najlepszym sposobem na rozpoczęcie czegoś jest… samo rozpoczęcie, zatem czas zabrać się za prawdziwy kod.

## Liczby

Zbiór podstawowych obiektów Pythona obejmuje typowe rodzaje liczb: *całkowite* (bez części ułamkowej), *
zmiennoprzecinkowe* (z częścią po przecinku), a także bardziej egzotyczne typy liczbowe (*zespolone*,
*stałoprzecinkowe*, *wymierne* z mianownikiem i licznikiem, oraz pełne zbiory).

Liczby w Pythonie obsługują normalne działania matematyczne. Na przykład znak `+` wykonuje dodawanie, a `*` mnożenie,
natomiast `**` potęgowanie.

```commandline
>>> 123 + 222
345
>>> 1.5 * 4
6.0
>>> 2 ** 100
1267650600228229401496703205376
>>> len(str(2 ** 10000))
3011
>>> 3.1415
6.283
```

W Pythonie dostępnych jest kilka przydatnych modułów do obliczeń numerycznych. Moduły są po prostu pakietami dodatkowych
narzędzi, które musimy zaimportować, aby móc z nich skorzystać.

```commandline
# Moduł math
>>>  import math
>>> math.pi
3.1415926535897931
>>> math.sqrt(85)
9.2195444572928871

# Funkcje trygonometryczne
# Metoda math.sin()
>>> sin30 = math.sin(math.radians(30))
>>> print(round(sin30, 3))
0.5
>>> print(type(round(sin30)))
<class 'int'>
>>> print(format(sin30, '.3'))
0.5
>>> print(type(format(sin30, '.3')))
<class 'str'>
print('{:.3}'.format(sin30))
0.5
print('{:.3}'.format(sin30))
0.5
print(type('{:3}'.format(sin30)))
<class 'str'>

# Metoda math.cos()
>>> cos60 = math.cos(math.radians(60)) 
>>> print(cos60)
0.5000000000000001
>>> print(round(cos60, 3))
0.5
>>> print(round(cos60, 2))
0.5
# Inne metody 
>>> math.round(4.56789, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'round'
>>> math.ceil(4.56789, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: math.ceil() takes exactly one argument (2 given)
>>> math.ceil(4.56789)
5
>>> round(4.5678945)
5
>>> round(4.5678945, 2)
4.57
```

Moduł `random` pozwala na generowanie liczb losowych, a także takowe wybieranie elementu z listy (umieszczonych w
nawiasach kwadratowych, czyli uporządkowana kolekcja obiektów)

```commandline
>>> import random
>>> random.random()
0.6292299476946973
>>> random.random()
0.4265825082072393
>>> random.choice([2, 34, 56, 78, 13, 99, 45, 2, 4, 5, 11])
2
>>> random.choice([2, 34, 56, 78, 13, 99, 45, 2, 4, 5, 11])
99
>>> random.choice([2, 34, 56, 78, 13, 99, 45, 2, 4, 5, 11])
2
>>> random.choice([2, 34, 56, 78, 13, 99, 45, 2, 4, 5, 11])
13
>>> random.random()*45
3.3314559389842966
>>> random.random()*45
12.450980541107253
>>> random.random()*45
17.03755782791286ramath
>>> math.floor(random.random() * 45)
25
>>> math.floor(random.random() * 45)
8
>>> math.floor(random.random() * 45)
32
for i in range(1, 6):
...     math.floor(random.random() * 45)
...
26
37
8
14
30
```

## Łańcuchy znaków

Łańcuchy znaków (ang. *strings*) są wykorzystywane zarówno do przechowywania informacji tekstowych, jak i dowolnych
kolekcji bajtów. Są przykładem sekwencji — czyli uporządkowanych kolekcji innych obiektów. Sekwencje zachowują
porządek przechowywanych elementów od lewej do prawej strony. Elementy sekwencji są przechowywane i pobierane według ich
pozycji względnych. Ściśle mówiąc, łańcuchy znaków są sekwencjami ciągów jednoznakowych; inne, bardziej ogólne typy
sekwencji obejmują listy i krotki.

### Operacje na sekwencjach

Będąc sekwencjami, łańcuchy znaków obsługują operacje zakładające pozycyjne uporządkowanie elementów.

> Zmiennych Pythona nigdy nie trzeba deklarować z wyprzedzeniem. Zmienna tworzona jest w momencie, kiedy przypisujemy
> do niej wartość; można do niej przypisać dowolny typ obiektu i zostanie zastąpiona swoją wartością, gdy pojawi się w
> wyrażeniu.

```commandline
>>> caption = 'Przykładowy tekst'
>>> len(caption)
17
>>> caption[10]
'y'
>>> for i in caption:
...     print(i)
...
P
r
z
y
k
ł
a
d
o
w
y

t
e
k
s
t
>>> caption[-1]
't'
>>> caption[len(caption) - 1]
't'
>>> caption[-2]
's'
>>> caption[len(caption) - 2]
's'
```

Warto zauważyć, że w nawiasach kwadratowych możemy wykorzystać *dowolne wyrażenie*, a nie tylko zakodowany na stałe
literał liczbowy. W każdym miejscu, w którym Python oczekuje wartości, można użyć literału, zmiennej lub dowolnego
wyrażenia.
Sekwencje obsługują również ogólną formę indeksowania znaną jako wycinki (ang. *slice*).

```commandline
>>> caption = 'inny przykładowy tekst'
>>> caption[5:16]
'przykładowy'
>>> caption[0:4]
'Inny'
>>> caption[:4]
'Inny'
caption[17:]
'tekst'
caption[:-6]
'Inny przykładowy'
caption[:]
'Inny przykładowy tekst'
```

Ich ogólna forma, X[I:J], oznacza: „zwróć wszystkie znaki z ciągu X od przesunięcia I aż do J, ale bez tego ostatniego
elementu”. Wynik zwracany jest w postaci nowego obiektu.

Będąc sekwencjami, łańcuchy znaków obsługują również konkatenację (ang. *concatenation*) za pomocą symbolu `+` (czyli
łączenie dwóch łańcuchów znaków w jeden ciąg), a także powtórzenia (ang. *repetition*), czyli budowanie nowego
łańcucha znaków poprzez powtórzenie innego:

```commandline
>>> longCaption = caption + ' do nauki manipulowania ciągami tekstu'
>>> longCaption
'Inny przykładowy tekst do nauki manipulowania ciągami tekstu'
>>> name = 'Marek'
>>> name * 5
'MarekMarekMarekMarekMarek'
```

Znak plus `+` dla różnych obiektów może oznaczać inne operacje — dodawanie dla liczb, a konkatenację dla łańcuchów
znaków. Jest to właściwość Pythona, którą będziemy nazywali `polimorfizmem` - działanie danej operacji
uzależnione jest od typu obiektów, na jakich się ją wykonuje.

### Niezmienność

Każda operacja na łańcuchach znaków zdefiniowana jest tak, by w rezultacie zwracać nowy, ponieważ są one w Pythonie
niezmienne (ang. *immutable*). Nie mogą być zmieniane już po utworzeniu, czyli nie można nadpisywać wartości obiektów
niezmiennych, ale zawsze jest możliwość stworzenia nowego łańcucha znaków i przypisnie go do tej samej nazwy (zmiennej).

<pre>
>>> name = 'Marek'
>>> name[0] = 'J'
<code style="color:red">
Traceback (most recent call last):
  File <span style="color:aqua; text-decoration: underline">"C:\Users\Mark\AppData\Local\Programs\Python\Python310\lib\code.
py"</span>, 
line 90,
in runcode
    exec(code, self.locals)
  File "input", line 1, in 
TypeError: 'str' object does not support item assignment
</code>
</pre>

```commandline
>>> caption = 'Inny przykładowy tekst' 
>>> caption
'Inny przykładowy tekst'
>>> caption = 'Jeszcze inny tekst'
>>> caption
'Jeszcze inny tekst'
```

Każdy obiekt Pythona klasyfikowany jest jako niezmienny (niemodyfikowalny) bądź zmienny (modyfikowalny). Wśród typów
podstawowych niezmienne są *liczby, łańcuchy znaków oraz krotki*. *Listy, słowniki i zbiory* można dowolnie zmieniać w
miejscu, podobnie jak większość obiektów, które tworzymy za pomocą klas.

Dane tekstowe można modyfikować w miejscu, jeżeli zamienisz je na listę pojedynczych znaków i połączysz z powrotem bez
używania separatorów lub użyjesz typu `bytearray`.



# 5. Typy liczbowe

W Pythonie dane przybierają formę obiektów — albo wbudowanych obiektów udostępnianych przez język, albo obiektów
tworzonych za pomocą narzędzi Pythona i innych języków, takich jak C. Obiekty są tak naprawdę podstawą każdego programu,
jaki pisze się w Pythonie. Ponieważ są podstawowym budulcem tego języka, będą również stanowiły nasz pierwszy obiekt
zainteresowania.

## Podstawy typów liczbowych

