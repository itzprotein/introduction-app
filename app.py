def knowing_you_qualification_app():
    print("Welcome!! Let's get to know you")
    print("Please answer the following questions one by one to better introduce yourself.\n")
    print("Type your answer and press Enter after each question.\n")
    
    # Initialize score counter
    yes_count = 0
    responses = {}
    
    # Question bank
    questions = [
        {"text": "1. What is your name? ", "type": "text"},
        {"text": "2. Where are you from?", "type": "text"},
        {"text": "3. Write one word that describes your person:", "type": "text"},
        {"text": "4. What political party do you belong to (APC, PDP, OR LP)?", "type": "text"},
        {"text": "5. What would you change if you were president for a day in your country?", "type": "text"},
        
        # Yes/No questions
        {"text": "6. Do you believe in God? (yes/no)", "type": "boolean"},
        {"text": "7. Do you believe Karma exist? (yes/no)", "type": "boolean"},
        {"text": "8. Do you believe in re-incarnation? (yes/no)", "type": "boolean"},
        {"text": "9. Would you sell your kidney for $100,000 today if the opportunity presents? (yes/no)", "type": "boolean"},
        {"text": "10. Feminists have caused more damage than improvment to our society? (yes/no)", "type": "boolean"},
        {"text": "11. Generally, do you think life has been fair to you? (yes/no)", "type": "boolean"},
        {"text": "12. Do you believe education is the way to wealth? (yes/no)", "type": "boolean"},
        {"text": "13. Have you ever been heartbroken? (yes/no)", "type": "boolean"},
        {"text": "14. Do you fear women? (yes/no)", "type": "boolean"},
        {"text": "15. Morality is humanity? (yes/no)", "type": "boolean"},
        {"text": "16. Can money buy happiness? (yes/no)", "type": "boolean"},
        {"text": "17. Religion is superior to culture? (yes/no)", "type": "boolean"},
        {"text": "18. Good things come to those who wait? (yes/no)", "type": "boolean"},
        {"text": "19. Silence would get you bullied in high school? (yes/no)", "type": "boolean"},
        {"text": "20. The beautiful ones are not yet born? (yes/no)", "type": "boolean"},
        {"text": "21. Smacking kids instills discipline? (yes/no)", "type": "boolean"},
        {"text": "22. Rats are feared than snakes by ladies ? (yes/no)", "type": "boolean"},
        {"text": "23. Ignorance is bliss? (yes/no)", "type": "boolean"},
        {"text": "24. Wisdom is bleak? (yes/no)", "type": "boolean"},
        {"text": "25. Oil and milk do not mix? (yes/no)", "type": "boolean"}
    ]
    
    for question in questions:
        while True:
            answer = input(question["text"] + " ").strip()
            
            if question["type"] == "text":
                if answer:  # Ensure answer isn't empty
                    responses[question["text"]] = answer
                    break
                else:
                    print("Please provide an answer.")
            
            elif question["type"] == "boolean":
                if answer.lower() in ["yes", "y"]:
                    responses[question["text"]] = "Yes"
                    yes_count += 1
                    break
                elif answer.lower() in ["no", "n"]:
                    responses[question["text"]] = "No"
                    break
                else:
                    print("Please answer with 'yes' or 'no'.")
        
        print()  # Add space between questions
    
    # Display results
    print("\n" + "="*50)
    print("ASSESSMENT RESULTS:")
    print("="*50 + "\n")
    
    if yes_count >= 9:
        print("Congratulations!! You are a qualified to join our class!")
    else:
        print("We are sorry, you do not meet our requirements. Try again later.")
    
    print(f"\nYou answered 'Yes' to {yes_count} out of 10 technical questions.")
    
    # Optional: Display all responses
    print("\n" + "-"*50)
    print("YOUR RESPONSES:")
    print("-"*50)
    for q, a in responses.items():
        print(f"\n{q}\n{a}")

# Run the app
if __name__ == "__main__":
    knowing_you_qualification_app()