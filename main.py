

def generate_ports(switches, manufacture):
	'''
		switches = int
			How many switches should it generate
			Normally 1 to 9

		manufacture = string ( juniper or cisco)
			Will generate code based on manufactire

		Return a list of string as ports

		Need to finish manifacture, for now any value works
	'''

	block = 0
	result_ports = []
	for i in range(0,switches):
		for port in range(0,48):
			result_ports.append(f"ge-{i}/0/{port}")

	return result_ports



def organize_ports(list1):
	'''
	list1 = list
		provide a list of port

	This function creates a new list for when the ports and labelling look like this

	ge-0/0/0 port 000
	ge-0/0/1 port 025
	ge-0/0/2 port 001

	return list 
	'''

	temp_list = list1
	result_even = []
	result_abc = []
	result = []
	while len(list1) > 0:

		for number in range(0,48):

			if temp_list:

				port = int(temp_list[0].split('/')[-1])
				
				if port % 2 == 0:
					result_even.append(temp_list.pop(0))
				else:
					result_abc.append(temp_list.pop(0))

		result.extend(result_even)
		result_even = []
		result.extend(result_abc)
		result_abc = []

	return result


list_ports = generate_ports(2,"tiago")

ports_organize = organize_ports(list_ports)

from pprint import pprint
pprint(ports_organize)


list1 = ["D46A91E24351","00:04:A5:0C:6A:28","00107FE24CB3","006074068E76","00:1B:21:E4:73:04","D46A91E24350","00:04:A5:0C:6A:55","00107FEE216E","00107FEE2163","00107FEBCB40","00107FEBCB41","006074068F2E","00:1B:21:E4:72:72","D46A91E2434F","00:04:A5:0C:6A:27","00107FE26D93","006074068FE6","00:1B:21:E4:74:F0"]

response = []

for raw_item in list1:
	item = raw_item.strip()
	temp = ""
	if len(item) == 12:
		temp = item[0:2] + ":" + item[2:4] + ":" + item[4:6] + ":" +item[6:8] + ":" +item[8:10] + ":" +item[10:12]
		print(temp)
		response.append(temp)
	elif item[2] == "-":
		new_item = item.split("-")
		temp = new_item[0] + ":" + new_item[1] + ":" + new_item[2] + ":" + new_item[3] + ":" + new_item[4] + ":" + new_item[5]
		print(temp)
		response.append(temp)
	else:
		print(item)
		response.append(item)

print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)


for i in response:
	print(i)