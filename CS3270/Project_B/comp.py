'''Finds specific suppliers who supply specific parts
or operate in different cities by using dict comprehension
Created by: Steven Schoebinger 1/28/2021'''
import parts2
# pylint: disable=invalid-name, undefined-loop-variable
# [X] Get names of all suppliers that supply bolts.
# [X] Get names of all suppliers that supply blueparts.
# [X] Get names of all suppliers not used in Athens projects
# [X] Get names and colors of all parts not used in Oslo
# [] Get pairs of names of all suppliers that are located in the same city.
# [] Print allsuppliers out by city

def bolt_suppliers():
    bolt_pno = [p.pno for p in parts2.parts if 'Bolt' in p]
    bolt_sno = [s.sno for s in parts2.spj if s.pno in bolt_pno]
    bolt_supplier = [s.sname for s in parts2.suppliers if s.sno in bolt_sno]
    print(bolt_supplier)

def blue_part_suppliers():
    blue_pno = [p.pno for p in parts2.parts if p.color == 'Blue']
    blue_sno = [s.sno for s in parts2.spj if s.pno in blue_pno]
    blue_supplier = [s.sname for s in parts2.suppliers if s.sno in blue_sno]
    print(blue_supplier)

def not_Athens():
    athens_proj = [p.jno for p in parts2.projects if p.city == 'Athens']
    noAthens_spj = [s.sno for s in parts2.spj if s.jno in athens_proj]
    noAthens_supplier = [s.sname for s in parts2.suppliers if s.sno not in noAthens_spj]
    print(noAthens_supplier)

def not_Oslo():
    oslo_jno = [j.jno for j in parts2.projects if j.city == 'Oslo']
    oslo_pno = [p.pno for p in parts2.spj if p.jno in oslo_jno]
    not_oslo_parts = [p.pno for p in parts2.spj if p.pno not in oslo_pno]
    parts_dict = [(p.pname, p.color) for p in parts2.parts if p.pno in not_oslo_parts]
    print(parts_dict)


#bolt_suppliers()
#blue_part_suppliers()
#not_Athens()
#not_Oslo()