import re

wordsFile = "AwordsBox/AwordsBox1/words.txt" 
convFile = "AwordsBox/AwordsBox1/conversation2.txt" 

counted_matched_words = {}
matched_words = []
matched_words2 = {}
matched_words3 = {}
non_matched_words = [] 
non_matched_words2 = []
non_matched_words3 = [] 


def list_making(file):
    with  open(file, 'r') as file:
        content = file.read().lower()
    wordsList = re.sub(r"[^a-zA-Z0-9 ]", " ", content).split()
    return wordsList

def searching(keywords, valuewords, level = None):
    for keyword in keywords:
        list = []
        for valueword in valuewords:
            pattern = r"\b" + keyword[:level] + r"\w*\b" 
            matches = re.findall(pattern, valueword)     
            list.extend(matches) 
        if len(list) > 0:
            list.append(len(list))
            if level is None:
                counted_matched_words[keyword] = list
                matched_words.append(keyword)
            elif level == -1:
                matched_words2[keyword] = list
            else:
                matched_words3[keyword] = list

        else:
            if level is None:
                non_matched_words.append(keyword)
            elif level == -1:
                non_matched_words2.append(keyword) 
            else:
                non_matched_words3.append(keyword)











print("-------------------First Level Search------------------")
searching(list_making(wordsFile), list_making(convFile)) 
print("-------------------matched words with count------------------")
print(counted_matched_words, "\n") 
print("-------------------matched words------------------")
print(matched_words, "\n") 
print("-------------------non matched words------------------")
print(non_matched_words, "\n")
print("\n \n") 




print("-------------------Second Level Search------------------")
searching(non_matched_words, list_making(convFile), -1) 
print("-------------------new matched words------------------")
print(matched_words2, "\n") 
print("-------------------non matched words------------------")
print(non_matched_words2, "\n")
print("\n \n") 



print("-------------------Third Level Search------------------")
searching(non_matched_words2, list_making(convFile), -2) 
print("-------------------new matched words------------------")
print(matched_words3, "\n") 
print("-------------------non matched words------------------")
print(non_matched_words3, "\n")
print("\n \n") 



