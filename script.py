from seatable_api import Base, context
import requests
server_url = context.server_url or 'https://cloud.seatable.io'
api_token = context.api_token or 'YOUR_API_TOKEN' #Replace with your actual API token

base = Base(api_token, server_url)
base.auth()

# Get data from seatable
name = context.current_row['Name']

# Send data to ChatGPT
model = "text-davinci-001"  # Replace with desired model
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR-API-KEY"  # Replace YOUR-API-KEY with your actual API key
}

data = {
    "model": model,
    "messages": [
        {
            "role": "system",
            "content": "You are an expert in anthroponymy." # Replace with desired system prompt
        },
        {
            "role": "user",
            "content": "Tell me about " + name + "."  # Replace with desired user prompt
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
json = response.json()
# Accessing content within choices
message = json["choices"][0]["message"]

# Update seatable row with data from ChatGPT

row_data = {
    'Meaning': message['content'],
}
base.update_row(context.current_table, context.current_row['_id'], row_data)



