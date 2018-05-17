import urllib.request
import re
import sys

if(len(sys.argv) < 2):
	print("You did not provide the requirement: a product detail page URL in hepsiburada.com ")
else:

	url = sys.argv[1]
	
	# Check the url if it is from hepsiburada.com
	url_check =  re.search('hepsiburada.com', url)
	if(url_check is None):
		print("The url provided is not from hepsiburada.com")
	else:
		response = urllib.request.urlopen(url);
		html_code = response.read().decode('utf-8')

		price = re.search(r'id=\"offering-price\".*content=(.*)>', html_code)
		currency = re.search(r'itemprop="priceCurrency".*content="TRY">(.*)</span>', html_code)

		if(price is not None):
			if(currency is not None):
				print(price.group(1), currency.group(1))
			else:
				print(price.group(1), "TL")
				print("(Warning! Currency is assumed to be TRY)")
		else:
			print("Price value couldn't be found for the given url")



