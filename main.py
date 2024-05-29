import subprocess
import sys
import time
import psutil

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import psutil
except ImportError:
    print("psutil not found, installing...")
    install('psutil')
    import psutil

try:
    from termcolor import colored
except ImportError:
    print("psutil not found, installing...")
    install('termcolor')
    from termcolor import colored

try:
    import pefile
except ImportError:
    print("pefile not found, installing...")
    install('pefile')
    import pefile

def get_loaded_modules(pid):
    process = psutil.Process(pid)
    modules = []
    for module in process.memory_maps():
        if module.path.endswith('.dll'):
            modules.append(module.path)
    return modules

def log_dlls(pid, logfile='dll_log.txt'):
    with open(logfile, 'a') as log:
        log.write(f"Monitoring DLLs for PID: {pid}\n")
        while True:
            try:
                loaded_modules = get_loaded_modules(pid)
                print(colored(f"Loaded DLLs at {time.ctime()}:","yellow"))
                log.write(f"\nLoaded DLLs at {time.ctime()}:\n")
                for module in loaded_modules:
                    print(colored(f"{module}","yellow"))
                    log.write(f"{module}\n")
                log.flush()
                time.sleep(10)
            except psutil.NoSuchProcess:
                print(colored("Process has been terminated.","red"))
                log.write("Process terminated.\n")
                break

def find_process_by_name(name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == name:
            return proc.info['pid']
    return None

if __name__ == "__main__":
    
    process_name = input("Process name (Including extension): ")
    
    print(f"Looking for {process_name}...")

    pid = None
    while pid is None:
        pid = find_process_by_name(process_name)
        if pid is None:
            time.sleep(0.1)

    print(colored(f"Found {process_name} with PID {pid}. Monitoring DLLs...","green"))
    log_dlls(pid)
