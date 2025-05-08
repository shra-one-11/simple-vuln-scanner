# Simple Vulnerability Scanner

A simple Python-based vulnerability scanner that checks for open ports in a network. It can be extended to scan for specific vulnerabilities and services, making it a useful tool for network security assessments.

## Features
- **Port Scanning**: Scans a specified range of ports to check if they are open or closed.
- **Threaded Scanning**: Uses threading to speed up the scanning process.
- **Customizable Range**: Allows users to scan any range of ports.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/simple-vuln-scanner.git
   cd simple-vuln-scanner
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage:

To use the scanner, run the script with the following arguments:
- `<target>`: The target IP address or hostname.
- `<start_port>`: The starting port for the range you want to scan.
- `<end_port>`: The ending port for the range you want to scan.

## Example:

```bash
python scanner.py 192.168.1.1 20 80
```

## How It Works:

    The script creates a socket connection to each port in the specified range.
    If the port is open, it returns a message indicating that the port is open.
    If the port is closed, it returns a message indicating that the port is closed.
    The scanning process is done in parallel using threading to improve speed.

## Contributing:

Feel free to fork the project and submit pull requests with improvements or fixes. Here are a few ways you can contribute:
    Adding more features (e.g., scanning for specific vulnerabilities).
    Improving the user interface.
    Optimizing performance.

## License:

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements:

This project was inspired by the need for quick and basic network vulnerability scanning. It’s an open-source project with the aim of helping developers understand the basics of network security and vulnerability scanning.

## Contact:

For any questions or suggestions, feel free to reach out to me at </br>
shravans755@gmail.com or shravanprotagonist@gmail.com.
