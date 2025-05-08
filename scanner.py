import socket
import sys
import threading

# Function to scan a single port
def scan_port(target, port):
    try:
        # Create a socket connection to the target IP and port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for the connection
        result = sock.connect_ex((target, port))  # Try to connect
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    except socket.error:
        print(f"Port {port} is CLOSED")

# Function to scan a range of ports
def scan_ports(target, start_port, end_port):
    print(f"Scanning target: {target}")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

# Main function to accept user input and start scanning
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python scanner.py <target> <start_port> <end_port>")
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    # Scan the ports using threading to speed up the process
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Scan complete.")
