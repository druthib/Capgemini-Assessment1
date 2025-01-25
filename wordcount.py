def wordcountcheck(string):
    sentence=string.lower()
    print(sentence)
    punctautions=",!."
    for i in punctautions:
        sentence=sentence.replace(i,"")
    separateWords=sentence.split()
    wordCountList=[]
    for word in separateWords:
        found=False
        for i in wordCountList:
            if i[0]==word:
                i[1]+=1
                found=True
                break
        if not found:
            wordCountList.append([word,1])
    return wordCountList
string=input("enter the string")
wc=wordcountcheck(string)
print('word counts:')
for word,count in wc:
    print(f"{word} occured {count} times")