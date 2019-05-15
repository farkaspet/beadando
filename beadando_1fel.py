import itertools

signs = ('+','-','')
nums = range(1,10)

for someSigns in itertools.product(signs,repeat=9):
    evalStr = ""
    for i, j in zip(someSings,nums):
        evalStr += i + str(int(j))
    try:
        if eval(evalStr) == 100:
            print (evalStr)
    except:
        continue
