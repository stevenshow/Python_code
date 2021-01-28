import parts

lprojids = {x[0] for x in parts.projects if x[2]=='London'}
print(lprojids)
suppids = {x[0] for x in parts.spj if x[2] in lprojids}
print(suppids)
suppnames = {x[1] for x in parts.suppliers if x[0] in suppids}
print(suppnames)

print ({s[1] for s in parts.suppliers
	for p in parts.projects\
		for j in parts.spj\
			if p[2]=='London'\
			if p[0]==j[2]\
			if j[0]==s[0]})
