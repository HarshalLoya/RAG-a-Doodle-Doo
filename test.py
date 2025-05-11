# import torch

# print(torch.__version__)           # Should print something like '2.2.2' or newer
# print(torch.version.cuda)          # Should print '12.8'
# print(torch.cuda.is_available())   # Should be True if GPU is accessible


# from sentence_transformers import SentenceTransformer
# import torch

# model = SentenceTransformer('all-MiniLM-L6-v2')
# print("CUDA available:", torch.cuda.is_available())
# print("Device:", model.device)

import openai
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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"
)

response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python used for?"}
    ]
)
print(response.choices[0].message.content)