Este repositorio contiene una colección de funciones en Python para generar y graficar señales clásicas en el dominio continuo y discreto. Las señales generadas incluyen:

Señales senoidales
Señales exponenciales
Señales triangulares
Señales cuadradas
Cada función grafica la señal correspondiente utilizando funciones personalizadas para graficar (continuous_plotter y discrete_plotter).

Estructura del Proyecto
.
├── src/
│   └── utils/
│       └── grapher.py      # Funciones personalizadas para graficar (no incluidas aquí)
├── signals.py              # Archivo principal con las funciones generadoras de señales
├── README.md               # Este archivo
Dependencias
Asegúrate de tener instaladas las siguientes bibliotecas de Python:

numpy
scipy
matplotlib (para las funciones de graficado)
Puedes instalarlas con:

pip install numpy scipy matplotlib
Funciones disponibles
1. Señales Senoidales
Continuo: continuous_sine() Genera y grafica una señal senoidal continua.

Discreto: discrete_sine() Genera y grafica una señal senoidal discreta.

2. Señales Exponenciales
Continuo: continuous_exponential() Genera y grafica una señal exponencial decreciente continua con función escalón.

Discreto: discrete_exponential() Genera y grafica una señal exponencial discreta con función escalón.

3. Señales Triangulares
Continuo: continuous_triangle() Genera y grafica una señal triangular continua.

Discreto: discrete_triangle() Genera y grafica una señal triangular discreta.

4. Señales Cuadradas
Continuo: continuous_square() Genera y grafica una señal cuadrada continua.

Discreto: discrete_square() Genera y grafica una señal cuadrada discreta.

Uso
Puedes importar las funciones en tu script o notebook y llamarlas directamente para generar las gráficas. Por ejemplo:

from signals import continuous_sine, discrete_exponential

# Graficar señal senoidal continua
continuous_sine()

# Graficar señal exponencial discreta
discrete_exponential()
Personalización
Cada función tiene parámetros internos (frecuencia, amplitud, número de puntos/muestras, etc.). Puedes modificar estos parámetros directamente en el código para ajustar las señales a tus necesidades.

Notas
Las funciones de graficado (continuous_plotter y discrete_plotter) están en src/utils/grapher.py y no están incluidas aquí. Asegúrate de que existan y funcionen correctamente.
El código está estructurado para facilitar la visualización de cómo varían las señales continuas y discretas.
Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE (si lo añades) para más detalles.

=========================================================== PROYECTO: Graficador de Señales Senoidales Continuas
DESCRIPCIÓN
Este proyecto permite visualizar una señal senoidal continua a partir de la frecuencia que el usuario indique. Utiliza la librería NumPy para el manejo de arreglos y cálculos numéricos, y una función de graficación (continuous_plotter) para mostrar la señal.

ARCHIVOS PRINCIPALES
main.py (o nombre que hayas dado al script): Contiene la función understanding_freq que genera y grafica la señal senoidal.

src/utils/grapher.py: Contiene la función continuous_plotter que permite graficar señales continuas. Esta función no está incluida aquí, pero es llamada en el script.

DEPENDENCIAS
Python 3.x
numpy
matplotlib (o cualquier otra librería usada por continuous_plotter)
EJECUCIÓN
Asegúrate de tener instaladas las dependencias necesarias:

Llama a la función understanding_freq desde el script principal o desde un intérprete de Python, pasando la frecuencia deseada:

understanding_freq(5)  # Genera una señal senoidal de 5 Hz
# Importa la función
from main import understanding_freq

# Genera y grafica una señal senoidal de 10 Hz
understanding_freq(10)




===========================================================
  PROYECTO: Comparador de Señales Senoidales
===========================================================

DESCRIPCIÓN
-----------
Este proyecto permite comparar dos señales senoidales: una señal
de referencia (con amplitud 1, frecuencia 1 Hz y fase 0) y una
señal modificada con parámetros (amplitud, frecuencia, fase)
proporcionados por el usuario.

El proyecto grafica la comparación tanto en tiempo continuo
como en tiempo discreto, utilizando las funciones
`continuous_plotter` y `discrete_plotter` para graficar.

ARCHIVOS PRINCIPALES
---------------------
- main.py (o el nombre que tenga tu script):
    Contiene la función `compare_sine_signals`, que genera las señales
    y las grafica.

- src/utils/grapher.py:
    Contiene las funciones `continuous_plotter` y `discrete_plotter`
    para graficar señales continuas y discretas, respectivamente.

DEPENDENCIAS
------------
- Python 3.x
- numpy
- matplotlib (o cualquier otra librería usada en `grapher.py`)

EJECUCIÓN
---------
1. Asegúrate de tener instaladas las dependencias necesarias:

2. Llama a la función `compare_sine_signals` desde el script
principal o desde un intérprete de Python, pasando los
parámetros deseados:
```python
compare_sine_signals(amplitude=2, frequency=3, phase=np.pi/4)
def compare_sine_signals(amplitude, frequency, phase):
    """
    Compara una señal senoidal modificada con una señal de referencia.

    Parámetros:
    - amplitude (float): Amplitud de la señal modificada.
    - frequency (float): Frecuencia de la señal modificada (Hz).
    - phase (float): Fase de la señal modificada (radianes).

    Retorna:
    - None. La función solo grafica las señales.
    """
# Importa la función
from main import compare_sine_signals
import numpy as np

# Compara una señal de amplitud 2, frecuencia 3 Hz y fase π/4
compare_sine_signals(2, 3, np.pi/4)


===========================================================
  PROYECTO: Análisis de Resolución de un DAC
===========================================================

DESCRIPCIÓN
-----------
Este proyecto permite analizar la resolución de un conversor
digital-analógico (DAC) de acuerdo con la cantidad de bits
que especifique el usuario.

El análisis incluye:
- Número de niveles.
- Tamaño del paso.
- Resolución porcentual.
- Gráfica de la curva de transferencia del DAC.

ARCHIVOS PRINCIPALES
---------------------
- main.py (o el nombre que tenga tu script):
    Contiene la función `analyze_dac_resolution` que calcula
    y grafica las características del DAC.

- src/utils/grapher.py:
    Contiene la función `dac_plotter`, que grafica la salida
    analógica del DAC en función de la entrada digital.

DEPENDENCIAS
------------
- Python 3.x
- numpy
- matplotlib (o cualquier otra librería usada en `grapher.py`)

EJECUCIÓN
---------
1. Asegúrate de tener instaladas las dependencias necesarias:
pip install numpy matplotlib


2. Llama a la función `analyze_dac_resolution` desde el script
principal o desde un intérprete de Python, pasando el número
de bits del DAC:
```python
analyze_dac_resolution(bits=8)
DETALLES DE LA FUNCIÓN
def analyze_dac_resolution(bits: int):
    """
    Analiza la resolución de un DAC de 'bits' bits e imprime
    los resultados.

    Parámetros:
    - bits (int): Número de bits del DAC.

    Retorna:
    - None. La función imprime resultados y grafica la curva.
    """
EJEMPLO DE USO
# Importa la función
from main import analyze_dac_resolution

# Analiza un DAC de 10 bits
analyze_dac_resolution(10)
SALIDA ESPERADA
La función imprime en consola los resultados:

Niveles totales
Tamaño del paso (V)
Resolución porcentual (%)
Y muestra una gráfica de la curva de salida del DAC.

OBSERVACIONES
El voltaje de referencia (Vref) está configurado en 5 V.
La señal de salida del DAC se grafica en forma de escalera, dependiendo de los niveles.
Puedes modificar el valor de Vref directamente en el código para adaptarlo a tu circuito real.
