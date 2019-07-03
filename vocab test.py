import xlrd
import random

# initialise the spreadsheet
workbook = xlrd.open_workbook('drops_es.xlsx')
workbook = xlrd.open_workbook('drops_es.xlsx', on_demand = True)
worksheet = workbook.sheet_by_index(0)

# build the master dictionary
first_row = []
for col in range(worksheet.ncols):
    first_row.append(worksheet.cell_value(0,col))
en_es =[]
for row in range(1, worksheet.nrows):
    element = {}
    for col in range(worksheet.ncols):
        element[first_row[col]]=worksheet.cell_value(row,col)
    en_es.append(element)

# build a list of categories
cat_list=[]
for row in range(1, worksheet.nrows):
    category=worksheet.cell_value(row,0)
    if category not in cat_list:
        cat_list.append(category)
    
# display list of categories
for i in cat_list:
    print(cat_list.index(i)+1," ",i)
print(" ")

# choose a category and build the sub dictionnary

cat_value=input("Choose a Category from the above ")
cat_int=int(cat_value)-1
cat_choice=cat_list[cat_int]
print(" ")
print("YOU CHOSE:",cat_choice)

subdict={}
rdict={}
if cat_int==0:
## build a dictionnary of ten random words from the master
    for item in en_es:
        key=item.get(worksheet.cell_value(0,1))
        value=item.get(worksheet.cell_value(0,3))
        rdict[key]=value
    random_keys = random.sample(list(rdict.keys()), 10)
    random_values = [rdict[k] for k in random_keys]
    subdict = dict(zip(random_keys, random_values))
        
else:
    for item in en_es:
        if cat_choice in item.values():
            key=item.get(worksheet.cell_value(0,1))
            value=item.get(worksheet.cell_value(0,2))
            subdict[key]=value
test_len=len(subdict.keys())


        
# define the test function
def test():
    turns=0
    test_len=len(subdict.keys())
    print("There are",test_len,"questions")
    print(" ")
    while subdict!={}:
        en_list=list(subdict.keys())
        random.shuffle(en_list)

        for keyword in en_list:
            display="{}"
            print("QUESTION: ",display.format(keyword))
            userInputAnswer=input("ANSWER:    ")
            if userInputAnswer==(subdict[keyword]):
                print("CORRECT")
                del subdict[keyword]   
            else:
                print("INCORRECT:",subdict[keyword])
            turns+=1
            print(" ")
            print("You've had",turns,"turns, with",len(subdict.keys()),"questions left.")
            print('_'*25)
            print(" ")
    return turns

# run the test
count=(test())
print(" ")
print("Well Done! You're hit rate was",round(100*test_len/count),"%")
print(" ")
print('_'*25)







