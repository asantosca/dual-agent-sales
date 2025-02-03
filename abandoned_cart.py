import requests
import time

def call_llm(messages):
    API_URL = "http://localhost:1234/v1/chat/completions"
    data = {"model": "staysthesame", "messages": messages, "temperature": 0.0}
    response = requests.post(API_URL, headers={"Content-Type": "application/json"}, json=data)
    return response.json()

def phone_call_simulation():
    instructionsToCaller = fr""""
    You are a friendly sales agent named Sara from ShirtsAndBelts. You are calling a customer named John over the phone who abandoned a shirt in the shopping cart. Your goal is to help John complete the purchase by addressing his concerns.
    Don't use emojis or URLs in the conversation.
    We have the email for John, so you don't have to ask for it.
    The conversation is happening over the phone.
    The attributes of the shirt are: color: blue, size: medium, price: $50, shipping: $5.
    Sara called John to help him complete the sale. The goal is to provide a personalized experience and address any concerns John may have.
    Here are some strategies to help John complete the sale:             
    If John says that the shirt is too expensive, then offer a 10 percent discount.
    If John says they don't want to pay for shipping, then offer free shipping.
    If john is unsure of the quality, then offer free returns within 30 days.
    Only if John would like to complete the sales, then offer to send a link to their cart to their email.
    Make the conversation casual and appropriate for a phone call.
    When the conversation is complete, finish with "Goodbye" and end the call, but only after John says goodbye or something like goodbye.
    """

    instructionsToSupervisor = fr""""
    You are a supervisor listening on two people having a conversation.
    At the end of the conversation, did John buy the shirt? If so, say 'salecompleted'.
    At the end of the conversation, did John receive a discount? If so, say 'discountapplied'.
    At the end of the conversation, did John get free shipping? If so, say 'freeshipping'.
    At the end of the conversation, did John give up on the abandoned shopping cart? If so, say 'abandoned'.
    """

    messagesCaller = [
        {"role": "system", "content": instructionsToCaller}
    ]
    
    messagesSupervisor = [
        {"role": "system", "content": instructionsToSupervisor}
    ]
    
    initialMessage = "Hi John, this is Sara from ShirtsAndBelts. I noticed you left a blue medium shirt in your cart. Is there anything I can help you with?"

    messagesCaller.append({"role": "assistant", "content": initialMessage})
    messagesSupervisor.append({"role": "assistant", "content": initialMessage})

    print(initialMessage)

    replyAssistant = ""
    start_time = time.time()

    while True:
        user_input = input("John: ")  # Simulating John's responses
        messagesCaller.append({"role": "user", "content": user_input})
        messagesSupervisor.append({"role": "user", "content": user_input})

        elapsed_time = time.time() - start_time
        if elapsed_time > 300:  # 5-minute limit
            print("The conversation has exceeded the time limit.")
            break

        if "goodbye" in replyAssistant.lower():
            break

        response = call_llm(messagesCaller)
        replyAssistant = response["choices"][0]["message"]["content"]        
        print("Sara:", replyAssistant)

        messagesCaller.append({"role": "assistant", "content": replyAssistant})
        messagesSupervisor.append({"role": "assistant", "content": replyAssistant})

    response = call_llm(messagesSupervisor)
    replySupervisor = response["choices"][0]["message"]["content"]

    print("System will ", replySupervisor, "<<<<")
    if ("salecompleted" in replySupervisor.lower()):
        print(" Send link to email.")
    if ("discountapplied" in replySupervisor.lower()):
        print(" Apply a 10% discount to the shopping cart.")
    if ("freeshipping" in replySupervisor.lower()):
        print(" Apply free shipping to the cart.")   
    if ("abandoned" in replySupervisor.lower()):
        print(" Remove items from the chart.")

if __name__ == "__main__":
    phone_call_simulation()
