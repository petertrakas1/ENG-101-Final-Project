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

CHUNK_SIZE = 450

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
    # SORT WORDS BY FREQUENCY
    # -----------------------------
    items = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)

    # -----------------------------
    # TOP 10 MOST COMMON WORDS GRAPH
    # -----------------------------
    top_n = 15
    top_items = items[:top_n]

    if len(top_items) > 0:
        top_words, top_counts = zip(*top_items)

        top_fig = go.Figure(
            go.Bar(
                x=top_words,
                y=top_counts,
                marker=dict(
                    color=top_counts,
                    colorscale=[
                        [0.0, "rgb(255,200,150)"],  # light orange
                        [1.0, "rgb(180,80,0)"]      # dark orange
                    ]
                )
            )
        )

        top_fig.update_layout(
            title=f"Top {top_n} Most Common Words (File {file_index+1})",
            xaxis_title="Word",
            yaxis_title="Count",
            height=500
        )

        figures_html += f"<h2>File {file_index+1}: {os.path.basename(path)}</h2>"
        figures_html += top_fig.to_html(full_html=False, include_plotlyjs=False)
        figures_html += "<hr>"

    # -----------------------------
    # SPLIT ITEMS INTO CHUNKS OF 400 WORDS
    # -----------------------------
    chunks = [items[i:i + CHUNK_SIZE] for i in range(0, len(items), CHUNK_SIZE)]

    # -----------------------------
    # GENERATE CHUNK GRAPHS
    # -----------------------------
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
