user_string=input("enter the string")
vowels="aeiouAeiou"
digits='0123456789'
specialcharacters="'~!@#$%^&*()_+{}[]-=;:'.,<>?/"
def stringAnalysis(user_string):
    vowel_count=0
    consonants_count=0
    specialchars_count=0
    digits_count=0
    for char in user_string:
        if (char in vowels):
            vowel_count+=1
        elif(char in digits):
            digits_count+=1
        elif(char in specialcharacters):
            specialchars_count+=1
        else:
            consonants_count+=1
    print(f'vovwel count:{vowel_count}, consonant count:{consonants_count}, digits count:{digits_count}, specialcharacters count:{specialchars_count}')
stringAnalysis(user_string)   

def reverseString(user_string):
    rev=user_string[::-1]
    print(f'the reverse of the string is:{rev}')
reverseString(user_string)