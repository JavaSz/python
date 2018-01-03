import re
import requests
from bs4 import BeautifulSoup


def getHTMLPage(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        print("��ȡҳ�����")


def getWikiURL(url,lst):

    soup=BeautifulSoup(getHTMLPage(url),'html.parser')
    links=soup.find_all('a')
    for link in links:
        try:
            if re.match(r'/wiki/\d+',link.attrs['href']):
                lst.append('http://www.liaoxuefeng.com'+link.attrs['href'])

        except:
            continue
            #�б��append����ֻ�ܸ�һ�������������Զ�ƴ�ӣ�ֻ���ֶ�ƴ��Ȼ���ٵ���
            #��ȡdiv��ǩ����class����Ϊ�յ������ѽ��
            #soup.find('div',attrs={'class':'x-wiki-content'})
            #�������ڵ�����ַ����ظ����ӽڵ��޷������ȷ��Ƕ�����ݣ�ʹ��
            #for string in soup.stripped_strings:
            #print(repr(string))
            #��ʹ��repr����Ѻ�
            #���write���ݵ�ʱ�����Ľ�ǰ��ĳ�����Ƚ�һ���ֵ䣬Ȼ���ֵ������һ����д���ļ���


def WriteFile(html,path,lst):
    #�ٶ�html��һ��r.text
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