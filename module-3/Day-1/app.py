f_x = lambda x: x**2 + 5*x + 3
five = f_x(5)
print(f_x(5))

f_x = lambda x,y: x**2 + 5*x*y + 3
five = f_x(5,2)
print(f_x(5,2))

def f_x(x):
    y = x**2 + 5*x + 3
    return  y
numbers = [1,2,3,4,5,6,7,8,9,10]
y = [f_x(x) for x in numbers]
print(y)

#map example
map_example = list(map(f_x, numbers))
print(map_example)

my_string = "hello, everyone! i'm nidhi and i'm presenting my culture which is very famous in nepal"
upper_string = my_string.upper()
upper_string_lambda = lambda x : x.upper()

def func_upper(word):
    if word.startswith("c"):
       a =  word.title()
    else:
        a = word.upper()
    return a

print(my_string.split())

splited_list = my_string.split(" ")
final_ans = list(map(func_upper, splited_list))
print(my_string.title())
print(my_string.capitalize)
print(final_ans)

jpt_list = "This is the world where we live and sleep"
def func_jpt(word, index):
    if index % 2 == 0:
        result_word = word.upper()
    else:
        result_word = word.title()
        return result_word

result = " ".join([func_jpt(word, index) for index, word in enumerate(jpt_list.split())])
print(result)
