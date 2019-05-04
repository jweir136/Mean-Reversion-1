# -*- coding: utf-8 -*-

import Functions as utils
import sys

global symbol_list
symbol_list = [
	"AVCO",
	"AWX",
	"CBO",
	"CCCL",
	"CLGN",
	"CLRBW",
	"CLSN",
	"CNACU",
	"CNET",
	"GBR",
	"GRNQ",
	"IHT",
	"MTSL",
	"NDRAW",
	"SGOC",
	"TOPS"
]

if __name__ == "__main__":
	if utils.market_open() == False:
		print("Market Not Open...Exiting")
		sys.exit(0)
	for ticker in symbol_list:
		if not utils.in_portfolio(ticker) and not utils.in_open_orders(ticker):
			z = utils.get_todays_zscore(ticker)
			if z >= 2.0:
				pass
			elif z <= -2.0:
				print("Buying 5 Shares of {}".format(ticker))
				utils.buy(ticker, 5)
	
	for ticker in utils.get_portfolio_stocks():
		z = util.get_todays_zscore(ticker)
		if z >= -0.5 and z <= 0.5:
			print("Selling 5 Shares of {}".format(ticker))
			utils.sell(ticker, 5)
	print("Script Complete!")
