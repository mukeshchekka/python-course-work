import random
Data = [{
        "question": "1. Which of the following is the correct extension of the Python file?",
        "options": ["a) .python","b) .pl","c) .py","d) .p"],
        "answer": "c; Explanation: ‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’."
    },
    {
        "question": "2. Is Python code compiled or interpreted?",
        "options": ["a) Python code is both compiled and interpreted","b) Python code is neither compiled nor interpreted","c) Python code is only compiled","d) Python code is only interpreted"],
       "answer": "a"
    },
    {
        "question": "3. What will be the value of the following Python expression? print(4 + 3 % 5)",
        "options": ["a) 7", "b) 2", "c) 4", "d) 1"],
        "answer": "a"
    },
    {
        "question": "4.Which keyword is used for function in Python language?",
        "options": ["a) Function", "b)def","c)Fun", "d)Define"],
        "answer": "b"
    },
    {
        "question": "5. Which of the following functions is a built-in function in python?",
        "options": ["a)factorial()","b)print()","c)seed()","d)sqrt()"],
        "answer": "b"
    },
    {
        "question": "6.Which module is used for regular expressions in Python?",
        "options": ["a) regex", "b) re", "c) string", "d) expression"],
        "answer": "b"
    },
    {
        "question": "7. What will be the output of the following Python code snippet if x=1,x<<2?",
        "options": ["a)4","b)2","c)1","d)8"],
        "answer": "a"
    },
    {
        "question": "8. Python supports the creation of anonymous functions at runtime, using a construct called __________?",
        "options": ["a)pi", "b)anonymous", "c)lambda", "d)none of the mentioned"],
        "answer": "c"
    },
    {
        "question": "9. What will be the output of the following Python function? print(min(max(False,-3,-4), 2,7))",
        "options": ["a)-4", "b)-3", "c)2", "d)False"],
        "answer": "d"
    },
    {
        "question": "10. What will be the output of the following Python program?def foo(x):,x[0] = ['def'],x[1] = ['abc'],return id(x),q = ['abc', 'def'],print(id(q) == foo(q))?",
        "options": ["a)Error", "b)None", "c)False", "d)True"],
        "answer": "b"
    },
    {
        "question": "11.What is the purpose of the 'if __name__ == \"__main__\":' block?",
        "options": ["a) It is a comment", "b) It is a loop construct", "c) It ensures the code inside it runs only when the script is executed directly", "d) It defines a main function"],
        "answer": "c"
    },
    {
        "question": "12.Which of these is the correct way to get the current working directory?",
        "options": ["a) os.path.cwd()", "b) os.getcwd()", "c) sys.getcwd()", "d) path.current()"],
        "answer": "b"
    },
    {
        "question": "13.What is a dictionary in Python?",
        "options": ["a) An ordered collection of items", "b) A collection of key-value pairs", "c) A list of unique elements", "d) A sequence of characters"],
        "answer": "b"
    },
    {
        "question": "14.How do you create an empty set in Python?",
        "options": ["a) {}", "b) ()", "c) []", "d) set()"],
        "answer": "d"
    },
    {
        "question": "15.What is the primary difference between `range()` and `xrange()` in Python 2?",
        "options": ["a) `range()` returns a list, `xrange()` returns an iterator", "b) `xrange()` is more memory-efficient", "c) `xrange()` returns a list, `range()` returns an iterator", "d) Both are the same"],
        "answer": "a"
    },
    {
        "question": "16.Which method is used to remove an item from a list by its value?",
        "options": ["a) pop()", "b) del", "c) remove()", "d) discard()"],
        "answer": "c"
    },
    {
        "question": "17.What is a generator in Python?",
        "options": ["a) A function that returns multiple values", "b) A function that returns an iterator", "c) A keyword for creating a class", "d) A type of loop"],
        "answer": "b"
    },
    {
        "question": "18.Which module is used for regular expressions in Python?",
        "options": ["a) regex", "b) re", "c) string", "d) expression"],
        "answer": "b"
    },
    {
        "question": "19.What does a negative index in a list or string do?",
        "options": ["a) Throws an error", "b) Accesses elements from the beginning", "c) Accesses elements from the end", "d) Reverses the list/string"],
        "answer": "c"
    },
    {
        "question": "20.Which of these is a correct way to create a function that takes an arbitrary number of arguments?",
        "options": ["a) def func(*args):", "b) def func(args):", "c) def func(**args):", "d) def func(args...):"],
        "answer": "a"
    }
]
def python_quiz(questions):
    
    
    random.shuffle(questions)  # Randomize the order of questions
    score = 0
    no_of_questions = len(questions)

    print(" Welcome to the Python Quiz Game!")

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer (a/b/c/d): ").strip().lower()

        if user_answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{q['answer']}'")

    print("\n---")
    print(f"🎯 Your Final Score: {score}/{no_of_questions}")
    if score == no_of_questions:
        print("🎉 Perfect score! You're ready for your interview!")
    elif score >= no_of_questions * 0.75:
        print("Great job! Keep practicing to ace that interview!")
    else:
        print("Keep practicing! You'll be there!")


if __name__ == "__main__":
    python_quiz(Data)

