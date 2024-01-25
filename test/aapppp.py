import time
from AudioRec import Recorder

rec = Recorder(channels=1)
rec.start()
time.sleep(5)   # Waits for 5 seconds
rec.stop()

rec.save("test.wav") 
Recorder.wavTomp3("test.wav")