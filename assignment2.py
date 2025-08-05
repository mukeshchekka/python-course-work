
def input_messages():
    n = int(input("Enter number of messages: "))
    messages = []
    for _ in range(n):
        messages.append(input())
    return messages


def extract_user_and_message(message):
    if ": " in message:
        return message.split(": ", 1)
    return None, message

def count_messages(messages):
    return f"Total messages: {len(messages)}"

def unique_users(messages):
    users = {extract_user_and_message(m)[0] for m in messages}
    return f"Unique users in the chat: {users}"

def total_words(messages):
    total = sum(len(extract_user_and_message(m)[1].split()) for m in messages)
    return f"Total words in the chat: {total}"

def average_words(messages):
    if not messages:
        return "Average words per message: 0.0"
    total = sum(len(extract_user_and_message(m)[1].split()) for m in messages)
    return f"Average words per message: {round(total / len(messages), 2)}"

def longest_message(messages):
    longest = max(messages, key=lambda m: len(extract_user_and_message(m)[1]), default="")
    return f"Longest message: \"{longest}\""

def most_active_user(messages):
    counter = Counter(extract_user_and_message(m)[0] for m in messages)
    user, count = counter.most_common(1)[0]
    return f"Most active user: {user} ({count} messages)"

def user_message_count(messages, user):
    count = sum(1 for m in messages if extract_user_and_message(m)[0] == user)
    return f"Messages sent by {user}: {count}"

def most_frequent_word(messages, user):
    words = []
    for m in messages:
        u, msg = extract_user_and_message(m)
        if u == user:
            words += re.findall(r'\b\w+\b', msg.lower())
    if not words:
        return f"No messages found for {user}"
    word, _ = Counter(words).most_common(1)[0]
    return f"Most frequent word used by {user}: \"{word}\""

def first_and_last_message(messages, user):
    user_msgs = [m for m in messages if extract_user_and_message(m)[0] == user]
    if not user_msgs:
        return f"No messages from {user}"
    return f"First message by {user}: \"{user_msgs[0]}\"\nLast message by {user}: \"{user_msgs[-1]}\""

def check_user_present(messages, user):
    users = {extract_user_and_message(m)[0] for m in messages}
    return f"User '{user}' {'is present' if user in users else 'not found'} in the chat."

def common_repeated_words(messages):
    all_words = [w.lower() for m in messages for w in re.findall(r'\b\w+\b', extract_user_and_message(m)[1])]
    counter = Counter(all_words)
    repeated = {word for word, count in counter.items() if count > 1}
    return f"Common repeated words: {repeated}"

def longest_avg_msg_user(messages):
    word_totals = {}
    msg_counts = Counter()
    for m in messages:
        user, msg = extract_user_and_message(m)
        word_totals[user] = word_totals.get(user, 0) + len(msg.split())
        msg_counts[user] += 1
    avg_lengths = {user: word_totals[user] / msg_counts[user] for user in msg_counts}
    user = max(avg_lengths, key=avg_lengths.get)
    return f"User with longest average message: {user} (avg {round(avg_lengths[user], 2)} words)"

def mention_count(messages, name):
    count = sum(1 for m in messages if name.lower() in extract_user_and_message(m)[1].lower())
    return f"Messages mentioning '{name}': {count}"

def remove_duplicates(messages):
    unique = list(dict.fromkeys(messages))
    result = f"Unique messages count: {len(unique)}"
    return result + "\n" + "\n".join(unique)

def sort_messages(messages):
    return "\n".join(sorted(messages, key=str.lower))

def extract_questions(messages):
    questions = [m for m in messages if "?" in extract_user_and_message(m)[1]]
    return "Questions:\n" + "\n".join(questions)

def reply_ratio(messages, user1, user2):
    count = 0
    for i in range(1, len(messages)):
        u1, _ = extract_user_and_message(messages[i-1])
        u2, _ = extract_user_and_message(messages[i])
        if u1 == user1 and u2 == user2:
            count += 1
    return f"Reply ratio from {user2} to {user1}: {count} replies"

def deleted_messages(messages):
    count = sum(1 for m in messages if extract_user_and_message(m)[1].strip().lower() == "this message was deleted")
    return f"Deleted messages found: {count}"

 messages = input_messages()
 while True:
    print("\n--- MENU ---")
    print("1. Total messages")
    print("2. Unique users")
    print("3. Total words")
    print("4. Average words per message")
    print("5. Longest message")
    print("6. Most active user")
    print("7. Message count by a user")
    print("8. Most frequent word by user")
    print("9. First & last message by user")
    print("10. Check if user is present")
    print("11. Common repeated words")
    print("12. Longest avg message length user")
    print("13. Count mentions of user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract questions")
    print("17. Reply ratio between users")
    print("18. Deleted messages")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(count_messages(messages))
    elif choice == "2":
        print(unique_users(messages))
    elif choice == "3":
        print(total_words(messages))
    elif choice == "4":
        print(average_words(messages))
    elif choice == "5":
        print(longest_message(messages))
    elif choice == "6":
        print(most_active_user(messages))
    elif choice == "7":
        user = input("Enter user name: ")
        print(user_message_count(messages, user))
    elif choice == "8":
        user = input("Enter user name: ")
        print(most_frequent_word(messages, user))
    elif choice == "9":
        user = input("Enter user name: ")
        print(first_and_last_message(messages, user))
    elif choice == "10":
        user = input("Enter user name: ")
        print(check_user_present(messages, user))
    elif choice == "11":
        print(common_repeated_words(messages))
    elif choice == "12":
        print(longest_avg_msg_user(messages))
    elif choice == "13":
        name = input("Enter name to check for mentions: ")
        print(mention_count(messages, name))
    elif choice == "14":
        print(remove_duplicates(messages))
    elif choice == "15":
        print(sort_messages(messages))
    elif choice == "16":
        print(extract_questions(messages))
    elif choice == "17":
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")
        print(reply_ratio(messages, u1, u2))
    elif choice == "18":
        print(deleted_messages(messages))
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


    

