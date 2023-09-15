import mpmath
import numpy as np
import sympy as sp
import librosa.display
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.signal import spectrogram


#########################################################################
#                   Instituto Tecnológico de Costa Rica
#                        Análsis de Señales Mixtas
#                               Taller 2 
#                    
#                     Mauricio Calderón Chavarría
#                             2019182667
# 
# 
#########################################################################
#
#                    Graficación de Espectrogramas
# 
#########################################################################

# Parámetros de la señal
fs = 22050  # Frecuencia de muestreo en Hz
t = np.arange(0, 2*np.pi, 2*np.pi/fs)  # Vector de tiempo de 0 a 2*pi

# Generar la señal seno
frecuencia_seno = 1  # Frecuencia de la señal seno en Hz
amplitud_seno = 1.0
x = amplitud_seno * np.sin(2 * np.pi * frecuencia_seno * t)


#···················· UTILIZANDO SCIPY Y MATPLOTLIB ····················#

def showSciPySpectrogram(x,fs):
    
    # Se calcula el espectrograma de la señal seno en dB usando SciPy
    f_sen, t_spec_sen, Sxx_sen = spectrogram(x, fs)
    Sxx_sen_db = 10 * np.log10(np.abs(Sxx_sen))

    # Se grafica el espetograma y la señal resultante
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.plot(t, x, label='sen(x)')
    plt.title('Señal Sen(x)')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.xlim(0, 2*np.pi)  
    plt.ylim(-1.5, 1.5)   

    plt.subplot(2, 1, 2)
    plt.pcolormesh(t_spec_sen, f_sen, Sxx_sen_db, shading='gouraud')
    plt.ylabel('Frecuencia [Hz]')
    plt.xlabel('Tiempo [s]')
    plt.title('Espectrograma de Sen(x) (dB)')
    plt.colorbar(label='Magnitud (dB)')

    plt.tight_layout()
    plt.show()

#·················· UTILIZANDO LIBROSA Y MATPLOTLIB ·····················#


# Método showSpectrogram que calcula el espectrograma y lo grafica.
def showLibrosaSpectrogram(y,fs):
    
    # Se calcula el espectrograma de la señal seno en dB usando librosa
    Sxx_sen_db = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # Se grafica el espetograma y la señal resultante
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.plot(t, y, label='sen(x)')
    plt.title('Señal Sen(x)')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.xlim(0, 2*np.pi)  
    plt.ylim(-1.5, 1.5)   

    plt.subplot(2, 1, 2)
    librosa.display.specshow(Sxx_sen_db, sr=fs, x_axis='time', y_axis='log', cmap='inferno')
    plt.ylabel('Frecuencia [Hz]')
    plt.xlabel('Tiempo [s]')
    plt.title('Espectrograma de sen(x) (dB)')
    plt.colorbar(format='%+2.0f dB')

    plt.tight_layout()
    plt.show()

showSciPySpectrogram(x,fs)
showLibrosaSpectrogram(x,fs)



#########################################################################
#                       
#                       Integración Compleja
#
#########################################################################

# Definir la función compleja que deseas integrar
def complexFunction(z):
    numerator = z**2
    denominator = (z**2 + 1)**2 * (z**2 + 2*z + 2)
    integrand = numerator / denominator
    return integrand

#·················· UTILIZANDO SCIPY ·····················#


# Realizar la integración en un intervalo
result, error = quad(complexFunction, -np.inf, np.inf)

print("Resultado de la integración compleja usando SciPy:", result)


#·················· UTILIZANDO MPMATH ·····················#

# Realizar la integración en un intervalo
result = mpmath.quad(complexFunction, [-mpmath.inf, mpmath.inf])

print("Resultado de la integración compleja usando MpMath:", result)



#·················· UTILIZANDO SYMPY ·····················#

# Función a integrar
z = sp.symbols('z', complex=True)
numerator = z**2
denominator = (z**2 + 1)**2 * (z**2 + 2*z + 2)
integrand = numerator / denominator

# Calcular la integral
integral_result = sp.integrate(integrand, (z, -sp.oo, sp.oo))

# Mostrar el resultado
print("Resultado de la integración compleja usando SymPy:", integral_result)
