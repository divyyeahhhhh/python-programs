def count(str1 ,str2) :
    # set of characters of string1
    set_string1 = set(str1)
 
    # set of characters of string2
    set_string2 = set(str2)
 
    # using (&) intersection mathematical operation on sets
    # the unique characters present in both the strings
    # are stored in matched_characters set variable
    matched_characters = set_string1 & set_string2
 
    # printing the length of matched_characters set
    # gives the no. of matched characters
    print("No. of matching characters are : " + str(len(matched_characters)) )
 
 
# Driver code
if __name__ == "__main__" :
 
    str1 = 'what'  # first string
    str2 = 'watch'     # second string
 
    # call count function
    count( str1 , str2 )
    
