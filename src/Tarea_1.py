import numpy as np 
from scipy import signal   # Importa funciones para generar señales como triangular y cuadrada
from src.utils.grapher import continuous_plotter, discrete_plotter  # Importa funciones personalizadas para graficar

# 1. Señal senoidal continua
def continuous_sine():
    frequency = 2   # Frecuencia de la señal senoidal
    amplitude = 1   # Amplitud de la señal
    number_of_points = 10000  # Número de puntos para la señal continua
    time_initial = -1    # Tiempo inicial
    time_final = 5       # Tiempo final
    time = np.linspace(time_initial, time_final, number_of_points)  # Vector de tiempo
    x_t = amplitude * np.sin(2 * np.pi * frequency * time)  # Señal senoidal

    # Graficar señal continua
    continuous_plotter(
        time, x_t,
        'Continuous Sine wave Signal', 'x₁(t) = sin(2π·f·t)',
        'Time [s]',  'Amplitude')

# 2. Señal senoidal discreta 
def discrete_sine():
    frequency = 2   # Frecuencia
    amplitude = 1   # Amplitud
    fs = 20         # Frecuencia de muestreo
    ts = 1 / fs     # Periodo de muestreo
    samples = 100   # Número de muestras
    n = np.arange(samples)  # Índices de muestra
    x_n = amplitude * np.sin(2 * np.pi * frequency * n * ts)  # Señal discreta

    # Graficar señal discreta
    discrete_plotter(
        n, x_n,
        'Discrete Sine wave Signal', 'x₁[n] = sin(2π·f·n)',
        'Sample index [n]', 'Amplitude')

# 3. Señal exponencial continua x₂(t) = e^(–2t)·u(t)
def continuous_exponential():
    number_of_points = 1000  # Número de puntos
    time = np.linspace(-1, 5, number_of_points)  # Vector de tiempo
    u = np.heaviside(time, 1)  # Función escalón unitario u(t)
    x_t = np.exp(-2 * time) * u  # Señal exponencial con escalón

    # Graficar señal continua
    continuous_plotter(
        time, x_t,
        'Continuous Exponential Signal', 'x₂(t) = e^(–2t)·u(t)',
        'Time [s]', 'Amplitude')

# 4. Señal exponencial discreta
def discrete_exponential():
    samples = 100  # Número de muestras
    ts = 0.05      # Periodo de muestreo
    n = np.arange(-20, samples)  # Índices de muestra
    t = n * ts  # Tiempo discreto
    u = np.heaviside(t, 1)  # Escalón unitario
    x_n = np.exp(-2 * t) * u  # Señal exponencial discreta

    # Graficar señal discreta
    discrete_plotter(
        n, x_n,
        'Discrete Exponential Signal', 'x₂[n] = e^(–2·n·Ts)·u[n]',
        'Sample index [n]', 'Amplitude')

# 5. Señal triangular continua
def continuous_triangle():
    frequency = 2
    number_of_points = 1000  # Número de puntos
    time = np.linspace(0, 2, number_of_points)  # Tiempo continuo
    x_t = signal.sawtooth(2 * np.pi * frequency * time, 0.5)  # Señal triangular (0.5 → forma triangular perfecta)

    # Graficar señal continua
    continuous_plotter(
        time, x_t,
        'Continuous Triangular Signal', 'x₃(t) = tri(t, f)',
        'Time [s]', 'Amplitude')

# 6. Señal triangular discreta
def discrete_triangle():
    frequency = 2
    fs = 100  # Frecuencia de muestreo
    ts = 1 / fs  # Periodo de muestreo
    samples = 200  # Número de muestras
    n = np.arange(samples)  # Índices de muestra
    t = n * ts  # Tiempo discreto
    x_n = signal.sawtooth(2 * np.pi * frequency * t, 0.5)  # Señal triangular discreta

    # Graficar señal discreta
    discrete_plotter(
        n, x_n,
        'Discrete Triangular Signal', 'x₃[n] = tri(n·Ts, f)',
        'Sample index [n]', 'Amplitude')

# 7. Señal cuadrada continua
def continuous_square():
    frequency = 2
    number_of_points = 1000  # Número de puntos
    time = np.linspace(0, 2, number_of_points)  # Tiempo continuo
    x_t = signal.square(2 * np.pi * frequency * time)  # Señal cuadrada continua

    # Graficar señal continua
    continuous_plotter(
        time, x_t,
        'Continuous Square Signal', 'x₄(t) = sq(t, f)',
        'Time [s]', 'Amplitude')

# 8. Señal cuadrada discreta
def discrete_square():
    frequency = 2
    fs = 100  # Frecuencia de muestreo
    ts = 1 / fs  # Periodo de muestreo
    samples = 200  # Número de muestras
    n = np.arange(samples)  # Índices de muestra
    t = n * ts  # Tiempo discreto
    x_n = signal.square(2 * np.pi * frequency * t)  # Señal cuadrada discreta

    # Graficar señal discreta
    discrete_plotter(
        n, x_n,
        'Discrete Square Signal', 'x₄[n] = sq(n·Ts, f)',
        'Sample index [n]', 'Amplitude')