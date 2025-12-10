#main :D
import yfinance as yf
from functions import comp_read2dct, comp_add, trackedf, marketf

def main():
	# read & print compaines of interest
	market_companies = comp_read2dct(marketf, pf=False)
	tracked_companies = comp_read2dct(trackedf)
	# prompt for additional compaines & validate symbols
	comp_add(tracked_companies, market_companies)
	# fetch & print stock data from yahoo finance
	
	# scrape new announcments from https://www.saudiexchange.sa/wps/portal/saudiexchange/newsandreports/issuer-news/issuer-announcements/
	
	# summarise new announcments via an AI API
	
	# print out AI announcments summaries
	
	return

main()