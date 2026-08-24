# Practice Task 4: Read a file and count words.
import os

def count_words_in_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file at '{filepath}' was not found.")
        
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        return len(words)

def main():
    print("=== File Word Counter ===")
    
    # Let's check for notes.txt or python-basics.md, or create a quick test file
    test_filename = "practice_sample.txt"
    if not os.path.exists(test_filename):
        with open(test_filename, "w", encoding="utf-8") as f:
            f.write("Welcome to Day 1 of the AI and Machine Learning Workshop.\n")
            f.write("Today we are practicing Python basics like loops, functions, and file handling!\n")
            f.write("This file is a sample file created dynamically for the word counter tool.\n")
        print(f"Created a sample file for testing: '{test_filename}'")
        
    filename = input(f"Enter file path to count words (default: {test_filename}): ").strip()
    if not filename:
        filename = test_filename
        
    try:
        count = count_words_in_file(filename)
        print(f"✔️ The file '{filename}' has {count} words.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
