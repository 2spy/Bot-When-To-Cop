import json
import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
import traceback

url = 'https://www.whentocop.fr/drops'
reponse = requests.get(url)



soup = BeautifulSoup(reponse.text, 'lxml')
post = soup.find('div', {"class": "infinite-scroll-component"})
allurl = soup.find_all('a',{'class':'DropCard__CardContainer-sc-1f2e4y6-0'})
x = post.findAll('div')
z = post.findAll('a')

dates = ""

modele = []


counter = 0
for v in range(len(x)):
    for row in x[v]:
        datesrow= row.findAll('p', {'class': "DropGroup__HeadDropDate-sc-fylop7-1"})
        if len(datesrow) != 0:
            dates = datesrow[0].text
        modelesrow = row.findAll('h4')
        pairesrow = row.findAll('h3')
        typesofrow = row.findAll('p')
        imagesofrow = row.findAll('img', {'class':'image'})

        try:
            typesofrow.pop(str(dates))
        except:
            pass
        for i in range(len(modelesrow)):
            if pairesrow[i].text in modele:
                pass
            else:
                reponse2 = requests.get(f"https://www.whentocop.fr{allurl[counter]['href']}")
                print(f"https://www.whentocop.fr{allurl[counter]['href']}")

                soup2 = BeautifulSoup(reponse2.text, 'lxml')

                post2 = soup2.findAll("p",{'class':'DropInfo__Text-sc-1okpqbg-4'})
                post3 = soup2.findAll('p',{'class':'slug__InfosTextImportant-sc-7auole-15'})
                post4 = soup2.findAll('a',{'class':'Retailer__Cta-sc-l6npmq-7'})
                post5 = soup2.findAll('div',{'class':'Retailer__RetailerImgContainer-sc-l6npmq-4'})
                post6 = soup2.findAll('p',{'class':'important'})
                post7 = soup2.findAll('img', {'class': 'image'})
                lessites = []
                lesliens = []
                for rows in post5:
                    v = rows.findAll('img')
                    for ele in v:
                        if ele['alt'] in lessites:
                            pass
                        else:
                            lessites.append(ele['alt'])

                for rows in post4:
                    lesliens.append(rows['href'])
                modele.append(pairesrow[i].text)
                with open('paires.json','r') as pairesjson:
                    paires = json.load(pairesjson)

                if pairesrow[i].text in paires:
                    pass
                else:
                    try:
                        with open('paires.json','w+') as pairesjson:
                            paires[pairesrow[i].text] = {}
                            paires[pairesrow[i].text]['paire'] = f"{modelesrow[i].text}"
                            paires[pairesrow[i].text]['url'] = f"https://www.whentocop.fr{allurl[counter]['href']}"
                            paires[pairesrow[i].text]['resell-type'] = f"{typesofrow[i].text}"
                            try:
                                paires[pairesrow[i].text]['retails-prix'] = f"{post2[3].text}"
                            except:
                                paires[pairesrow[i].text]['date'] = "None"
                            try:
                                paires[pairesrow[i].text]['date'] = f"{post2[1].text} {post2[2].text}"
                            except:
                                paires[pairesrow[i].text]['date'] = "None"
                            try:
                                paires[pairesrow[i].text]['resell-prix'] = f"{post3[0].text}"
                            except:
                                paires[pairesrow[i].text]['resell-prix'] = "None"
                            try:
                                paires[pairesrow[i].text]['image'] = post7[1]['src']
                            except:
                                paires[pairesrow[i].text]['image'] = "None"
                            try:
                                paires[pairesrow[i].text]['sites'] = lessites
                            except:
                                paires[pairesrow[i].text]['sites'] = "None"
                            try:
                                paires[pairesrow[i].text]['liens-achat'] = lesliens
                            except:
                                paires[pairesrow[i].text]['liens-achat'] = "None"
                            try:
                                paires[pairesrow[i].text]["id"] = post6[0].text
                            except:
                                paires[pairesrow[i].text]['liens-achat'] = lesliens
                            json.dump(paires, pairesjson, indent=4)
                        counter += 1
                    except Exception as err:
                        print(traceback.print_exc())


# Prochaine MISE à JOUR

#driver = webdriver.Chrome(executable_path=r"C:\Users\yzquu\Documents\despy\whentocop\chromedriver.exe")

#driver.get(url)


#speed = 4
#current_scroll_position = 0
#new_height = 1
#for i in range(6000):
#   current_scroll_position += speed
#    driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
#    new_height = driver.execute_script("return document.body.scrollHeight")
#    print(i)

#html = driver.page_source

