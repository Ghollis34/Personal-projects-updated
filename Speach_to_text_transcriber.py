import speech_recognition as sr
sr.__version__
r=sr.Recognizer()
audio_file = sr.AudioFile("test.wav")
with audio_file as source:
    audio = r.record(source)
type(audio)
r.recognize_google(audio)