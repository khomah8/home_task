 # script do the part of home task items(# 1, # 2):

import json
f2 = open("output.txt", "w")
with open('/home/omth/homeTask/data.json') as f1:
	data1 = json.load(f1);	data2 = data1["assignment_results"][0]["shown_price"]
	data3 = data2.items();
	for x, y in data3: 	minim = float(y);
	for x, y in data3:
		if float(y)<minim: minim = float(y);
#	print(minim);
	for x, y in data3:
		if float(y)==minim: output_str = "The cheapest price in USD is:" + str(minim) + " for room named:" + str(x[:(x.find("- ")-1)]) + "; room_type is:" + str(x[x.find(" - ")+2:]) + "; number of guests:" + str(data1["assignment_results"][0]["number_of_guests"]) + "."; print(output_str); f2.write("the result is: " + output_str);
# print("The cheapest price in USD is:",minim, "for room named:",x[:(x.find("- ")-1)],"; room_type is:",x[x.find(" - ")+2:],"; number of guests:",data1["assignment_results"][0]["number_of_guests"] ); f2.write("the result is: ",output_str)

#   1  Find and return the cheapest (lowest) shown price (Please avoid using the minimum function)
#   2  Find and return the room type, number of guest with the cheapest price
f2.close()
#   4  Please add your output to a file
