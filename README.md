# Dual-Agent Sales Call Simulation

This project simulates a sales call between an AI sales agent (**Sara**) and a customer (**John**) who abandoned a shirt in their shopping cart. The AI interacts with the customer to complete the purchase, and a **supervisor agent** evaluates the conversation at the end to determine the next steps.

## Features
- AI-powered **sales agent (Sara)** that engages with the customer.
- **Customer intent detection** using a language model.
- **Supervisor agent** that analyzes the conversation after it ends.
- Automatic handling of objections:
  - **Price concerns** → 10% discount.
  - **Shipping concerns** → Free shipping.
  - **Quality concerns** → Free returns.
  - **Completed purchase** → Send cart link.
- **Conversation timeout** after 5 minutes.

## Installation
### Prerequisites
- Python 3.x
- `requests` library
- Local instance of an LLM API (e.g., DeepSeek) running at `http://localhost:1234`

### Setup
1. Clone this repository:
   ```
   git clone https://github.com/asantosca/dual-agent-sales.git
   cd dual-agent-sales
   ```
2. Install dependencies:
   ```
   pip install requests
   ```
3. Run the script:
   ```
   python sales_agent.py
   ```

## How It Works
1. The sales agent (**Sara**) calls the customer and engages in a natural conversation.
2. Sara responds to objections and tries to close the sale.
3. If the customer says "goodbye" or 5 minutes pass, the conversation ends.
4. The **supervisor agent** analyzes the conversation and determines:
   - Whether to send an email with the cart link.
   - Whether a discount, free shipping, or free returns were applied.
   - Whether the customer abandoned the cart.
5. The final action is printed to the console.

## Example Interaction
```
Hi John, this is Sara from ShirtsAndBelts. I noticed you left a blue medium shirt in your cart. Is there anything I can help you with?
John: It's too expensive.
Sara: I understand! I can offer you a 10% discount. Would that help?
John: Yes, that works.
Sara: Great! I’ll send a link to your email to complete the purchase.
Supervisor: Sending email with cart link.
```

