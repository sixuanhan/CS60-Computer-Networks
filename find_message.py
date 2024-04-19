import socket

# Define the IP address and port of the bot
bot_ip = "129.170.212.8"
bot_port = 603

# Connect to the bot
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((bot_ip, bot_port))

init_error_response = None

# Loop through all possible 10-byte messages
for i in range(256):  # Assuming bytes are in range 0-255
    message = bytes([9, 0, i, 0, 0, 0, 0, 0, 0, 0])
    sock.send(message)
    response = sock.recv(1024).decode()
    if init_error_response == None:
        init_error_response = response
        print("init_error_response: ", init_error_response)
    # Check if the response is different from the initial error message
    if response != init_error_response:
        print("Found a message:", message)
        print("Response from the bot:", response)
        # exit()

# Close the connection
sock.close()

