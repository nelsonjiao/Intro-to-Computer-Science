# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.
# Below code is from stackoverflow.
# http://stackoverflow.com/questions/10809302/string-split-issue

def split_string(source,splitlist):
    result = []
    lasti = -1
    for i, e in enumerate(source):
        if e in splitlist:
            tmp = source[lasti+1:i]
            if tmp not in splitlist:
                result.append(tmp)
            lasti = i
        if e not in splitlist and i == len(source) - 1:
            tmp = source[lasti+1:i+1]
            result.append(tmp)
    return result

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']