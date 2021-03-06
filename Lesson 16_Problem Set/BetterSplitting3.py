def split_string(source,splitlist):
    output = []
    atsplit = True #At a split point
    for char in source: #iterate through string by each letter
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                #add character to last word
                output[-1] = output[-1] + char
    return output
	
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print (out)
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print (out)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']