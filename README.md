# Module 01: The Rule-Based AI Chatbot
### DecodeLabs Industrial Training Kit | Batch: 2026
---

## 📌 Project Overview
Project 1 forms the foundational track of the DecodeLabs Artificial Intelligence Engineering program[cite: 427, 429]. This phase focuses strictly on **Control Flow and Logic (System 2: The Engineer)** rather than probabilistic deep learning[cite: 431, 462]. 

The goal is to master the precision of a deterministic logic engine by establishing a continuous digital loop that simulates basic human interaction through pure programmatic decision-making[cite: 433, 476]. Building this explicit `if-else` structural foundation acts as the essential control layer and deterministic guardrail used in production environments (such as NVIDIA NeMo and Llama Guard) to filter probabilistic outputs, eliminate hallucination risks, and ensure absolute safety and compliance[cite: 433, 482, 489, 494].

## 🛠️ Key Requirements & Architecture
The codebase adheres strictly to the **Input-Process-Output (IPO)** architecture model[cite: 498]:
1. **Input (Raw Feed) & Sanitization:** Captures the raw user stream via `input()` and subjects it to a normalization process (`.lower().strip()`) to remove variations, case disparities, and whitespace padding before routing[cite: 501, 503, 533].
2. **Process (The Logic Skeleton):** A rigid, hard-coded conditional routing matrix (`if-elif-else`) that matches clean user string sequences to predefined target intent structures[cite: 506, 507, 516].
3. **Output (Feedback Loop):** Connects matched intents directly to precise, hard-coded string outputs to achieve 100% predictable, safe outcomes with zero mystery and absolute traceability[cite: 481, 512, 517].
4. **Continuous Digital Loop:** Runs indefinitely within an active state machine loop until an explicit, universal exit command is issued[cite: 446, 449].

## 🚀 Key Skills Mastered
* Control flow & deterministic routing structures[cite: 450, 451].
* Text normalization and input data data sanitization[cite: 450, 503].
* Hard-coded application safety guardrails[cite: 489].
* Designing clear, "White Box" explainable program pathways[cite: 478, 484].
