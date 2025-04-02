from bs4 import BeautifulSoup

def extract_words_from_html(html_file_path, output_file_path):
    """
    Reads an HTML file, extracts all words, and writes them to a text file,
    one word per line.

    Args:
        html_file_path (str): The path to the input HTML file.
        output_file_path (str): The path to the output text file.
    """

    try:
        # Read file in binary mode first
        with open(html_file_path, 'rb') as html_file:
            content = html_file.read()
        
        # Try different encodings
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        decoded_content = None
        
        for encoding in encodings:
            try:
                decoded_content = content.decode(encoding)
                break
            except UnicodeDecodeError:
                continue
        
        if decoded_content is None:
            raise Exception("Could not decode the file with any supported encoding")

        soup = BeautifulSoup(decoded_content, 'html.parser')

        # Extract text from the body of the HTML
        text_content = soup.body.get_text(separator=' ')  # Use space as a separator

        # Split the text into words (handling punctuation and extra spaces)
        words = text_content.split()
        words = [word.strip('.,;!?()[]{}<>"\'') for word in words]  # Remove punctuation
        words = [word for word in words if word]  # Remove empty strings

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for word in words:
                output_file.write(word + '\n')

        print(f"Successfully extracted and saved words to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: HTML file '{html_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python extract_words_from_html.py <input_html_file> <output_txt_file>")
        sys.exit(1)
    
    html_file = sys.argv[1]
    output_file = sys.argv[2]
    extract_words_from_html(html_file, output_file)
