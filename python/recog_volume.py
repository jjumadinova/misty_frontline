# from pydub import AudioSegment
#
# source1 = "audio/s_Acceptance.wav"
# song = AudioSegment.from_wav(source1)
#
# print(song)

from scipy.io.wavfile import read
from math import log10, sqrt
from statistics import mean
import numpy as np

samprate, wavdata = read('audio/s_Acceptance.wav')
print(len(wavdata))
chunks = np.array_split(wavdata, len(wavdata))

high_dbs_list = []
low_dbs_list = []

for chunk in chunks:
    high = chunk[0][0]
    low = chunk[0][1]
    # print(high, low)
    high_dbs = 20*log10(sqrt(mean(high**2)))
    low_dbs = 20*log10(sqrt(mean(low**2)))
    # print(high_dbs, low_dbs)

# print(chunks[0][0][0])
# print(chunks[0])

# print(chunks)

# dbs = [20*log10(sqrt(mean(chunk[0][0]**2)) ) for chunk in chunks]

# print(dbs)
