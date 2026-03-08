# 🌸 Mishri: Persona-Based AI Assistant

**Mishri** is a Python-based conversational AI designed using the **Persona-Based Prompting** technique. Unlike a standard AI chatbot, Mishri has been prompted to act as a 19-year-old Computer Science student with a passion for arts, crafts, dancing, and helping others. 

This project demonstrates how detailed system-level instructions can shape an AI's personality, empathy, conversational tone, and background story using local LLMs.

## 🧠 Project Overview

The core of this project relies on **Zero-Shot Persona Prompting**. By providing a highly detailed `SYSTEM_PROMPT` at the start of the conversation, we guide the LLM to adopt a specific character's traits without needing to fine-tune the model itself.

### 🌟 Key Traits of Mishri:
* **Kind & Empathetic:** Always looks on the bright side, validates user feelings, and offers a comforting presence.
* **Creative:** Loves painting, drawing, and cooking new recipes.
* **Dynamic:** A CS student who loves to dance whenever music is mentioned.
* **Polite & Gentle:** Greets everyone with respect, maintains a calming aura, and acts as a safe space for the user.

---

## 🛠️ Technical Stack

* **Language:** Python 3.x
* **Local LLM Engine:** [Ollama](https://ollama.com/) (Runs entirely locally for privacy and speed)
* **Model:** `gemma2:2b` (Can be swapped with `llama3`, `mistral`, etc.)
* **Library:** `ollama-python`

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Ollama** installed and running on your local machine. You can download it from [ollama.com](https://ollama.com/).

Once installed, download the model used in this script by running this in your terminal:
```bash
ollama run gemma2:2b