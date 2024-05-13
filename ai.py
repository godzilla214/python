import openai

# Set your OpenAI API key
api_key = "YOUR_API_KEY"
openai.api_key = api_key

# Generate image using DeepAI's API
response = openai.Image.create(
    model="image-generator-v1",
    prompts=["a scenic landscape with mountains and a lake"],
    temperature=0.5,
    max_tokens=200
)

# Print the generated image URL
print(response.url)