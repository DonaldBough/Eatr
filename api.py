import myfitnesspal
import time

old_day = ""
client = myfitnesspal.Client('donaldbough@gmail.com', 'password')
# while True:
# 	try:		
day = client.get_date(2019, 2, 1);
if day != old_day:
	print(day)
	old_day = day
# time.sleep(5)
	# except:
	# 	print("Whoops, let's keep going")