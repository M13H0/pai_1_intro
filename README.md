<body>

 <h1><center>pai_1_intro</center></h1>

<h2><center>Programowanie aplikacji Internetowych -mgr inż. Wojciech Barczyński</center></h2>

<href>https://github.com/wojciech11/se_internet_app_development/tree/master/cwiczenia/01_basics</href>

<h1><b><center>Pytania</center></b></h1>

<h2>1. HTTP</h2>
<ul>
<li><b>Do czego służy PATCH czy różni się od PUT?</b>
<p style ="color:red"><b>PUT jest używane do całkowitej zamiany zasobu, podczas gdy PATCH jest stosowane do częściowej aktualizacji zasobu.</b></p>
<li><b>Na jakich metodach http polega API REST, kryjącymi się za skrótem CRUD?</b>
<p style ="color:red"><b>Skrót CRUD odzwierciedla te cztery podstawowe operacje, które mogą być wykonywane na zasobach w API REST: Create (Utworzenie), Read (Odczyt), Update (Aktualizacja) i Delete (Usunięcie). </b></p>
</ul>

<h2>2. Klient web API 1 - GET</h2>
<ul>
<li><b>1.Napisz w znanym tobie języku (i umieść w repozytorium git), program, który będzie wywoła/ściągnie: https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>2. Jeśli Twój program działa, to dodaj obsługę błędów:
<ul>
<li>Sprawdzał kodu http,
<li>Jeśli kod jest błędny, zakończył program,
<li>Wyświetlił dane kiedy nie było błędu.</b>
</ul>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>3.Jeśli powyższy program działa, umieść go w repozytorium git.</b>
<p style ="color:red"><b>Odp: </b>---</p>
</ul>

<h2>3.Klient web API 2 - POST</h2>
<ul>
<li><b>1.Zmień web API URL na https://httpbin.org/post, żebyśmy mogli zobaczyć w jaki sposób możemy przesyłać dane i zweryfikować, że we właściwy sposób wywołujemy API.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>2.Zanim prześlesz dane, nagłówek (header) Content-Type: application/json, który informuje, że mamy zamiar przesłać JSON.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>3.Dodaj dane do wywołania serwisu, powinnaś/powinienieś przesłać:
{
"name": "natalia"
}
</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>4.Zweryfikuj, że program działa i że httpbin zwrócił twoje dane w odpowiedzi.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>5.Jeśli wszystko działa, umieść tą wersję twojego programu w repozytorium git. Jako, że to jest repozytorium git, możemy nadpisać poprzednią wersję bez obaw.</b>
<p style ="color:red"><b>Odp: </b>---</p>
</ul>

<h2>4.Klient web API 3 - timeout</h2>
<ul>
<li><b>1.Zmień wywoływany url na https://httpbin.org/delay/2 (doc).</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>2.Dodaj timeout 1 sekundowy.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>3.Przetestuj aplikację, czy timeout działa.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>4.Dodaj retries and backoff, czyli N razy, jeśli wywołanie nie zadziała poczekaj dłużej przed ponownym wywołaniem API.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>5.Co to są circuit breakers i do czego służą? Dlaczego to jest ważny element aplikacji Netfixa? Zanotuj w README.md.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>6.Patrząc od strony programisty w Netflixie czy Allegro budującego serwis, dlaczego chcemy uniknąć cascading failures?</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>7.Patrząc od strony programisty w Amazonie budującego serwis, dlaczego graceful degradation jest ważny?</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>8.Jeśli powyższy program działa, umieść tą wersję twojego programu w repozytorium git.</b>
<p style ="color:red"><b>Odp: </b>---</p>
</ul>

<h2>5.Praca z danymi w formacie z JSON 1</h2>
<ul>
<li><b>1.Napisz program, który odczyta https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json i wypisze na ekran imiona wszyskich członków zespołu super bohaterów.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>2.W drugiej iteracji, wyszukaj bibliotekę jmespath (docs) dla twojego języka oprogramowania.</b>
<p style ="color:red"><b>Odp: </b>---</p>
<li><b>3.Umieść program w repozytorium git.</b>
<p style ="color:red"><b>Odp: </b>---</p>
</ul>

<h2>6.Praca z danymi w formacie JSON 2</h2>
<ul>
<li><b>Wrzuć pełną instrukcję z curl i jq do pliku README.md w Twoim repozytorium.</b>
<p style ="color:red"><b>Odp: </b>---</p>
</ul>

</body>
</html>
