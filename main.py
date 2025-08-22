    import os

    api_key = os.environ.get('CLOUD_PASS_KEY')
    if api_key:
        print(f"API Key: {api_key}")
    else:
        print("API Key not found in environment variables.")
