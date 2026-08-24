# Practice Task 3: Count vowels in a string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_counts = {v: 0 for v in "aeiou"}
    total = 0
    
    for char in text:
        if char in vowels:
            vowel_counts[char.lower()] += 1
            total += 1
            
    return total, vowel_counts

def main():
    print("=== Vowel Counter ===")
    while True:
        text = input("\nEnter a string to count vowels (or 'q' to quit): ").strip()
        if text.lower() == 'q':
            print("Goodbye!")
            break
            
        total, break_down = count_vowels(text)
        print(f"\nTotal vowels: {total}")
        print("Details:")
        for v, count in break_down.items():
            print(f"  {v.upper()}: {count}")

if __name__ == "__main__":
    main()
