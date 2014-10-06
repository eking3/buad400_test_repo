import copy 

def flatten(elts):
	if elts == []:
		return []
	elif type(elts[0])== type([]):
		return flatten(elts[0]) + flatten(elts[1:])
	else:
		return [elts[0]] + flatten(elts[1:])


def powerset(item):
	new = []
	
	if item == None:
		return []
	
	if len(item) == 1:
		return [item]
	
	new.append(flatten(item))
	
	for i in range(len(item)):
		item2 = []
		item2 = copy.deepcopy(item)
		item2.remove(item[i])
		ans = powerset(item2)
		
		for j in range(len(ans)):
			if ans[j] not in new:
				new.append(ans[j])
	
	return new
