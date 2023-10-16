import serial
import matplotlib.pyplot as plt

# Establecer la conexión con el puerto serie
ser = serial.Serial('COM3', 9600)  # Reemplaza 'COMX' con el nombre de tu puerto serie

# Lista para almacenar los valores del puerto serie
data = []

# Número de muestras que deseas recibir
num_samples = 1000

# Leer datos del puerto serie
for _ in range(num_samples):
    # Leer línea desde el puerto serie y convertir a entero
    value = int(ser.readline().strip())
    data.append(value)

# Cerrar la conexión con el puerto serie
ser.close()

# Graficar los datos
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.xlabel('Tiempo')
plt.ylabel('Valor del Micrófono')
plt.title('Señal del Micrófono en el Tiempo')
plt.grid(True)
plt.show()
