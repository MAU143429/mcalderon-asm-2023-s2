import numpy as np
import librosa.display
import matplotlib.pyplot as plt
import soundfile as sf

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
#         RECONSTRUCCION DE UNA SEÑAL DE AUDIO CON RUIDO GAUSSIANO
#   
#########################################################################

'''
Método signalReconstruction

Permite reconstruir la señal de audio sin ruido realizando una integración
de la misma en el dominio del tiempo para luego aplicarle una normalización.

@param signal señal con ruido que se desea integrar
@return signalReconstructed señal de salida normalizada y sin ruido

'''   
def signalReconstruction(signal):
    
    # Aplicar la integración en sobre la señal 
    signalReconstructed = librosa.util.normalize(np.cumsum(signal))
    
    return (signalReconstructed)
    

# Cargar archivo de audio real
originalSignal, fs = librosa.load("sample.wav", sr=None)
# Agregar ruido a la muestra original (opcional)
noise = np.random.normal(0, 0.1, originalSignal.shape)
noiseSignal = originalSignal + noise

# Aplicando el método de reconstrucción

signalReconstructed = signalReconstruction(noiseSignal)


# Eportando los archivos de Audio
sf.write('originalSignal.wav', originalSignal, fs)
sf.write('noisySignal.wav', noiseSignal, fs)
sf.write('reconstructedSignal.wav', signalReconstructed, fs)
 
 
# Creación del plot para mostrar las señales original, con ruido y reconstruida
plt.figure(figsize=(12, 8))

#########################################################################
#
#                            Audio Original
#        
#########################################################################
plt.subplot(3, 2, 1)
librosa.display.waveshow(originalSignal[int(0.01*fs):int(0.05*fs)], sr=fs, axis='time')
plt.title('Señal de Audio Original')

plt.subplot(3, 2, 2)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(originalSignal)), ref=np.max), y_axis='log', sr=fs,cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal de Audio Original')


#########################################################################
#
#                       Audio con Ruido Gaussiano
#        
#########################################################################

plt.subplot(3, 2, 3)
librosa.display.waveshow(noiseSignal[int(0.01*fs):int(0.05*fs)], sr=fs, axis='time')
plt.title('Señal de Audio con Ruido Gaussiano')

plt.subplot(3, 2, 4)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(noiseSignal)), ref=np.max), y_axis='log', sr=fs,cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal de Audio con Ruido Gaussiano')

#########################################################################
#
#                            Audio Reconstruido
#        
#########################################################################

plt.subplot(3, 2, 5)
librosa.display.waveshow(signalReconstructed[int(0.01*fs):int(0.05*fs)], sr=fs, axis='time')

plt.ylim(-0.1, 0.7)
plt.title('Señal de Audio Reconstruida')

plt.subplot(3, 2, 6)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(signalReconstructed)), ref=np.max), y_axis='log', sr=fs,cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de la Señal de Audio Reconstruida')

plt.tight_layout()
plt.show()


    
    
    
    

    












