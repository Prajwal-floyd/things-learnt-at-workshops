import os
from openai import OpenAI

# Set Parameters
model_id = "minimax/minimax-m2.5:free"

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# Loop until user enters "quit"
while True:
    # Query to send to llm
    query = input("👤 Enter your query (or 'quit' to exit): ")

    # Check if user wants to quit
    if query.lower() == "quit":
        print("Goodbye!")
        break

    # Make the API call using OpenRouter
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            max_tokens=1024
        )

        # Extract and print the response
        output = response.choices[0].message.content
        print(f"👤 Query: {query}")
        print(f"\nResponse:\n{output}\n")

    except Exception as e:
        print(f"Error calling OpenRouter: {e}\n")