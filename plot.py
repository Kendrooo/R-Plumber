# load requests library
import requests

# submit API request
resp = requests.get("http://localhost:8000/plot")
print(resp)

f = open("sample_plot.png", "wb")
f.write(resp.content)
f.close()
