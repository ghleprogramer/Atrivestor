import yfinance as yf
import pandas as pd
from rich.console import Console
from rich.markdown import Markdown

console = Console()
marketf = "data/saudi companies.csv"
trackedf = "data/tracked companies.csv"

def comp_read2dct(f, pf=True):
	""" returns a dictionary of the companies to be tracked {symbol : name} """
	comp = {}
	df = pd.read_csv(f)
	dataf = open(f, "r")
	
	for i in dataf.readlines()[1:]:
		tmp = i.strip().split(",")
		comp[tmp[1]] = tmp[0]
	dataf.close()
	if pf:
		table = df[["name", "ticker"]] 
		table = table.astype(str)
		for col in table.columns:
			max_width = table[col].str.len().max()
			table[col] = table[col].str.ljust(max_width)
		print("\nTracked Companies:\n")
		print(table.to_string(index=False, justify="left"))
		print()
	return comp

def comp_add(tracked, market):
	""" prompts for new companies and validaits before adding them """
	msg = "type company symbol to add to tracker, if not type skip: "
	inp = input(msg)
	while inp.upper() != "SKIP":
		if inp in tracked:
			print(inp, "is already tracked")
			inp = input(msg)
			continue
		if not inp in market:
			print(inp, "not a valid symbol")
			inp = input(msg)
			continue
		tracked[inp] = market[inp]
		print("name, symbol")
		for i in tracked:
			print(tracked[i], i)
		inp = input(msg)
	print()
	return

def print_tdy_data(tracked):
	symbols = [i+".SR" for i in tracked]
	data = yf.download(symbols, period="1d", interval="1d", auto_adjust=False, progress=False)
	data = data[["Open", "High", "Low", "Close", "Volume"]]
	data = data.iloc[-1]
	table = data.unstack()
	
	for col in table.columns:
		if col != "Volume":
			table[col] = table[col].map(lambda x: f"{x:.2f}")
		else:
			table[col] = table[col].map(lambda x: f"{int(x):,}")

	print(table.to_string(), "\n")
	return

def display_markdown(text):
    md = Markdown(text)
    console.print(md)
