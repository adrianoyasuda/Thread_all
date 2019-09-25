import re
from urllib.request import urlopen

url= "http://infopguaifpr.com.br"
html = str(urlopen(url).read())
# print(html)


sub_html = str(html).count("http://infopguaifpr.com.br/")

print(sub_html)

x = re.findall("http://infopguaifpr.com.br/[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-] ?", html)

print(x)