
def ReturnBase(theFile = 'Overwerk-Conquerbass'):
	fload = open(theFile, 'r')
	base = []
	for line in fload:
		base.append(line.split())
	fload.close()
	for i in base:
		i[0] = int(i[0])
		i[1] = int(i[1])
	return base
