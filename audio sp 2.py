import sounddevice as sd
from scipy.io.wavfile import write

fs = 48000  # Sample rate
seconds = 10  # Duration of recording
k=0
try:
    while True:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write('output'+str(k)+'.wav', fs, myrecording) # Save as WAV file
        k+=1
except KeyboardInterrupt:
    raise SystemExit
