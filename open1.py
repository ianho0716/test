data = []
with open('cars.txt', 'r') as f: #讀取檔案，r = read，f = file
	for line in f:
		data.append(line) #若原txt檔案有按過enter則會出現多餘的符號
print(data)

data = []
with open('cars.txt', 'r') as f:
	for line in f:
		data.append(line.strip()) # .strip() 消除空格
print(data)