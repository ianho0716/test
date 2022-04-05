import datetime
start = str(input('請輸入開始日期yyyymmdd：'))
sd = datetime.datetime.strptime(start,'%Y%m%d')
end = str(input('請輸入結束日期yyyymmdd：')) 
ed = datetime.datetime.strptime(end,'%Y%m%d')
n = ed - sd
print(str(n))