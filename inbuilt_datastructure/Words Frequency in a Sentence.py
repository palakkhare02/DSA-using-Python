def count_word_frequency(sentence):
    # Initialize an empty dictionary to store word frequencies
    word_count = {}
    
    # Split the sentence into words using space as the delimiter
    words = sentence.split()
    
    # Iterate through each word in the list of words
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_count[word] = 1
    
    return word_count
 
