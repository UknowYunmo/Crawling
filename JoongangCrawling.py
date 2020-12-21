from bs4 import BeautifulSoup
import urllib.request
def j_scroll(n):
    list_url="https://news.joins.com/Search/JoongangNews?page="+str(n)+"&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
    url=urllib.request.Request(list_url)
    result=urllib.request.urlopen(url).read().decode('UTF-8')
    soup=BeautifulSoup(result,"html.parser")
    
    result1=soup.find_all('h2',class_ ='headline mg')
    
    params=[]
    for i in result1:
        for k in i:
            params.append(k.get('href'))
    return params
 
def j_detail_scroll(n):
    params2=[]
    list_url=j_scroll(n)
    for i in list_url:
        url=urllib.request.Request(i)
        result=urllib.request.urlopen(url).read().decode('UTF-8')
        soup=BeautifulSoup(result,"html.parser")
         
        result1=soup.find_all('div', class_ ='article_body mg fs4')
         
        for i in result1:
            params2.append(i.get_text(" ",strip=True))
    return params2
for k in range(1,4):
    print(j_detail_scroll(k))
    print('------------------'+'            '+str(k)+'페이지'+'              '+'------------------')
    print()
    print()
    print()
    print('---------------------------------------------------------------------')