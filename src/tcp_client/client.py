import socket
import time
import random
import os

HOST = ""
PORT = 5000
print(os.environ.get('CLIENT_NAME'))
if os.environ.get('CLIENT_NAME') != None:
    HOST = 'server'  # Use service name for Docker Compose network
else:
#     HOST = '127.0.0.1'
    HOST = '0.0.0.0'
    
if __name__ == "__main__":
    try:
        # Connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            for counter in range(0, 5):
                # Send the counter value with the client (container) name from ENV
                client_name = os.environ.get('CLIENT_NAME')
                message = f"{client_name}:{counter}"
                s.sendall(message.encode('utf-8'))
                # Receive the response from the server
                response = s.recv(1024)
                print(f"Sent: {message}")
                print(f"Received from server: '{response.decode('utf-8')}'")
                # Wait for a random time between 1 and 5 seconds
                wait_time = random.randint(0, 3)
                time.sleep(wait_time)
            # Auto destroy after 10 sendings (exit)
    except Exception as e:
        print(f"Error: {e}")
