# item 3 Print the total price (Net price + taxes) for all rooms along with the room type
import json
with open('data.json') as f1:
	data1 = json.load(f1);	data2 = data1["assignment_results"][0]["net_price"]
	data3 = data2.items();
	data4 = data1["assignment_results"][0]["ext_data"];
	data5 = data4.items();
	for x, y in data3:
		print("net_price is:",y, "for room named:",x[:(x.find("- ")-1)],"; room_type is:",x[x.find(" - ")+2:],"; number of guests:",data1["assignment_results"][0]["number_of_guests"] );
	for q, r in data5:
		if q=="taxes":  tt1 = r[(r.find(":")+2):r.find(",")-1]; tt2 = r[(r.rfind(":")+2):-2]; print("taxes_summary: ",tt1,"+",tt2,"=",float(tt1)+float(tt2)) # parse dict  as just str
	print("* If taxes values are fixed, the [room's] end_price = net_price + taxes_summary");
