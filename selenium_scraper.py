from selenium import webdriver
from time import sleep
from HTMLParser import HTMLParser

def get_data():
	myParser = HTMLParser()
	browser = webdriver.Firefox()
	browser.get("https://twitter.com/Horse_ebooks/followers")
	sleep(6)
	browser.execute_script('$(".js-username-field").val("rboling91@gmail.com");');
	browser.execute_script('$(".js-password-field").val("beethoven3");');
	sleep(2)
	browser.execute_script('$(".submit").click();')
	sleep(5)
	ol_stuff = browser.find_element_by_class_name("stream-items")
	#for i in range(10):
	browser.execute_script("window.scrollTo(0, document.body.scrollTop);")
	sleep(1)
	browser.execute_script("window.scrollTo(0, document.body.scrollTop + 500);")
	sleep(1)
	browser.execute_script("window.scrollTo(0, document.body.scrollTop + 1750);")
	sleep(1)
	browser.execute_script("window.scrollTo(0, document.body.scrollTop + 2000);")
	sleep(1)
	browser.execute_script("window.scrollTo(0, document.body.scrollTop + 2200);")
	sleep(1)
	browser.execute_script("window.scrollTo(0, document.body.scrollTop + 2400);")
	sleep(1)
	browser.execute_script("window.scrollTo(0, document.body.scrollTop + 3000);")
	sleep(1)
	browser.execute_script("window.scrollTo(0, document.body.scrollTop + 5000);")
	sleep(1)
	li_array = ol_stuff.find_elements_by_tag_name("li")
	for item in li_array:
		try:
			span_array = item.find_elements_by_tag_name("span")
			print span_array[len(span_array) - 1].text
		except:
			pass
if __name__ == "__main__":
	get_data()