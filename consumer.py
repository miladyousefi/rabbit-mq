#!/usr/bin/env python
import pika, sys, os
import json

def main():
    credentials = pika.PlainCredentials('', '')
    parameters = pika.ConnectionParameters(host='', port=5672, virtual_host='/', credentials=credentials)
    
    # credentials = pika.PlainCredentials('', '')
    # parameters = pika.ConnectionParameters(host='', port=5672, virtual_host='/', credentials=credentials)
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()      
    channel.queue_declare(queue='#')
    
    def callback(ch, method, properties, body):
        # Assuming body is a string
        body_str = body.decode('utf-8')

        # Construct a valid JSON string
        json_str = '{"data": {' + body_str + '}}'

        try:
            data = json.loads(json_str)
            print(" [x] Parsed data:", data['data'])
        except json.JSONDecodeError as e:
            print(" [!] Error decoding JSON:", e)


    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)