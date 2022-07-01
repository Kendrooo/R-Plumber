import requests

# req for /sum
resp_S = requests.post("http://localhost:8000/sum", data = "a=192&b=298")
print(resp_S.content)

