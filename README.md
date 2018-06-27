# gearbest.com products tracker
Price and availability tracker for gearbest.com

---

## Before running the script for a first time, configure it by updating  these lines:
````
url_list = []
url_list.append("http://www.gearbest.com/batteries-chargers/pp_140785.html")
url_list.append("http://www.gearbest.com/electronics-gadgets/pp_280338.html")

email_list = []
email_list.append("user@gmail.com")
email_list.append("user1@gmail.com")
````
and make sure you have these python modules installed: 
- beautifulsoup4
- requests
- configparser
- logging
```
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run this script with a cron job and you'll get an email each time there are price or availability changes in the list of tracked urls.

## Cronjob example:
````
10 */1 * * * /usr/bin/python /home/user/gearbest/gearbetst-prices.py
````
In this example the script will run once per hour and notify you if there is a change.

## Script output example:
````
************** [ITEM] **************
Name: Xiaomi Redmi Note 5 4G Phablet Global Version - $229.99 Free~
URL: https://www.gearbest.com/cell-phones/pp_1660531.html
New price: $335.79 / Old price: $0.0
Stock: Availability changed to 'In stock'!
````
Python 3  		
This script uses BeautifulSoup and needs a folder to store previous product data.
