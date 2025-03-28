import matplotlib.pyplot as plt
import numpy as np

# File path to the .sig file
file_path = 'mntdataGB.sig'

# Read the file as binary and decode to interpret the content
with open(file_path, 'rb') as file
    sig_data = file.read()

sig_text_data = sig_data.decode('utf-8')

# Split the data into lines to identify the header and data sections
lines = sig_text_data.splitlines()

# Extract the lines where the actual data begins
data_lines = []
header_ended = False

for line in lines
    if header_ended
        data_lines.append(line.strip())
    if data= in line
        header_ended = True

# Convert the data lines to a numpy array for easier manipulation
data_array = np.array([list(map(float, line.split())) for line in data_lines])

# Extract the first column as the x-axis (wavelengths) and the rest as y-axis (intensities)
wavelengths = data_array[, 0]
intensities = data_array[, 1]

# Plot the spectral data
plt.figure(figsize=(10, 6))
for i in range(intensities.shape[1])
    plt.plot(wavelengths, intensities[, i], label=f'Intensity {i+1}')

plt.title('Spectral Signature Data')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)
plt.show()
