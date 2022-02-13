import logging

logging.basicConfig(level=logging.INFO)

'''

How to use the code

list_ports = generate_ports(2,"juniper")

ports_organize = organize_ports(list_ports)

pprint(ports_organize)


'''


from pprint import pprint


def generate_ports(switches, manufacture):
	'''
		switches = int
			How many switches should it generate
			Normally 1 to 9

		manufacture = string ( juniper or cisco)
			Will generate code based on manufactire

		Return a list of string as ports

		>>> generate_ports(2,"juniper")
		['ge-0/0/0', 'ge-0/0/1', 'ge-0/0/2', 'ge-0/0/3', 'ge-0/0/4', 'ge-0/0/5', 'ge-0/0/6', 'ge-0/0/7', 'ge-0/0/8', 'ge-0/0/9', 'ge-0/0/10', 'ge-0/0/11', 'ge-0/0/12', 'ge-0/0/13', 'ge-0/0/14', 'ge-0/0/15', 'ge-0/0/16', 'ge-0/0/17', 'ge-0/0/18', 'ge-0/0/19', 'ge-0/0/20', 'ge-0/0/21', 'ge-0/0/22', 'ge-0/0/23', 'ge-0/0/24', 'ge-0/0/25', 'ge-0/0/26', 'ge-0/0/27', 'ge-0/0/28', 'ge-0/0/29', 'ge-0/0/30', 'ge-0/0/31', 'ge-0/0/32', 'ge-0/0/33', 'ge-0/0/34', 'ge-0/0/35', 'ge-0/0/36', 'ge-0/0/37', 'ge-0/0/38', 'ge-0/0/39', 'ge-0/0/40', 'ge-0/0/41', 'ge-0/0/42', 'ge-0/0/43', 'ge-0/0/44', 'ge-0/0/45', 'ge-0/0/46', 'ge-0/0/47', 'ge-1/0/0', 'ge-1/0/1', 'ge-1/0/2', 'ge-1/0/3', 'ge-1/0/4', 'ge-1/0/5', 'ge-1/0/6', 'ge-1/0/7', 'ge-1/0/8', 'ge-1/0/9', 'ge-1/0/10', 'ge-1/0/11', 'ge-1/0/12', 'ge-1/0/13', 'ge-1/0/14', 'ge-1/0/15', 'ge-1/0/16', 'ge-1/0/17', 'ge-1/0/18', 'ge-1/0/19', 'ge-1/0/20', 'ge-1/0/21', 'ge-1/0/22', 'ge-1/0/23', 'ge-1/0/24', 'ge-1/0/25', 'ge-1/0/26', 'ge-1/0/27', 'ge-1/0/28', 'ge-1/0/29', 'ge-1/0/30', 'ge-1/0/31', 'ge-1/0/32', 'ge-1/0/33', 'ge-1/0/34', 'ge-1/0/35', 'ge-1/0/36', 'ge-1/0/37', 'ge-1/0/38', 'ge-1/0/39', 'ge-1/0/40', 'ge-1/0/41', 'ge-1/0/42', 'ge-1/0/43', 'ge-1/0/44', 'ge-1/0/45', 'ge-1/0/46', 'ge-1/0/47']

	'''

	if manufacture == "juniper":

		block = 0
		result_ports = []
		for i in range(0,switches):
			for port in range(0,48):
				result_ports.append(f"ge-{i}/0/{port}")
		return result_ports

	elif manufacture == "cisco_catalyst":

		block = 0
		result_ports = []
		for i in range(0,switches):
			for port in range(0,48):
				result_ports.append(f"gi-{i}/0/{port + 1}")
		

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

['ge-0/0/0', 'ge-0/0/2', 'ge-0/0/4', 'ge-0/0/6', 'ge-0/0/8', 'ge-0/0/10', 'ge-0/0/12', 'ge-0/0/14', 'ge-0/0/16', 'ge-0/0/18', 'ge-0/0/20', 'ge-0/0/22', 'ge-0/0/24', 'ge-0/0/26', 'ge-0/0/28', 'ge-0/0/30', 'ge-0/0/32', 'ge-0/0/34', 'ge-0/0/36', 'ge-0/0/38', 'ge-0/0/40', 'ge-0/0/42', 'ge-0/0/44', 'ge-0/0/46', 'ge-0/0/1', 'ge-0/0/3', 'ge-0/0/5', 'ge-0/0/7', 'ge-0/0/9', 'ge-0/0/11', 'ge-0/0/13', 'ge-0/0/15', 'ge-0/0/17', 'ge-0/0/19', 'ge-0/0/21', 'ge-0/0/23', 'ge-0/0/25', 'ge-0/0/27', 'ge-0/0/29', 'ge-0/0/31', 'ge-0/0/33', 'ge-0/0/35', 'ge-0/0/37', 'ge-0/0/39', 'ge-0/0/41', 'ge-0/0/43', 'ge-0/0/45', 'ge-0/0/47', 'ge-1/0/0', 'ge-1/0/2', 'ge-1/0/4', 'ge-1/0/6', 'ge-1/0/8', 'ge-1/0/10', 'ge-1/0/12', 'ge-1/0/14', 'ge-1/0/16', 'ge-1/0/18', 'ge-1/0/20', 'ge-1/0/22', 'ge-1/0/24', 'ge-1/0/26', 'ge-1/0/28', 'ge-1/0/30', 'ge-1/0/32', 'ge-1/0/34', 'ge-1/0/36', 'ge-1/0/38', 'ge-1/0/40', 'ge-1/0/42', 'ge-1/0/44', 'ge-1/0/46', 'ge-1/0/1', 'ge-1/0/3', 'ge-1/0/5', 'ge-1/0/7', 'ge-1/0/9', 'ge-1/0/11', 'ge-1/0/13', 'ge-1/0/15', 'ge-1/0/17', 'ge-1/0/19', 'ge-1/0/21', 'ge-1/0/23', 'ge-1/0/25', 'ge-1/0/27', 'ge-1/0/29', 'ge-1/0/31', 'ge-1/0/33', 'ge-1/0/35', 'ge-1/0/37', 'ge-1/0/39', 'ge-1/0/41', 'ge-1/0/43', 'ge-1/0/45', 'ge-1/0/47']

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


'''
					CODE






'''

list_ports = generate_ports(2,"juniper")
logging.info('Correctly generated list of ports')

ports_organize = organize_ports(list_ports)
logging.info('Port are now organized')


pprint(ports_organize[0])
logging.info('First port printed')




