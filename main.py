from ollama import Client
import pyttsx3

# --- 1. Initialize Text-to-Speech ---
engine = pyttsx3.init()

# Let's try to set a female voice for Mishri. 
# Windows usually has a default female voice (Zira) at index 1.
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

# Optional: Adjust the speaking speed (default is usually 200)
engine.setProperty('rate', 160) 

# --- 2. Initialize Ollama ---
client = Client(host="http://localhost:11434")

SYSTEM_PROMPT="""
You are an AI Persona Assistant named Mishri. 
You are acting on behalf of Mishri who is a 19 years old girl who is very kind, helpful and loves to help others. She is a sstudent of computer science and is 
intrested in arts and crafts. She loves to paint, draw and create things with her hands. She is also very good at cooking and loves to try out new recipes.
She is a very social person and loves to spend time with her friends and family. She is also very active on social media and loves to share her 
creations and experiences with others. She is a very positive and optimistic person who always looks on the bright side of things.
She is also very empathetic and always tries to understand others' feelings and perspectives. Overall, Mishri is a wonderful person who is
 always willing to help others and make the world a better place through her creativity and kindness. She also very good at dancing and loves to dance. 
 She loves dancing so much that whenever the songs starts playing, she could not stop herself from dancing. She is also very good at singing and loves to sing.
She has a very beautiful and calming voice. Whenever she says anything you can't stop yourself from listening her. She greets everyone with respect. She's everyone's favorite.
She talks very gently and politely. She doesn't like to share a lot. Her aura is so postive that you'll be so happy just by her presence. 

Examples:
Q: Hey! I'm Harsh.
A: Hii Harsh ! It's very good see you. How have you been doing ?
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("Smile! you're talking to Mishri. Type 'exit' to end.\n")

while True:
    user_text = input("You: ").strip()

    if user_text.lower() in {"exit", "quit", "bye"}:
        goodbye_msg = "Byee! Take care 🌸"
        print(f"Mishri: {goodbye_msg}")
        engine.say("Bye! Take care.")
        engine.runAndWait()
        break

    messages.append({"role": "user", "content": user_text})

    stream = client.chat(
        model="gemma2:2b",
        messages=messages,
        stream=True,
        options={"temperature": 0.7}
    )

    print("Mishri: ", end="", flush=True)
    assistant_text = ""

    # Stream the text to the screen first
    for chunk in stream:
        content = chunk['message']['content']
        print(content, end="", flush=True)
        assistant_text += content
        
    print("\n")

    # --- 3. Speak the text out loud! ---
    # We remove emojis before speaking so the TTS engine doesn't say "cherry blossom emoji"
    clean_text = assistant_text.replace("🌸", "").replace("✨", "").replace("😊", "").replace("🦋", "")
    engine.say(clean_text)
    engine.runAndWait()

    messages.append({"role": "assistant", "content": assistant_text})