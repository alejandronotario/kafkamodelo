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
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "Sentiment analysis of the following text: {}".format(texto)}
      ]
    )
    print(response.choices[0].message.content)
    if "negative" in response.choices[0].message.content:
        print("ALERTA")  
