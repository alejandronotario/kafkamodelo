from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers = 'localhost:29092')

with open("textos.txt", "r") as f:
	for msg in f:
		producer.send("textos", msg.encode('utf-8'))
		print("Enviando mensaje \"{}\"".format(msg))
		print("Mensaje enviado")
		time.sleep(15)