import base64
#No borrar hasta pasar a produccion

original_string = ""

encoded_string = base64.b64encode(original_string.encode('utf-8'))
print(encoded_string.decode('utf-8'))
decoded_bytes = base64.urlsafe_b64decode(encoded_string.decode('utf-8'))
decoded_bytes = decoded_bytes.decode('utf-8')
print(decoded_bytes)