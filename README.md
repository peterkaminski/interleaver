# Interleaver - interleave two strings of text

Interleaver is a simple Flask-based web application that interleaves two input texts word by word and displays the result. This application provides a straightforward web interface where users can input two separate texts and get them interleaved. Additionally, users can copy the output to their clipboard with a single click.

## Features

- Interleave two texts word by word.
- Condense whitespaces in inputs to a single space.
- Preserve the case of the input texts.
- Basic and clean web interface, accessible and responsive for both mobile and desktop.
- "Copy to Clipboard" functionality for easy output text copying.

## Installation

To run the Interleaver app, you'll need Python installed on your system. This app was developed with Python 3, so ensure you have Python 3.6 or newer.

### Step 1: Clone the Repository

Clone this repository to your local machine using git:

```bash
git clone https://github.com/peterkaminski/interleaver.git
cd interleaver
```

If you're not using git, you can simply download the source code as a ZIP file and extract it.

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for Python projects. This keeps dependencies required by different projects separate by creating isolated environments for them. You can create one using:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

Install the Flask web framework:

```bash
pip install Flask
```

### Step 4: Run the Application

Navigate to the directory containing `app.py` and run:

```bash
python app.py
```

### Step 5: Access the Web App

Open a web browser and navigate to `http://127.0.0.1:5000/`. You should see the Interleaver web interface.

## Usage

1. Enter text into the "Text 1" and "Text 2" input fields on the web page.
2. Click the "Interleave" button to merge the texts.
3. The interleaved text will be displayed in the output area below the button.
4. Click the "Copy to Clipboard" button next to the output area to copy the interleaved text.

## Support

For support, please open an issue in the GitHub repository.

## Contributing

Contributions to the Interleaver project are welcome. Please fork the repository and submit a pull request with your improvements.

## Initial Development with ChatGPT 4

The initial version of Interleaver was written by ChatGPT, with prompting by Peter Kaminski:

https://chat.openai.com/share/10480578-dbee-4128-88ee-9ab17faaaaaa

## License

This project is licensed under the MIT License. See the LICENSE file for details.
