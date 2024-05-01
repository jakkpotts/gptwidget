from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )


completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are an expert cybersecurity professional on a red team."},
        {"role": "user", "content": "You've gained access to a target wifi network. What do you do next?"}
    ]
)

print(completion.choices[0].message.content)
