from groq import Groq

client = Groq(api_key="YOUR_API_KEY_HERE")

print("AI Study Helper is starting...")
print("I can explain any topic and quiz you!")

while True:
    topic = input("\nWhat topic do you want to study? (or type 'quit' to exit) ")
    
    if topic.lower() == "quit":
        print("Good job studying today! See you next time!")
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a friendly study helper. Explain topics simply and clearly for beginners."},
            {"role": "user", "content": "Please explain this topic simply: " + topic}
        ]
    )

    explanation = response.choices[0].message.content
    print("\nHere is your explanation:")
    print(explanation)

    print("\nNow let's test your understanding with a quiz!")
    input("Press Enter when you are ready...")

    quiz_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a study helper. Create 3 simple quiz questions about the topic."},
            {"role": "user", "content": "Give me 3 quiz questions about: " + topic}
        ]
    )

    quiz = quiz_response.choices[0].message.content
    print("\nYour Quiz:")
    print(quiz)

    with open("study_sessions.txt", "a") as f:
        f.write("Topic: " + topic + "\n")
        f.write("Explanation:\n" + explanation + "\n")
        f.write("Quiz:\n" + quiz + "\n")
        f.write("-" * 50 + "\n\n")

    print("\nSession saved to study_sessions.txt!")