class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def raiz_cuadrada(self, x):
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        aproximacion = x / 2.0
        for _ in range(20):  # 20 iteraciones para aproximación
            aproximacion = (aproximacion + x / aproximacion) / 2.0
        return aproximacion