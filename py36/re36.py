import re

pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()
#上述两个要在匹配之后才有值
print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))
    
print("*"*40)
regexes = [#其实这是一个生成器表达式，返回的是生成结果的列表
    re.compile(p)
    for p in ['this', 'that']
]
text = 'Does this text match the pattern?'
print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match')

print("*"*40)
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.findall(pattern, text):
    print('Found {!s}'.format(match))#!后面分别跟s=str(),r=repr(),a=ascii()
    print('Found {!r}'.format(match))#作用是在填充前先用对应的函数来处理参数
    print('Found {!a}'.format(match))

print("*"*40)
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
#与 findall() 返回字符串不同的是， finditer() 函数返回一个产生 Match 实例的迭代器
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(text[s:e], s, e))

print("*"*40)
def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa',
                  [('ab', "'a' followed by 'b'"),])