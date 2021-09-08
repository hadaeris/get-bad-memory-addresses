import sys, parse

if len(sys.argv) != 2:
	print("Incorrect number of arguments (2 needed). (start, end, number of zeroes)", file=sys.stderr)
	exit()

fp = open(sys.argv[1], 'r');
lines = fp.readlines()
all_addresses = {*()} #create empty set because fuck one of these imports that overrides set wtf

for line in lines:
	result = parse.search("Address: {}, Expected", line)
	if result != None:
		result_by_page = result[0][:-3]
		if result_by_page not in all_addresses:
			all_addresses.add(result_by_page)
print("bcdedit /set {badmemory} badmemorylist", end = ' ')

for address in all_addresses:
	print("0x"+address, end = ' ')

print("Total memory lost: " + str(len(all_addresses) * 4.096) + " kilobytes", file=sys.stderr)

fp.close()