# Brahm Brar, String Notes Python

#string is a data type that holds any info surrounded by quotation marks "" ''

note ="Brahm's class"

name = input("what is your first name\n").strip().capitalize()

#print(f"hello {name} welcome to my program!)
print(f"this is your name"+ name)

print(note)

sentence = "The quick brown fox jumps over the lazy dog"

#print(len(sentence))
#print(sentence[4])
start= sentence.find("brown")
length= len("brown")
print(sentence[start:start+length])