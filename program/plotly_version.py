import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

plt.ion()


files_to_read = [
    r"C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1.txt",
    r"C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1_new.txt"
]

CHUNK_SIZE = 400
OUTPUT_FILE = r"C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\graphs\all_word_graphs_separate_by_file.html"


figures_html = ""

# -----------------------------
# PROCESS EACH FILE SEPARATELY
# -----------------------------
for file_index, path in enumerate(files_to_read):
    word_count_dict = {}  # reset dictionary for each file

    try:
        with open(path, 'r', encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            for word in words:
                word = word.lower().strip('.,!?;"()[]{}')
                if word:
                    word_count_dict[word] = word_count_dict.get(word, 0) + 1
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.\n")
        continue
    except Exception as e:
        print(f"An unexpected error occurred while reading {path}: {e}\n")
        continue

    # -----------------------------
    # SORT AND SPLIT INTO CHUNKS
    # -----------------------------
    items = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)
    chunks = [items[i:i + CHUNK_SIZE] for i in range(0, len(items), CHUNK_SIZE)]

    # -----------------------------
    # GENERATE FIGURES FOR THIS FILE
    # -----------------------------
    figures_html += f"<h2>File {file_index+1}: {os.path.basename(path)}</h2>"

    for i, chunk in enumerate(chunks):
        words_chunk, counts_chunk = zip(*chunk)
        fig = go.Figure(
            go.Bar(
                x=words_chunk,
                y=counts_chunk,
                marker=dict(
                    color=counts_chunk,
                    colorscale=[
                        [0.0, "rgb(150,200,225)"],  # light blue
                        [1.0, "rgb(0,30,120)"]      # dark blue
                    ]
                )
            )
        )

        fig.update_layout(
            title=f"Word Frequency Graph {i+1} (File {file_index+1})",
            xaxis_title="Word",
            yaxis_title="Count",
            height=600
        )

        figures_html += fig.to_html(full_html=False, include_plotlyjs=False)
        figures_html += "<hr>"

# -----------------------------
# WRAP IN HTML AND SAVE
# -----------------------------
full_html = f"""
<html>
<head>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
<h1>All Word Frequency Graphs (Separate by File)</h1>
{figures_html}
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Saved:", OUTPUT_FILE)


# files_to_read = [ r"C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1.txt", 
#                   r"C:\Users\dunky\Desktop\New folder\school\ENG101\final\ENG-101-Final-Project\text-files\assignment_1.txt" 
#                 ]

# word_count_dict = {}

# for path in files_to_read:
#     try:
#         with open(path, 'r', encoding = "utf-8" ) as file:
#             content = file.read()
#             words = content.split()
#             for word in words:
#                 word = word.lower().strip('.,!?;"()[]{}')
#                 if word:
#                     word_count_dict[word] = word_count_dict.get(word, 0) + 1
#     except FileNotFoundError:
#         print(f"Error: The file at {path} was not found.\n")
#     except Exception as e:
#         print(f"An unexpected error occurred while reading {path}: {e}\n")
        
        
# # Plotting the word frequency


# # -----------------------------
# # SETTINGS (YOU CAN CHANGE THIS)
# # -----------------------------
# CHUNK_SIZE = 100      # <--- Change this number
# OUTPUT_FILE = "all_word_graphs.html"

# # -----------------------------
# # SPLIT INTO CHUNKS
# # -----------------------------
# items = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)

# chunks = [items[i:i + CHUNK_SIZE] for i in range(0, len(items), CHUNK_SIZE)]

# # -----------------------------
# # GENERATE ALL FIGURES
# # -----------------------------
# figures_html = ""

# for i, chunk in enumerate(chunks):
#     words = [w for w, _ in chunk]
#     counts = [c for _, c in chunk]

#     fig = go.Figure(
#         go.Bar(
#             x=words, 
#             y=counts,
#             marker=dict(
#                 color=counts,          # <--- color by frequency
#                 colorscale=[
#                 [0.0, "rgb(150,200,225)"],  # light blue
#                 [1.0, "rgb(0,30,120)"]      # dark blue
#             ]
#             )
#         )
#     )

#     fig.update_layout(
#         title=f"Word Frequency Graph {i+1}",
#         xaxis_title="Word",
#         yaxis_title="Count",
#         height=600    # you can change this
#     )

#     # Convert each graph to HTML fragment
#     figures_html += fig.to_html(full_html=False, include_plotlyjs=False)
#     figures_html += "<hr>"  # separator between graphs

# # -----------------------------
# # WRAP IN FULL HTML DOCUMENT
# # -----------------------------
# full_html = f"""
# <html>
# <head>
# <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
# </head>
# <body>
# <h1>All Word Frequency Graphs</h1>
# {figures_html}
# </body>
# </html>
# """

# # -----------------------------
# # SAVE TO FILE
# # -----------------------------
# with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
#     f.write(full_html)

# print("Saved:", OUTPUT_FILE)

