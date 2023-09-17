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


def signalReconstruction(signal):
    
    # Calcular la transformada de Fourier de la señal utilizando librosa
    D = librosa.stft(signal)

    # Obtener la fase de la señal en el dominio de la frecuencia para poder integrarla
    phase = np.angle(D)

    # Aplicar la integración en la fase extraida 
    integrated_phase = np.cumsum(phase, axis=1)

    # Reconstruir la señal a partir de la fase integrada
    dReconstructed = np.abs(D) * np.exp(1j * integrated_phase)
    
    # Aplicamos transformada inversa de Fourier para volver al formato original de la señal
    signalReconstructed = librosa.istft(dReconstructed)
    
    
    return signalReconstructed
    
    
    
    
    
    
    
    

    












