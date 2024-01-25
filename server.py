# Import the socket module to enable network communication
import socket

# Obtain the local IP address and specify a port number for the server
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455

# Create a tuple (address, port) to represent the server address
ADDR = (IP, PORT)

# Set constants for buffer size and data encoding format
SIZE = 1024
FORMAT = "utf-8"

# Define the main function where the server logic will be implemented
def main():
    print("[STARTING] Server is starting.")
    
    # Create a TCP socket using IPv4 addressing
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server to the specified address and port
    server.bind(ADDR)
    
    # Put the server in listening mode to accept incoming connections
    server.listen()
    print("[LISTENING] Server is listening.")

    # Initialize data structures to store information about connected clients and received files
    connected_clients = []  # List to store connected clients
    files_received = {}     # Dictionary to store information about files

    try:
        # Infinite loop to continuously accept and handle client connections
        while True:
            """ Server has accepted the connection from the client. """
            conn, addr = server.accept()
            print(f"[NEW CONNECTION] {addr} connected.")
            
            # Store connected client information in a list
            connected_clients.append({"address": addr, "connection": conn})
            
            # Store information about files in a dictionary
            files_received[addr] = {"files": []}

            """ Receiving the filename from the client. """
            filename = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the filename.")
            
            # Open the file in read mode to extract the first line
            file = open(filename, "r")
            first_line = file.readline()
            print(f"[FILE CONTENT] First line of {filename}: {first_line}")
            
            # Send acknowledgment to the client about the received filename
            conn.send(f"[SERVER] First line of {filename}: {first_line}".encode(FORMAT))
            conn.send("Your file has been received!".encode(FORMAT))

            """ Receiving the file data from the client. """
            data = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the file data.")
            
            # Close the file in read mode before opening in write mode
            file.close()
            file = open(filename, "w")  # Open the file in write mode
            file.write(data)
            
            # Send acknowledgment to the client about the received file data
            conn.send("File data received".encode(FORMAT))
            
            # Append information about the received file to the dictionary
            files_received[addr]["files"].append({"filename": filename, "data": data})

            """ Closing the file. """
            file.close()

            """ Closing the connection from the client. """
            conn.close()
            
            # Remove the disconnected client information from the list
            connected_clients.remove({"address": addr, "connection": conn})
            print(f"[DISCONNECTED] {addr} disconnected.")

            # Print connected clients and files_received for debugging
            print("[CONNECTED CLIENTS]:", connected_clients)
            print("[FILES RECEIVED]:", files_received)

    except KeyboardInterrupt:
        # Handle a keyboard interrupt to gracefully shut down the server
        print("[SERVER] Server is shutting down.")
    finally:
        # Close connections and perform cleanup here
        for client_info in connected_clients:
            client_info["connection"].close()

# Entry point for the script
if __name__ == "__main__":
    main()
