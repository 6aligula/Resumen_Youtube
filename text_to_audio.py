from transformers import WhisperTokenizer, WhisperForConditionalGeneration
import soundfile as sf
import torch

def transcribir_audio_whisper(audio_path):
    # Cargar el audio
    audio_input, sample_rate = sf.read(audio_path, dtype="float32")
    # Asegurarse de que la tasa de muestreo sea la adecuada para Whisper
    if sample_rate != 16000:
        raise ValueError("La tasa de muestreo debe ser de 16kHz.")

    # Cargar el modelo y el tokenizador de Whisper
    model_name = "openai/whisper-medium"
    model = WhisperForConditionalGeneration.from_pretrained(model_name)
    tokenizer = WhisperTokenizer.from_pretrained(model_name)
    
    # Procesar el audio
    inputs = tokenizer(audio_input, return_tensors="pt", padding="longest", sampling_rate=sample_rate)
    with torch.no_grad():
        generated_ids = model.generate(inputs["input_values"], attention_mask=inputs["attention_mask"])
    
    # Decodificar el texto
    texto = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    return texto


# from transformers import Wav2Vec2Tokenizer, Wav2Vec2ForCTC
# import torch
# import librosa

# def audio_a_texto(audio_path):
#     # Cargar el audio con librosa
#     audio_input, _ = librosa.load(audio_path, sr=16000)
    
#     # Cargar el modelo y el tokenizador de Wav2Vec2
#     tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h")
#     model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
    
#     # Procesar el audio
#     input_values = tokenizer(audio_input, return_tensors="pt").input_values
#     logits = model(input_values).logits
    
#     # Decodificar los logits a texto
#     predicted_ids = torch.argmax(logits, dim=-1)
#     texto = tokenizer.decode(predicted_ids[0])
    
#     return texto


