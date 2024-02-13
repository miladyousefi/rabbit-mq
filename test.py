import paho.mqtt.publish as publish
import json
import pika
import paho.mqtt.client as mqtt

username = ''
password = ''
rabbitmq_host = ""
rabbitmq_port = 1883  # Default MQTT port
virtual_host = "/"
exchange = "main"
queue = "main"
routing_key = "#"
message = {"data": "Hello, RabbitMQ!"}  # Update to a valid JSON payload

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = rabbitmq_host, port = 5672, virtual_host = '/', credentials = pika.PlainCredentials(username, password)))
channel = connection.channel()

channel.basic_publish(exchange = "amq.topic", routing_key = "test", body = "Hello World!", properties = None)

connection.close()