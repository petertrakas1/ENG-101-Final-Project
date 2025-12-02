import os
import matplotlib.pyplot as plt

###  C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1_new.txt
#print( os.path.exists("text-files\\assignment_1.txt") )
#print( os.getcwd() )
#print( os.path.exists("C:\\Users\\dunky\\Desktop\\New folder\\school\\ENG101\\final\\ENG-101-Final-Project\\text-files\\assignment_1.txt") )

files_to_read = [ "text-files/assignment_1.txt", 
                  "text-files/assignment_1_new.txt" 
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
            print(f"Contents of {path}:\n{content}\n")
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.\n")
    except Exception as e:
        print(f"An unexpected error occurred while reading {path}: {e}\n")
        
print("Word Count Dictionary:")
print( word_count_dict )



# Plotting the word frequency

words = list(word_count_dict.keys())
frequencies = list(word_count_dict.values())
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title('Word Frequency Distribution')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
