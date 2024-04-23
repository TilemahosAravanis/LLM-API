import cohere

API_KEY = 'Bf7BYX4apb7AZEVfGGdsZojD5uvD3BfCgNZaRlJk'

def Chat(history: list[dict], prompt: str):
    # Enter your free API key
    co = cohere.Client(API_KEY)
    
    response = co.chat(
    # choose one of the available cohere models
    model = 'command-r-plus',
    # Provide previous conversation
    chat_history=history,
    # Ask something
    message=prompt,
    # perform web search before answering the question. You can also use your own custom connector.
    connectors=[{"id": "web-search"}]
    )

    return response
