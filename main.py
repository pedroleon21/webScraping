from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# header

_path = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+cards#'

file_name='produtos.csv'
f = open(file_name,'w')
headers = 'fabricante, nome_produto, entrega \n'
f.write(headers)
# abrindo conexao e pegando conteudo
req_page = uReq(_path)
html_page = req_page.read()
req_page.close()
#parser contend
soup_page = soup(html_page, 'html.parser')
itens = soup_page.findAll('div',{'class':'item-container'})
for item in itens:
    fabricante = item.div.div.a.img['title']
    produto = item.findAll('a',{'class':'item-title'})[0].text.strip()
    entrega = item.findAll('li',{'class':'price-ship'})[0].text.strip()
    print(fabricante)
    print(produto)
    print(entrega)
    f.write(fabricante + ',' + produto.replace(',', '|') + ',' + entrega + '\n')
f.close()