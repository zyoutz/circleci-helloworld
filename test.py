import urllib.request
import sys
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   print(html)
   
sys.exit(1)
