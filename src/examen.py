import numpy as np
from src.utils.grapher import continuous_plotter

def calcular_transformada_fourier(x):
    """
    Implementación de la Transformada Discreta de Fourier (DFT)
    usando operaciones matriciales para mejor eficiencia
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    matriz_twiddle = np.exp(-2j * np.pi * k * n / N)
    return np.dot(matriz_twiddle, x)

def analizar_componentes_frecuenciales(senal, frecuencia_muestreo, nombre_senal, umbral_deteccion=0.0008):
    """
    Analiza las componentes frecuenciales de una señal mediante DFT
    e identifica los picos principales en el espectro con mayor precisión
    """
    # Calcular la transformada de Fourier
    espectro = calcular_transformada_fourier(senal)
    N = len(senal)
    
    # Calcular frecuencias y magnitudes normalizadas
    eje_frecuencias = np.arange(N) * frecuencia_muestreo / N
    magnitudes = np.abs(espectro) / N
    
    # Considerar solo la mitad del espectro (simetría)
    punto_nyquist = N // 2
    delta_f = frecuencia_muestreo / N
    
    # Detectar picos significativos en el espectro con algoritmo mejorado
    picos_detectados = []
    for i in range(2, punto_nyquist-2):  # Evitar bordes del espectro
        # Condición para identificar un pico local con umbral ajustable
        if (magnitudes[i] > magnitudes[i-1] and 
            magnitudes[i] > magnitudes[i+1] and 
            magnitudes[i] > umbral_deteccion):
            picos_detectados.append((eje_frecuencias[i], magnitudes[i]))
    
    # Ordenar picos por amplitud descendente
    picos_detectados.sort(key=lambda x: x[1], reverse=True)
    
    # Mostrar resultados con formato mejorado
    print(f"\n{nombre_senal.upper()}:")
    print(f"   Resolución frecuencial: {delta_f:.5f} Hz")
    print(f"   Muestras analizadas: {N}")
    print("   Componentes principales identificadas:")
    
    for idx, (frecuencia, amplitud) in enumerate(picos_detectados[:4], 1):
        print(f"     {idx}. {frecuencia:.3f} Hz - Amplitud: {amplitud:.5f}")
    
    return eje_frecuencias[:punto_nyquist], magnitudes[:punto_nyquist], delta_f

def examen_p1():
    """
    Primera parte del examen: Análisis de señal modulada en amplitud
    con parámetros optimizados para mejor visualización espectral
    """
    print("="*65)
    print("EXAMEN PARTE 1: ANÁLISIS DE SEÑAL MODULADA EN AMPLITUD")
    print("="*65)
    
    # Parámetros de la señal optimizados
    freq_moduladora = 1.8    # Hz (frecuencia de modulación)
    freq_portadora = 15.0    # Hz (frecuencia portadora)
    indice_modulacion = 0.7  # Índice de modulación
    freq_muestreo = 120.0    # Hz (frecuencia de muestreo)
    tiempo_total = 7.5       # segundos (duración)
    
    # Generar señal modulada con mayor resolución
    puntos_muestreo = int(freq_muestreo * tiempo_total)
    t = np.linspace(0, tiempo_total, puntos_muestreo, endpoint=False)
    
    # Crear señal AM con componentes bien definidas
    envolvente = 1 + indice_modulacion * np.cos(2 * np.pi * freq_moduladora * t)
    senal_modulada = envolvente * np.sin(2 * np.pi * freq_portadora * t)
    
    # Analizar espectro con mayor sensibilidad
    frecuencias, magnitudes, resolucion = analizar_componentes_frecuenciales(
        senal_modulada, freq_muestreo, "Señal modulada en amplitud", 0.005)
    
    # Visualizar resultados con etiquetas mejoradas
    expr_mat = f'[1+{indice_modulacion}cos(2π{freq_moduladora}t)]·sin(2π{freq_portadora}t)'
    continuous_plotter(t, senal_modulada, f'Señal Modulada AM: {expr_mat}', 
                       "Dominio Temporal", "Tiempo (s)", "Amplitud (V)")
    
    continuous_plotter(frecuencias, magnitudes, f'Espectro de Frecuencia (Δf={resolucion:.4f}Hz)', 
                       "Dominio Frecuencial", "Frecuencia (Hz)", "Magnitud Normalizada")
    
    print("\n" + "="*65)
    print("CONCLUSIÓN: La DFT revela claramente las bandas laterales")
    print("características de la modulación AM alrededor de la portadora")

def examen_p2():
    """
    Segunda parte del examen: Identificación de interferencia en señal
    con parámetros actualizados para mejor detección espectral
    """
    print("="*65)
    print("EXAMEN PARTE 2: IDENTIFICACIÓN DE INTERFERENCIA EN SEÑAL")
    print("="*65)
    
    # Parámetros de la señal optimizados
    freq_muestreo = 320.0    # Hz (mayor frecuencia de muestreo)
    tiempo_total = 4.2       # segundos (ventana temporal)
    freq_1 = 12.0           # Hz (componente principal)
    freq_2 = 28.0           # Hz (componente secundaria)
    
    # Generar señal base con mejor resolución
    n_muestras = int(freq_muestreo * tiempo_total)
    t = np.arange(n_muestras) / freq_muestreo
    
    señal_original = (np.sin(2 * np.pi * freq_1 * t) + 
                      0.35 * np.sin(2 * np.pi * freq_2 * t))
    
    # Añadir interferencia con amplitud diferente
    freq_interferencia = 45.0  # Hz (frecuencia de interferencia)
    interferencia = 0.22 * np.sin(2 * np.pi * freq_interferencia * t)
    señal_con_interferencia = señal_original + interferencia
    
    # Analizar ambas señales con mayor precisión
    freqs_orig, mags_orig, resolucion = analizar_componentes_frecuenciales(
        señal_original, freq_muestreo, "Señal original")
    
    freqs_interf, mags_interf, _ = analizar_componentes_frecuenciales(
        señal_con_interferencia, freq_muestreo, "Señal con interferencia")
    
    # Visualizar resultados con mejor presentación
    expr_orig = f'sin(2π{freq_1}t) + 0.35sin(2π{freq_2}t)'
    continuous_plotter(t, señal_original, f'Señal de Referencia: {expr_orig}', 
                       "Señal Libre de Interferencia", "Tiempo (s)", "Amplitud (V)")
    
    continuous_plotter(freqs_orig, mags_orig, f'Espectro de Referencia (Δf={resolucion:.4f}Hz)', 
                       "Composición Espectral Limpia", "Frecuencia (Hz)", "Densidad Espectral")
    
    continuous_plotter(t, señal_con_interferencia, f'Señal con Interferencia a {freq_interferencia}Hz', 
                       "Señal Contaminada", "Tiempo (s)", "Amplitud (V)")
    
    continuous_plotter(freqs_interf, mags_interf, f'Espectro con Contaminación (Δf={resolucion:.4f}Hz)', 
                       "Detección de Componente Espuria", "Frecuencia (Hz)", "Densidad Espectral")
    
    print("\n" + "="*65)
    print("CONCLUSIÓN: El análisis espectral permite identificar")
    print("componentes de interferencia no discernibles en el dominio temporal")