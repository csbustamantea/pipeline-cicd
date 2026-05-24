# app.py — Aplicación de calculadora simple

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

if __name__ == "__main__":
    print("Calculadora lista")
    print(f"2 + 3 = {sumar(2, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"3 x 5 = {multiplicar(3, 5)}")
    print(f"10 / 2 = {dividir(10, 2)}")
