import requests
from bs4 import BeautifulSoup

pagina=requests.get("https://www.segurossura.com.co/paginas/preguntas-frecuentes.aspx")
sopa=BeautifulSoup(pagina.text, 'html.parser')

contenidos=sopa.find_all('div',class_='blog-sura-card-content')

arregloh3=[]
arreglop=[]

for contenedor in contenidos:
    h3=contenedor.find('h3')
    p=contenedor.find('p')

    if h3 and p:
        arregloh3.append(h3.text.strip())
        arreglop.append(p.text.strip())



print(arregloh3)
print(arreglop)