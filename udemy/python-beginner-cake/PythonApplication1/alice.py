def build_index(f):
    book_index = {}
    for line in f:
        words = line.split() # splits line into words between spaces
        for w in words:
            if w[-1] in ('.',',','!',':',';','?','\'', '\"'): # remove punctuation
                w = w[:-1]
            word = w.lower() # prevents duplicates
            if word in book_index:
                book_index[word] = book_index[word] + 1
            else:
                book_index[str(word)] = 1
    return book_index


def sort_index(book_index):
    word_list = book_index.items() # create a list of key, value pairs from the dict book_index
    top_twenty = sorted(word_list, key = lambda count: count[1], reverse = True) # sorts list based on second element in reverse
    for i in range (0,20):
        print(top_twenty[i])


def main():
    f = open('alice.txt', 'rU')
    book_index = build_index(f)
    print("book index generated successfully")
    f.close()
    sort_index(book_index)
    

if __name__ == '__main__':
     main()
