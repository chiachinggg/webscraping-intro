from bs4 import BeautifulSoup
import requests

url = "https://lms.monash.edu/course/view.php?id=149590"
response = requests.get(url, timeout=10)
content = BeautifulSoup(response.content, "html.parser")
print(content)
