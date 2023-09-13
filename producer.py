#!/usr/bin/env python
import pika
import json

def main():
    credentials = pika.PlainCredentials('rgbackend', 'hTw6@1l8^Z')
    parameters = pika.ConnectionParameters(host='80.191.200.176', port=5672, virtual_host='/', credentials=credentials)
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    
    # Declare a queue where you want to send messages
    channel.queue_declare(queue='#')
    
    try:
        # Create a dictionary in the specified format
        data = {
            "data": "0e8d05e3",
            # "data": "CA3EFEA0",
            # "data": "F77F44B3",
            "time": 48587147,
            "action": "read"
        }
        
        # Convert the dictionary to a JSON string
        message = json.dumps(data)
        
        # Send the JSON message to the queue
        channel.basic_publish(exchange='', routing_key='pool', body=message)
        print(f" [x] Sent {message}")
    except Exception as e:
        print(f"Error: {e}")
    
    connection.close()

if __name__ == '__main__':
    main()
