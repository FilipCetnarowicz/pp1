def f(text):
    text=list(text)
    i=len(text)
    print(f"text1={text}")
    for y in range(len(text)):
        text.append("-")
    print(f"text2={text}")
    for x in range(len(text)//2,-1):
        text[x]=text[x+1]
        text[x+1]="-"
        #text.append("-")
    print(f"text3={text}")
    return str(text)

text="UNIVERSITY"
print(f(text))
