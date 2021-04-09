# re1.py: Sample RE searches
import re

s = "there's no business like show business"

def lookup(pattern,s):
    match = re.search(pattern,s)
    if not match:
        print('No match')
        return
    start = match.start()
    end = match.end()
    print('pattern =', match.re.pattern)
    print('start =',start)
    print('end =',end)
    print('substring =', s[start:end])
    print('groups =',match.groups())
    print()

lookup('b.*s',s)

"""
pattern = b.*s
start = 11
end = 38
substring = business like show business
groups = ()
"""

# Non-greedy ("lazy") version
lookup('b.*?s',s)

"""
pattern = b.*?s
start = 11
end = 14
substring = bus
groups = ()
"""

lookup('b.*?ss',s)

"""
pattern = b.*?ss
start = 11
end = 19
substring = business
groups = ()
"""

# Match end of string ($)
lookup('ess$',s)

"""
pattern = ess$
start = 35
end = 38
substring = ess
groups = ()
"""

# Match beginning of string
lookup('^.*?s',s)

"""
pattern = ^.*?s
start = 0
end = 7
groups = ()
substring = there's
"""

# One or more (Finds first match, of course)
lookup('s+',s)

'''
pattern = s+
start = 6
end = 7
substring = s
groups = ()
'''

# Repeat previous but anchored at end
lookup('s+$',s)

'''
pattern = s+$
start = 36
end = 38
substring = ss
groups = ()
'''

lookup('s{2}',s)    # Same as 'ss'

'''
pattern = s{2}
start = 17
end = 19
substring = ss
groups = ()
'''

# Anything but from ['s','t','u'], from beginning
lookup('[^stu]+',s)

"""
pattern = [^stu]+
start = 1
end = 6
substring = here'
groups = ()
"""

# Strigns consisting of 2 or 3 from ['n','e','i','s']
lookup ('[neis]{2,3}',s)

"""
pattern = [neis]{2,3}
start = 13
end = 16
substring = sin
groups = ()
"""

# Repeat
lookup ('[neis]{2,3}?',s)

'''
pattern = [neis]{2,3}?
start = 13
end = 15
substring = si
groups = ()
'''

# Repeat, anchored at end
lookup ('[neis]{2,3}$',s)

"""
pattern = [neis]{2,3}$
start = 35
end = 38
substring = ess
groups = ()
"""

# Union (one or the other)
lookup('([neis]{2,3})|([her]+)',s)

"""
pattern = ([neis]{2,3})|([her]+)
start = 1
end = 5
substring = here
groups = (None, 'here')
"""

# Union (one or the other *without groups*)
lookup('(?:[neis]{2,3})|(?:[her]+)',s)

"""
pattern = ([neis]{2,3})|([her]+)
start = 1
end = 5
substring = here
groups = ()
"""

# Repeat, anchored at end
lookup('([neis]{3,4}|[her]+)$',s)

"""
pattern = ([neis]{3,4}|[her]+)$
start = 34
end = 38
substring = ness
groups = ('ness',)
"""

print(re.findall('[neis]{2,3}|[her]+',s))
print()

"""
['here', 'sin', 'ess', 'e', 'h', 'sin', 'ess']
"""

# An HTML string to search
html = """
<html>
<body>
Hello. This is string in HTML format.
<a href="http://foo.com">Link 1</a>
Here's another link:
<a href="http://bar.com">Link 2</a>
</body>
</html>
"""

# Find first link
lookup('<a href="http://.*?>',html)

'''
pattern = <a href="http://.*?>
start = 53
end = 78
substring = <a href="http://foo.com">
groups = ()
'''

# All links
print(re.findall('<a href="http://.*?>',html))
print()

"""
['<a href="http://foo.com">', '<a href="http://bar.com">']
"""

# All tags
print(re.findall('<.*?>', html))
print()

"""
['<html>', '<body>', '<a href="http://foo.com">', '</a>', '<a href="http://bar.com">',
'</a>', '</body>', '</html>']
"""

# All non-tags
print(re.split('<.*?>', html))
print()

"""
['\n', '\n', '\nHello. This is string in HTML format.\n', 'Link 1',
"\nHere's another link:\n", 'Link 2', '\n', '\n', '\n']
"""

# All "words"
print(re.findall(r'\w+',html))
print()

"""
['html', 'body', 'Hello', 'This', 'is', 'string', 'in', 'HTML', 'format', 'a',
'href', 'http', 'foo', 'com', 'Link', '1', 'a', 'Here', 's', 'another', 'link',
'a', 'href', 'http', 'bar', 'com', 'Link', '2', 'a', 'body', 'html']
"""
