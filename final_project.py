import xlsxwriter
import xlrd
import re
from bs4 import *
import urllib.request
class SEO:
    def __init__(self,wbk,wsht):
        self.wbk = wbk
        self.wsht = wsht
    def read_sheet_data(self):
        col_no = int(input("Enter column number where data is stored : "))
        col_no = col_no -1
        if(col_no < 0):
            print("Enter valid column number!")
        elif(col_no >= 0):
            self.data = self.wsht.col_values(col_no)
            #removing empty elements from list
            self.data = [x.lower() for x in self.data if(x)]
            del self.wbk,self.wsht
            if(len(self.data)==0):
                return False
            else:
                print(self.data)
                return True
    def read_url_from_data(self):
        pattern = re.compile('(https://)|(http://)')
        for x in self.data:
            if(pattern.match(x)):
                self.url = x
                self.data.remove(x)
                return True
                break
        return False
    
    def web_scrapping(self):
        req = urllib.request.Request(self.url, data=None, 
             headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' } 
                                      )
        req = urllib.request.urlopen(req)
        soup = BeautifulSoup(req,'lxml')
        for x in soup(['script','style']):
            x.extract()
        soup = soup.getText()
        urlConts=[]
        self.urlContents=[]
        for x in soup.splitlines(): #split('\n')
            if(len(x)>0):
                x=x.lower()
                urlConts.append(x.strip())
        for x in urlConts:
            self.urlContents.extend(x.split())
        print(self.urlContents)
    def CountFrequency(self):
        wbk = xlsxwriter.Workbook('RESULT.xlsx')
        wsht = wbk.add_worksheet('new')
        count=[y for y in map((lambda y:self.urlContents.count(y)),self.data)]
        i=0
        for x in count:
            wsht.write(i,1,x)
            i=i+1
        i=0
        for x in self.data:
            wsht.write(i,0,x)
            i=i+1
        count ={x:y for x,y in zip(self.data,count)}
        print(count)
        
wbk = input("Enter location of workbook : ")
try:
    wbk = xlrd.open_workbook(wbk)
except Exception:
    print("Sorry unable to locate the file specified")
    print("Hint: use extension (eg .xlsx)")
else:
    wsht = input("Enter worksheet name : ")
    try:
        wsht = wbk.sheet_by_name(wsht)
    except Exception:
        print("Please enter valid worksheet name")
    else:
        seo = SEO(wbk,wsht)
        if(seo.read_sheet_data()):
            if(seo.read_url_from_data()):
                seo.web_scrapping()
                seo.CountFrequency()
            else:
                print("No url found")
            #del wbk,wsht
        else:
            print("The specified column is empty!")