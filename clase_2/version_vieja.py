# Deprecado
# import openai # Llamado a la librería
# from env import API_KEY # Importación de la API_KEY

# openai.api_key = API_KEY # Asignación de la API_KEY

# def generar_tarea_para_reunion(reunion):
#   # Definimos una prompt
#   prompt = f"Genera una tarea pendiente para la reunión de {reunion}:"

#   response = openai.Completion.create(
#     engine="text-davinci-002", # Modelo a usar
#     prompt=prompt, # Prompt
#     max_tokens=100 # Máximo de tokens a generar
#   )

#   tarea_pendiente = response.choices[0].text.strip() # Obtenemos el texto generado

#   return tarea_pendiente # Retornamos el texto generado

# # Ejemplo de uso
# if __name__ == "__main__":
#   reunion = "reunión de equipo"

#   tarea_pendiente = generar_tarea_para_reunion(reunion)

#   print(f"La tarea pendiente para la {reunion} es: {tarea_pendiente}") # Imprimimos el texto generado
