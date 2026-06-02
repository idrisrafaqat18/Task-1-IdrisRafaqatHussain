# Rule-Based AI Chatbot

A simple rule-based AI chatbot built with Python using deterministic logic and control flow patterns.

## 📌 Project Overview

This project demonstrates the foundational principles of artificial intelligence engineering through a **Rule-Based Chatbot** implementation. It focuses on:

- **Control Flow and Logic**: Building a deterministic logic engine that simulates basic human interaction through programmatic decision-making
- **Precision and Predictability**: Establishing a continuous digital loop that ensures 100% predictable and safe outcomes with complete traceability

## 🛠️ Key Requirements & Architecture

The codebase adheres to the **Input-Process-Output (IPO)** architecture model:

1. **Input (Raw Feed) & Sanitization**: Captures user input via `input()` and normalizes it using `.lower().strip()` to remove variations, case disparities, and whitespace inconsistencies

2. **Process (The Logic Skeleton)**: A rigid, hard-coded conditional routing matrix (`if-elif-else`) that matches clean user strings to predefined intent structures

3. **Output (Feedback Loop)**: Connects matched intents directly to precise, hard-coded string outputs to achieve predictable outcomes

4. **Continuous Digital Loop**: Runs indefinitely within an active state machine loop until an explicit exit command is issued

## 🚀 Key Skills Mastered

- Control flow and deterministic routing structures
- Text normalization and input data sanitization
- Hard-coded application safety guardrails
- Designing clear, explainable program pathways ("White Box" transparency)

## 💻 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/idrisrafaqat18/rule-based-ai-bot.git
cd rule-based-ai-bot
```

2. Run the chatbot:
```bash
python main.py
```

## 📖 Usage

Simply run the script and interact with the chatbot by typing your messages. The bot will process your input and respond based on predefined rules.

Example:
```
You: Hello
Bot: Hi there! How can I help you?

You: What is your name?
Bot: I'm a rule-based chatbot.

You: exit
Bot: Goodbye!
```

## 🔧 How It Works

The chatbot uses a series of conditional statements to match user input patterns with predefined responses. Each input is:

1. **Normalized** - converted to lowercase and stripped of whitespace
2. **Matched** - checked against a set of predefined patterns
3. **Responded** - with a corresponding hard-coded output

## 📝 License

This project is provided as-is for educational purposes.

## 👤 Author

**Idris Rafaqat**

---

*This is a foundational project demonstrating core AI principles through rule-based logic implementation.*
