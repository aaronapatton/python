#import spellcheck dictionary
import enchant

d=enchant.Dict("en_US")

# create list of list subsets without repeating
# count should be (2^n)-1



# add number to duplicates

def numbered_dupes (input_list):
    global numbered_list
    char_num = 1
    for x in input_list:
        x+=str(char_num)
        char_num += 1
        numbered_list.append(x)


# generates starter lists with one value
def generate_list(input_list):
    global list_all
    for i in input_list:
        temp_list = [i]
        list_all += [temp_list]
        iterate_list(input_list, i)

# generates two value lists to pass into reiterate function
def iterate_list(input_list, i):
    global list_all
    temp_list=[]
    for j in input_list:
        temp_list = [i] + [j]
        if temp_list not in list_all:
            list_all += [[i]+[j]]
        reiterate_list(input_list, temp_list)


#generates all further iterations of list, removing duplicates
def reiterate_list(input_list, tack_on):
    global list_all
    for k in input_list:
        temp_list=tack_on +[k]
        #temp_list.sort()
        if len(temp_list) == len(set(temp_list)):
            if temp_list not in list_all:
                list_all += [temp_list]
            reiterate_list(input_list, temp_list)

letters = input("Enter characters: ")
min_length = int(input ("Minimum word length: "))

#split input into list
def split(letters):
    return list(letters)

list_start = split(letters)
numbered_list = []
list_all = []
final_list = []

numbered_dupes(list_start)
generate_list(numbered_list)

for i in list_all:
    str_word = ''.join(i)
    word = ''.join([x for x in str_word if not x.isdigit()])
    if len(word) >= min_length:
        if d.check(word) and word not in final_list:
            final_list += [word]

final_list=sorted(final_list, key=len)

for i in final_list:
    print(i)

print("total letter combinations: " + str(len(list_all)))
print("total words found: " + str(len(final_list)))