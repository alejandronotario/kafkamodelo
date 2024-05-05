# kafkamodelo

## Alcance

Simulador de modelo de sentimiento para clasificar llamadas transcritas a formato texto de apertura de siniestros
de una aseguradora. Tiene que se clasificarse en tiempo real por si es necesario actuar por parte
de los tramitadores. Los resultados se imprimirían en un frontal que los tramitadores usan.
En este emulador, se imprimirá __ALERTA__ en caso de que el texto se clasifique como negativo.

## Componentes 

__Docker__

La aplicación se despliega con servicio docker. Se incluye un docker-compose con servicios zookeeper y kafka para ello.

__Kafka__

En el docker-compose se incluye la configuración de los servidores donde se ubicarán el productor y consumidor.

__OpenAI__

Se ha seleccionado el modelo __gpt-3.5-turbo__ para preguntar por sentimiento a cada entrada de texto.

## Manual

En primer lugar se levanta el servicio:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo service docker start
sudo docker run hello-world
#comenzar el servidor kafka
docker-compose up -d
#comprobación de que los servidores escuchan
nc -zv localhost 22181
nc -zv localhost 29092
```

Seguidamente se ejecutan el consumidor y el productor en dos terminales diferentes:

```bash
#terminal1
python consumer.py
#terminal2
python producer.py
```
Nota: para que funcione se debe tener cuenta de OpenAI e incluir la API KEY personal.

## Consideraciones

La idea de esta aplicación en producción con AWS es la siguiente:

```mermaid
flowchart LR
    A[DynamoDB textos] --> B(kafka producer)
    B(kafka producer) --> C(TOPIC)
    C(TOPIC) --> D(kafka consumer)
    D(kafka consumer) --> E(Frontal de tramitadores)
```
