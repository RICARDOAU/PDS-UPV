# Importa la librería numpy para manejar arreglos y cálculos numéricos
import numpy as np

# Importa la función para graficar señales continuas desde el módulo grapher
from src.utils.grapher import continuous_plotter

# Función que genera una señal senoidal con la frecuencia que el usuario indique
def understanding_freq(des_freq):
    initial_time = 0      # Tiempo inicial del eje temporal
    end_time = 5          # Tiempo final del eje temporal
    frequency = float(des_freq)  # Convierte el parámetro recibido a tipo float para usarlo como frecuencia
    amplitude = 1         # Amplitud de la señal senoidal
    number_of_points = 1000  # Número de puntos para generar la gráfica suave (más puntos = mejor resolución)

    # Genera el arreglo de tiempo con valores uniformemente espaciados
    time = np.linspace(initial_time, end_time, number_of_points)

    # Calcula la señal senoidal: x(t) = A * sin(2πft)
    xt = amplitude * np.sin(2 * np.pi * frequency * time)

    # Llama a la función que grafica la señal continua
    continuous_plotter(
        time, xt,                        # Eje x (tiempo) y eje y (señal)
        'Continuous Sine wave Signal',  # Título de la gráfica
        'Sin wave Signal',              # Subtítulo o etiqueta de la función
        'Time [s]',                     # Etiqueta del eje x
        'Amplitude'                     # Etiqueta del eje y
    )
