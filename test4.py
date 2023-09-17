import signalReconstruction
import numpy as np
import librosa.display
import matplotlib.pyplot as plt


# Parámetros de la señal de tono seno

duration = 1       # Duración de la señal en segundos
fs = 4000          # Frecuencia de muestreo en Hz
frequency = 10.0  # Frecuencia de la señal en Hz

# Generar una señal de tono seno con ruido gaussiano

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
originalSignal = np.sin(2 * np.pi * frequency * t)
noise = np.random.normal(0, 0.1, originalSignal.shape)
noiseSignal = originalSignal + noise

# Se aplica la reconstrucción de la señal

signalReconstructed = signalReconstruction.signalReconstruction(noiseSignal)


# Creación del plot para mostrar las señales original y reconstruida
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
librosa.display.waveshow(originalSignal, sr=fs, axis='time')
plt.title('Señal de Tono Seno Original')

plt.subplot(3, 2, 2)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(originalSignal)), ref=np.max), y_axis='log', sr=fs)
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal Original')

plt.subplot(3, 2, 3)
librosa.display.waveshow(noiseSignal, sr=fs, axis='time')
plt.title('Señal de Tono Seno con Ruido Gaussiano')

plt.subplot(3, 2, 4)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(signalReconstructed[1]), ref=np.max), y_axis='log', sr=fs)
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal con Ruido Gaussiano')

plt.subplot(3, 2, 5)
librosa.display.waveshow(signalReconstructed[0], sr=fs, axis='time')
plt.title('Señal Reconstruida después de la Integración Compleja')

plt.subplot(3, 2, 6)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(signalReconstructed[2]), ref=np.max), y_axis='log', sr=fs)
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal Reconstruida')

plt.tight_layout()
plt.show()