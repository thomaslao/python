from urllib.parse import urlparse

addr="http://www.puiching.edu.mo"

result=urlparse(addr)
print("回傳的parseResult物件:")
print(result)