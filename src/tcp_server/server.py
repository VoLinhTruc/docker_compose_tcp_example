import socket
import threading
import uuid
import os

class TCPServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = {}  # Dictionary to store client connections and their IDs

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            client_socket, address = self.server_socket.accept()
            client_id = str(uuid.uuid4())[:8]  # Generate a unique ID for each client
            self.clients[client_id] = client_socket
            
            print(f"New connection from {address}, assigned ID: {client_id}")
            
            # Start a new thread to handle this client
            client_thread = threading.Thread(target=self.handle_client, 
                                          args=(client_socket, client_id))
            client_thread.start()

    def handle_client(self, client_socket, client_id):
        log_dir = os.path.join(os.path.dirname(__file__), 'client_data')
        log_file = os.path.join(log_dir, 'log.txt')
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                
                message = data.decode('utf-8')
                print(f"Received message from client {client_id}: {message}")
                
                # Log the message to client_data/log.txt
                with open(log_file, 'a') as f:
                    f.write(f"Client {client_id}: {message}\n")
                
                # Send back the message with server port
                response = f"Server on port {self.port} received: {message}"
                client_socket.send(response.encode('utf-8'))
                
        except Exception as e:
            print(f"Error handling client {client_id}: {str(e)}")
        finally:
            print(f"Client {client_id} disconnected")
            client_socket.close()
            del self.clients[client_id]

    def close(self):
        for client_socket in self.clients.values():
            client_socket.close()
        self.server_socket.close()

if __name__ == "__main__":
    server = TCPServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        server.close()
