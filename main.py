from openai import OpenAI

client = OpenAI()


# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

def query_gpt():
    role = input("GPT Role: ")
    ask = input("Ask: ")

    query = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": ask}
        ],
        stream=True
    )

    # Stream the response, end="" is to ensure output is streamed
    # with readbility since the stream is in chunks
    for chunk in query:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    print("\n")


while True:
    query_gpt()


# Print the completed output
# print(query.choices[0].message.content)
