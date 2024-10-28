import os
from collections import Counter

class WordCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_words(self):
        if not os.path.exists(self.file_path):
            print(f"File '{self.file_path}' not found.")
            return
        
        with open(self.file_path, 'r') as file:
            text = file.read().lower()
            words = text.split()
            word_count = Counter(words)
            
            print(f"Word counts for '{self.file_path}':")
            for word, count in word_count.items():
                print(f"'{word}': {count}")

if __name__ == "__main__":
    file_path = 'example.txt' 
    counter = WordCounter(file_path)
    counter.count_words()
