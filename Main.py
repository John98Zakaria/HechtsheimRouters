pswrd = "Johnstk98"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




try:

    driver = webdriver.Chrome()

    driver.get("http://192.168.178.1")

    bigframe = driver.find_element_by_id("frame_content")

    driver.switch_to_frame(bigframe)

    driver.find_element_by_xpath('//*[@id="uiPass"]').send_keys(pswrd, Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[2]/a').click()

    driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[2]/ul/li[2]/a').click()

    # MAC = driver.find_elements_by_xpath("//*[contains(text(), 'MAC-Adresse')]").text
    # MAC = driver.find_element_by_class_name('ml25').text
    MAC = driver.find_element_by_xpath('//*[@id="uiDslIp"]/div/div/div/div/div/p[9]').text
    print("Pass MC ")

    print(MAC)
    # //*[@id="menucontent"]/div[2]/ul/li[2]/ul/li[2]/a
    # "//*[@id="uiPass"]"
    # //*[@id="uiPass"]
    print("Pass")
except:
    print("Error not found")

finally:
    driver.close()
