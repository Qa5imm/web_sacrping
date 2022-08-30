from email.mime import base
from tempfile import tempdir
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
import time





 
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

headers={
    'User-agent': 'Mozilla/5.0 (X11; Linux i686; rv:104.0) Gecko/20100101 Firefox/104.0'
 }
base_url= 'https://myip.ms'

web_list=[]
lenght=0

for i in range(1,1001):
    print(i)
    r= requests.get(f'https://myip.ms/browse/sites/{i}/own/376714', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    productlist= soup.find_all('td',class_='row_name')
    lenght= len(productlist)
    
        
    if (lenght==0): 
        print("inside if")
        # try:
        #     driver.get(f'https://myip.ms/browse/sites/{i}/own/376714')
        #     captcha = driver.find_element(By.ID,'captcha_submit')  
        #     captcha.click() 
        #     time.sleep(20)
            
        # except:
        #     driver.get(f'https://myip.ms/browse/sites/{i}/own/376714')
        #     captcha = driver.find_element(By.ID,'captcha_submit')  
        #     captcha.click() 
        #     time.sleep(20)
        time.sleep(120)
        
        i= i-1
        print("here")
       
             
    print('td lenght',len(productlist))























#     for item in productlist:
#         name= item.text
#         item_url=item.find('a').get('href')
#         product={
#             'name':name,
#             'link': base_url +  item_url,
#             'td_length': lenght
#         }



#         # print(product)
#         web_list.append(product)
    

# print(len(web_list))
# df= pd.DataFrame(web_list)
# df.to_csv('test_list.csv')













 
        # r= requests.get(f'https://myip.ms/browse/sites/{i}/own/376714', headers=headers)
        # productlist= soup.find_all('td',class_='row_name')
        # lenght= len(productlist)


    # if (lenght == 0):
    #     print("inside if")
    #     # print(soup)
    #     try:
    #         driver.get(f'https://myip.ms/browse/sites/{i}/own/376714')
    #         captcha = driver.find_element(By.ID,'captcha_submit')  
    #         captcha.click() 
            
    #         driver.implicitly_wait(10)

    #         r= requests.get(f'https://myip.ms/browse/sites/{i}/own/376714', headers=headers)
    #         soup = BeautifulSoup(r.content, 'lxml')
    #         productlist= soup.find_all('td',class_='row_name')
    #         lenght= len(productlist)
    #         print('try td lenght',len(productlist))


    #         # print(productlist)
    #     except:
    #         print("error")
    #         r= requests.get(f'https://myip.ms/browse/sites/{i}/own/376714', headers=headers)
    #         soup = BeautifulSoup(r.content, 'lxml')
    #         productlist= soup.find_all('td',class_='row_name')
    #         lenght= len(productlist)
    #         print('excpet td lenght',len(productlist))