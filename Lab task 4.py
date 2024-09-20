def luhn_algorithm(card_number):
    total = 0
    reverse_digits = [int(d) for d in str(card_number)][::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0

def remove_punctuations(input_string):
    cleaned_string = ''
    for char in input_string:
        if char.isalnum() or char.isspace():
            cleaned_string += char
    return cleaned_string

def alphabetical_sort(input_text):
    words = input_text.split()
    sorted_words = []
    while words:
        smallest = words[0]
        for word in words:
            if word < smallest:
                smallest = word
        sorted_words.append(smallest)
        words.remove(smallest)
    return ' '.join(sorted_words)

card_number = 88532023212830366
print("Luhn algorithm result:", luhn_algorithm(card_number))

input_string = "Hello, World!"
print("Cleaned string:", remove_punctuations(input_string))

input_text = "hello world python programming"
print("Alphabetically sorted text:", alphabetical_sort(input_text))