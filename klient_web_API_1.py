import requests 

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json" 
response = requests.get(url)  # Wykonanie żądania GET na podany adres URL i zapisanie odpowiedzi

if response.status_code == 200:  # Sprawdzenie, czy żądanie zakończyło się sukcesem (200 = sukces)
    data = response.json()  # Przetworzenie odpowiedzi do formatu JSON i przypisanie jej do zmiennej "data"
    
    print(data)  
else:
    print("Wystąpił błąd podczas pobierania danych.")  