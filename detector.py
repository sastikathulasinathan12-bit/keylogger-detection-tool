import psutil
import os
import time

# List of known suspicious names (Signatures)
SUSPICIOUS_NAMES = ["keylogger", "hook", "spy", "notepad"]

def scan_processes():
    print("--- Scanning Running Processes ---")
    suspicious_found = []

    # Loop through all running processes
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            p_info = proc.info
            p_name = p_info['name'].lower() if p_info['name'] else ""
            p_path = p_info['exe'] if p_info['exe'] else ""

            # Check 1: Signature Matching (Name)
            for bad_name in SUSPICIOUS_NAMES:
                if bad_name in p_name:
                    print(f"[!] Suspicious Process Found: {p_name} (PID: {p_info['pid']})")
                    suspicious_found.append(proc)
            
            # Check 2: Heuristics (Running from Temp folder)
            if p_path and "temp" in p_path.lower():
                 print(f"[!] Warning: Process running from TEMP: {p_name}")
                 suspicious_found.append(proc)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return suspicious_found

def terminate_process(proc):
    try:
        proc.terminate()
        print(f"Process {proc.name()} terminated successfully.")
    except Exception as e:
        print(f"Failed to terminate: {e}")

# Main Execution
if __name__ == "__main__":
    while True:
        bad_procs = scan_processes()
        
        if bad_procs:
            choice = input("\nSuspicious activity detected. Terminate processes? (y/n): ")
            if choice.lower() == 'y':
                for p in bad_procs:
                    terminate_process(p)
        
        print("Scan complete. Sleeping for 10 seconds...")
        time.sleep(10)