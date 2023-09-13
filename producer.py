#!/usr/bin/env python
import pika
import json

def main():
    credentials = pika.PlainCredentials('rg', 'rg123123')
    parameters = pika.ConnectionParameters(host='192.168.50.35', port=5672, virtual_host='/', credentials=credentials)
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    
    # Declare a queue where you want to send messages
    channel.queue_declare(queue='#')
    
    try:
        # Create a dictionary in the specified format
        data = {
            # "data": "0e8d05e3",
            # "data": "CA3EFEA0",
            "data": "F77F44B3",
            "time": 48587147,
            "action": "read"
        }
        
        # Convert the dictionary to a JSON string
        message = json.dumps(data)
        
        # Send the JSON message to the queue
        channel.basic_publish(exchange='', routing_key='shahin', body=message)
        print(f" [x] Sent {message}")
    except Exception as e:
        print(f"Error: {e}")
    
    connection.close()

if __name__ == '__main__':
    main()
