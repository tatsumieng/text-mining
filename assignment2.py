import urllib.request
import random
import string
from thefuzz import fuzz

# analyzing romeo and juliet text
url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt' 
with urllib.request.urlopen(url) as f:
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    # print(text) # for testing

def process_file(filename, skip_header):
    """
    Makes a histogram that contains the words from the file.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    strippables = string.punctuation + string.whitespace

    for line in fp:
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def total_words(hist):
    """
    Returns the word frequencies for all words in the text
    """
    total = 0
    for freq in hist.values():
        total += freq
    return total

def most_common(hist, excluding_stopwords=False):
    """
    Makes a list of word frequency pairs in descending order by frequency.
    """
    common_words = []
    stopwords = process_file('data/stopwords.txt', False)
    stopwords = list(stopwords.keys())

    for word, freq in hist.items():
        if word in stopwords:
            hist[word] = None
        else:
            t = (freq, word)
            common_words.append(t)
    
    common_words.sort(reverse=True)
    
    return common_words

def print_most_common(hist, num=10):
    """
    Prints the top 10 most commons words in the histgram
    as well as their frequencies.
    """
    t = most_common(hist, excluding_stopwords=True)
    print ('The most common words are:')
    for freq, word in t[:num]:
        print (word, '\t', freq)

def subtract(d1, d2):
    """
    Returns a dictionary with all keys that appear in d1 but not d2.
    """
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res 

def similarity(content1, content2):
    """
    Will return the similarity percentage between two texts
    """
    print(f'The similarity ratio between Hamlet and Romeo and Juliet is:')

def main():
    hist = process_file('data/romeoandjuliet.txt', skip_header=True)
    # print(hist)
    print('Total number of words:', total_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:10]:
         print(word, '\t', freq)

    hamlet = process_file('data/hamlet.txt', skip_header=False)
    romeoandjuliet = process_file('data/romeoandjuliet.txt', skip_header=False)

    diff = subtract(hist, hamlet)
    print("The words in romeo and juliet that aren't in hamlet are:")
    for word in diff.keys():
        print(word, end=' ')

    content1 = romeoandjuliet
    content2 = hamlet
    similarity(content1, content2)

if __name__ == '__main__':
    main()