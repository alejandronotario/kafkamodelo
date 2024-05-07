from kafka import KafkaConsumer
import csv
from datetime import datetime
import os
import openai
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ''
client = OpenAI()

consumer = KafkaConsumer('textos', bootstrap_servers=['localhost:29092'],
     api_version=(0,10))

for mensaje in consumer:
    texto = str(mensaje.value.decode())

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role":"system","content":
          "This is an application to help call center employees"
          "Assistant takes inputs from users and determines its positive neutral and negative weights."
          "This weights are in 0-1 scale and their sum is 1."
          "Assistant must print the weights"
          "Assistant must print the input text"
          "Besides, if the negative weight is above 0.5, the Assistant must suggest a text in Spanish."
          "If the input text is a query te Assistant must suggest a solution in Spanish"},
        {"role": "user", "content": "{}".format(texto)}
      ]
    )
    print(response.choices[0].message.content)
     
