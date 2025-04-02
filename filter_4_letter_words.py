import sys

def filter_4_letter_words(input_file, output_file):
    """
    Reads words from an input file, filters for 4-letter words,
    and writes them to an output file.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                word = line.strip().lower()  # Remove whitespace
                if len(word) == 4 and word.isalpha():
                    outfile.write(word + '\n')
        print(f"Successfully filtered 4-letter words from '{input_file}' to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filter_words.py <input_file> <output_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    filter_4_letter_words(input_file_path, output_file_path)
