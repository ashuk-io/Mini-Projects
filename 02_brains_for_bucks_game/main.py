questions = [
    ["Who is Elon Musk?", "Scientist", "Entrepreneur", "Actor", "Politician", 2],
    ["What is the capital of Italy?", "Madrid", "Paris", "Rome", "Athens", 3],
    ["Which planet is the largest in our solar system?", "Earth", "Saturn", "Jupiter", "Neptune", 3],
    ["What is the tallest animal?", "Horse", "Elephant", "Giraffe", "Kangaroo", 3],
    ["Who wrote 'Pride and Prejudice'?", "Jane Austen", "Mark Twain", "Charles Dickens", "Leo Tolstoy", 1],
    ["What is the square root of 81?", "7", "8", "9", "10", 3],
    ["Which country is famous for the Great Wall?", "Japan", "China", "India", "South Korea", 2],
    ["Who painted 'Starry Night'?", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo", "Salvador Dalí", 2],
    ["What is the slowest land animal?", "Cheetah", "Tortoise", "Snail", "Sloth", 4],
    ["Which continent is the largest?", "Africa", "Asia", "Europe", "Australia", 2],
    ["What is the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2]
]

win = [1000,2000,5000,10000,25000,69000,130000,200000,500000,1000000,2500000]
i = 0

for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    answer = int (input ('Lock the option : '))

    if answer == question[5] :
        print("Correct Answer")

    else:
        print("You guessed it wrong\nYou lose!")
        print("Better luck next time :)")
        break
    sum = win[i]
    print(f"You won : {win[i]}")
    
    i += 1

print(f"Total winnigs : {sum}")

