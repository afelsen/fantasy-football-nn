import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome(executable_path='/Users/adielfelsen/Downloads/chromedriver')
    driver.get("https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=single&draft=0&year_min=1980&year_max=2018&season_start=1&season_end=-1&league_id=NFL&pos%5B%5D=te&draft_year_min=1936&draft_year_max=2014&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos%5B%5D=qb&draft_pos%5B%5D=rb&draft_pos%5B%5D=wr&draft_pos%5B%5D=te&draft_pos%5B%5D=e&draft_pos%5B%5D=t&draft_pos%5B%5D=g&draft_pos%5B%5D=c&draft_pos%5B%5D=ol&draft_pos%5B%5D=dt&draft_pos%5B%5D=de&draft_pos%5B%5D=dl&draft_pos%5B%5D=ilb&draft_pos%5B%5D=olb&draft_pos%5B%5D=lb&draft_pos%5B%5D=cb&draft_pos%5B%5D=s&draft_pos%5B%5D=db&draft_pos%5B%5D=k&draft_pos%5B%5D=p&c5val=1.0&order_by=fantasy_points_per_game")

    fo = open("TEdata.csv","w")
    fo.write("")
    fo.close()


    fo = open("TEdata.csv","a")
    for j in range(100,100000,100):

        element_to_hover_over = driver.find_elements_by_class_name("hasmore")[-1]

        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()


        a = driver.find_elements(By.XPATH, '//button')
        for i in a:
            if i.get_attribute("tip") == "Export table as <br>suitable for use with Excel":
                break
        i.click()

        csv = driver.find_element_by_id("csv_results")
        print(csv.text)
        fo.write(csv.text)
        fo.write("\n")

        a = driver.find_elements(By.XPATH, '//a')
        for i in a:
            if i.get_attribute("class") == "button2 next":
                break
        i.click()



        # driver.get("https://www.pro-football-reference.com/play-index/psl_finder.cgi?request=1&match=single&draft=0&year_min=1980&year_max=2018&season_start=1&season_end=-1&league_id=NFL&pos%5B%5D=qb&draft_year_min=1936&draft_year_max=2014&draft_slot_min=1&draft_slot_max=500&draft_pick_in_round=pick_overall&conference=any&draft_pos%5B%5D=qb&draft_pos%5B%5D=rb&draft_pos%5B%5D=wr&draft_pos%5B%5D=te&draft_pos%5B%5D=e&draft_pos%5B%5D=t&draft_pos%5B%5D=g&draft_pos%5B%5D=c&draft_pos%5B%5D=ol&draft_pos%5B%5D=dt&draft_pos%5B%5D=de&draft_pos%5B%5D=dl&draft_pos%5B%5D=ilb&draft_pos%5B%5D=olb&draft_pos%5B%5D=lb&draft_pos%5B%5D=cb&draft_pos%5B%5D=s&draft_pos%5B%5D=db&draft_pos%5B%5D=k&draft_pos%5B%5D=p&c5val=1.0&order_by=fantasy_points_per_game&offset=" + str(j))
    fo.close()

main()
