import openai

#openai.api_key = "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"
openai.api_key="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"
client = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response)
