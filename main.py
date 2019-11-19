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
    
    
    try:
        username_box = driver.find_element_by_css_selector("#login_userid")
        username_box.send_keys(username)
        password_box = driver.find_element_by_css_selector("#login_password")
        password_box.send_keys(password)
        password_box.submit()
        time.sleep(2)
        world_box = driver.find_element_by_css_selector(".world_name.type_wonder")
        world_box.click()
        time.sleep(2)
        driver.find_element_by_css_selector(".town_name_area > .town_groups_dropdown > .js-button-caption").click()
        time.sleep(2)
        cities = driver.find_elements_by_css_selector(".group_towns > div > .town_group_town")
        driver.find_element_by_css_selector(".town_name_area > .town_groups_dropdown > .js-button-caption").click()
        n_cities = len(cities)
        print(cities)
        for i in range(n_cities):
            try:
                #Select city
                driver.find_element_by_css_selector(".town_name_area > .town_groups_dropdown > .js-button-caption").click()
                time.sleep(2)
                
                cities = driver.find_elements_by_css_selector(".group_towns > div > .town_group_town")[i].click()
                #Recompensa diaria
                if(len(driver.find_elements_by_css_selector(".daily_login_wrapper")) > 0 ):
                    driver.find_element_by_css_selector(".wnd_border_t > .buttons_container > .close").click()
        		#Close Window
        		
                try:
                    driver.find_element_by_css_selector(".buttons_container > .close").click()
                except:
                    pass
                #Go to city overview
                driver.find_element_by_css_selector(".city_overview").click()
                time.sleep(1)
                
                #Autocompletar edificio se disponivel
                if(len(driver.find_elements_by_css_selector(".type_instant_buy.type_free")) > 0 ):
                    driver.find_element_by_css_selector(".type_instant_buy.type_free > .js-caption").click()
                arrows = driver.find_elements_by_css_selector(".construction_overlay_frame_instant_buy")
                for element in arrows:
                    driver.execute_script("arguments[0].style.visibility='hidden'", element)
                
                
                #Ver recursos
                wood =  int(driver.find_element_by_css_selector(".ui_resources_bar > .wood > .wrapper > .amount").text)
                stone =  int(driver.find_element_by_css_selector(".ui_resources_bar > .stone > .wrapper > .amount").text)
                silver =  int(driver.find_element_by_css_selector(".ui_resources_bar > .iron > .wrapper > .amount").text)
                population =  int(driver.find_element_by_css_selector(".ui_resources_bar > .population > .wrapper > .amount").text)
                storage = 7321
                if wood > storage*0.9 or stone > storage*0.9 or silver > storage*0.9:
                    
                    if population <= 5:
                        #Level Farm
                        if(len(driver.find_elements_by_css_selector(".construction_queue_sprite > .farm")) > 0):
                            print("Already leveling up farm")
                        else:
                            driver.find_element_by_id("building_main_area_main").click()
                            time.sleep(1.5)
                            try:
                                driver.find_element_by_css_selector("#building_main_farm > .building > .build_up").click()
                            except Exception:
                                pass
                            driver.find_element_by_css_selector(".ui-dialog-titlebar-close").click()
                    else:
                        #Recruit Units
                        
                        #driver.find_element_by_css_selector("div[data-id='barracks']").click()
                        driver.find_element_by_id("building_main_area_barracks").click() #ui_box > div.ui_city_overview.night > div > div > div.viewport.js-city-construction-overlay-viewport > div > div.construction_overlay_frame_instant_buy.barracks.single > div.arrow
                        time.sleep(1.5)
                        unit_count = driver.find_element_by_id("unit_order_input")
                        unit_count.clear()
                        unit_count.send_keys("2")
                        #driver.find_element_by_id("unit_order_confirm").click()
                        driver.find_element_by_css_selector(".ui-dialog-titlebar-close").click()
                        
                    
                driver.find_element_by_css_selector(".island_view.option").click()
                time.sleep(2)
                
                driver.find_element_by_css_selector(".btn_jump_to_town").click()
                farm_town = driver.find_elements_by_css_selector(".owned.farm_town")[0]
                farm_town.click()
                time.sleep(2)
                
                farm_name = driver.find_element_by_css_selector(".village_info > .village_name").text
                try:
                    driver.find_element_by_css_selector(".action_card:nth-child(1) > .card_click_area").click()
                    time.sleep(1)
                except:
                    pass
                if(len(driver.find_elements_by_css_selector(".btn_confirm > .caption")) >0):
                    driver.find_element_by_css_selector(".btn_confirm > .caption.js-caption").click()
                    time.sleep(1)
                driver.find_element_by_css_selector(".btn_next.next_prev").click()
                time.sleep(2)
                #Enquanto não tiver percorrido as aldeias todas, recolhe os recursos
                while(driver.find_element_by_css_selector(".village_info > .village_name").text != farm_name):
                    time.sleep(2)
                    try:
                        driver.find_element_by_css_selector(".action_card:nth-child(1) > .card_click_area").click()
                        time.sleep(1)
                    except:
                        pass
                    if(len(driver.find_elements_by_css_selector(".btn_confirm > .caption.js-caption")) >0):
                        driver.find_element_by_css_selector(".btn_confirm > .caption.js-caption").click()
                        time.sleep(1)
                    driver.find_element_by_css_selector(".btn_next.next_prev").click()
                
                
            except Exception as e:
                print(str(e))
                continue
    except Exception as e:
        print(str(e))
    driver.close() 
    waiting_time = randint(290,315)
    t = Timer(waiting_time, grepolis_bot)
    t.start()

grepolis_bot()