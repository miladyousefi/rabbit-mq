import pika
import json
import time
import requests
import base64

def get_rabbitmq_connections(host, port, username, password):
    # Encode credentials for basic authentication
    credentials = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
    
    # RabbitMQ Management API endpoint for connections
    api_url = f"http://{host}:{port}/api/connections"

    # Set up HTTP headers for authentication
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/json',
    }

    # Make a GET request to the RabbitMQ Management API to retrieve connections
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve connections. Status code: {response.status_code}")
        return None

def main():
    # credentials = pika.PlainCredentials('rgbackend', 'hTw6@1l8^Z')
    # parameters = pika.ConnectionParameters(host='80.191.200.176', port=5672, virtual_host='/', credentials=credentials)


    credentials = pika.PlainCredentials('', '')
    parameters = pika.ConnectionParameters(host='', port=5672, virtual_host='/', credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Create a queue for your application
    channel.queue_declare(queue='#')

    # Publish messages to the amq.rabbitmq.log exchange
    exchange_name = 'pool'
    channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

    # Bind the queue to the exchange
    channel.queue_bind(exchange=exchange_name, queue='#')

    uuids = ['0e8d05e3']

    for i in uuids:
        time.sleep(4)
        try:
            data = {
                "data": i,
                "time": 48587147,
                "action": "read"
            }
            message = json.dumps(data)
            channel.basic_publish(exchange=exchange_name, routing_key='', body=message)
            print(f" [x] Sent {message}")
        except Exception as e:
            print(f"Error: {e}")

    # Get the list of RabbitMQ connections
    # rabbitmq_connections = get_rabbitmq_connections('192.168.50.41', 15672, 'admin', 'admin123')

    # if rabbitmq_connections:
    #     print("List of RabbitMQ Connections:")
    #     for connection in rabbitmq_connections:
    #         print(f"Connection: {connection['name']}, Host: {connection['peer_host']}, Port: {connection['peer_port']}")
    # else:
    #     print("Failed to retrieve connections.")

    # connection.close()

if __name__ == '__main__':
    main()
