import datetime
d1 = str(input('請輸入指定日期yyyymmdd：'))
dt = datetime.datetime.strptime(d1,'%Y%m%d')
nds = input('請輸入往前或往後的天數：')
nds = int(nds)
nd = dt + datetime.timedelta(days=nds)
n = nd.strftime('%Y%m%d')
print(str(n))