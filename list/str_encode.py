text = "Hello, 世界"
utf8_bytes = text.encode("utf-8")
print(utf8_bytes) # prints: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

decoded_text = utf8_bytes.decode("utf-8")
print(decoded_text) # prints: Hello, 世界