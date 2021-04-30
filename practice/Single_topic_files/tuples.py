info = ['Steven', 'Password', True]
nothing = [info, 'something', 'nothing']

candy = tuple(info)
something = tuple(nothing)
username, password, accepted = candy
print(candy)
print(username)
print(password)
print(accepted)

print(something)
print(type(something))
something += candy
print(something)
print(type(something))

