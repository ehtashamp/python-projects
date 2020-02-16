"""
Regular expression program.
"""
import re
#help(re.match)
match = re.match('th','this is a sample text')
#They are case insensitive.
#they match characters and not words.

if match:
    print("simple match")
    print(match)
    print(match.start())
    print(match.end())
    print(match.span())
    print(match.group())
matchs = re.search('Is','these is a sample text')
#They are case sensitive.
if matchs:
    print("search match")
    print(matchs)
    print(matchs.start())
    print(matchs.end())
    print(matchs.span())
    print(matchs.group())
matchitr = re.finditer('bc','abcbcbc', flags=re.I)
#returns iterbale object
for m in matchitr:
    if m:
        print("iterable match")
        print(m)
        print(m.start())
        print(m.end())
        print(m.span())
        print(m.group())
matchfndall = re.findall('IS', 'This is a sample string with Is.', flags=re.I)
#case insensitive
#returns lists
print("findall match")
print(matchfndall)
pattern = re.compile('IS', flags=re.I)
matchptrn = pattern.search('This is a sample string with Is.')
if matchptrn:
    print("pattern maatch match")
    print(matchptrn)
    print(matchptrn.start())
    print(matchptrn.end())
    print(matchptrn.span())
    print(matchptrn.group())

# dot operator
mreg = re.search('.....is\.','This is a sample string with Is.', flags=re.I)
if mreg:
    print("dot search output")
    print(mreg.group())
else:
    print("patterns not found")

mreg = re.search('ab{,10}','This is abbbb sample string with Is.', flags=re.I)
if mreg:
    print("{n,m} output")
    print(mreg.group())
else:
    print("patterns not found")

mreg = re.search('\w*\s*\w*\s?\w?','This is abbbb sample string with Is.', flags=re.I)
if mreg:
    print("shortcut word digit and spaces output")
    print(mreg.group())
else:
    print("patterns not found")