def rzymskie_na_arabskie(rzymskie):
    # twój kod
    if not isinstance(rzymskie, str):
        raise ValueError("Liczba rzymska musi być napisem (str).")

    rzymskie = rzymskie.upper()
    slownik = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    for znak in rzymskie:
        if znak not in slownik:
            raise ValueError("Niepoprawny format liczby rzymskiej.")

    wartosc = 0
    i = 0

    while i < len(rzymskie):
        if i + 1 < len(rzymskie) and slownik[rzymskie[i]] < slownik[rzymskie[i+1]]:
            wartosc += slownik[rzymskie[i+1]] - slownik[rzymskie[i]]
            i += 2
        else:
            wartosc += slownik[rzymskie[i]]
            i += 1

    if arabskie_na_rzymskie(wartosc) != rzymskie:
        raise ValueError("Niepoprawny format liczby rzymskiej.")

    return wartosc


def arabskie_na_rzymskie(arabskie):
    # twój kod
    if not isinstance(arabskie, int):
        raise ValueError("Liczba arabska musi być typu int.")
    if not (1 <= arabskie <= 3999):
        raise ValueError("Liczba musi być w zakresie 1-3999.")

    tlumacz = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    rzymskie = ""
    liczba = arabskie

    for wartosc, znak in tlumacz:
        while liczba >= wartosc:
            rzymskie += znak
            liczba -= wartosc
    return rzymskie

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
