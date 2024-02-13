from convert_to_mp3 import descargar_audio
#from sumarry_openai import generar_resumen
from text_to_audio import audio_a_texto

# Integración de los Pasos
def procesar_video():
    #descargar_audio(video_url)
    texto = audio_a_texto("input.mp3")
    #resumen = generar_resumen(texto)
    print(texto)
    
# # Integración de los Pasos
# def procesar_video(video_url):
#     descargar_audio(video_url)
#     texto = audio_a_texto("input.mp3")
#     #resumen = generar_resumen(texto)
#     print(texto)

# Ejemplo de Uso
video_url = "tu_url_de_video"
procesar_video(video_url)
