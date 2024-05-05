from kafka import KafkaConsumer
import csv
from datetime import datetime
import os
import openai
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ''
client = OpenAI()

consumer = KafkaConsumer('llamadas', bootstrap_servers=['localhost:29092'],
     api_version=(0,10))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Sentiment analysis of the following text: hoy es un dis soleado pero me pongo triste cuando llueve"}
  ]
)


print(response.choices[0].message.content)
