from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from time import 
import random

username = ""
password = ''


def login(username,password):

	### Log in ###
	browser = webdriver.Chrome()
	home_url = "https://accounts.craigslist.org/login/home"
	url_inactive_posts = "?lang=en&cc=us&filter_active=inactive&filter_cat=0&show_tab=postings"
	browser.get(home_url)

	usernameelem = browser.find_element_by_name("inputEmailHandle")
	usernameelem.clear()
	usernameelem.send_keys(username)
	#  
	# (randint(10,100))
	
	passwordelem = browser.find_element_by_name("inputPassword")
	passwordelem.clear()
	passwordelem.send_keys(password)
	#  	
	# (randint(10,100))
	
	passwordelem.submit()
	#  	
	# (randint(10,100))

	########### Select city to post and submit ################

	# open city options
	opencityoptions = browser.find_element_by_xpath('/html/body/article/section/form[2]/select')
	opencityoptions.click()
	# (randint(10,100))

	cityoptions = ["option[247]", "option[284]", "option[391]", "option[166]", "option[153]", "option[510]" ]
	secondcity = ["option[509]", "option[521]", "option[544]", "option[241]", "option[148]", "option[32]"]

	city = random.choice(cityoptions)
	scity = random.choice(secondcity)

	# select Vancouver
	selectcity = browser.find_element_by_xpath('/html/body/article/section/form[2]/select/'+ city)
	
	# (randint(10,100))

	# submit
	postgo = browser.find_element_by_xpath('/html/body/article/section/form[2]/button')
	postgo.click()
	# (randint(10,100))

	cockblock = browser.find_element_by_xpath('/html/body/article/section/form/select')

	if cockblock:
		cockblock.click()
		cockblockcity = browser.find_element_by_xpath('/html/body/article/section/form/select/'+ scity)
		cockblockcity.click()
		cockblockgo = browser.find_element_by_xpath('/html/body/article/section/form/button')
		cockblockgo.click()


	########### Select post type and submit ################

	# Select services
	serviceOffered = browser.find_element_by_xpath('/html/body/article/section/form/ul/li[10]/label/span[1]/input')
	serviceOffered.click()	
	# (randint(10,100))
	

	########### Select post type and submit ################

	# Select type of services
	automativeServices = browser.find_element_by_xpath('//*[@id="picker"]/ul/li[4]/label/span[1]/input')
	automativeServices.click()
	# (randint(10,100))


	### Contact info and post body ###

	# post title
	PostingTitle = browser.find_element_by_xpath('//*[@id="PostingTitle"]')
	PostingTitle.send_keys("")
	# (randint(10,100))

	# postal code
	postal_code = browser.find_element_by_xpath('//*[@id="postal_code"]')
	# enter zip code or make an array with zip codes so you don't manually have to add them in the variables everytime better yet
	zipcodes = [""]
	runzip = random.choice(zipcodes)
	postal_code.send_keys(runzip)
	# (randint(10,100))

	# posting body
	PostingBody = browser.find_element_by_xpath('//*[@id="PostingBody"]')
	PostingBody.send_keys("")

	# submit button
	postingForm = browser.find_element_by_xpath('//*[@id="postingForm"]/div/button')
	postingForm.click()
	# (randint(10,100))


	# continue
	leafletForm = browser.find_element_by_xpath('//*[@id="leafletForm"]/button[1]')
	leafletForm.click()
	# (randint(10,100))

	# done with image
	imageForm = browser.find_element_by_xpath('/html/body/article/section/form/button')
	imageForm.click()
	# (randint(10,100))

	# publish
	publish_top = browser.find_element_by_xpath('//*[@id="publish_top"]/button')
	publish_top.click()

	# (randint(10,100))

	# verification
	

	if not publish_top:
		verify = browser.find_element_by_xpath('//*[@id="phoneAuthForm"]/form/fieldset/input[2]')
		# entert phone number here
		verify.send_keys("")

		#sendtextmessage
		text = browser.find_element_by_xpath('//*[@id="phoneAuthForm"]/form/fieldset/blockquote/label[2]/input')
		text.click()

		# publish
		post_see = browser.find_element_by_xpath('//*[@id="phoneAuthForm"]/form/p/button')
		post_see.click()
		
	
	# takes a screenshot
	browser.save_screenshot('screenshot.png')

	logout = browser.find_element_by_xpath('//*[@id="loginWidget"]/p[2]/a')
	logout.click()

	# quits the browser
	browser.quit()

for x in range(3):
	login(username,password)



