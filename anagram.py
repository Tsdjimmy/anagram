def find_anagrams(str1, str2):
    if(sorted(str1) == sorted(str2)):
        print("True")
    else:
        print("False")

str1 ="silent"
str2 = "listen"
find_anagrams(str1,str2)

str1 ='cigar'
str2 ='bush'
find_anagrams(str1,str2)