# Created by Ícaro Freire on September 2nd, 2022.
# São Paulo, Brazil

import pandas as pd

class Network:
	def __init__(self, title, path='network.csv'):
		self.title = title
		self.lines = [ [] ]

		self.load_network(path)

		print(self.lines)

		return
	
	def load_network(self, path):

		nw = pd.read_csv(path)

		line = 0
		for i, row in nw.iterrows():
			if row['line'] != line:
				line += 1
				self.lines.append([])
			self.lines[line].append([
				row['name'],
				row['time']
			])

		return

	def __str__(self):
		return self.title

if __name__ == '__main__':
	network = Network('Python City Metropolitan')
	print(network)