from collections import Counter

def find_unique_words(string):
    # split the string into words
    words = string.split()
    # use the Counter class to count the occurrences of each word
    word_count = Counter(words)
    # iterate over the word_count dictionary and print each word and its count
    for word, count in word_count.items():
        print(f"{word}: {count}")

        
paragraph = "Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph."

find_unique_words(paragraph)