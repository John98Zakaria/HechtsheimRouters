import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def usereingabe(arr):
    try:
        while (True):
            eingabe = int(input())
            if (eingabe in arr):
                return eingabe
            print("Falsche Eingabe")
    except ValueError:
        print("Falsche Eingabe")
        return usereingabe(arr)


def has_pswrd_screen():
    global driver
    try:
        pswrd_feld = driver.find_element_by_xpath('//*[@id="uiPass"]')
        return True
        print("Dieses Router hat ein Password feld")
        print("1 Fur Passwort Eingabe")
        print("2 Fur Zurucksetzen Eingabe")

        wahl = usereingabe([1, 2])
        if (wahl == 1):
            pswrd = input("Passworteingeben")
            pswrd_feld.send_keys(pswrd, Keys.ENTER)

            driver.find_element_by_xpath('//*[@id="tProdukt"]/tbody/tr[1]/td[1]')
        if (wahl == 2):
            driver.find_element_by_xpath('//*[@id="uiMainForm"]/p/a').click()
            driver.find_element_by_xpath('//*[@id="btn_form_foot"]/button[2]').click()


    except:
        return False


def pswrd_eingabe():
    print("Dieses Router hat ein Password feld")

    pswrd = input("Passworteingeben")
    # pswrd_feld.send_keys(pswrd, Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="tProdukt"]/tbody/tr[1]/td[1]')


def runner(xPaths):
    for i in xPaths:
        driver.find_element_by_xpath(i).click()


def post_reset():
    try:
        xPaths = ['//*[@id="uiActive"]', '//*[@id="uiNoReminder"]',
                  '//*[@id="uiApply"]']  # Password fur  router ignorieren
        runner(xPaths)
    except:
        ansicht()


def reset_when_pass():
    try:
        xPaths = ['//*[@id="uiMainForm"]/p/a', '//*[@id="btn_form_foot"]/button[1]']  # Zurucksetzen beim Login
        runner(xPaths)
        for i in range(1, 150):
            print(f"{121 - i} Sekunden bis zum Neustart ")
            time.sleep(1)
        driver.refresh()
        bigframe = driver.find_element_by_id("frame_content")

        driver.switch_to_frame(bigframe)

        post_reset()

    except:
        pass


def reset_when_nopass():
    xPaths = ['//*[@id="menucontent"]/div[2]/ul/li[6]/a', '//*[@id="menucontent"]/div[2]/ul/li[6]/ul/li[9]/a',
              '//*[@id="page_content"]/ul/li[2]/a', '//*[@id="btn_form_foot"]/button[1]']
    runner(xPaths)

    driver.switch_to.alert.accept()
    for i in range(1, 121):
        print(f"{121 - i} Sekunden bis zum Neustart ")
        time.sleep(1)
    driver.refresh()
    bigframe = driver.find_element_by_id("frame_content")

    driver.switch_to_frame(bigframe)

    post_reset()


def ansicht():
    xPaths = ['//*[@id="sub_menu_head"]/a[2]/span', '//*[@id="uiMode"]', '//*[@id="btn_form_foot"]/button[1]']
    runner(xPaths)


def einrichten():
    xPaths = ['//*[@id="menucontent"]/div[2]/ul/li[2]/a', '//*[@id="menucontent"]/div[2]/ul/li[2]/ul/li[2]/a',
              '//*[@id="uiViewDslType10"]', '//*[@id="uiViewDslType2"]', '//*[@id="uiViewDslIpEncaps1"]',
              '//*[@id="uiView_RunConnectTest"]', '//*[@id="buttonSave"]'
              ]
    runner(xPaths)
    MAC = driver.find_element_by_xpath('//*[@id="uiDslIp"]/div/div/div/div/div/p[9]').text
    print(MAC)


def wlan_setup(name):
    driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[5]/a').click()
    wlan_Name = driver.find_element_by_xpath('//*[@id="uiView_SSID"]')
    wlan_Name.clear()
    wlan_Name.send_keys(name)
    driver.find_element_by_xpath('//*[@id="buttonSave"]').click()

    driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[5]/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="uiManuChannel"]').click()
    dropdown = driver.find_element_by_xpath('//*[@id="uiChannels"]')
    random_channel = random.randint(1, 11)
    random_channel = 'Kanal ' + str(random_channel)
    for i in dropdown.find_elements_by_tag_name("option"):
        if (i.text == random_channel):
            i.click()

    driver.find_element_by_xpath('//*[@id="content"]/div[5]/div/div/div/div/div/input[1]').click()

    print("WlanPassword wie auf der Ruckseite")


try:

    driver.get("http://192.168.178.1")
    time.sleep(5)
    bigframe = driver.find_element_by_id("frame_content")

    driver.switch_to_frame(bigframe)
    wlan_name = input("Geben sie den WLAN Name ein")
    pswrd_exist = has_pswrd_screen()
    try:
        if (has_pswrd_screen()):
            reset_when_pass()
        else:
            reset_when_nopass()
    except:
        print("Skip Reset")

    try:
        post_reset()
    except:
        print("Skip Postreset")

    try:
        ansicht()
    except:
        print("Ansicht Skip")

    try:
        einrichten()
    except:
        print("Einrichten Skip")

    try:
        wlan_setup(wlan_name)
    except:
        print("WLan setup Failed")
    # # driver.find_element_by_xpath('//*[@id="uiPass"]').send_keys(pswrd, Keys.ENTER)
    #
    # driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[2]/a').click()
    #
    # driver.find_element_by_xpath('//*[@id="menucontent"]/div[2]/ul/li[2]/ul/li[2]/a').click()
    #
    # # MAC = driver.find_elements_by_xpath("//*[contains(text(), 'MAC-Adresse')]").text
    # # MAC = driver.find_element_by_class_name('ml25').text
    # MAC = driver.find_element_by_xpath('//*[@id="uiDslIp"]/div/div/div/div/div/p[9]').text
    # print("Pass MC ")
    #
    # print(MAC)
    # # //*[@id="menucontent"]/div[2]/ul/li[2]/ul/li[2]/a
    # # "//*[@id="uiPass"]"
    # # //*[@id="uiPass"]
    # print("Pass")
except:
    print("Error not found")

finally:
    driver.close()
