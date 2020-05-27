def convert(number):
    resultstr = ""
    if (number % 3 == 0):
        resultstr = resultstr + 'Pling'
    
    if (number % 5 == 0):
        resultstr = resultstr + 'Plang'
    
    if (number % 7 == 0):
        resultstr = resultstr + 'Plong'
    
    if (resultstr == ""):
        resultstr = str(number)
    
    return(resultstr)
