import os
import sys
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

#print(sys.version)
#print(np.__version__)



###  C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1_new.txt
#print( os.path.exists("text-files\\assignment_1.txt") )
#print( os.getcwd() )
#print( os.path.exists("C:\\Users\\dunky\\Desktop\\New folder\\school\\ENG101\\final\\ENG-101-Final-Project\\text-files\\assignment_1.txt") )

#files_to_read = [ "text-files/assignment_1.txt", 
#                  "text-files/assignment_1_new.txt" 
#                ]

files_to_read = [ r"C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1.txt", 
                  r"C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1.txt" 
                ]

word_count_dict = {}

for path in files_to_read:
    try:
        with open(path, 'r', encoding = "utf-8" ) as file:
            content = file.read()
            words = content.split()
            for word in words:
                word = word.lower().strip('.,!?;"()[]{}')
                if word:
                    word_count_dict[word] = word_count_dict.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.\n")
    except Exception as e:
        print(f"An unexpected error occurred while reading {path}: {e}\n")
        
#print("Word Count Dictionary:")
#print( word_count_dict )

sorted_items = sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)

word_count_dict = dict(sorted_items)



# Plotting the word frequency

words = list(word_count_dict.keys())
frequencies = list(word_count_dict.values())
#print(len(word_count_dict))

items = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)


chunk_size = 100

for i in range(0, len(items), chunk_size):
    chunk = items[i:i + chunk_size]
    
    words, freqs = zip(*chunk)
    
    plt.figure(figsize=(20, 6))
    plt.bar(words, freqs)
    plt.gca().invert_yaxis()
    plt.xticks(rotation=90, fontsize=8)
    plt.title(f"Words {i+1} to {i+len(chunk)}")
    plt.tight_layout()
    #plt.show()
    
    plt.savefig(f"word_freq_{i+1}_{i+len(chunk)}.png")  # ← saves instead of showing
    plt.close()


# plt.figure(figsize=(120, 12))
# plt.bar(words, frequencies, width = .5)
# plt.xticks(rotation=90, fontsize = 3)
# plt.xlabel('Words')
# plt.ylabel('Frequencies')
# plt.title('Word Frequency Distribution')
# plt.tight_layout()
# plt.show()

"""plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title('Word Frequency Distribution')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
"""
