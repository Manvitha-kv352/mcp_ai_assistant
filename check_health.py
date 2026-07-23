import urllib.request

try:
    with urllib.request.urlopen('http://127.0.0.1:8013/health', timeout=5) as response:
        print(response.status)
        print(response.read().decode())
except Exception as e:
    print('ERROR')
    print(type(e).__name__)
    print(e)
