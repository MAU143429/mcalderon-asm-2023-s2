import numpy as np
from matplotlib import pyplot as plt
#Sample_rate
sample_rate = 100000
#Duracion del audio 
duration = 5
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

def generate_cosine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.cos((2 * np.pi) * frequencies)
    return x, y

x1, y1 = generate_sine_wave(100, sample_rate, duration)
x2, y2 = generate_cosine_wave(5000, sample_rate, duration)  #Senal portadora con 5khz

#Señal Modulada
s_modulada = y1 * y2
#Senal Demodulada
s_demodulada = s_modulada*y2

#Fourier Modulada
frequency_domain = np.fft.fft(s_modulada)
freq_axis = np.fft.fftfreq(len(s_modulada), 1/sample_rate)

#Fourier demodulada
frequency_domain_demodulada = np.fft.fft(s_demodulada)
freq_axis_demodulada = np.fft.fftfreq(len(s_demodulada),1/sample_rate)

# Graficar los resultados
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ax1.plot(freq_axis, np.abs(frequency_domain))
ax1.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude')
ax1.set_title('Frequency Domain Representation (AM Modulation Signal)')
ax1.grid()

ax2.plot(freq_axis_demodulada, np.abs(frequency_domain_demodulada))
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude')
ax2.set_title('Frequency Domain Representation (AM Demodulation Signal)')
ax2.grid()
plt.tight_layout()
plt.show()
