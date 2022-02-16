from my_modules.Chapter02_1_classes import TextContainer

print("Chapter03 Exercise 01")
text_container1 = TextContainer("This is the input# text& with 8 words!!!")
print(text_container1.text)
print(text_container1.count_words())
print(text_container1.count_chars())
print(text_container1.count_letters())
print(text_container1.remove_punctuation())

print("END")