number=int(input("please enter the number to generate the multipliaction table"))
start=int(input("specify the starting range"))
end=int(input('specify the ending range'))
def multiGen(number):
    for i in range(start,end+1):
        print(f" {number}*{i}= {number*i}")
multiGen(number)