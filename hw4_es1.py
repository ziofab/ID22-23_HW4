# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import StaleElementReferenceException


from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import time

GECKO_PATH = "./geckodriver"
ADBLOCK_PATH = "./adblock_plus-3.10-an fx.xpi"

start_urls = [
    'https://www.amazon.it/dp/B07YXH2DLL/',
    'https://www.amazon.it/dp/B09JPCB3WR/',
    'https://www.amazon.it/dp/B0837HK2DT/',
    'https://www.amazon.it/dp/B07QJ21YQ6/',
    'https://www.amazon.it/dp/B00Q2KEVA2/',
    'https://www.amazon.it/dp/B09JPCNS3X/',
    'https://www.amazon.it/dp/B08NDZRJJP/',
    'https://www.amazon.it/dp/B08485YF1Z/',
    'https://www.amazon.it/dp/B073D2G7XY/',
    'https://www.amazon.it/dp/B084S59W2S/',
    'https://www.amazon.it/dp/B08F7MWWFQ/'
]

#'file:///D:/Univ/ID/HW4/src1/B07YXH2DLL.htm',
#'file:///D:/Univ/ID/HW4/src1/B09JPCB3WR.htm',
#'file:///D:/Univ/ID/HW4/src1/B0837HK2DT.htm',
#'file:///D:/Univ/ID/HW4/src1/B07B322GL5.htm',
#'file:///D:/Univ/ID/HW4/src1/B07MWDP1VD.htm',
#'https://www.amazon.it/dp/B09JPCNS3X/',
#'https://www.amazon.it/dp/B08NDZRJJP/',
#'https://www.amazon.it/dp/B08485YF1Z/',
#'https://www.amazon.it/dp/B07B9RXC8M/',
#'https://www.amazon.it/dp/B084S59W2S/'

print_xpath = True

def my_find_subelement(attribute, driver, elem):
    global print_xpath
    t = None
    try:
        t = driver.find_element("xpath", elem)
        if (print_xpath and (not attribute.startswith('_'))):
            print(attribute+": "+elem);
    except Exception as e:
        print("Attribute "+attribute+". Cannot find element: ", elem)
        pass
    return t

def my_find_element(attribute, driver, elem):
    l = len(elem)
    i = elem.find('/')
    if i==0:
        i = elem.find('/', 1)
        if i==1:
            i = elem.find('/', 2)

    att_ = attribute
    while (i!=-1) and (i<l):
        att_ = '_'+att_
        t = my_find_subelement(att_, driver, elem[:i])
        if t is None:
            return t
        i = elem.find('/', i+1)

    return my_find_subelement(attribute, driver, elem)

def my_get_text(elem):
    if (elem is None) or not (hasattr(elem, 'text')):
        return "N/A"
    else:
        return str(elem.text)


def my_find_and_get(attribute, driver, elem0, find0, sub0):
    s0 = find0.replace("§", elem0)
    t = my_find_element('_'+attribute, driver, s0)
    if t is None:
        return None
    else:
        return my_find_element(attribute, driver, s0+sub0)

find0 = "//tr[@class='a-spacing-small §']"
sub0  = "/td[2]/span"

find1 = "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and normalize-space()='§']"
sub1 = "/../td[1]"

find2 = "//th[contains(@class,'comparison_table_first_col')]/span[normalize-space()='§']"
sub2 = "/../../td[1]"

print("crawl")

start = time.time()

profile_path = r'%AppData%\Mozilla\Firefox\Profiles\y1uqp5mi.default'
options=Options()
options.set_preference('profile', profile_path)
service = Service(GECKO_PATH)

driver = Firefox(service=service, options=options)

for i in range(0, len(start_urls)):
    print_xpath = (i == 0)
    url = start_urls[i]
    print("\n"+str(i+1)+": "+url)

    cont = True

    try:
        driver.get(url)

    except Exception as e:
        print("Error retriving url. The error is: ", e)
        exit(-1)
        cont = False

    if cont:
        with open("D:/Univ/ID/HW4/"+url[25:35]+".html", "w", encoding='utf-8') as f:
            f.write(driver.page_source)

        try:
            ccrl = driver.find_elements("xpath", "//a[@id='sp-cc-rejectall-link']")

            if len(ccrl)>0:
                ccrl[0].click()
                time.sleep(1)

        except Exception as e:
            print("No rejectall. The error is: ", e)
            pass

        try:
            driver.find_element("xpath", "//div[@id='poToggleButton']/a").click()
        except Exception as e:
            print("No toggle button. The error is: ", e)
            pass

        nome = my_find_and_get("Nome", driver, "po-model_name", find0, sub0)
        prezzo = my_find_element("Prezzo", driver, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")

        brand = my_find_and_get("Marca", driver, "po-brand", find0, sub0)
        fattoreDiForma = my_find_and_get("Fattore di forma", driver, "po-form_factor", find0, sub0)
        risoluzione = my_find_and_get("Risoluzione fissa efficace", driver, "po-effective_still_resolution", find0, sub0)

        id_articolo = my_find_and_get("ID articolo", driver, "Numero modello articolo", find1, sub1)
        dimensioni = my_find_and_get("Dimensioni prodotto", driver, "Dimensioni prodotto", find1, sub1)

        schermo = my_find_and_get("Dimensione schermo", driver, "Dimensione schermo", find2, sub2)
        
        
        colArticolo = 1
        while ((colArticolo<10) and (driver.find_element("xpath", "//tr[@class='comparison_table_image_row']/th["+str(colArticolo)+"]/div[2]/div/span[1]") == None)):
            colArticolo += 1
        
        venduto_da = my_find_and_get("Venduto da", driver, "Venduto da", find2, "/../../td["+str(colArticolo)+"]")

        sh = my_get_text(prezzo)

        # print complete elements
        print('Nome: '+my_get_text(nome))
        print('Prezzo: '+"".join(c if ord(c)!= 10 else ',' for c in sh))
        print('Marca: '+my_get_text(brand))
        print('Fattore di forma: '+my_get_text(fattoreDiForma))
        print('Risoluzione fissa efficace: '+my_get_text(risoluzione))
        print('ID articolo: '+my_get_text(id_articolo))
        print('Dimensioni prodotto: '+my_get_text(dimensioni))
        print('Dimensione schermo: '+my_get_text(schermo).strip())
        print('Venduto da: '+my_get_text(venduto_da).strip())
        
        if (colArticolo != 1):
            print("\nColonna articolo: "+str(colArticolo)+"\n")

driver.quit()

end = time.time()
t = str(end-start)
p = t.find('.')
if (p == -1):
    p = t.find(',')
if (p != -1) and (len(t)>=p+4):
    t = t[:p+4]
print("\n\nSpent "+t+" sec, crawling\n")

