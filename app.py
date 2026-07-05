import json
import datetime

with open("faq_data.json", "r") as file:
    faq = json.load(file)

print("=" * 60)
print("🌌 AETHERIS AI")
print("🚀 The Cosmic Knowledge Assistant")
print("=" * 60)

print("\nHello Explorer!")
print("Ask me anything about space.")
print("Type 'help' to see available questions.")
print("Type 'exit' to quit.\n")

while True:

    question = input("👨‍🚀 You: ").lower().strip()

    if question == "exit":
        print("\n🤖 Aetheris AI: Safe travels, Explorer!")
        break

    elif question == "help":
        print("\nAvailable Questions:")
        for q in faq:
            print("-", q)

    elif question in faq:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(f"\n🤖 Aetheris AI [{current_time}]")
        print(f"{faq[question]}\n")

    else:
        print("\n🤖 Aetheris AI:")
        print("Sorry, I don't have information on that topic yet.\n")