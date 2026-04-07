#Project
#URL Shortner


import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.length = 6
        self.chars = string.ascii_letters + string.digits  # base62

    def _generate_code(self):
        return ''.join(random.choices(self.chars, k=self.length))

    def shorten_url(self, original_url):
        if original_url in self.url_to_code:
            return self.url_to_code[original_url]

        while True:
            short_code = self._generate_code()
            if short_code not in self.code_to_url:
                break

        self.url_to_code[original_url] = short_code
        self.code_to_url[short_code] = original_url  
        return short_code

    def retrieve_url(self, short_code):
        return self.code_to_url.get(short_code, "Short code not found")

# --- Main Program ---
shortener = URLShortener()

while True:
    print("\n--- URL Shortener ---")
    print("1. Shorten a URL")
    print("2. Retrieve original URL from short code")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == '1':
        url = input("Enter a URL to shorten: ")
        short_code = shortener.shorten_url(url)
        print(f"Shortened code for '{url}' is: {short_code}")

    elif choice == '2':
        code = input("Enter the short code: ")
        original_url = shortener.retrieve_url(code)
        print(f"Original URL: {original_url}")

    elif choice == '3':
        print("Exiting program.thank you")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
