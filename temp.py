tempc = input('請輸入攝氏溫度：')
tempf =float(tempc) * 9 / 5 + 32
print('攝氏', tempc, "'C，等於華氏溫度", tempf, "'C")
tempf = input('請輸入華氏溫度：')
tempc = float(tempf) - 32
tempc_1 = float(tempc) * 5 / 9
print('華氏', tempf, "'C，等於攝氏溫度", tempc_1, "'C")