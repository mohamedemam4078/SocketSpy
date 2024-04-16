# SocketSpy

SocketSpy is a Python-based port scanning tool that allows you to scan one or multiple targets for open ports on specified port ranges.

## Features

- Scan single or multiple targets for open ports
- Specify custom port ranges to scan
- Lightweight and easy-to-use
- Support for both IPv4 and IPv6 targets

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mohamedemam4078/SocketSpy.git
    ```

2. Navigate to the project directory:

    ```bash
    cd SocketSpy
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Scan a single target:

    ```bash
    python SocketSpy.py target_ip_address -p port_range
    ```

2. Scan multiple targets:

    ```bash
    python SocketSpy.py target1_ip_address,target2_ip_address -p port_range
    ```

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
