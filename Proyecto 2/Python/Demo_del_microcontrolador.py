import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import librosa
from scipy.signal import butter, lfilter

# Parámetros de la señal
frecuencia_moduladora1 = 440  # Frecuencia de la señal moduladora 1 (Hz)
frecuencia_moduladora2 = 1200  # Frecuencia de la señal moduladora 2 (Hz)
frecuencia_portadora1 = 10000  # Frecuencia de la primera señal portadora (Hz)
frecuencia_portadora2 = 17500  # Frecuencia de la segunda señal portadora (Hz) ajustada a 100 kHz
duracion = 10  # Duración de la señal en segundos
tasa_muestreo = 44100  # Tasa de muestreo en muestras por segundo
indice_modulacion = 0.5  # Índice de modulación

# Generar la señal moduladora 1 (tono seno) a 440 Hz
tiempo = np.linspace(0, duracion, int(duracion * tasa_muestreo), endpoint=False)
senal_moduladora1 = np.sin(2 * np.pi * frecuencia_moduladora1 * tiempo)

# Cargar la señal de audio
audio_path = "homelander.wav"
audio, sr = librosa.load(audio_path, sr=tasa_muestreo, mono=True, duration=duracion)
audio = audio*10

# Generar la primera señal portadora (tono coseno)
senal_portadora1 = np.cos(2 * np.pi * frecuencia_portadora1 * tiempo)

# Generar la segunda señal portadora (tono coseno)
senal_portadora2 = np.cos(2 * np.pi * frecuencia_portadora2 * tiempo)

# Realizar la modulación AM para ambas señales moduladoras
senal_modulada1 = (1 + indice_modulacion * senal_moduladora1) * senal_portadora1
senal_modulada2 = (1 + indice_modulacion * audio) * senal_portadora2

# Sumar ambas señales moduladas
senal_sumada = senal_modulada1 + senal_modulada2

# Filtrar la señal sumada para obtener la primera señal modulada
cutoff_frequency1 = frecuencia_portadora1  # Frecuencia de la primera portadora
order = 6  # Orden del filtro

def butter_bandpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = [cutoff - 500, cutoff + 500]  # Ancho de banda de +/- 500 Hz
    normal_cutoff = [freq / nyquist for freq in normal_cutoff]
    b, a = butter(order, normal_cutoff, btype='band', analog=False)
    return b, a

def butter_bandpass_filter(data, cutoff, fs, order=5):
    b, a = butter_bandpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
# Función para diseñar un filtro pasa bajos
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Función para diseñar un filtro pasa altas
def butter_highpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

# Función para aplicar el filtro pasa altas a una señal
def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


senal_modulada1_filtrada = butter_bandpass_filter(senal_sumada, cutoff_frequency1, tasa_muestreo, order)

# Filtrar la señal sumada para obtener la segunda señal modulada
cutoff_frequency2 = frecuencia_portadora2  # Frecuencia de la segunda portadora
senal_modulada2_filtrada = butter_highpass_filter(senal_sumada, cutoff_frequency2, tasa_muestreo)




# Demodular ambas señales moduladas
senal_demodulada1 = senal_modulada1_filtrada * senal_portadora1
senal_demodulada2 = senal_modulada2_filtrada * senal_portadora2



# Amplificar las señales demoduladas por un factor de 3
factor_amplificacion = 3
senal_demodulada1 *= factor_amplificacion
senal_demodulada2 *= factor_amplificacion

# Desplazar las señales demoduladas al eje 0 (restar el valor medio)
senal_demodulada1 -= np.mean(senal_demodulada1)
senal_demodulada2 -= np.mean(senal_demodulada2)

# Realiza la FFT de las señales
fft_modulada = np.fft.fft(senal_sumada)


frecuencias = np.fft.fftfreq(len(senal_sumada), 1.0 / tasa_muestreo)




# Aplicar el filtro pasa bajos a las señales demoduladas
cutoff_frequency_lowpass = 5000  # Frecuencia de corte del filtro pasa bajos (ajusta según sea necesario)
senal_demodulada1_filtrada = butter_lowpass_filter(senal_demodulada1, cutoff_frequency_lowpass, tasa_muestreo)
#senal_demodulada2_filtrada_aux = butter_highpass_filter(senal_demodulada2, 200, tasa_muestreo)
#senal_demodulada2_filtrada=butter_lowpass_filter(senal_demodulada2_filtrada_aux, 500, tasa_muestreo)
cutoff_frequency_lowpass2 = 1500
senal_demodulada2_filtrada=butter_lowpass_filter(senal_demodulada2, cutoff_frequency_lowpass2, tasa_muestreo)
# Guardar las señales demoduladas filtradas como archivos de audio
sf.write('results//seno_Dem_Filtrada.wav', senal_demodulada1_filtrada, tasa_muestreo)
sf.write('results//audio_Dem_Filtrada.wav', senal_demodulada2_filtrada, tasa_muestreo)

# Graficar las señales
plt.figure(figsize=(12, 8))
plt.subplot(5, 1, 1)
plt.title('Suma de Señales Moduladas ')
plt.plot(tiempo, senal_sumada)

plt.subplot(5, 1, 2)
plt.title('Señal demodulada 1 ')
plt.plot(tiempo, senal_demodulada1_filtrada)

plt.subplot(5, 1, 3)
plt.title('Señal demodulada 2 ')
plt.plot(tiempo, senal_demodulada2_filtrada)

plt.subplot(5, 1, 4)
plt.title('FFT de la Señal Modulada sumada')
plt.plot(frecuencias, np.abs(fft_modulada))

plt.tight_layout()
plt.show()


