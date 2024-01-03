from openai import OpenAI

client = OpenAI(api_key="")

tipo_reunion = input("Ingresa el tipo de reunion: ")

def generar_tarea_para_reunion(tipo_reunion):
  prompt = f"Genera una tarea pendiente para una reunion de tipo {tipo_reunion}"

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ],
    max_tokens=100
  )

  tarea_pendiente = response.choices[0].message.content

  return tarea_pendiente

if __name__ == "__main__":
  tarea_pendiente = generar_tarea_para_reunion(tipo_reunion)

  print(f"La tarea pendiente para la {tipo_reunion} es: {tarea_pendiente}") # Imprimimos el texto generado
