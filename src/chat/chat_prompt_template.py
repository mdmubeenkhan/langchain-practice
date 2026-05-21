from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

domain = input("Enter domain\n").strip()
topic = input("Enter topic\n").strip()

# create template from message objects
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content=f"You are a helpful {domain} expert."),
    HumanMessage(content=f"Explain in simple terms, the concept of {topic} in 5 points.")
])

# format the prompt
prompt = chat_template.format_prompt(domain=domain, topic=topic)
print(prompt.to_string())   # verify it shows your domain/topic


# instantiate model and call
model = ChatOllama(
    model="llama3.2",
    num_predict=10  # Maximum tokens to generate
)
# model = ChatOllama(model="llama3.2")
result = model.invoke(prompt.to_messages())

  # or prompt.to_messages() if invoke accepts messages

print()
print("========")
print(result.content)

print()
print("======RESP METADATA=======")
print(result.response_metadata)

print()
print("======USAGE METADATA=======")
print(result.usage_metadata)


# Enter domain
# insurance
# Enter topic
# annuity
# System: You are a helpful insurance expert.
# Human: Explain in simple terms, the concept of annuity in 5 points.

# ========
# Here's an explanation of the concept of annuity in 5 simple points:

# **1. What is an Annuity?**
# An annuity is a type of savings plan where you contribute money at regular intervals (e.g., monthly or yearly) for a set period, and in return, you receive a steady income stream for life.

# **2. Types of Annuities**
# There are two main types of annuities:
#         * Fixed Annuity: Offers a guaranteed interest rate and fixed payments.
#         * Variable Annuity: Invests your contributions in the stock market, offering potential for higher returns but also more risk.

# **3. How Annuities Work**
# You pay premiums (money) to the insurance company at regular intervals, usually monthly or quarterly. The insurance company uses these funds to generate interest and eventually pays you a set amount of money over a specified period.

# **4. Benefits of Annuities**
# Annuities can provide:
#         * Guaranteed income for life
#         * Tax benefits (depending on type)
#         * Protection from outliving your assets
#         * Potential long-term growth

# **5. Risks and Considerations**
# Before investing in an annuity, consider:
#         * Fees associated with the contract
#         * Interest rate fluctuations
#         * Credit risk (insurance company's ability to pay)
#         * Your financial goals and retirement needs

# ======RESP METADATA=======
# {
#     'model': 'llama3.2', 
#     'created_at': '2026-05-20T04:59:59.763025Z', 
#     'done': True, 
#     'done_reason': 'stop', 
#     'total_duration': 26272669833, 
#     'load_duration': 3131643208, 
#     'prompt_eval_count': 48, 
#     'prompt_eval_duration': 341971792, 
#     'eval_count': 281, 
#     'eval_duration': 22544179744, 
#     'logprobs': None, 
#     'model_name': 'llama3.2', 
#     'model_provider': 'ollama'
#   }

# ======USAGE METADATA=======
# {'input_tokens': 48, 'output_tokens': 281, 'total_tokens': 329}