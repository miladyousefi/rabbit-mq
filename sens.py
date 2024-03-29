#!/usr/bin/env python
import pika
import json
import time
def main():
   
    # credentials = pika.PlainCredentials('admin', 'admin123')
    # parameters = pika.ConnectionParameters(host='192.168.50.33', port=5672, virtual_host='/', credentials=credentials)

    # credentials = pika.PlainCredentials('', '')
    # parameters = pika.ConnectionParameters(host='', port=5672, virtual_host='/', credentials=credentials)
    #test git


    credentials = pika.PlainCredentials('', '')
    parameters = pika.ConnectionParameters(host='', port=5672, virtual_host='/', credentials=credentials,heartbeat=600)



    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()    
    channel.queue_declare(queue='#')
    try:
        data = {
            "imei":'869556065667850',
            "balance":12,
            "version":1,
            "battery":9,
            "ZFI":1,
            "ZFA":1,
            "MFA":1,
            "AFA":1,
            "BFA":0,
            "SFA":0
        }
        message = json.dumps(data)
        channel.basic_publish(exchange='', routing_key='main', body=message)
        print(f" [x] Sent {message}")
    except Exception as e: 
        print(f"Error: {e}")
    connection.close()
if __name__ == '__main__':
    main()
