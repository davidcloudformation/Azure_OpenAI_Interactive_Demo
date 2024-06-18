import openai
import pandas as pd

# Load preprocessed data
data = pd.read_csv('data/preprocessed_data.csv')

# Set up OpenAI API
openai.api_key = 'your-api-key'

# Example 1: Basic Text Completion
response = openai.Completion.create(
  engine="davinci",
  prompt="Once upon a time",
  max_tokens=50
)
print("Example 1: Basic Text Completion")
print(response.choices[0].text.strip())

# Example 2: Few-shot Prompting
few_shot_prompt = """
Translate the following English text to French:

English: Hello, how are you?
French: Bonjour, comment ça va?

English: What is your name?
French: Quel est votre nom?

English: I love programming.
French: J'aime programmer.

English: This is a test.
French: Ceci est un test.

English: I am learning AI.
French: J'apprends l'IA.

English: The weather is nice today.
French: Le temps est agréable aujourd'hui.
"""
response = openai.Completion.create(
  engine="davinci",
  prompt=few_shot_prompt,
  max_tokens=60
)
print("Example 2: Few-shot Prompting")
print(response.choices[0].text.strip())

# Example 3: Summarization
text_to_summarize = """
Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by 
humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment 
and takes actions that maximize its chance of successfully achieving its goals.
"""
response = openai.Completion.create(
  engine="davinci",
  prompt="Summarize the following text: " + text_to_summarize,
  max_tokens=50
)
print("Example 3: Summarization")
print(response.choices[0].text.strip())

# Example 4: Contextual Prompting
context = "The capital of France is Paris."
response = openai.Completion.create(
  engine="davinci",
  prompt="Based on the context, what is the capital of France?",
  max_tokens=10
)
print("Example 4: Contextual Prompting")
print(response.choices[0].text.strip())

# Example 5: Chatbot Interaction
response = openai.Completion.create(
  engine="davinci",
  prompt="You are a helpful assistant. How can I assist you today?",
  max_tokens=50
)
print("Example 5: Chatbot Interaction")
print(response.choices[0].text.strip())