import openai


with open("side-project/openai-project/openai_key", "r") as key_file:
    api_key = key_file.read()
    print(api_key)


openai.api_key = "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"


response = openai.Completion.create(
    model="gpt-3.5-turbo",
    promopt="Write a tagline for an ice cream shop",
    temperature=0.7,
    max_token=300,
)

print(response)
