import docx as doc
import re as re
from collections import Counter
def docimport_clean(FilePath: str):
    '''Reads the Word file at FilePath (a string) and returns its text as a list of clean words. 
    The paragraph text is joined with a single space and lowercased. 
    Any character that is not a letter, digit, underscore or whitespace is then removed, 
    and the result is split into a list of strings.'''
    document = doc.Document(FilePath)
    textlist = []
    for paragraph in document.paragraphs:
        textlist.append(paragraph.text)
    text = " ".join(textlist)
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    working_list = text.split()
    return working_list
    

def RemoveCommonWords(FilePath: str):
    '''Takes FilePath (a string) and returns a list of words from that Word file with the common words left out. 
    It gets the full word list from docimport_clean, 
    then keeps only the words that are not in the built-in common_words list. Nothing is printed.'''
    common_words = ["the", "and", "to", "a", "of", "was", "that", "in", "you", "it",
    "but", "they", "had", "for", "with", "on", "at", "i", "as", "were",
    "their", "them", "from", "all", "be", "into", "so", "what", "then",
    "out", "have", "who", "this", "not", "would", "if", "when", "could",
    "your", "didnt", "other", "about", "me", "by", "there", "we", "did",
    "do", "which", "no", "been", "or", "its", "is", "before", "after",
    "are", "youre", "an", "my", "im", "dont", "up", "down", "off", "over",
    "through", "here", "where", "some", "than", "both", "more", "can",
    "because", "too", "how", "any", "each", "wasnt", "couldnt", "us", "why",]
    final_list = []
    for word in docimport_clean(FilePath):
            if word not in common_words:
                final_list.append(word)
    return final_list

def CountMostCommonWord_CommonExcluded(FilePath:str):
    '''Takes FilePath (a string) and counts the words in that Word file, leaving out the common words. 
    It uses RemoveCommonWords to get the filtered list, then Counter to count each word. 
    It prints the file path followed by the 150 most common words, and returns them as a list of (word, count) pairs.'''
    working_list = RemoveCommonWords(FilePath)
    CountedList = Counter(working_list)
    MostCommon = CountedList.most_common(150)
    print(f"this is the list for {FilePath} \n{MostCommon}")
    return MostCommon

def CountMostCommonWord(FilePath:str):
    '''Takes FilePath (a string) and counts every word in that Word file, common words included. 
    It uses docimport_clean to get the word list, then Counter to count each word. 
    It prints the file path followed by the 150 most common words, and returns them as a list of (word, count) pairs.'''
    working_list = docimport_clean(FilePath)
    CountedList = Counter(working_list)
    MostCommon = CountedList.most_common(150)
    print(f"this is the list for {FilePath} \n{MostCommon}")
    return MostCommon

def PhrasesOfTwo(FilePath):
    '''Counts the two-word phrases in the Word file at FilePath (a string). 
    The word list comes from docimport_clean, and common words are not removed. 
    Each word is joined to the word after it with a single space, 
    and the loop stops before the last word so it never runs past the end of the list. 
    Counter then counts each phrase, and the function prints the file path followed by the 150 most common phrases. 
    It returns them as a list of (phrase, count) pairs.'''
    working_list = docimport_clean(FilePath)
    phrases_list = []
    for i in range(len(working_list)):
         if i < (len(working_list) - 1):
              phrases_list.append(" ".join([working_list[i], working_list[i+1]]))
    CountedList = Counter(phrases_list)
    MostCommon = CountedList.most_common(150)
    print(f"this is the list of two-word phrases for {FilePath} \n{MostCommon}")
    return MostCommon

def PhrasesOfThree(FilePath):
    '''See PhrasesOfTwo'''
    working_list = docimport_clean(FilePath)
    phrases_list = []
    for i in range(len(working_list)):
         if i < (len(working_list) - 2):
              phrases_list.append(" ".join([working_list[i], working_list[i+1], working_list[i+2]]))
    CountedList = Counter(phrases_list)
    MostCommon = CountedList.most_common(150)
    print(f"this is the list of three-word phrases for {FilePath} \n{MostCommon}")
    return MostCommon

def PhrasesOfFour(FilePath):
    '''See PhrasesOfTwo but with 50 instead of 150'''
    working_list = docimport_clean(FilePath)
    phrases_list = []
    for i in range(len(working_list)):
         if i < (len(working_list) - 3):
              phrases_list.append(" ".join([working_list[i], working_list[i+1], working_list[i+2], working_list[i+3]]))
    CountedList = Counter(phrases_list)
    MostCommon = CountedList.most_common(50)
    print(f"this is the list of four-word phrases for {FilePath} \n{MostCommon}")
    return MostCommon

def PhrasesOfFive(FilePath):
    '''See PhrasesOfTwo but with 50 instead of 150'''
    working_list = docimport_clean(FilePath)
    phrases_list = []
    for i in range(len(working_list)):
         if i < (len(working_list) - 4):
              phrases_list.append(" ".join([working_list[i], working_list[i+1], working_list[i+2], working_list[i+3], 
                                            working_list[i+4]]))
    CountedList = Counter(phrases_list)
    MostCommon = CountedList.most_common(50)
    print(f"this is the list of five-word phrases for {FilePath} \n{MostCommon}")
    return MostCommon
              

