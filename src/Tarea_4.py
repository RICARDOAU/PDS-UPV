import numpy as np
from src.utils.grapher import dac_plotter  # ← Nueva función que debes tener en grapher.py


def analyze_dac_resolution(bits: int):
    # Parámetros del DAC
    Vref = 5.0  # Voltaje de referencia
    N = bits

    # Cálculos
    niveles = 2**N
    tamaño_paso = Vref / (niveles - 1)
    resolucion_porcentual = (tamaño_paso / Vref) * 100

    # Mostrar resultados
    print(f"--- Análisis DAC de {N} bits ---")
    print(f"Niveles totales      : {niveles}")
    print(f"Tamaño del paso      : {tamaño_paso:.6f} V")
    print(f"Resolución porcentual: {resolucion_porcentual:.6f} %")

    # Generar datos de la señal DAC
    entradas_digitales = np.arange(0, niveles)
    salida_analogica = entradas_digitales * tamaño_paso

    # Llamar a la función de graficación desde grapher
    dac_plotter(entradas_digitales, salida_analogica, bits)


    