# phyton function

# define a new function that will get the AT content of the DNA
# we decide to give the function a name: get_at_content
# the function only needs a DNA sequence as an input
# the only thing that comes out of a function is what we tell it to return
#
# Our AT content function
def get_at_content(some_dna):
    length = len(some_dna)
    a_count = some_dna.upper().count('A')
    t_count = some_dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return at_content

# Call the function to process our input
# get_at_content(), didalam
at = get_at_content("actgatacatatatatcgatgcgttcat")
print(at)

# Write the AT content for a sequence to a file
with open('output.txt', 'w') as result :
   result.write(str(get_at_content('ACTGTcGa')))


# Our AT content function, v2, two decimal places
def get_at_content_v2(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)     #we modify the result value directly in the function



# Our AT content function, v3, specify number of significant figures
def get_at_content_v3(dna, sig_figs):           # function, boleh multiple arguments
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

at = get_at_content_v3("ATGCGTATtttTGAGCA",4)
print(at)

# What happens if you forget to put in how many significant figures you want
# how to check your function. Put it in try
# We could try it first!
try :
  try_try = get_at_content_v3("ATGCGTATtttTGAGCA")
  print(try_try)
except :
  f'Nah, ya broke it, numpty!'

def get_at_content_v4(dna, sig_figs=2):           # function, boleh multiple arguments
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, sig_figs)

at_4 = get_at_content_v4("ATGCGTATtttTGAGCA")   # ini tetep jalan karena kita set default argument buat sig_figs =2
print(at_4)

# testing testing testing
testing_func_4_1 = get_at_content_v4("A")
print(testing_func_4_1)
testing_func_4_2= get_at_content_v4("t")
print(testing_func_4_2)
testing_func_4_3= get_at_content_v4("c")
print(testing_func_4_3)

# Use a for loop to check things, calling our function each time!
for base in 'gatcx':
   print("Was A or T? "+ base.upper() + ": " + str(get_at_content_v4(base) == 1))

# another try methods: assert (outputnya bollean)
assert get_at_content_v4("A") == 1
assert get_at_content_v4("AAA") == 1
assert get_at_content_v4("G") == 0
assert get_at_content_v4("ATGC") == 0.5


# Notes   ##############################################################################################################
# code error from the experiment
# read aa_residu argument
split_list_aa = aa_residu.split(",")
length_list = len(split_list_aa)

# fungsi split diatas cuma bisa di string, kalau udah list, ya dia udah iterable. Jadi kalau kita mau filter input aa sebagai single object atau list
# ya dia gak bisa

# In the case of a list, it's already an iterable, meaning you can directly access each element without needing to convert or split it further.
# For example, when you have a list of amino acids, you can iterate over it.