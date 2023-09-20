# Python program HW4 Ingegneria dei Dati, es. 2

# Sorgenti scelte
# "basketball.realgm.com"
# "basketball-reference.com"
# "hoopshype.com"
# "nba.com"
# "nbadraft.net"
#
# Sorgente non stampata: devono essere 5 sorgenti.
# "nbcsports.com"


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

# https://bleacherreport.com/articles/6159-five-basketball-websites-you-cant-live-without

# bb=$x("//button[@class='Button__StyledButton-a1qza5-0 goJrkv']")
# bb[0].click()
# cp = $x("//input[@type='checkbox']")
# for (let step = 0; step < cp.length; step++) {
#   if (cp[step].checked) {
#     cp[step].checked = false;
#   }
# }
# ca = $x("//div[@class='Card__CardBody-sc-1s2p2gv-2 a__sc-3vtlsk-2 cXghWF ccdgWR']")
# ca[0].scrollTo(0, 0);
# for (let step = 0; step < ca[0].scrollHeight; step+=ca[0].scrollHeight/20) {
#   ca[0].scrollTo(0, step);
#   cp = $x("//input[@type='checkbox']")
#   for (let stepp = 0; stepp < cp.length; stepp++) {
#     if (cp[stepp].checked) {
#       cp[stepp].checked = false;
#     }
#   }
# }

# hcl = $x("//div[@class='half-column-left']/h2")
p11 = "https://basketball.realgm.com/player/Danilo-Gallinari/Summary/761"
p12 = "https://basketball.realgm.com/player/Rudy-Gobert/Summary/25858"
p13 = "https://basketball.realgm.com/player/Tyrese-Haliburton/Summary/132168"
p14 = "https://basketball.realgm.com/player/Jaren-Jackson-Jr/Summary/88806"
p15 = "https://basketball.realgm.com/player/Joel-Embiid/Summary/49880"

# $x("//span[text()='DISAGREE']/..")[0].click()
# $x("//button[@id='meta_more_button']")[0].click()
p21 = "https://www.basketball-reference.com/players/g/gallida01.html"
p22 = "https://www.basketball-reference.com/players/z/zubaciv01.html"
p23 = "https://www.basketball-reference.com/players/r/ryanma01.html"
p24 = "https://www.basketball-reference.com/players/a/aytonde01.html"
p25 = "https://www.basketball-reference.com/players/m/manntr01.html"

p31 = "https://hoopshype.com/player/danilo-gallinari/"
p32 = "https://hoopshype.com/player/jaden-ivey/"
p33 = "https://hoopshype.com/player/donovan-mitchell/"
p34 = "https://hoopshype.com/player/dennis-smith/"
p35 = "https://hoopshype.com/player/ivica-zubac/"

# //button[@id="onetrust-reject-all-handler"]
p41 = "https://www.nba.com/player/201568/danilo-gallinari"
p42 = "https://www.nba.com/player/1629652/luguentz-dort"
p43 = "https://www.nba.com/player/1630206/jay-scrubb"
p44 = "https://www.nba.com/player/1628369/jayson-tatum"
p45 = "https://www.nba.com/player/1629048/goga-bitadze/bio"

p51 = "https://www.nbadraft.net/players/danilo-gallinari/"
p52 = "https://www.nbadraft.net/players/jimmy-butler/"
p53 = "https://www.nbadraft.net/players/adem-bona/"
p54 = "https://www.nbadraft.net/players/gg-jackson/"
p55 = "https://www.nbadraft.net/players/victor-wembanyama/"

# //button[@id="onetrust-accept-btn-handler"]
p61 = "https://www.nbcsports.com/basketball/nba/player/29378/danilo-gallinari"
p62 = "https://www.nbcsports.com/basketball/nba/player/51073/luguentz-dort"
p63 = "https://www.nbcsports.com/basketball/nba/player/29574/john-wall"
p64 = "https://www.nbcsports.com/basketball/nba/player/30438/luke-kennard"
p65 = "https://www.nbcsports.com/basketball/nba/player/50968/rj-barrett"

s1 = [p11, p12, p13, p14, p15]
s2 = [p21, p22, p23, p24, p25]
s3 = [p31, p32, p33, p34, p35]
s4 = [p41, p42, p43, p44, p45]
s5 = [p51, p52, p53, p54, p55]
s6 = [p61, p62, p63, p64, p65]

start_urls = [
    s1,
    s2,
    s3,
    s4,
    s5
]

def my_find_subelement(driver, elem):
    t = None
    try:
        t = driver.find_element("xpath", elem)
    except Exception as e:
        print("Cannot find element: ", elem)
        pass
    return t

