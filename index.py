from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()

driver.get("https://www.olight.com/")

driver.maximize_window()

time.sleep(1)

driver.find_element(By.ID,"ptrek_show_all_button").click()

time.sleep(10)





i =0
while i<25:
    driver.execute_script("window.scrollBy(0, 2500)")
    time.sleep(0.5)
    i+=1

products = driver.find_elements()







time.sleep(50)
driver.quit()
    


urls = []

for product in products :
    url = product.find_element(By.CLASS_NAME,"link-box").get_attribute("href")

    urls.append(url)


urlNo = 0
while urlNo < len(urls):
    driver.get(urls[urlNo])

    time.sleep(2)
    
    try:
        expandItem = driver.find_element(By.CLASS_NAME,"collapse-view-icon")
    except NoSuchElementException:
        print("in except")
        readMoreItem = driver.find_element(By.PARTIAL_LINK_TEXT,"Read more").click()

        time.sleep(5)

        items = driver.find_elements(By.CLASS_NAME,"attributes-item")

        print(urls[urlNo])
        print(len(items))

        for e in items:
            us = e.find_elements(By.CLASS_NAME,"attributes-item-child")


            for u in us:
                evren = u.find_element(By.CLASS_NAME,"attributes-item-name").text
                cagdas = u.find_element(By.CLASS_NAME,"attributes-item-value").text

                print(str(evren) + " / " + str(cagdas))
        

        driver.back()

        time.sleep(5)

        urlNo+=1
    
    if expandItem:
        expandItem.click()
        time.sleep(2)

        items = driver.find_elements(By.CLASS_NAME,"attributes-item")

        print(urls[urlNo])
        print(len(items))

        for e in items:
            us = e.find_elements(By.CLASS_NAME,"attributes-item-child")


            for u in us:
                evren = u.find_element(By.CLASS_NAME,"attributes-item-name").text
                cagdas = u.find_element(By.CLASS_NAME,"attributes-item-value").text

                print(str(evren) + " / " + str(cagdas))
        

        driver.back()

        time.sleep(5)

        urlNo+=1
    

p =0
while p < len(products):
    
    newUrl = products[p].find_element(By.CLASS_NAME,"link-box").get_attribute("href")
    print(newUrl)

    time.sleep(1)

    driver.get(newUrl)

    

    time.sleep(2)

    driver.find_element(By.CLASS_NAME,"collapse-view-icon").click()

    time.sleep(2)


    items = driver.find_elements(By.CLASS_NAME,"attributes-item")


    for e in items:
        us = e.find_elements(By.CLASS_NAME,"attributes-item-child")

        for u in us:
            evren = u.find_element(By.CLASS_NAME,"attributes-item-name").text
            cagdas = u.find_element(By.CLASS_NAME,"attributes-item-value").text

            print(str(evren) + " / " + str(cagdas))



    p+=1
    driver.back()

    time.sleep(2)

    driver.refresh()

    time.sleep(2)


        


