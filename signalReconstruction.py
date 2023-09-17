import mpmath
import numpy as np
import sympy as sp
import librosa.display
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.signal import spectrogram
from scipy.integrate import simps


#########################################################################
#                   Instituto Tecnológico de Costa Rica
#                        Análsis de Señales Mixtas
#                          Proyecto Individual 
#                    
#                     Mauricio Calderón Chavarría
#                             2019182667
# 
# 
#########################################################################



# Parámetros de la señal de tono seno
duration = 1  # Duración de la señal en segundos
fs = 1000    # Frecuencia de muestreo en Hz
frecuencia = 10.0  # Frecuencia en Hz (por ejemplo, un la440)

# Generar una señal de tono seno con ruido gaussiano
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
senal_original = np.sin(2 * np.pi * frecuencia * t)
ruido = np.random.normal(0, 0.1, senal_original.shape)
senal_con_ruido = senal_original + ruido

# Calcular la transformada de Fourier de la señal
D = librosa.stft(senal_con_ruido)

# Obtener la fase de la señal en el dominio de la frecuencia
phase = np.angle(D)

# Aplicar la integración en la fase
integrated_phase = np.cumsum(phase, axis=1)

# Reconstruir la señal a partir de la fase integrada
D_reconstructed = np.abs(D) * np.exp(1j * integrated_phase)
senal_reconstructed = librosa.istft(D_reconstructed)

# Crear una figura con dos subgráficos para mostrar las señales original y reconstruida
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
librosa.display.waveshow(senal_original, sr=fs, x_axis='time')
plt.title('Señal de Tono Seno Original')

plt.subplot(3, 2, 2)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(D), ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal Original con Ruido')

plt.subplot(3, 2, 3)
librosa.display.waveshow(senal_con_ruido, sr=fs, x_axis='time')
plt.title('Señal de Tono Seno con Menos Ruido Gaussiano')

plt.subplot(3, 2, 4)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(D), ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal con Menos Ruido Gaussiano')

plt.subplot(3, 2, 5)
librosa.display.waveshow(senal_reconstructed, sr=fs, x_axis='time')
plt.title('Señal Reconstruida después de la Integración Compleja')

plt.subplot(3, 2, 6)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(D_reconstructed), ref=np.max), y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal Reconstruida')

plt.tight_layout()
plt.show()

'''
# Cargar la señal de audio con ruido
audio_path = 'tu_archivo_de_audio_con_ruido.wav'
y, sr = librosa.load(audio_path)

y, sr = librosa.load(librosa.example('trumpet'), duration=5)


# Calcular el espectrograma de la señal original
D_original = librosa.stft(y)


# Aplicar la integración compleja para la reconstrucción
D_reconstructed = np.angle(D_original)

# Reconstruir la señal a partir del espectrograma modificado
y_reconstructed = librosa.istft(np.abs(D_original) * np.exp(1j * D_reconstructed))

# Crear una figura con dos subgráficos para mostrar las señales originales y reconstruidas
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
librosa.display.waveshow(y, sr=sr)
plt.title('Señal Original con Ruido')

plt.subplot(2, 1, 2)
librosa.display.waveshow(y_reconstructed, sr=sr)
plt.title('Señal Reconstruida después de la Integración Compleja')

plt.tight_layout()
plt.show()

'''












