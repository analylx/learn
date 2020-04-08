
print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))

"""
Sample Input

177
10
Sample Output

17
7
(17, 7)

FJSevilla is using the string format method. The things in the curly braces (i.e. {}),
are references to the items in the format() method parentheses.
The '\n' means line break. The * means unpack.
The first int(input()) will take the 177 (using the first example), 
and the second one will take the 10.
Those numbers will go into the divmod function. 
The divmod function will produce a tuple that looks like (17, 7).
When that's unpacked you get a 17 and then a 7 and these are printed with a line break separating them.
"""
