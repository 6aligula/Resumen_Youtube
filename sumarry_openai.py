# # Paso 3: Generación de Resúmenes con GPT-3.5
# import openai

# def generar_resumen(texto):
#     openai.api_key = 'tu_api_key'
    
#     response = openai.Completion.create(
#       engine="text-davinci-003",
#       prompt="Resumir el siguiente texto:\n\n" + texto,
#       temperature=0.5,
#       max_tokens=150,
#       top_p=1.0,
#       frequency_penalty=0.0,
#       presence_penalty=0.0
#     )
    
#     return response.choices[0].text.strip()
