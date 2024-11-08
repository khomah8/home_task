# item 3 Print the total price (Net price + taxes) for all rooms along with the room type
import json
with open('data.json') as f1:
	data1 = json.load(f1);	data2 = data1["assignment_results"][0]["shown_price"]
	data3 = data2.items();
	data4 = data1["assignment_results"][0]["ext_data"];
	data5 = data4.items();
	for x, y in data3:
		print("net_price is:",y, "for room named:",x[:(x.find("- ")-1)],"; room_type is:",x[x.find(" - ")+2:],"; number of guests:",data1["assignment_results"][0]["number_of_guests"] );
	for q, r in data5:
		if q=="taxes":  print(r[(r.find(":")+2):r.find(",")-1]); print(r[(r.rfind(":")+2):-2]);
