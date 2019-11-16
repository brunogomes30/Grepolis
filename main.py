from threading import Timer
from selenium import webdriver
from getpass import getpass
import selenium
import time
from random import randint
   
#username = input("Insert Username.")
#password = getpass.getpass("Insert Password.")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
username = input("Username: ")
password =  getpass("Password(Não irá ser vísivel): ")
def grepolis_bot():
    global username, password
    driver = webdriver.Chrome("webdriver\\chromedriver.exe") #options=chrome_options
    driver.get("https://pt.grepolis.com")
    
    #list = ["#farm_town_258","#farm_town_254","#farm_town_255","#farm_town_256"]
    #farm_town = "#farm_town_254"
    
    try:
        #driver = webdriver.Chrome("webdriver\\chromedriver.exe") #options=chrome_options
        #driver.get("https://pt.grepolis.com")
        username_box = driver.find_element_by_css_selector("#login_userid")
        username_box.send_keys(username)
        password_box = driver.find_element_by_css_selector("#login_password")
        password_box.send_keys(password)
        password_box.submit()
        time.sleep(2)
        world_box = driver.find_element_by_css_selector(".world_name.type_wonder")
        world_box.click()
        time.sleep(2)
        #driver.find_element_by_css_selector(".pointer").click()
        driver.find_element_by_css_selector(".island_view.option").click()
        time.sleep(2)
        """for i in list:
            driver.find_element_by_css_selector(i).click()
            time.sleep(2)
            driver.find_element_by_css_selector(".card_click_area").click()
            time.sleep(2)
            driver.find_element_by_css_selector(".btn_wnd.close").click()
            time.sleep(2)
        """
        farm_town = driver.find_elements_by_css_selector(".owned.farm_town")[0]
        farm_town.click()
        time.sleep(2)
        
        farm_name = driver.find_element_by_css_selector(".village_info > .village_name").text
        try:
            driver.find_element_by_css_selector(".action_card:nth-child(1) > .card_click_area").click()
        except:
            pass
        driver.find_element_by_css_selector(".btn_next.next_prev").click()
        time.sleep(2)
        #Enquanto não tiver percorrido as aldeias todas, recolhe os recursos
        while(driver.find_element_by_css_selector(".village_info > .village_name").text != farm_name):
            time.sleep(1)
            try:
                driver.find_element_by_css_selector(".action_card:nth-child(1) > .card_click_area").click()
            except:
                pass
            driver.find_element_by_css_selector(".btn_next.next_prev").click()
        
        driver.close() 
    except Exception as e:
        print(str(e))
        driver.close()
    waiting_time = randint(290,315)
    t = Timer(waiting_time, grepolis_bot)
    t.start()

grepolis_bot()