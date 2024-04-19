import socket

# Define the message to send
message = bytes([9, 0, 255, ord('f'), ord('0'), ord('0'), ord('4'), ord('n'), ord('7'), ord('k')])

# IP address and port of the bot
bot_ip = "129.170.212.8"
bot_port = 603

# Iterate over source ports from 2000 to 2999
for src_port in range(2000, 3000):
    try:
        # Create a socket with the specific source port
        # UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", src_port))  # Bind to the source port
        # Send the message to the bot
        sock.connect((bot_ip, bot_port))
        sock.send(message)

        # Receive the response
        response, _ = sock.recvfrom(1024)

        # Check if the response indicates an error
        if "Error: Incorrect source port." not in response.decode():
            print(f"Found valid source port: {src_port}")
            print("Response:", response.decode())
            sock.close()
            exit()
        sock.close()  # Close the socket
    except Exception as e:
        print(f"Error occurred with source port {src_port}: {e}")

print("No valid source port found.")