def my_find_element(driver, elem):
    l = len(elem)
    i = elem.find('/')
    if i==0:
        i = elem.find('/', 1)
        if i==1:
            i = elem.find('/', 2)

    while (i!=-1) and (i<l):
        t = my_find_subelement(driver, elem[:i])
        if t is None:
            return t
        i = elem.find('/', i+1)

    return my_find_subelement(driver, elem)

def my_get_text(elem):
    if (elem is None) or not (hasattr(elem, 'text')):
        return "N/A"
    else:
        return str(elem.text)

def my_find_element_text(driver, elem):
    return my_get_text(my_find_element(driver, elem))

def my_find_and_get(driver, elem0, find0, sub0):
    s0 = find0.replace("§", elem0)
    t = my_find_element(driver, s0)
    if t is None:
        return None
    else:
        return my_find_element(driver, s0+sub0)

print("crawl")

start = time.time()

profile_path = r'%AppData%\Mozilla\Firefox\Profiles\y1uqp5mi.default'
options=Options()
options.set_preference('profile', profile_path)
service = Service(GECKO_PATH)

driver = Firefox(service=service, options=options)

for j in range(0, len(start_urls)):
  site_urls = start_urls[j]
  for i in range(0, len(site_urls)):
    url = site_urls[i]
    site = url[url.find('//')+2:url.find('/', url.find('//')+2)]
    if (site.startswith('www.')):
        site = site[4:]

    if i==0:
        print("\nSite: "+site)

    print("\n["+str(j+1)+":"+str(i+1)+"]: "+url)

    driver.get(url)
