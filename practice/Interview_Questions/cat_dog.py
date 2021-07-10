# Return True if the string "cat" and "dog" appear
# the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    cat_count = str.count('cat')
    dog_count = str.count('dog')
    return cat_count == dog_count

def main():
    print(cat_dog('catdog'))
    print(cat_dog('catcat'))
    print(cat_dog('1cat1cadodog'))

if __name__ == '__main__':
    main()