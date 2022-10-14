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

## Dlaczego korzystamy z typów wbudowanych.

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

Kiedy tworzymy obiekt, wiążemy go z określonym zbiorem operacji. Na łańcuchach znaków można wykonywać tylko operacje dostępne dla łańcuchów znaków, a na listach — tylko operacje przeznaczone dla list. Oznacza to, że Python jest językiem z typami dynamicznymi (co znaczy, że automatycznie przechowuje informacje o typach, zamiast wymagać kodu z deklaracją typu), ale jednocześnie jego typy są silne (to znaczy na obiekcie można wykonać tylko te operacje, które są poprawne dla określonego typu).

Najlepszym sposobem na rozpoczęcie czegoś jest… samo rozpoczęcie, zatem czas zabrać się za prawdziwy kod.

## Liczby

 Zbiór podstawowych obiektów Pythona obejmuje typowe rodzaje liczb: *całkowite* (liczby bez części ułamkowej), *zmiennoprzecinkowe* (liczby z częścią po przecinku), a także bardziej egzotyczne typy liczbowe (*liczby zespolone*, *liczby stałoprzecinkowe*, *liczby wymierne* z mianownikiem i licznikiem, a także pełne zbiory).

 Liczby w Pythonie obsługują normalne działania matematyczne. Na przykład znak `+` wykonuje dodawanie, znak `*` mnożenie, natomiast `**` potęgowanie.

 


# 5. Typy liczbowe

W Pythonie dane przybierają formę obiektów — albo wbudowanych obiektów udostępnianych przez język, albo obiektów
tworzonych za pomocą narzędzi Pythona i innych języków, takich jak C. Obiekty są tak naprawdę podstawą każdego programu,
jaki pisze się w Pythonie. Ponieważ są podstawowym budulcem tego języka, będą również stanowiły nasz pierwszy obiekt
zainteresowania.

## Podstawy typów liczbowych

