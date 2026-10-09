from transformers import pipeline
asr_pipeline = pipeline('automatic-speech-recognition', model="openai/whisper-base")
audio_path = "audio/audio.wav"
result = asr_pipeline(audio_path)
print(result["text"])