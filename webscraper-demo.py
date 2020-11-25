from selenium import webdriver

driver = webdriver.Chrome()

link = driver.get("https://www.cnet.com/news")

# you don't really need to set these as variables.
target = driver.find_element_by_link_text("The PS5 is the weirdest thing I've ever seen in my life").click()
