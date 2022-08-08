from pydub import AudioSegment
import wave
import contextlib
fname = 'About-a-Mile-Born-to-Live_1_.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
t1=0
t2=0
k=1
while t2<=duration:
  t2=t1+30
  newAudio = AudioSegment.from_wav(fname)
  newAudio = newAudio[t1*1000:t2*1000]
  newAudio.export('newSong'+str(k)+'.wav', format="wav")
  t1=t2
  k+=1