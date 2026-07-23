import requests

with open('test.pdf', 'wb') as f:
    f.write(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 24 Tf 72 100 Td (Hello) Tj ET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f\n0000000010 00000 n\n0000000064 00000 n\n0000000112 00000 n\n0000000211 00000 n\ntrailer\n<< /Root 1 0 R /Size 5 >>\nstartxref\n312\n%%EOF\n')

with open('test.pdf', 'rb') as f:
    response = requests.post(
        'http://127.0.0.1:5174/upload',
        files={'file': ('test.pdf', f, 'application/pdf')},
        data={'session_id': 'test-session'}
    )

print(response.status_code)
print(response.text)
