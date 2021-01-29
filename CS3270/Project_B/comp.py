'''Finds specific suppliers who supply specific parts
or operate in different cities by using dict comprehension
Created by: Steven Schoebinger 1/28/2021'''
import parts
# pylint: disable=invalid-name, undefined-loop-variable
# [X] Get names of all suppliers that supply bolts.
# [X] Get names of all suppliers that supply blueparts.
# [X] Get names of all suppliers not used in Athens projects
# [X] Get names and colors of all parts not used in Oslo
# [X] Get pairs of names of all suppliers that are located in the same city.
# [] Print all suppliers out by city

def bolt_suppliers():
    '''Populates a set with the names of the suppliers that supply
    botls.'''
    bolt_pno = {p.pno for p in parts.parts if 'Bolt' in p}
    bolt_sno = {s.sno for s in parts.spj if s.pno in bolt_pno}
    bolt_supplier = {s.sname for s in parts.suppliers if s.sno in bolt_sno}
    print(bolt_supplier)

def blue_part_suppliers():
    '''Populates a set with the names of the suppliers that supply
    blue parts.'''
    blue_pno = {p.pno for p in parts.parts if p.color == 'Blue'}
    blue_sno = {s.sno for s in parts.spj if s.pno in blue_pno}
    blue_supplier = {s.sname for s in parts.suppliers if s.sno in blue_sno}
    print(blue_supplier)

def not_Athens():
    '''Populates a set with the names of the suppliers that are not
    used in the Athens projects.'''
    athens_proj = {p.jno for p in parts.projects if p.city == 'Athens'}
    noAthens_spj = {s.sno for s in parts.spj if s.jno in athens_proj}
    noAthens_supplier = {s.sname for s in parts.suppliers if s.sno not in noAthens_spj}
    print(noAthens_supplier)

def not_Oslo():
    '''Populates a set with the names and colors of the parts that
    are not used in the city of Oslo.'''
    oslo_jno = {j.jno for j in parts.projects if j.city == 'Oslo'}
    oslo_pno = {p.pno for p in parts.spj if p.jno in oslo_jno}
    not_oslo_parts = {p.pno for p in parts.spj if p.pno not in oslo_pno}
    parts_set = {(p.pname, p.color) for p in parts.parts if p.pno in not_oslo_parts}
    print(parts_set)

def same_city():
    '''Populates a set with 2 suppliers that are located in the same city.
    Thi sis done by going through all the suppliers and comparing them to
    another loop and making sure that they are not the same supplier,
    then making sure they are in the same city, and then making sure that
    there is not another duplicate in the set already by making sure that
    set is always in that configuration.'''
    city_supp = {(s1.sname, s2.sname) for s1 in parts.suppliers
        for s2 in parts.suppliers if s1 != s2 and s1.city == s2.city and s1 < s2}
    print(city_supp)

def sup_by_city():
    '''Populates a dictionary of sets with the key being the city and the set
    within the dictionary being the suppliers who supply in that city.'''
    city_suppliers = {s2.city:{s1.sname for s1 in parts.suppliers if s1.city == s2.city}
        for s2 in parts.suppliers}
    print(city_suppliers)

bolt_suppliers()
blue_part_suppliers()
not_Athens()
not_Oslo()
same_city()
sup_by_city()
