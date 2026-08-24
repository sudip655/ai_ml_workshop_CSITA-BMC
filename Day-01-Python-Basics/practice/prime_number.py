# Practice Task 2: Check if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    print("=== Prime Number Checker ===")
    while True:
        user_input = input("\nEnter an integer to check (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        
        try:
            num = int(user_input)
            if is_prime(num):
                print(f"✔️ {num} is a PRIME number!")
            else:
                print(f"❌ {num} is NOT a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
