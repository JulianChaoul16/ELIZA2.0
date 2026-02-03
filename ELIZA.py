'''
Eliza.pu
Julian Chaoul
2/2/2026

Simple chatbot program that acts as a therapist
What techniques I used: 
- Word Spotting for emotions like sadness, anger, happiness, anxiety, love, loneliness, family
- Rephrasing questions and statements
- Classic responses when input is not recognized
- Random fun responses for common questions like "how are you" and "tell me a joke"

Programmer notes: 
Most of these techniques were inspired by Joseph Weizenbaum's original ELIZA program, the simple techniques were what truly interested me. 
I asked my friends who were frequently in therapy how these conversations usually went, and I tried to mimic that as best as I could with simple techniques.
'''
import random

# If ELIZA does not recognize input, will randonomly choose one of these 
CLASSICS = [
    "I see. Tell me more.",
    "Can you say that another way?",
    "How does that make you feel?",
    "Why do you think that is?",
    "That's interesting.Go into detail.", 
    "I'm not sure I understand.", 
    "Feeling that way is valid, say more",
    "Please Contiue"
]
# Responses for Sadness
SAD = [
    "I'm sorry to hear that you're feeling sad. Would you like to talk about it?",
    "It's okay to feel sad sometimes. I'm here to listen if you want to share more.",
    "What do you think is making you feel sad?"
]
# Responses for Anger
ANGRY  = [
    "It's understandable to feel angry sometimes. What is making you feel this way?",
    "Anger can be a powerful emotion. Would you like to talk about what's causing it?"
    "What do you usually do when you feel angry?"
]
# Responses for Happiness
HAPPY = [
    "That's great to hear! What's making you feel happy?",
    "Happiness is a wonderful feeling. Would you like to share more about it?"
    "Being excited is contagious! What's got you feeling this way?"
]
# Responses for Anxiety
ANXIOUS = [
    "Anxiety can be tough to deal with. Would you like to share what's making you feel this way?",
    "It's okay to feel anxious sometimes. I'm here to listen if you want to talk about it."
]
# Responses for  Love and Loneliness
LOVE = [
    "Love is a powerful emotion. What does love mean to you?",
    "How does love impact your life?",
    "What experiences with love have been significant for you?"
]
# Responses for Loneliness
LONELY = [
    "Loneliness can be hard. Would you like to talk about what's making you feel this way?",
    "It's okay to feel lonely sometimes. I'm here to listen if you want to share more."
]
# Responses for Family
PARENTS = [
    "Tell me more about your relationship with your parents.",
    "How do you feel about your parents?",
    "What role do your parents play in your life?"
]



def response(name: str, user_input: str) -> str:

    user_input = user_input.lower()

    #Random user inputs I saw my friends input 
    if "how are you" in user_input:
        return f"-> [eliza] I'm just a program, but thanks for asking, {name}!"
    
    if "what are you" in user_input or "what is your purpose" in user_input:
        return f"-> [eliza] I'm ELIZA2.0, a therapist created to chat with you, {name}."


    if "tell me a joke" in user_input:
        return f"-> [eliza] Why do COmputers like linux? ... Because they dont like Windows in their house!"

    #Rephrasing Questions 
    if user_input.endswith("?"):
        return f"-> [eliza] Why do you ask that {name}?"
    
    #Word Spotting
    if "sad" in user_input or "unhappy" in user_input or "depressed" in user_input:
        return f"-> [eliza] {random.choice(SAD)}"
    if "angry" in user_input or "mad" in user_input or "furious" in user_input:
        return f"-> [eliza] {random.choice(ANGRY)}"
    if "anxious" in user_input or "worried" in user_input or "nervous" in user_input:
        return f"-> [eliza] {random.choice(ANXIOUS)}"
    if "happy" in user_input or "excited" in user_input or "joyful" in user_input:
        return f"-> [eliza] {random.choice(HAPPY)}"
    if "love" in user_input or "loved" in user_input or "loving" in user_input:
        return f"-> [eliza] {random.choice(LOVE)}"
    if "lonely" in user_input or "alone" in user_input or "isolated" in user_input:
        return f"-> [eliza] {random.choice(LONELY)}"
    if "mother" in user_input or "father" in user_input or "parents" in user_input:
        return f"-> [eliza] {random.choice(PARENTS)}"
    
    #Statements to Rephrase 
    if user_input.startswith("i want "):
        return f"{name}, why do you want {user_input[7:]}?"

    if user_input.startswith("i need "):
        return f" -> [eliza] {name}, why do you need {user_input[7:]}?"
    
    #Function for any emotions that were not covered above
    if user_input.startswith("i feel "):
        return f"-> [eliza] What makes you feel {user_input[7:]}?"

    if user_input.startswith("i am "):
        return f"-> [eliza] How long have you been {user_input[5:]}?"

    return f"-> [eliza] {random.choice(CLASSICS)}"
    

    
def main() : 
    #Get Users Name
    name = ""
    print("-> [eliza] Hi, I am ELIZA2.0. What is your name?")
    while True:
        user = input("=> [user] ").strip()

        if user.lower() in ["quit", "exit", "bye", "goodbye", "stop", "end"]:
            print("-> [eliza] Goodbye.")
            return

        words = user.split()

        if "name" in words and "is" in words or "I" in words and "am" in words:
            name = words[-1].strip(".")
            break

        if len(words) == 1:
            name = words[0].strip(".")
            break

        print("-> [eliza] Sorry, what is your name?")
    
    #Begin Conversation
    print(f"-> [eliza] Hello {name}, how can I help you today?")

    #Loop for user input
    while True:
        user_input = input(f"=> [{name}] ").strip()

        if user_input.lower() in ["quit", "exit", "bye", "goodbye", "stop", "end"]:
            print("-> [eliza] Goodbye.")
            break
        
        #Generate and print ELIZa's replies
        reply = response(name, user_input)
        print(reply)

    
if __name__ == "__main__":
    main()

