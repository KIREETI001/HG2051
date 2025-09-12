# # # # greeting.lower 
# # # # greeting.upper
# # # # greeting.capitalize
# # # # greeting.title
# # # # greeting.strip 
# # # # greeting.startswith(pattern) 
# # # # greeting.endswith(pattern) 

# # # # greeting.islower()
# # # # greeting.isupper()
# # # # greeting.istitle()
# # # # greeting.isalpha()
# # # # greeting.isalnum()
# # # # greeting.isdecimal()
# # # # greeting.isspace()
# # # # greeting.isprintable()
# # # # greeting.count(substring)
# # # # greeting.find(substring)
# # # # greeting.index(substring)
# # # # greeting.rfind(substring)

# # # # greeting.replace(old, new)
# # # # greeting.split(separator)
# # # # greeting.join(iterable)
# # # # greeting.format(*args, **kwargs)

# # # # greeting.encode(encoding)
# # # # greeting.decode(encoding)   
# # # # greeting.center(width)
# # # # greeting.ljust(width)
# # # # greeting.rjust(width)
# # # # greeting.zfill(width)
# # # # greeting.partition(separator)
# # # # greeting.rpartition(separator)
# # # # greeting.splitlines(keepends)
# # # # greeting.expandtabs(tabsize)
# # # # greeting.maketrans(x, y, z)
# # # # greeting.translate(table)
# # # # greeting.removeprefix(prefix)
# # # # greeting.removesuffix(suffix)   
# # # # greeting.isidentifier()
# # # # greeting.isascii()
# # # # greeting.casefold()
# # # # greeting.swapcase()
# # # # greeting.format_map(mapping)
# # # # greeting.isnumeric()
# # # # greeting.isdecimal()
# # # # greeting.isdigit()
# # # # greeting.rsplit(separator, maxsplit)
# # # # greeting.rjust(width, fillchar)
# # # # greeting.lstrip(chars)
# # # # greeting.rstrip(chars)
# # # # greeting.partition(separator)
# # # # greeting.rpartition(separator)
# # # # greeting.splitlines(keepends)
# # # # greeting.expandtabs(tabsize)
# # # # greeting.maketrans(x, y, z)
# # # # greeting.translate(table)
# # # # greeting.removeprefix(prefix)

# # # # greeting.removesuffix(suffix)
# # # # greeting.isidentifier()
# # # # greeting.isascii()


# # # request = "eggs and milk and apples"
# # # splrequest = request.split(" and ")
# # # print(splrequest)

# # # guests = ['John', 'Jane', 'Doe']
# # # conjuncntion = " and "
# # # jguests = conjuncntion.join(guests)
# # # print(jguests)
# # # jguests = ", ".join(guests)
# # # print(jguests)  

# # # '-'.join('respect')
# # # print('-'.join('respect'))

# # # x = int(input("Please enter an integer: "))

# # # if x < 0:
# # #     x = 0
# # #     print('Negative changed to zero')
# # # elif x == 0:
# # #     print('Zero')
# # # elif x == 1:
# # #     print('Single')
# # # else:
# # #     print('More')
    
    
# # # Measure some strings:
# # words = ['cat', 'window', 'defenestrate']

# # middle =""

# # for w in words:
# #     middle = w
# #     # if len(w) > 3:
# #         #  print(w, len(w))
# #         #  wd = w.upper()
# #         #  print(wd)
        
   
# # # for num,  item in enumerate(words):
# # #     print(num, item)
# # #     print(words[num])
        
        
# # print(middle)
# # print(middle.upper())

# def fib(n):    # write Fibonacci series less than n
#     """Print a Fibonacci series less than n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# # Now call the function we just defined:
# sequence = fib(2000)
# print(sequence)

import nltk
nltk.corpus.gutenberg.fileids() 
hehe = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
len(hehe)

lines = hehe.splitlines()
len(lines)













