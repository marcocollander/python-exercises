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

|Typ obiektu | Przykładowe literały ( tworzenie)|
|  :-------  |:----------------------------- |
| Liczby          | 1234, 3.1415, 3 + 4j, 0b111, Decimal(), Fraction() |
| Łańcuchy znaków | 'napis', John", b'a\x01c', u'sp\xc4m'|
| Listy | [1, [2, 'trzy'], 4.5], list(range(10)) |
| Słowniki | {'jedzenie': 'mielonka', 'picie': 'kawa'}, dict(godziny=10)|
| Krotki | (1, 'mielonka', 4, 'U'), tuple('mielonka'), namedtuple |
| Pliki | open('eggs.txt'), open(r'C:\ham.bin', 'wb')|
| Zbiory | set('abc'), {'a', 'b', 'c'} |
| Inne typy podstawowe | Wartości Boolean, typy, None|
| Typy jednostek programu | Funkcje, moduły, klasy|
| Typy powiązane z implementacją | Kod skompilowany, ślady stosu |















# 5. Typy liczbowe

W Pythonie dane przybierają formę obiektów — albo wbudowanych obiektów udostępnianych przez język, albo obiektów
tworzonych za pomocą narzędzi Pythona i innych języków, takich jak C. Obiekty są tak naprawdę podstawą każdego programu,
jaki pisze się w Pythonie. Ponieważ są podstawowym budulcem tego języka, będą również stanowiły nasz pierwszy obiekt
zainteresowania.

## Podstawy typów liczbowych

