import openai 
client = openai.OpenAI()
# export OPENAI_API_KEY=xxxxxxxxxxxx

TEXT_TO_SUMMARIZE = 'transcribe_output.txt'

def openai_completion(prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[

        {"role": "user", "content": prompt} 
        
        ])
    return response.choices[0].message.content


with open(TEXT_TO_SUMMARIZE, 'r') as file:
    text_content = file.read()
    print("Text content loaded successfully.")


prompt = f"summarize the text in backticks `{text_content}`"


completion = openai_completion(prompt)
print("Completion:", completion)