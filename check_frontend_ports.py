import urllib.request
import socket

for port in [5174, 5175]:
    url = f'http://127.0.0.1:{port}/'
    print(f'Checking {url}')
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            print('status:', response.status)
            print('content snippet:', response.read(200).decode('utf-8', errors='replace'))
    except Exception as e:
        print('ERROR:', type(e).__name__, e)
    print('---')
