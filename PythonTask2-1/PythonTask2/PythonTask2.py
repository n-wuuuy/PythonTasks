def Replse(text):
    return print(text.translate(str.maketrans({'"':"'","'":'"'})))

slovo=input("Vvedite tekst");
Replse(slovo)

