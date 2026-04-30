import json
import os
from groq import Groq

client = Groq(api_key=("API"))

print("AI Study Helper is starting...")
print("I can explain any topic and quiz you!")

while True:
    topic = input("\nWhat topic do you want to study? (or type 'quit' to exit) ")
    
    if topic.lower() == "quit":
        print("Good job studying today! See you next time!")
        break

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a friendly study helper. Explain topics simply and clearly for beginners."},
                {"role": "user", "content": "Please explain this topic simply: " + topic}
            ]
        )
        explanation = response.choices[0].message.content
    except Exception as e:
        print("Explanation error:", e)
        continue

    print("\nHere is your explanation:")
    print(explanation)

    print("\nNow let's test your understanding with a quiz!")
    input("Press Enter when you are ready...")

    try:
        quiz_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a study helper. Create 3 simple quiz questions about the topic."},
                {"role": "user", "content": "Give me 3 quiz questions about: " + topic}
            ]
        )
        quiz = quiz_response.choices[0].message.content
    except Exception as e:
        print("Quiz error:", e)
        continue

    print("\nYour Quiz:")
    print(quiz)

    session = {
        "topic": topic,
        "explanation": explanation,
        "quiz": quiz
    }

    data = []
    try:
        with open("study_sessions.json", "r") as f:
            data = json.load(f)
    except:
        pass

    data.append(session)

    with open("study_sessions.json", "w") as f:
        json.dump(data, f, indent=4)

    print("\nSession saved to study_sessions.json!")
