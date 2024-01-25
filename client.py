# Import necessary modules for networking and GUI file dialog
import socket
from tkinter import Tk, filedialog

# Obtain the local IP address and specify a port number for the server
IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)

# Set constants for buffer size, data encoding format, and file selection dialog
FORMAT = "utf-8"
SIZE = 1024

# Function to open a file dialog for selecting a file
def select_file():
    # Create a Tkinter root window and hide it
    root = Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog for selecting a file
    file_path = filedialog.askopenfilename(title="Select a file")

    # Close the Tkinter window
    root.destroy()

    return file_path

# Main function to execute the file transfer client
def main():
    """ Starting a TCP socket. """
    # Create a TCP socket using IPv4 addressing
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    # Connect to the server using the specified address
    client.connect(ADDR)

    """ Opening and reading the file data. """
    # Use the select_file function to get the path of the selected file
    file_path = select_file()
    
    # Check if the file selection was canceled
    if not file_path:
        print("File selection canceled.")
        client.close()
        return

    # Open the selected file in binary mode for reading
    with open(file_path, "rb") as file:
        # Read the entire content of the file
        data = file.read()

    """ Sending the filename to the server. """
    # Extract the filename from the path using '/' as the separator
    filename = file_path.split("/")[-1]

    # Send the filename to the server in the specified encoding
    client.send(filename.encode(FORMAT))

    # Receive and print a message from the server
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Sending the file data to the server. """
    # Send the file data to the server
    client.send(data)

    # Receive and print a message from the server
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the connection from the server. """
    # Close the client socket
    client.close()

# Entry point for the script
if __name__ == "__main__":
    main()

