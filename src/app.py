import time
import sys
import pyttsx3

# Inicializa o motor
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# AJUSTE PARA VOZ FEMININA:
# Geralmente voices[1] é a voz feminina (Zira ou Maria) no Windows.
# Se ainda sair masculina, mude o índice para 0.
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175) # Velocidade levemente mais rápida para soar natural

def speak_and_type(text):
    print("\033[93m" + "AI Concierge: " + "\033[0m", end="")
    sys.stdout.flush()
    
    # Fala o texto
    engine.say(text)
    engine.runAndWait()
    
    # Digitação dinâmica
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def ai_demo_video():
    print("\033[94m" + "--- AGENCIA IA DINIZ | HIGH-END REAL ESTATE DEMO ---" + "\033[0m")
    time.sleep(1.5)
    
    # Introdução mais profissional
    intro = ("Hello Ivan and Mike. This is the Agencia IA Diniz specialized backend. "
             "I am currently processing the data for your exclusive Marea Condo listing to ensure "
             "instant, high-level engagement for every potential lead.")
    speak_and_type(intro)
    time.sleep(1)
    
    # Pergunta 1: Detalhes Técnicos
    print(f"\033[92mLead Question: Does it have a private elevator and balcony space?\033[0m")
    p1 = ("Absolutely. The PH602 Penthouse features a private elevator foyer for total exclusivity. "
          "Beyond that, it boasts an expansive wraparound terrace with breathtaking ocean views, "
          "seamlessly blending indoor and outdoor living spaces.")
    speak_and_type(p1)
    time.sleep(1)
    
    # Pergunta 2: Valor e Qualificação
    print(f"\033[92mLead Question: What is the current asking price and HOA?\033[0m")
    p2 = ("The property is currently positioned at 7 point 7 million dollars. "
          "This includes access to Marea’s world-class amenities and 24-hour concierge services. "
          "To provide the best service, would you like to schedule a brief call to review the "
          "financials or book a private showing for this week?")
    speak_and_type(p2)
    time.sleep(1)

    # Fechamento com autoridade
    outro = ("While other brokers take hours to reply, our AI engages your clients in seconds. "
             "Let's scale your luxury portfolio. Agencia IA Diniz is ready. Back to you, Ivan.")
    speak_and_type(outro)

if __name__ == "__main__":
    ai_demo_video()