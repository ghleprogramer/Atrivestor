marketf = "data/saudi companies.csv"
trackedf = "data/tracked companies.csv"

def comp_read2dct(f, pf=True):
	""" returns a dictionary of the companies to be tracked {symbol : name} """
	comp = {}
	dataf = open(f, "r")
	
	for i in dataf.readlines()[1:]:
		tmp = i.strip().split(",")
		comp[tmp[1]] = tmp[0]
	dataf.close()
	if pf:
		print("name, symbol")
	for i in comp:
		if pf:
			print(comp[i], i)
	return comp

def comp_add(tracked, market):
	""" prompts for new companies and validaits before adding them """
	inp = input("type company symbol to add to tracker, if not type skip:")
	while inp.upper() != "SKIP":
		if inp in tracked:
			print(inp, "is already tracked")
			inp = input("type company symbol to add to tracker, if not type skip:")
			continue
		if not inp in market:
			print(inp, "not a valid symbol")
			inp = input("type company symbol to add to tracker, if not type skip:")
			continue
		tracked[inp] = market[inp]
		print("name, symbol")
		for i in tracked:
			print(tracked[i], i)
		inp = input("type company symbol to add to tracker, if not type skip:")
	return