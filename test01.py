from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '192.168.68.103:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
el = WebDriverWait(driver,5,0.5).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'显示')]"))
TouchAction(driver).long_press(el=el,duration=3000).perform()
driver.quit()

# el_more = driver.find_element_by_xpath("//*[contains(@content-desc,'更多选项') and contains(@class,'android.widget.ImageView')]")
# el_more.click()
# driver.quit()