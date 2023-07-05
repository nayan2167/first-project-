def calculate_average(numbers):
    if not numbers:
        return None

    total = 0
    count = 0

    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
            count += 1

    if count == 0:
        return None

    average = total / count
    return average

def generate_fibonacci_sequence(n):
    if n <= 0:
        return []

    sequence = [0, 1]

    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence

def reverse_string(input_string):
    return input_string[::-1]

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

