import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

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
#
#         GRAFICACIÓN DE LA SEÑAL DE AUDIO PARA ANALIZAR
#                  ARMÓNICOS, TRANSITORIOS Y TIMBRE
#   
#########################################################################


# Cargar un archivo de audio
audio_file = 'sample.wav'
y, sr = librosa.load(audio_file)

#########################################################################
#
#                              ARMÓNICOS
#   
#########################################################################

# Calcular el espectrograma de amplitud
D = librosa.stft(y)
mag = librosa.amplitude_to_db(abs(D))


#########################################################################
#
#                             TRANSITORIOS
#   
#########################################################################

# Calcular el espectrograma de potencia
power = np.abs(D)**2


#########################################################################
#
#                             TIMBRE
#   
#########################################################################


# Calcular el espectrograma de Mel
S = librosa.feature.melspectrogram(y=y, sr=sr)
log_S = librosa.power_to_db(S, ref=np.max)




# Crear una figura con tres subplots
plt.figure(figsize=(12, 8))

# Espectrograma de magnitud (Armónicos)
plt.subplot(3, 1, 1)
librosa.display.specshow(mag, sr=sr, x_axis='time', y_axis='log',cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Magnitud (Armónicos)')

# Espectrograma de potencia (Transitorios)
plt.subplot(3, 1, 2)
librosa.display.specshow(librosa.power_to_db(power, ref=np.max), sr=sr, x_axis='time', y_axis='log',cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Potencia (Transitorios)')

# Espectrograma de Mel (Timbre)
plt.subplot(3, 1, 3)
librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel',cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Mel (Timbre)')

# Ajustar los subplots
plt.tight_layout()

# Mostrar el gráfico
plt.show()

