# Anti-Keylogger System

This is a Python-based tool that scans running processes to detect and terminate suspicious activities (like keyloggers).

## Prerequisites
Before running the code, you must install the required library using the command prompt:
```bash
pip install psutil
```

## How to Run
1.Navigate to the folder containing the script:
```bash
cd Desktop
```
2.Run the Python script:
```bash
py detector.py
```


## Sample Output
Here is what the system looks like when it detects a suspicious process:

```text
--- Scanning Running Processes ---
[!] Suspicious Process Found: notepad.exe (PID: 1234)

Suspicious activity detected. Terminate processes? (y/n): y
Process notepad.exe terminated successfully.
