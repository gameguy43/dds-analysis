import urllib
import datetime

# where we will keep the scraped html menu pages
SCRAPE_DEST="/home/pyrak/scrapes/"

def scrape():
	#the url of the dailymenus page is based on the day of the week
	now = datetime.datetime.now()	
	weekdayDec = int(now.strftime("%w")) #[0,6]
	#for them, mon = 1, sun = 7
	#in what we just did, sun = 0, sat = 6
	#so we adjust
	if (weekdayDec == 0):
		menuPageName = "7. sunday.htm"	
	elif (weekdayDec == 1):
		menuPageName = "2. Tuesday.htm"
	elif (weekdayDec == 2):
		menuPageName = "3. Wednesday.htm"	
	elif (weekdayDec == 3):
		menuPageName = "4. thursday.htm"	
	elif (weekdayDec == 4):
		menuPageName = "5. friday.htm"	
	elif (weekdayDec == 5):
		menuPageName = "6. saturday.htm"	
	elif (weekdayDec == 6):
		menuPageName = "1. Monday.htm"	
	
	# download the html page with the daily menus
	urllib.urlretrieve('http://www.dartmouth.edu/~dds/' + menuPageName, SCRAPE_DEST + '/' + str(now))

if __name__ == '__main__':
    scrape()
