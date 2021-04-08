# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    if(type(N) == int and N < 2147483647 and N > 0):
        N = b(N)
    
        string = str(N)

        

        if(len(string)>2):
            
            l = split(string)
            inter = arange(l)
            
            
            if(len(inter) > 0):
                size = max(inter)
                size = len(str(size))
            else:
                size = 0
            
            #print(l, inter, size)
            return size

        

    else:
        return 0



def b(n):
    return bin(n).replace("0b", "")

def split(s):
    final = []
    tmp = ""
    i = 0
    for char in s:
        if char=="1":
            final.append(tmp)
            final.append(char)
            tmp = ""
        else:
            tmp += char
        if(i == len(s)-1 and char =="0"):
            final.append(tmp)
        i +=1
    return final[1:]

def arange(l):
    final = []
    if(len(l) % 2 != 0):
        for i in range(1, len(l)-1):
            if( contains(l[i]) and l[i-1] == l[i+1] == "1"):
                final.append(l[i])
    else:
        for i in range(1, len(l)-1):
            if( contains(l[i]) and l[i-1] == l[i+1] == "1"):
                final.append(l[i])

    return final

def contains(string):
    for i in string:
        if i!="0":
            return False
        else:
            return True


if __name__ == "__main__":
    print(solution(6291457))