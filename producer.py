#!/usr/bin/env python
import pika
import json

def main():
    credentials = pika.PlainCredentials('rg', 'rg123123')
    parameters = pika.ConnectionParameters(host='192.168.50.35', port=5672, virtual_host='/', credentials=credentials)
#    test git
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()    
    channel.queue_declare(queue='#')
    uuids=[
        '0e8d05e3',
        # 'b7e7efc6',
        # '05139FB1',
        # '6A122664',
        # '77a7c4c6',
        # 'c546e2b2',
        # '1250880',
        # '0748d3c6',
        # '15df3ab2',
        # 'CA3EFEA0',
        # 'F77F44B3',
        # '2CAC228F',
        # 'DAAC2779'
    ]
    for i in uuids:
        try:
            data = {
                "data": i,
                "time": 48587147,
                "action": "read"
            }
            message = json.dumps(data)
            channel.basic_publish(exchange='', routing_key='shahin', body=message)
            print(f" [x] Sent {message}")
        except Exception as e:
            print(f"Error: {e}")
    
    connection.close()

if __name__ == '__main__':
    main()