#    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
#    leaves = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class,'priceToPay')]/span[@class='a-offscreen']")))

    name = "N/A"
    player_number = "N/A"
    teamname = "N/A"
    birthday = "N/A"
    height = "N/A"
    weight = "N/A"

    if site == "basketball.realgm.com":
        teamname = my_find_element_text(driver, "//div/p/strong[contains(.,'Current Team:')]/following-sibling::a")
        name = my_find_element_text(driver, "//li[@class='mobile-menu']/following-sibling::li")
        player_number = my_find_element_text(driver, "//h2[contains(.,'#')]").strip()
        if (player_number.find("#") != -1):
            player_number = player_number.split("#",1)[1]
        birthday = my_find_element_text(driver, "//div/p/strong[contains(.,'Born:')]/following-sibling::a")
        hw = my_find_element_text(driver, "//div/p/strong[contains(.,'Height:')]/..")
        if ((hw.find('Height:') != -1) and (hw.find('Weight:') != -1)):
            height = hw.split("Height:")[1].split("Weight:")[0].strip()
            weight = hw.split("Weight:")[1].strip()

    elif site == "basketball-reference.com":
       time.sleep(2)
       butt = driver.find_elements("xpath", "//span[text()='DISAGREE']/..")
       if len(butt)>0:
          butt[0].click()
          time.sleep(1)
       butt = driver.find_elements("xpath", "//button[@id='meta_more_button']")
       if len(butt)>0:
          butt[0].click()
          time.sleep(1)
       
       name =  my_find_element_text(driver, "//div[@id='meta']/div/h1/span")
       player_number = my_find_element_text(driver, "//div[@class='uni_holder bbr']")
       #print(player_number)
       player_number = player_number.rsplit(" ", 1)[-1]
       
       ll=0
       while ll<10:
         teamnames = driver.find_elements("xpath", "//table[starts-with(@id,'contracts')]/tbody/tr/td")
         if len(teamnames)>0:
            teamname = str(teamnames[0].text)
            break
         else:
            ll = ll+1
            print("Wait #"+str(ll)+" for 'contracts'")
            time.sleep(1)
       """
       ll=0
       while ll<10:
         gshm = driver.find_elements("xpath", "//li[@class='groupstuff hasmore']/span")
         if len(gshm)>0:
         	teamname = str(gshm[0]).text
         	break
         else:
         	ll = ll+1
         	print("Wait #"+str(ll)+" for 'groupstuff hasmore'")
         	time.sleep(1)
       """
       birthday = my_find_element_text(driver, "//span[@id='necro-birth']")
       info = my_find_element_text(driver, "//span[@id='necro-birth']/../preceding-sibling::p[1]")
       # print(info)
       height = info.split(", ",1)[0]
       weight = info.split(", ",1)[1] # .split(" (",1)[0]

    elif site == "hoopshype.com":
        butt = driver.find_elements("xpath", "//button[@id='onetrust-reject-all-handler']")
        if len(butt) > 0:
            butt[0].click()
            time.sleep(1)
        teamname = my_find_element_text(driver, "//div[@class='player-team']")
        name = my_find_element_text(driver, "//div[@class='player-fullname']")
        player_number = my_find_element_text(driver, "//div[@class='player-jersey']")

        info = driver.find_elements("xpath", "//span[@class='player-bio-text-line']")
        #print("Len info: "+str(len(info))+" - "+str(dir(info[0])))
        for i in range(len(info)):
            s = str(info[i].get_attribute("textContent"))
            lv = s.split(":")
            if len(lv)>1:
                v = lv[1].strip()
                if (s.find("Born:") != -1):
                    birthday = v
                elif (s.find("Height:") != -1):
                    height = v
                elif (s.find("Weight:") != -1):
                    weight = v

    elif site == "nba.com":
        butt = driver.find_elements("xpath", "//button[@id='onetrust-reject-all-handler']")
        if len(butt) > 0:
            butt[0].click()
            time.sleep(1)
        name = my_find_element_text(driver, "//div[@class='PlayerSummary_mainInnerBio__JQkoj']/p[2]") + " "
        name += my_find_element_text(driver, "//div[@class='PlayerSummary_mainInnerBio__JQkoj']/p[3]")
        info = my_find_element_text(driver, "//div[@class='PlayerSummary_mainInnerBio__JQkoj']/p[1]")
        if info.find(" | ") != -1:
            player_number = info.split(" | ", 2)[1]
            teamname = info.split(" | ", 2)[0]
        birthday = my_find_element_text(driver,
                                        "//p[@class='PlayerSummary_playerInfoLabel__hb5fs' and text()='BIRTHDATE']/following-sibling::p")
        height = my_find_element_text(driver,
                                      "//p[@class='PlayerSummary_playerInfoLabel__hb5fs' and text()='HEIGHT']/following-sibling::p")
        weight = my_find_element_text(driver,
                                      "//p[@class='PlayerSummary_playerInfoLabel__hb5fs' and text()='WEIGHT']/following-sibling::p")

    elif site == "nbadraft.net":
       ll = 0;
       info = ""
       while ll<10:
         info = my_find_element_text(driver, "//h1[@class='player-name']")
         if len(info)>0:
            break;
         else:
            time.sleep(1)
            ll = ll+1
       #print("Info: " + info)
       if " - " in info:
           name = info.split(" - ",1)[1]
           player_number = info.split(" - ",1)[0]
       else:
           name = info
           player_number = "N/A"
       teamname = "N/A" # my_find_element_text(driver, "//span[@class='team-title']")
       birthday = my_find_element_text(driver, "//div[@class='div-table-cell attribute-name' and normalize-space()='Birthday']/../div[@class='div-table-cell attribute-value']")
       height = my_find_element_text(driver, "//span[@class='player-height']")
       weight = my_find_element_text(driver, "//span[@class='player-weight']")

    elif site == "nbcsports.com":
       # Sito cambiato: le espressioni NON funzionano più!
       # Cannot find element:  //span[@class='player-highlight__player-first']

       butt = driver.find_elements("xpath", "//button[@id='onetrust-accept-btn-handler']")
       if len(butt)>0:
          butt[0].click()
          time.sleep(1)

       # get elements
       name = my_find_element_text(driver, "//span[@class='player-highlight__player-first']") + " ";
       name += my_find_element_text(driver, "//span[@class='player-highlight__player-last']/span[@class='player-highlight__player-last']")

       player_number = my_find_element_text(driver, "//div[@class='player-highlight__player-number']")
       teamname = my_find_element_text(driver, "//div[@class='player-highlight__team-name']")
       birthday = my_find_element_text(driver, "//table[@class='player-details']/tbody/tr[1]/td[2]")
       height = my_find_element_text(driver, "//table[@class='player-details']/tbody/tr[2]/td[2]").split(" / ",1)[0]
       weight = my_find_element_text(driver, "//table[@class='player-details']/tbody/tr[2]/td[2]").split(" / ",1)[1]


    # print complete elements
    print('Name:      '+name)
    print('Number:    '+player_number.replace("#",""))
    print('Team Name: '+teamname)
    print('Birthdate: '+birthday)
    print('Height:    '+height)
    print('Weight:    '+weight)
    

end = time.time()
t = str(end-start)
p = t.find('.')
if (p == -1):
    p = t.find(',')
if (p != -1) and (len(t)>=p+4):
    t = t[:p+4]
print("Spent "+t+" sec, crawling\n")

driver.quit()
