import os

api_key = os.environ.get("MY_API_KEY")
if api_key:
    print(f"API Key: {api_key}")
else:
    print("API Key not found in environment variables.")

print("Hello")
