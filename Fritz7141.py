import random
import sys
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)


def runner(Names):
    global driver
    for i in Names:
        driver.find_element_by_link_text(i).click()


def loaded():
    global driver

    for t in range(200):
        print("Trying to reach router attempt ", t)
        try:
            driver.get("http://192.168.178.1")
            bigframe = driver.find_element_by_id("frame_content")
            driver.switch_to_frame(bigframe)
            return True
        except:
            time.sleep(1)
    return False


def ansicht(state):
    Names = ['Einstellungen', 'System', 'Ansicht'] if state else ['Einstellungen', 'Erweiterte Einstellungen', 'System',
                                                                  'Ansicht']
    runner(Names)
    inputs = driver.find_elements_by_css_selector('input')
    for i in inputs:
        if (i.get_attribute('type') == 'checkbox'):
            i.click()
            break
    for i in inputs:
        if (i.get_attribute('value') == 'Übernehmen'):
            i.click()
            break


def einrichten():
    Names = ['Internet']
    runner(Names)
    inputs = driver.find_elements_by_css_selector('input')
    for i in inputs:
        if (i.get_attribute('onclick') == 'uiDoDslType(10)'):
            i.click()
            break
    inputs = driver.find_elements_by_css_selector('input')
    for i in inputs:
        if (i.get_attribute('onclick') == 'uiDoDslType(2)'):
            i.click()
            break
    inputs = driver.find_elements_by_css_selector('input')
    for i in inputs:
        if (i.get_attribute('onclick') == 'uiDoDslIpEncaps(1)'):
            i.click()
            break
    MAC()
    for i in inputs:
        if (i.get_attribute('value') == 'Übernehmen'):
            i.click()
            break


def MAC():
    global driver
    ml25 = driver.find_elements_by_class_name('ml25')
    for i in ml25:
        if (i.text[:11] == 'MAC-Adresse'):
            print(i.text)
            break


def reset():
    Names = ['Einstellungen', 'Erweiterte Einstellungen', 'System', 'Zurücksetzen', 'Werkseinstellungen',
             ]
    runner(Names)
    btns = driver.find_elements_by_class_name('Pushbutton')
    for i in btns:
        if (i.size == {'height': 21, 'width': 360}):
            i.click()
            break
    driver.switch_to.alert.accept()
    for i in range(51):
        print(f"Router wird gerade restarted bitte {50 - i} Sekunden warten")
        time.sleep(1)


def wlan():
    Names = ['WLAN', 'Funkeinstellungen']
    runner(Names)
    random_channel = random.randint(1, 11)
    random_channel = 'Kanal ' + str(random_channel)
    Eingabefelder = driver.find_elements_by_class_name('Eingabefeld')
    kanaldrop = []
    a = False
    b = False
    wlan_name = input("Wahlen sie einen WLAN name")
    for i in Eingabefelder:
        if (i.get_attribute('onchange') == 'uiSetChannel()' and not a):
            kanaldrop = i
            a = True
        if (i.get_attribute('id') == 'uiView_SSID' and not b):
            b = True
            i.clear()
            i.send_keys(wlan_name)

        if (a and b):
            break

    for i in kanaldrop.find_elements_by_tag_name("option"):
        if (i.text == random_channel):
            i.click()
            break
    inputs = driver.find_elements_by_css_selector('input')
    for i in inputs:
        if (i.get_attribute('value') == 'Übernehmen'):
            i.click()
            break


def reset_whenpass():
    Names = ['hier']
    runner(Names)
    inputs = driver.find_elements_by_css_selector('input')
    for i in inputs:
        if (i.get_attribute('onclick') == 'uiRestoreFactoryDefaults()'):
            i.click()
            break
    driver.switch_to.alert.accept()
    for i in range(51):
        print(f"Router wird gerade restarted bitte {50 - i} Sekunden warten")
        time.sleep(1)


try:
    ready = loaded()
    print(ready)
    if (not ready):
        print("Router war nach 200 Sekunden nicht zu erreichen, koennte kaputt sein")
        sys.exit()
    normal_reset = False
    try:
        reset()
        normal_reset = True

    except:
        print("Router hat ein Password alternative wird durchgeführt ")
        reset_whenpass()

    ready = loaded()
    if (not ready):
        print("Router war nach 200 Sekunden nicht zu erreichen, koennte kaputt sein")
        sys.exit()

    try:
        ansicht(normal_reset)
    except:
        print("Experten Ansicht wurde nicht aktiviert")

    einrichten()

    try:
        wlan()
    except:
        print("WLAN einrichten Error")

    print("Alles Prima")


except:
    print("ROUTER WURDE NICHT EINGERICHTET")

finally:
    driver.close()
