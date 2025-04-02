import nltk
from nltk.corpus import words
import sys

def get_nltk_4_letter_words(output_file_path):
    """
    Fetches all words from the NLTK words corpus, filters for 4-letter words,
    and saves them to a text file.

    Args:
        output_file_path (str): The path to the output text file.
    """
    try:
        # Download the NLTK words corpus (only needs to be done once)
        nltk.download('words')

        # Get the list of words from the NLTK corpus
        all_words = words.words()

        # Filter for 4-letter words and convert to lowercase
        four_letter_words = [word.lower() for word in all_words if len(word) == 4]

        # Remove any non-alphabetical characters
        four_letter_words = [''.join(filter(str.isalpha, word)) for word in four_letter_words]

        # Remove empty strings after filtering
        four_letter_words = [word for word in four_letter_words if word]
        
        # Save the 4-letter words to a text file
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for word in four_letter_words:
                outfile.write(word + '\n')

        print(f"Successfully saved 4-letter words to '{output_file_path}'")

    except Exception as e:
        print(f"An error occurred: {e}")
        print(e)

if __name__ == "__main__":
    # Check if the output file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <output_file_path>")
        sys.exit(1)

    output_file_path = sys.argv[1]
    get_nltk_4_letter_words(output_file_path)
