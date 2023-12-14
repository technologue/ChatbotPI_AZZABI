import openai
#openai.api_key = "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"
openai.api_key="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"
model = "text-davinci-003"
question = "C'est quoi HTML5 ?"

response = openai.Completion.create(model=model, prompt=question)

print(response)


