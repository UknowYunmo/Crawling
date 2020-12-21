from  bs4  import  BeautifulSoup
import  urllib.request
def bs_scroll():
    params=[]
    for i in range(1,3):
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup( result, "html.parser")
        result1=soup.find_all('div',class_ ='elementor-post__title')
        for i in result1:
            params.append(i.find_all('a')[0].get("href"))
    my_result=set(params)
    my_result2=list(my_result)
    return my_result2
def bs_detail_scroll():
    list_url = bs_scroll()
    final=[]
    for i in list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup( result, "html.parser")
        result1=soup.find_all('div',class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        final.append(result1[0].get_text())
    return final
print(bs_detail_scroll())