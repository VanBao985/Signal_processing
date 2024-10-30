# Viết chương trình lọc nhiễu trong tín hiệu âm thanh theo phương trình sau: y(n) = x(n) + x(n-1) + x(n-2) + … + x(n-N).
# Input: file âm thanh đã thu âm
# Output: file âm thanh sau khi lọc nhiễu
# So sánh chất lượng của âm thanh sau khi lọc nhiễu bằng cách nghe trực tiếp với các giá trị N khác nhau (4, 8, 16, 32, 64, 128, 256, 512, 1024)
# Lưu ý: xử lý dữ liệu trực tiếp với số bít giống như số bít đã được thu âm.

import wave
import numpy as np

def read_wave(file_path):
    with wave.open(file_path, 'rb') as wf:
        params = wf.getparams()
        frames = wf.readframes(params.nframes)
        audio_data = np.frombuffer(frames, dtype=np.int16)
    return params, audio_data

def write_wave(file_path, params, audio_data):
    with wave.open(file_path, 'wb') as wf:
        wf.setparams(params)
        wf.writeframes(audio_data.tobytes())

def filter_noise(audio_data, N):
     filtered_data = np.copy(audio_data).astype(np.int32)
     for i in range(N, len(audio_data)):
         filtered_data[i] = np.sum(audio_data[i-N:i+1])
     return np.clip(filtered_data, -32768, 32767).astype(np.int16) 


def main(input_file, output_file_template, N_values):
    params, audio_data = read_wave(input_file)
    
    for N in N_values:
        filtered_data = filter_noise(audio_data, N)
        output_file = output_file_template.format(N)
        write_wave(output_file, params, filtered_data)
        print(f"Filtered audio with N={N} written to {output_file}")

input_file = '../sound/female.wav'
output_file_template = '../sound/processed_noise/output_N{}.wav'
N_values = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
main(input_file, output_file_template, N_values)