#main :D
from functions import *
from GemiAPI import gemini_summary

def main():
	# read & print compaines of interest
	market_companies = comp_read2dct(marketf, pf=False)
	tracked_companies = comp_read2dct(trackedf)
	comp_add(tracked_companies, market_companies)
	# fetch & print stock data from yahoo finance
	print_tdy_data(tracked_companies)
	# scrape new announcments from https://www.saudiexchange.sa/wps/portal/saudiexchange/newsandreports/issuer-news/issuer-announcements/
	
	# summarise new announcments via an Google Geminie API
	summary_text = gemini_summary("data/teststatements.pdf",
		"Please provide a clear, concise summary of this PDF. Highlight the main points, key arguments, and any conclusions."
	)
	# print out AI announcments summaries
	display_markdown(summary_text)
	return

main()