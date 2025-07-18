#strings are immutable 
a = "Hridoy!!!"
print(len(a))
print(a.upper())
print(a.lower())

b = "AbCdEfG!!!"
print(b.lower())

c = "!!!Hridoy!!!"

d = "Hridoy!!Hridoy!!"

e = "Hridoy Hridoy Hridoy"

f = "welcome tO mY coding world"

print(a.rstrip("!")) #3 ta !!! ke soray dibe
print(b.rstrip())
print(c.rstrip("!")) #pichoner !!! soray dileo samner !!! sorate parbe na rstrip

print(d.replace("Hridoy", "Proma")) #d er Hridoy ke Proma diye replace korlam replace method use kore

print(e.split(" ")) #List creation

print(f.capitalize()) #kono line er 1st word capital na hole seta capital kore & sentence er majhe capital hole seta small kore
print(len(f))
print(len(f.center(50))) #website er middle e word ta rakhe

print(e.count("Hridoy")) #e string e Hridoy kotobar seta ber korar jonno count method use kora

print(a.endswith("!")) #a te sentence sheshe ki ! symbol ache ki nai seta check kore

str1 = "Welcome to the console !!!"
print(str1.endswith("to", 4, 10)) #4 theke 10 character er por setar last character ba words ki "to" hobe kina seta check kora

str2 = "He's name is Hridoy. He is an honest man."
print(str2.find("is")) #is koto number character e ache seta ber korbe & is na thakle -1 return korto
print(str2.index("is")) #sentence e is ba alada kichu khujar khettre seta na thakle -1 na diye error dekhay

str3 = "HridoyIsGood"
print(str3.isalnum()) #[alphabet and number] A-Z, a-z, 0-9 er baire kono comma / semi colon etc. ashle false dekhabe

str4 = "Welcom,e"
print(str4.isalnum())

str4 = "Welcome"
print(str4.isalpha()) #[only alphabet]

str4 = "Welcome05"
print(str4.isalpha())

str5 = "hello world"
print(str5.islower())

str5 = "hello worlD"
print(str5.islower())

str5 = "hello worlD"
print(str5.isprintable())

str5 = "hello worlD\n"
print(str5.isprintable()) #\n printable na

str6 = "  "
print(str6.isspace())


str6 = ""
print(str6.isspace())

str7 = "World Health Organization"
print(str7.istitle())

str7 = "To bring a pen"
print(str7.istitle()) #eta kokhono title hote pare na

str8 = "Hridoy is a python programmer"
print(str8.startswith("Hridoy")) #Sentence Hridoy diye shuru hole true na hole false

str8 = "Hridoy is a python programmer"
print(str8.startswith("python"))

str9 = "Hridoy Is A good Boy"
print(str9.swapcase()) #upper case ke lower r lower ke upper case e convert kore

str10 = "His name is hridoy. he is a good person"
print(str10.title()) #sob word er start capitle words diye shuru kore
