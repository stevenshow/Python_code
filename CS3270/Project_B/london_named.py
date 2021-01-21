import parts2

# Sample: Get suppliers that supply parts for London projects (sample problem; not graded)
londonprojs = {j.jno for j in parts2.projects if j.city == 'London'}
londonsuppids = {r.sno for r in parts2.spj if r.jno in londonprojs}
londonsupps = {s.sname for s in parts2.suppliers if s.sno in londonsuppids}
print(londonsupps)
