markdown
# Docx scanner

## What the project is

My goal is a Python program that reads a Word document and does some basic searches on the text. It finds the most common words, and it finds the most common phrases too. I first planned to read PDF files, but I changed to .docx. Word keeps its text in clear paragraphs, so getting the text out is easier than it is with a PDF.

## What I have finished

The word counting and the phrase counting are both written. Here is what each function does:

1. `docimport_clean` takes the path of a Word file and returns a list of clean lowercase words with the punctuation removed. It joins the paragraph text with a single space, lowercases it, removes punctuation with `re.sub(r"[^\w\s]", "", text)`, and then splits it into words.
2. `RemoveCommonWords` calls `docimport_clean` and drops every word that is in my `common_words` list.
3. `CountMostCommonWord` counts every word with `Counter` and prints and returns the 150 most common.
4. `CountMostCommonWord_CommonExcluded` does the same count, but on the list from `RemoveCommonWords`, so the common words are left out.
5. `PhrasesOfTwo`, `PhrasesOfThree`, `PhrasesOfFour` and `PhrasesOfFive` count phrases of that many words in a row. The first two print and return the top 150, and the last two print and return the top 50. These four use `docimport_clean` directly, so common words are not removed from the phrases.

Every function takes a file path as a string and has a docstring that describes what it does.

## Decisions I made

- Punctuation gets deleted, and nothing replaces it. A word like "don't" turns into "dont", which I am happy with for this project.
- For finding punctuation I chose the pattern `[^\w\s]` over `string.punctuation`. Word often swaps straight quotes for curly ones and adds long dashes, and the `string.punctuation` list misses both of those.
- I use `Counter` instead of building my own dictionary, because it counts the words for me.
- My `common_words` list holds only the most general grammar words, such as "the", "and" and "of". Gendered pronouns like "she" and "her" are not in it, because they say something about who a book is about.
- To build a phrase, I join a word with its neighbours using `" ".join(...)`. An `if` check stops the loop early enough that it never asks for a word past the end of the list.
- Each phrase function reads `docimport_clean` once and keeps the result in a variable, so the Word file is only opened one time per call.