from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/vits", progress_bar=True, gpu=True)
#tts = TTS(model_name="best_model.pth", progress_bar=True, gpu=True)
#tts = TTS(model_name="tts_models/en/jenny/jenny", progress_bar=True, gpu=True)

text = "Can you believe my neighbor's dog dug up my entire garden again? This is the third time this month! I've tried to stay patient, but I'm really fed up with the situation."

tts.tts_to_file(text=text, file_path="output1.wav", emotion="Happy", speed=1.0)
