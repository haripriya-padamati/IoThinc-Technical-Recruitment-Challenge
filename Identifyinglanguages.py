def lang():
    n=int(input())
    tcount=0
    scount=0
    for i in range(n):
        l=input().lower()
        for i in l:
            if i=='s':
                scount+=1
            elif i=='t':
                tcount+=1
    if scount>=tcount:
        print("French")
    else:
        print("English")

if __name__ == "__main__":
    lang()
