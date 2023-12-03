# f("integrated development environment") returns "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing computer programs") returns "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms" 

def f(toShorten):
    shortened=""
    toShorten=toShorten.split()
    shortened=shortened.join(toShorten)
    return shortened
    
toShorten1= "integrated development environment"
toShorten2=" A programming language is a system of notation for writing computer programs"
print(f(toShorten1))
print(f(toShorten2))