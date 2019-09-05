<<<<<<< HEAD
# -*- coding: UTF-8 -*-
import time

try:   #import webdriver
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
except ImportError:
    print ("Selenium module is not installed...Exiting program.")
    exit(1)


def Check(keywords, text): #check keywords
    for i in keywords:
        if i not in text:
            return False
    return True


def searchCommodity(browser, category, keywords, color):
    print ("[/i][i] Searching Commodity ...")
    browser.get("http://www.supremenewyork.com/shop/all/" + category) #get url
    links = browser.find_elements_by_class_name("name-link")
    i = 0
    while i < len(links):
        if (Check(keywords, links[i].text) & (color in links[i + 1].text)):
            print ("Description : " + links[i].text)
            print ("Color : " + links[i + 1].text)
            links[i].click()
            print ("[/i][i] Item found")
            return True
        i += 2
    print ("[/i][i]Item not found")
    return False


def fillForm(browser):  #input billing infos
    billing_name = "Yize Wu"
    email = "xxxxx@gmail.com"
    tel = "1111111111"
    billing_address = "xxxxxxxxx"
    billing_city = "Los Angeles"
    billing_zip = "11111"
    billing_state = "CA"
    billing_country = "USA"
    nlb = "9999 9999 9999 9999"
    month = "09"
    year = "2019"
    rvv = "888"
    name = browser.find_element_by_name("order[billing_name]").send_keys(billing_name)  #browser find billing infos
    email = browser.find_element_by_name("order[email]").send_keys(email)
    tel = browser.find_element_by_name("order[tel]").send_keys(tel)
    address = browser.find_element_by_name("order[billing_address]").send_keys(billing_address)
    address = browser.find_element_by_name("order[billing_city]").send_keys(billing_city)
    postCode = browser.find_element_by_name("order[billing_zip]").send_keys(billing_zip)
    billing_state = browser.find_element_by_name('order[billing_state]').send_keys(billing_state)
    countrySelect = Select(browser.find_element_by_name("order[billing_country]")).select_by_visible_text(
        billing_country)
    creditCardSelect = browser.find_element_by_name('credit_card[nlb]').send_keys(nlb)
    monthExpirationSelect = Select(browser.find_element_by_name("credit_card[month]")).select_by_visible_text(month)
    yearExpirationSelect = Select(browser.find_element_by_name("credit_card[year]")).select_by_visible_text(year)
    cvv = browser.find_element_by_name("credit_card[rvv]").send_keys(rvv)
    browser.find_element_by_class_name("terms").click()


def main():

    print ("[/i][i] Opening Browser ...")
    browser = webdriver.Chrome() #open browser
    browser.implicitly_wait(5)  # wait5s
    print ("[/i][i] Browser Opened")
    raw_input('[/i][i] Press Enter to buy your item')
    category = "pants"  # item category
    keywords = []
    keywords.append("box")  # item keywords, for example, the key words of a box logo hoodie it box
    color = "white"  # color
    size = 'Medium' #size
    if searchCommodity(browser, category, keywords, color) == False:
        return -1
    if size != "":
        try:
            sizeSelect = Select(browser.find_element_by_id("s"))
            sizeSelect.select_by_visible_text(size)
        except:
            print ("[/i][i]  Item sold out.......")
            return -1
    try:
        browser.find_element_by_name("commit").click()
    except:
        print ("[/i][i] Item sold out")
        return -1
    time.sleep(1)  # sleep 1 sec to avoid error and banned
    browser.find_element_by_class_name("checkout").click()
    print ("Filling in the information")
    fillForm(browser)
    print ("Filled...")
    print ("Prepare to buy a bill.....")
    browser.find_element_by_name("commit").click() #click to make the purchase
    print ("Finshed,congratulations on your favorite things!!!!!") #confirmed


if __name__ == '__main__':
=======
# -*- coding: UTF-8 -*-
import time

try:   #import webdriver
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
except ImportError:
    print ("Selenium module is not installed...Exiting program.")
    exit(1)


def Check(keywords, text): #check keywords
    for i in keywords:
        if i not in text:
            return False
    return True


def searchCommodity(browser, category, keywords, color):
    print ("[/i][i] Searching Commodity ...")
    browser.get("http://www.supremenewyork.com/shop/all/" + category) #get url
    links = browser.find_elements_by_class_name("name-link")
    i = 0
    while i < len(links):
        if (Check(keywords, links[i].text) & (color in links[i + 1].text)):
            print ("Description : " + links[i].text)
            print ("Color : " + links[i + 1].text)
            links[i].click()
            print ("[/i][i] Item found")
            return True
        i += 2
    print ("[/i][i]Item not found")
    return False


def fillForm(browser):  #input billing infos
    billing_name = "Yize Wu"
    email = "xxxxx@gmail.com"
    tel = "1111111111"
    billing_address = "xxxxxxxxx"
    billing_city = "Los Angeles"
    billing_zip = "11111"
    billing_state = "CA"
    billing_country = "USA"
    nlb = "9999 9999 9999 9999"
    month = "09"
    year = "2019"
    rvv = "888"
    name = browser.find_element_by_name("order[billing_name]").send_keys(billing_name)  #browser find billing infos
    email = browser.find_element_by_name("order[email]").send_keys(email)
    tel = browser.find_element_by_name("order[tel]").send_keys(tel)
    address = browser.find_element_by_name("order[billing_address]").send_keys(billing_address)
    address = browser.find_element_by_name("order[billing_city]").send_keys(billing_city)
    postCode = browser.find_element_by_name("order[billing_zip]").send_keys(billing_zip)
    billing_state = browser.find_element_by_name('order[billing_state]').send_keys(billing_state)
    countrySelect = Select(browser.find_element_by_name("order[billing_country]")).select_by_visible_text(
        billing_country)
    creditCardSelect = browser.find_element_by_name('credit_card[nlb]').send_keys(nlb)
    monthExpirationSelect = Select(browser.find_element_by_name("credit_card[month]")).select_by_visible_text(month)
    yearExpirationSelect = Select(browser.find_element_by_name("credit_card[year]")).select_by_visible_text(year)
    cvv = browser.find_element_by_name("credit_card[rvv]").send_keys(rvv)
    browser.find_element_by_class_name("terms").click()


def main():

    print ("[/i][i] Opening Browser ...")
    browser = webdriver.Chrome() #open browser
    browser.implicitly_wait(5)  # wait5s
    print ("[/i][i] Browser Opened")
    raw_input('[/i][i] Press Enter to buy your item')
    category = "pants"  # item category
    keywords = []
    keywords.append("box")  # item keywords, for example, the key words of a box logo hoodie it box
    color = "white"  # color
    size = 'Medium' #size
    if searchCommodity(browser, category, keywords, color) == False:
        return -1
    if size != "":
        try:
            sizeSelect = Select(browser.find_element_by_id("s"))
            sizeSelect.select_by_visible_text(size)
        except:
            print ("[/i][i]  Item sold out.......")
            return -1
    try:
        browser.find_element_by_name("commit").click()
    except:
        print ("[/i][i] Item sold out")
        return -1
    time.sleep(1)  # sleep 1 sec to avoid error and banned
    browser.find_element_by_class_name("checkout").click()
    print ("Filling in the information")
    fillForm(browser)
    print ("Filled...")
    print ("Prepare to buy a bill.....")
    browser.find_element_by_name("commit").click() #click to make the purchase
    print ("Finshed,congratulations on your favorite things!!!!!") #confirmed


if __name__ == '__main__':
>>>>>>> ffa2129e6b31ea9b455a2541f70478727ec852b0
    main()