import openai

# Set your OpenAI API key
openai.api_key = "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"

# Create a chat completion
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use a valid model
        messages=[
            {"role": "system", "content": "You are a helpful virtual assistant named Jarvis."},
            {"role": "user", "content": "What is coding?"}
        ]
    )

    # Print the response
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"An error occurred: {e}")
