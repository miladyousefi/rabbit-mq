#!/usr/bin/env python
import pika
import json
import time
def main():
    # credentials = pika.PlainCredentials('gabpkgoo', 'TCS6PVx12BrAW34FyigUdfGozaWD7pwm')
    # parameters = pika.ConnectionParameters(host='amqps://gabpkgoo:TCS6PVx12BrAW34FyigUdfGozaWD7pwm@porpoise.rmq.cloudamqp.com/gabpkgoo', port=5672, virtual_host='gabpkgoo', credentials=credentials)
    
    # credentials = pika.PlainCredentials('admin', 'admin123')
    # parameters = pika.ConnectionParameters(host='192.168.50.33', port=5672, virtual_host='/', credentials=credentials)

    # credentials = pika.PlainCredentials('rgbackend', 'hTw6@1l8^Z')
    # parameters = pika.ConnectionParameters(host='80.191.200.176', port=5672, virtual_host='/', credentials=credentials)
    #test git


    credentials = pika.PlainCredentials('RgRabbit', 'ZSNVqEj9b2')
    parameters = pika.ConnectionParameters(host='195.214.235.212', port=5672, virtual_host='/', credentials=credentials)
    # print(parameters)



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
        # set a delay 
        # time.sleep(4)
        try:
            data = {
                "imei":'1531das54d',
                "balance":123,
                "version":2,
                "battery":1,
                "ZFI":1,
                "ZFA":0,
                "MFA":0,
                "AFA":0,
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
