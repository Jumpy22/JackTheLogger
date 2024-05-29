# JackTheLogger

JackTheLogger is a Python-based tool designed for cybersecurity professionals to monitor and log the Dynamic Link Libraries (DLLs) loaded by a specific process. This tool is particularly useful for analyzing the behavior of potentially malicious software or understanding the dependencies of a legitimate application.

## Features

- Monitors and logs the DLLs loaded by a specific process.
- Automatically installs required Python packages if not already present.
- Provides real-time updates on the loaded DLLs.
- Handles process termination gracefully.

## Requirements

- Python 3.x
- `psutil` library
- `termcolor` library
- `pefile` library

## Installation

JackTheLogger will automatically install the required libraries (`psutil`, `termcolor`, and `pefile`) if they are not already installed on your system. To ensure smooth operation, it's recommended to run the script in a Python virtual environment.

## Usage

1. Clone the repository or download the `main.py` file.
2. Open a terminal or command prompt and navigate to the directory containing `main.py`.
3. Run the script:

    ```bash
    python3 main.py
    ```

4. When prompted, enter the name of the process you want to monitor (including the extension, e.g., `example.exe`).
5. The tool will search for the specified process and start monitoring its loaded DLLs once the process is found.
6. The loaded DLLs will be printed to the console and logged to `dll_log.txt` in the same directory as the script.

## Example

```bash
$ python3 main.py
Process name (Including extension): example.exe
Looking for example.exe...
Found example.exe with PID 1234. Monitoring DLLs...
Loaded DLLs at Tue May 28 14:22:01 2024:
C:\Windows\System32\example.dll

