#https://realpython.com/python-wav-files/
#https://docs.python.org/3/library/wave.html
import wave
import numpy as np
import matplotlib.pyplot as plt

file_path = 'female.wav' 
wav_file = wave.open(file_path, 'r')

n_channels = wav_file.getnchannels() 
sample_width = wav_file.getsampwidth()   #number of bytes
framerate = wav_file.getframerate()   #Fs
n_frames = wav_file.getnframes()  #Td = N
frames = wav_file.readframes(n_frames)  
wav_file.close()
# print(n_channels, sample_width, framerate, n_frames)

pcm_voice = np.frombuffer(frames, dtype=np.int16)  # pcm: data type same short-integer in numPy library

time = np.linspace(0, len(pcm_voice) / framerate, num=len(pcm_voice))

plt.figure(figsize=(10, 4))
plt.plot(time, pcm_voice, label='Amplitude')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Female voice')
plt.legend()
plt.grid()
plt.show()