import urllib
import datetime

SCRAPE_DEST="/home/pyrak/scrapes/"

def main():
	now = datetime.datetime.now()	
	weekdayDec = int(now.strftime("%w")) #[0,6]
	#for them, mon = 1, sun = 7
	#in what we just did, sun = 0, sat = 6
	#so we adjust
	if (weekdayDec == 0):
		menuPageName = "7. sunday.htm"	
	if (weekdayDec == 1):
		menuPageName = "2. Tuesday.htm"
	if (weekdayDec == 2):
		menuPageName = "3. Wednesday.htm"	
	if (weekdayDec == 3):
		menuPageName = "4. thursday.htm"	
	if (weekdayDec == 4):
		menuPageName = "5. friday.htm"	
	if (weekdayDec == 5):
		menuPageName = "6. saturday.htm"	
	if (weekdayDec == 6):
		menuPageName = "1. Monday.htm"	
	
	urllib.urlretrieve('http://www.dartmouth.edu/~dds/' + menuPageName, SCRAPE_DEST + '/' + str(now))

if __name__ == '__main__':
    main()
