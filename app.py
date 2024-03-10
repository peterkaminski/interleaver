#!/usr/bin/env python3

# Interleaver v1.0.0 - https://github.com/peterkaminski/interleaver

# Copyright 2024 Peter Kaminski. Licensed under MIT license, see accompanying LICENSE file.

from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interleaver</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .container { max-width: 600px; margin: auto; }
        label, button, .output { display: block; margin-top: 20px; }
        textarea { width: 100%; }
        #output { white-space: pre-wrap; }
        .error { color: red; }
    </style>
</head>
<body>
<div class="container">
    <h1>Interleaver</h1>
    <form method="post">
        <label for="text1">Text 1:</label>
        <textarea id="text1" name="text1" rows="4"></textarea>
        <label for="text2">Text 2:</label>
        <textarea id="text2" name="text2" rows="4"></textarea>
        <button type="submit">Interleave</button>
    </form>
    <div class="output">{{output}}</div>
    {% if error %}
        <div class="error">{{error}}</div>
    {% endif %}
    <button onclick="navigator.clipboard.writeText(document.querySelector('.output').innerText)">Copy to Clipboard</button>
</div>
<script>
    // Optionally, add any JavaScript here for dynamic behavior, like the copy to clipboard functionality.
</script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def interleave_texts():
    output = ""
    error = ""
    if request.method == 'POST':
        text1 = request.form.get('text1', '')
        text2 = request.form.get('text2', '')
        try:
            output = interleave(text1, text2)
        except Exception as e:
            error = str(e)
    return render_template_string(HTML_TEMPLATE, output=output, error=error)

def interleave(text1, text2):
    # Condense whitespace and split the texts into words
    words1 = re.sub(r'\s+', ' ', text1.strip()).split(' ')
    words2 = re.sub(r'\s+', ' ', text2.strip()).split(' ')
    
    # Interleave words
    interleaved = []
    for w1, w2 in zip(words1, words2):
        interleaved.append(w1)
        interleaved.append(w2)
    # Append the remaining words from the longer text
    longer_tail = words1[len(words2):] if len(words1) > len(words2) else words2[len(words1):]
    interleaved.extend(longer_tail)
    
    return ' '.join(interleaved)

if __name__ == '__main__':
    app.run(debug=True)
