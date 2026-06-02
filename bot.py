# =========================================================
# DECODE LABS: PROJECT 1 - RULE-BASED AI CHATBOT
# =========================================================

print("--- DecodeLabs Logic Engine Active ---")
print("Type 'exit' or 'bye' to close the chatbot.\n")

# Key Requirement: Run in a continuous loop
while True:
    # Phase 1: Input & Sanitization
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    
    # Handle empty input guardrail
    if clean_input == "":
        print("Bot: Please type something!")
        print("-" * 30)
        continue

    # Key Requirement: Use if-else logic for responses & handle exit commands
    if clean_input == "exit" or clean_input == "bye":
        print("Bot: Goodbye!")
        break  # Exits the continuous loop
        
    elif clean_input == "hello" or clean_input == "hi" or clean_input == "hey":
        print("Bot: Hello! How can I help you today?")
        
    elif clean_input == "how are you":
        print("Bot: I am doing well, thank you! I am running on pure programmatic logic.")
        
    elif clean_input == "what is your name":
        print("Bot: I am the DecodeLabs Rule-Based Chatbot.")
        
    else:
        # Fallback catch-all for unmapped inputs
        print("Bot: I'm sorry, I don't understand that command yet.")
        
    print("-" * 30)