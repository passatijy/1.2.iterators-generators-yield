import hashlib
def my_gener(file):
	with open(file) as f:
		for line in f:
			yield hashlib.md5(line.encode('utf-8')).hexdigest()

for k in my_gener('mygener.py'):
	print(k)