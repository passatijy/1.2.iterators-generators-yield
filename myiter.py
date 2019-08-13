import json


class MyIter:
	def __init__(self, start, end):
		self.start = start - 1
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.start == self.end:
			raise StopIteration
		self.start += 1
		return self.start

def parse_json(filename):
	with open (filename,'r', encoding = 'UTF8') as f:
		#print('filename: ', filename)
		json_obj = json.load(f)
	return json_obj

class MyIterJsCountries:
	def __init__(self, start, end, filename):
		self.start = start - 1
		self.end = end
		self.filename = filename

	def __iter__(self):
		return self

	def __next__(self):
		if self.start == self.end:
			raise StopIteration
		result = 'https://en.wikipedia.org/wiki/' + parse_json(self.filename)[self.start]['name']['common']
		self.start += 1
		return result


if __name__ == '__main__':
	#for item in MyIter(1,4):
		#print('item: ', item)
	print(parse_json('countries_small.json')[0]['name']['common'])
	for item in MyIterJsCountries(1,10,'countries.json'):
		print('countries: ', item)