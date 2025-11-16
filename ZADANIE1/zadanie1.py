def dodaj_element(wejscie):
    listy=[]

    def znajdz_listy(obj, poziom):
        if isinstance(obj, list):
            listy.append((obj, poziom))
            for el in obj:
                znajdz_listy(el, poziom + 1)
        elif isinstance(obj, tuple):
            for el in obj:
                znajdz_listy(el, poziom + 1)
        elif isinstance(obj, dict):
            for val in obj.values():
                znajdz_listy(val, poziom + 1)

    znajdz_listy(wejscie, 0)

    if not listy:
        return wejscie

    max_poziom = max(poziom for _, poziom in listy)

    for lst, poziom in listy:
        if poziom == max_poziom:
            if len(lst) == 0:
                lst.append(1)
                continue 
            numeric = [x for x in lst if isinstance(x, (int, float))]
            if numeric:
                lst.append(max(numeric) + 1)
            else:
                lst.append(1)
    return wejscie

if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)