import sys
from src.Tarea_1 import (
    continuous_sine, discrete_sine,
    continuous_exponential, discrete_exponential,
    continuous_triangle, discrete_triangle,
    continuous_square, discrete_square
)
from src.Tarea_2 import understanding_freq
from src.Tarea_3 import compare_sine_signals
from src.Tarea_4 import analyze_dac_resolution


def main(options):
    if options[1].lower() == "tarea_1":
        if len(options) < 3:
            print("Qué señal quieres: seno, exponencial, triangular, cuadrada")
            return

        signal_type = options[2].lower()

        if signal_type == "seno":
            continuous_sine()
            discrete_sine()
        elif signal_type == "exponencial":
            continuous_exponential()
            discrete_exponential()
        elif signal_type == "triangular":
            continuous_triangle()
            discrete_triangle()
        elif signal_type == "cuadrada":
            continuous_square()
            discrete_square()
        else:
            print("No tengo esa. Usa: seno, exponencial, triangular o cuadrada.")

    elif options[1].lower() == "tarea_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Dame una frecuencia. Ejemplo: python main.py tarea_2 2")

    elif options[1].lower() == "tarea_3":
        if len(options) < 5:
            print("Faltan argumentos. Uso: python main.py tarea_3 <A> <f> <phi>")
            return
        A = float(options[2])
        f = float(options[3])
        phi = float(options[4])
        compare_sine_signals(A, f, phi)

    elif options[1].lower() == "tarea_4":
        if len(options) < 3:
            print("Falta el número de bits. Ejemplo: python main.py tarea_4 8")
            return
        bits = int(options[2])
        analyze_dac_resolution(bits)

    else:
        print("Tarea no reconocida. Usa: tarea_1, tarea_2, tarea_3 o tarea_4")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Dame un argumento")
        print("Ejemplos:")
        print(" python main.py tarea_1 seno")
        print(" python main.py tarea_2 2")
        print(" python main.py tarea_3 1 2 0.785")
        print(" python main.py tarea_4 8")
