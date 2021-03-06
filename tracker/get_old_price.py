import os.path
import logging
log = logging.getLogger(__name__)

def get_old_price(db_dir,link,stock_lvl,price): # reads old data and updates it with current data
	'''
	Get old price from db_dir
	'''
	db_filename = db_dir + link + ".txt"

	if os.path.isfile(db_filename):  # check if file exists
		# log.info('File exist, writing into %s' % db_filename)
		fo = open(db_filename, "r+")
		line = fo.readline() # if there is a file read the previous value
		old_price = line.split(",")[0]
		stock_avail = line.split(",")[1]
		
	else:
		# log.info('File doesn't exist, creating missing file: %s' % db_filename)
		fo = open(db_filename, "w+") # create the missing file
		old_price = "0" # set previous price to 0
		stock_avail = "Unknown"
		
	position = fo.seek(0, 0)
	fo.write('%s,%s\n' % (price, stock_lvl))		# write the new value
	fo.close()

	return old_price,stock_avail