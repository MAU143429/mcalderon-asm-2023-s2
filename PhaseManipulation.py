import librosa
import librosa.display
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

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
#            MANIPULACION DE LA FASE PARA UNA SEÑAL DE AUDIO
#   
#########################################################################


# Cargar la señal de audio usando librosa
originalSignal, sr = librosa.load("sample.wav", sr=None)

# Se pasa la señal al dominio de frecuencia para aplicar las manipulaciones fase

D = librosa.stft(originalSignal)
magnitude = np.abs(D)
magnitude, phase = librosa.magphase(D)

#########################################################################
#
#                       Señal Con Fase Invertida
#        
#########################################################################

# Invertir la fase de la señal

invertedPhase = -phase

# Reconstruir la señal con la fase invertida
invertedSignal = librosa.istft(magnitude * np.exp(1j * invertedPhase))

# Guardar la señal con fase invertida en un archivo de audio
sf.write('audioInverted.wav', invertedSignal, sr)


#########################################################################
#
#                       Señal Con Cambio de Fase
#        
#########################################################################


# Aplicar un desplazamiento de fase aleatorio
shifted_phase = np.roll(phase, shift=100, axis=1) 

# Reconstrucción de la señal al dominio del tiempo
shiftedSignal = librosa.istft(magnitude * shifted_phase)


# Guardar la señal con cambio de fase en un archivo de audio
sf.write("audioShifted.wav", shiftedSignal, sr)

#########################################################################
#
#                      Señal Con Máscara de Fase
#        
#########################################################################


# Se aplica una máscara de fase entre dos frecuencias
maskPhase = np.zeros_like(phase)
maskPhase[100:200, :] = phase[100:200, :]

# Reconstruct the signal with the masked phase
maskedSignal = librosa.istft(magnitude * maskPhase)

# Guardar la señal con la mascara de fase en un archivo de audio
sf.write("audioMasked.wav", maskedSignal, sr)

#########################################################################
#
#                Graficando las Manipulaciones de Fase
#        
#########################################################################

plt.figure(figsize=(10, 6))

# Gráfica de la señal original
plt.subplot(4, 2, 1)
librosa.display.waveshow(originalSignal, sr=sr)
plt.title("Señal de Audio Original")

plt.subplot(4, 2, 2)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(originalSignal)), ref=np.max), y_axis='log', sr=sr,cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Audio Original')

# Gráfica de la señal con desplazamiento de fase
plt.subplot(4, 2, 3)
librosa.display.waveshow(shiftedSignal, sr=sr)
plt.title("Señal de Audio con Desplazamiento de Fase")

plt.subplot(4, 2, 4)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(shiftedSignal)), ref=np.max), y_axis='log', sr=sr,cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Audio con Desplazamiento de Fase')

# Gráfica de la señal con invertida
plt.subplot(4, 2, 5)
librosa.display.waveshow(invertedSignal, sr=sr)
plt.title("Señal de Audio con Fase Invertida")

plt.subplot(4, 2, 6)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(invertedSignal)), ref=np.max), y_axis='log', sr=sr,cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Audio con Fase Invertida')

plt.subplot(4, 2, 7)
librosa.display.waveshow(maskedSignal, sr=sr)
plt.title("Señal de Audio con Fase Enmascarada")
plt.show()

plt.subplot(4, 2, 8)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(maskedSignal)), ref=np.max), y_axis='log', sr=sr,cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Audio con Fase Enmascarada')

plt.tight_layout()
plt.show()