import re
import requests
from bs4 import BeautifulSoup


def getHTMLPage(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        print("获取页面出错")


def getWikiURL(url,lst):

    soup=BeautifulSoup(getHTMLPage(url),'html.parser')
    links=soup.find_all('a')
    for link in links:
        try:
            if re.match(r'/wiki/\d+',link.attrs['href']):
                lst.append('http://www.liaoxuefeng.com'+link.attrs['href'])

        except:
            continue
            #列表的append方法只能给一个参数，不能自动拼接，只能手动拼接然后再调用
            #获取div标签属性class可能为空的问题已解决
            #soup.find('div',attrs={'class':'x-wiki-content'})
            #针对子孙节点输出字符串重复，子节点无法输出正确的嵌套内容，使用
            #for string in soup.stripped_strings:
            #print(repr(string))
            #不使用repr会更友好
            #解决write数据的时候后面的将前面的冲掉，先建一个字典，然后将字典的数据一次性写入文件中


def WriteFile(html,path,lst):
    #假定html是一个r.text
    data={}
    soup=BeautifulSoup(html,'html.parser')
    divs=soup.find('div',attrs={'class':'x-wiki-content'})
    #for string in divs.strings:
    #   print(string)
    for i,string in range(len(lst)),divs.strings:
        key=i
        val=string
        data[key]=val
    with open(path,'w') as f:
        #for string in divs.strings:
        f.write(str(data)+'\n')


def main():
    source_url='http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    urllist=[]
    output_file='D:/wikis.txt'
    getWikiURL(source_url,urllist)
    for url in urllist:
        WriteFile(getHTMLPage(url),output_file,urllist)