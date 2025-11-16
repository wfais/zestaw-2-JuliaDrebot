import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Generowanie wartości x i y przy użyciu eval()
    # Rysowanie wykresu ale bez show()
    expr_str, przedzial = wejscie.split(",")
    expr_str = expr_str.strip()
    a, b = map(float, przedzial.split())
    x = np.linspace(a, b, 400)
    lokalne = {"x": x, "sin": np.sin, "cos": np.cos, "np": np}
    y_val = eval(expr_str, {}, lokalne)
    plt.figure()
    plt.plot(x, y_val)

    # Zwracanie wartości na granicach przedziału
    return y_val[0], y_val[-1]

# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Definicja symbolu i konwersja do funkcji numerycznej za pomocą SymPy
    # Generowanie wartości x i y przy użyciu funkcji numerycznej
    # Rysowanie wykresu ale bez show()
    expr_str, przedzial = wejscie.split(",")
    expr_str = expr_str.strip()
    a, b = map(float, przedzial.split())
    x = symbols("x")
    expr = sympify(expr_str)
    f = lambdify(x, expr, "numpy")
    xs = np.linspace(a, b, 400)
    y_val_sympy = f(xs)
    plt.figure()
    plt.plot(xs, y_val_sympy)

    # Zwracanie wartości na granicach przedziału
    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.show()
