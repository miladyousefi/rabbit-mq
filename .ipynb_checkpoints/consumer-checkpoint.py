#!/usr/bin/env python
import pika, sys, os

def main():
    # credentials = pika.PlainCredentials('admin', '123456')
    # parameters = pika.ConnectionParameters(host='192.168.50.28', port=5672, virtual_host='/', credentials=credentials)
    
    credentials = pika.PlainCredentials('admin', 'admin123')
    parameters = pika.ConnectionParameters(host='192.168.50.41', port=5672, virtual_host='/', credentials=credentials)
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()      
    channel.queue_declare(queue='#')
    
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

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