# -*- coding: utf-8 -*-
"""Untitled134.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xBpeXf6WUz9bCb1gqYwQvXG4rcsz5N_n
"""

import alpaca_trade_api as trade_api
from scipy.stats import zscore
import requests

global iex_base
global alpaca_base
global api

iex_base = "https://api.iextrading.com/1.0"
api = trade_api.REST("PKLIXRCAA5A02LDY103W", "AwjPye0nwFZIvuxtlbDnG8UlkMD4eN4rMkmR16DU", "https://paper-api.alpaca.markets/")
alpaca_base = "https://api/alpaca.markets"

def can_short(symbol):
	try:
		url = iex_base + "/deep/ssr-status?symbols={}".format(symbol)
		data = requests.get(url).json()
		if len(data) == 0:
			return True
		return False
	except Exception as e:
		print("Error: {}".format(e))
		return None

def market_open():
	try:
  		clock = api.get_clock().is_open
  		return bool(clock)
	except Exception as e:
		print("Error: {}".format(e))
		return None

def todays_open(symbol):
	try:
  		bars = api.get_barset(symbol.upper(), "day", limit=10)
  		opens = [a.o for a in bars[symbol.upper()]]
  		return opens[-1]
	except Exception as e:
		print("Error: {}".format(e))
		return None

def get_todays_zscore(symbol):
	try:
  		bars = api.get_barset(symbol.upper(), 'day', limit=200)
  		opens = [a.o for a in bars[symbol.upper()]]
  		return zscore(opens)[-1]
	except Exception as e:
		print("Error: {}".format(e))
		return None

def get_cash():
	try:
  		return float(api.get_account().cash)
	except Exception as e:
		print("Error: {}".format(e))
		return None

def get_cash_percent(percent=0.03):
	try:
  		return float(get_cash()) * percent
	except Exception as e:
		print("Error: {}".format(e))
		return None

def in_portfolio(symbol):
	try:
  		symbols = [i.symbol for i in api.list_positions()]
  		return symbol.upper() in symbols
	except Exception as e:
		print("Error: {}".format(e))
		return None

def in_open_orders(symbol):
	try:
  		orders = [i.symbol for i in api.list_orders()]
  		return symbol.upper() in orders
	except Exception as e:
		print("Error: {}".format(e))
		return None

def buy(symbol, amount):
	try:
  		side = "buy"
  		_type = "market"
  		time = "day"
  		api.submit_order(symbol, amount, side, _type, time)
	except Exception as e:
		print("Error: {}".format(e))
		return None

def sell(symbol, amount):
	try:
  		side = "sell"
  		_type = "market"
  		time = "day"
  		api.submit_order(symbol, amount, side, _type, time)
	except Exception as e:
		print("Error: {}".format(e))
		return None

def n_shares(symbol):
	try:
		positions = api.list_positions()
		for i in positions:
			if i.symbol == symbol.upper():
				return i.qty
		return 0
	except Exception as e:
		print("Error: {}".format(e))
		return None

def get_order_id(symbol):
	try:
		all_orders = api.list_orders()
		for order in all_orders:
			if order.symbol == symbol.upper():
				return order.id
		return -1
	except Exception as e:
		print("Error: {}".format(e))
		return None

def cancel_order(symbol):
	try:
		order_id = get_order_id(symbol.upper())
		api.cancel_order(order_id)
		return 1
	except Exception as e:
		print("Error: {}".format(e))
		return None

def get_portfolio_stocks():
	try:
		symbols = []
		portfolios = api.list_positions()
		for port in portfolios:
			symbols.append(port)
		return symbols
	except Exception as e:
		print("Error: {}".format(e))
		return None
