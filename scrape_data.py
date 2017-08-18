import urllib.request
from bs4 import BeautifulSoup
query=input("Enter product to be searched: ")
url='https://www.flipkart.com/search?q='+query
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')  
output=soup.prettify().encode('utf8')

for names in soup.find_all("div", "_3wU53n"):
    print(names.text)
#for names in soup.find_all("div", "_3wU53n"):
 #   print(names.text)
#file = open("testfile.html","w")  
#file.write(str(output)) 
#file.close() 