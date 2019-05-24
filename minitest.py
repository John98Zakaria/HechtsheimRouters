import random
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://192.168.178.1")

bigframe = driver.find_element_by_id("frame_content")

driver.switch_to_frame(bigframe)

driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[5]/a').click()
wlan_Name = driver.find_element_by_xpath('//*[@id="uiView_SSID"]')
wlan_Name.clear()
name = input("wifiname")
wlan_Name.send_keys(name)
driver.find_element_by_xpath('//*[@id="buttonSave"]').click()

driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[5]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="uiManuChannel"]').click()
dropdown = driver.find_element_by_xpath('//*[@id="uiChannels"]')
random_channel = random.randint(1, 11)
random_channel = 'Kanal ' + str(random_channel)
for i in dropdown.find_elements_by_tag_name("option"):

    print(i.text)
    if (i.text == random_channel):
        i.click()

driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div/input[1]').click()

print("WlanPassword wie auf der Ruckseite")

time.sleep(10)

driver.close()
