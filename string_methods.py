b='hello PYTHON'
print(b.capitalize()) # Hello

x='HI HELLO'
print(x.casefold()) # hi hello

e='pavan'
print(e.center(20,"0")) # answer is center

h='i like bullet bike,bullet bike is my fvt bike'
print(h.count('bullet')) # answer is 2

a='my name is pavan'
# # print(a.encode())  # answer bytes b

# # h='hello, welcome to my world .  '
# # print(h.endswith('.'))       # if ending with specified valu its True other wise false


g='h\te\tl\tl\to'
print(g.expandtabs(5))  # between  specified number of whitespaces

f='hello,welcome to my world'
print(f.find('my'))  # find value 17

e='my name is {;pavan}'
print(e.format_map())

R="Hello,welcome to my world"
print(R.index('world'))  # index value 20

# # h='45hellogoodmorning' 
# # print(h.isalnum())   # all are alphanumeric values True are False

# # w='hellopython'
# # print(w.isalpha()) # all are alphabets only True

# # t='0057'
# # print(t.isdecimal())  # decimal True

# # q="3490"
# # print(q.isdigit()) # True

# # i='hellopython'
# # print(i.isidentifier()) # True

# # s='hello world'
# # print(s.islower()) # all are lowercase True

# # f='HELLO WORLD'
# # print(f.isupper())  # all are uppercase True

# # z='5264'
# # print(z.isnumeric())  # only numbers True are False

# # t='hi hello welcome to world'
# # print(t.isprintable())      # True

# # u="   "
# # print(u.isspace())  # with space its True

# # d='Hello,Welcome To My World'
# # print(d.istitle())            # starting letters will uppercase True

# # web=("hello","welcome","to","python")
# # print("/".join(web))       # hello/welcome/to/python

# # s="apple"
# # print(s.ljust(20,"0"))  # apple000000000000000

# from re import X


# # txt="   banana    "
# # X=txt.lstrip()
# # print("of all fruits",X,"is my favorite") # of all fruits banana    is my favorites

# # y="hello python"
# # X=(y.maketrans("p","w"))
# # print(y.translate(X))      # replaces w answer wython

# # e="I could eat apples all day"
# # print(e.partition("apples"))   # ('I could eat ', 'apples', ' all day') tuple three elements

# # h='i like games'
# # print(h.replace("games","videos"))  # replace videos i like videos

# # o='Hello, welcome to my world'
# # print(o.rfind("t"))             # 15  (-1 )

# # t="Hello, welcome to my world"
# # print(t.rindex("m"))        # 18

# # we="apple"
# # print(we.rjust(20,"0"))   # 000000000000000apple

# # j='I could eat bananas all day, bananas are my favorite fruit'

# # print(j.rpartition('bananas'))                     # ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')


# # re='apple,bananas,cherrys'
# # print(re.rsplit(','))       #  ['apple', 'bananas', 'cherrys']

# # us='   apple   '
# # re=us.rstrip()
# # print('my favorite fruit',re,'one of the best fruit')  # my favorite fruit    apple one of the best fruit

# # q='welcome to the world'
# # print(q.split())         # ['welcome', 'to', 'the', 'world']

# # f='hi hello welcome\nto the my world' 
# # print(f.splitlines())       # ['hi hello welcome', 'to the my world']

# # you=' Hello,welcome to the world.'
# # print(you.startswith('Hello'))      # false

# # b="    cherry    "
# # c=b.strip()
# # print(' is my favorite fruit',c,'and healthly')   #  is my favorite fruit cherry and healthly

# # k='HELLO,welCOME To My WOrld'
# # print(k.swapcase())          #   hello,WELcome tO mY woRLD

# # x='welcome to my world'
# # print(x.title())       # starting letter is uppercase answer Welcome To My World

# # txt = "Hello python"
# # mytable = txt.maketrans("y", "r")
# # print(txt.translate(mytable))       # Hello prthon

# # m="56"
# # print(m.zfill(11))    # 0000000000056
