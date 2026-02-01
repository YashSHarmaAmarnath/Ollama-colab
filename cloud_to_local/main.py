import ollama

def ask_llm(prompt, client,history=None,model='gemma3'):
    messages = []
    if history:
        for u, b in history:
            messages.append({"role": "user", "content": u})
            messages.append({"role": "assistant", "content": b})
    messages.append({"role": "user", "content": prompt})

    response = client.chat(
        model=model,
        messages=messages,
        stream=False
    )
    return response["message"]["content"]

def start_chat(client, model='gemma3'):
    history = []
    while True:
        prompt = input("\nask-> ")
        if prompt in ('/bye', 'exit'): break
        response = ask_llm(prompt=prompt,client=client,history=history,model=model)
        print("\n",response)
        history.append((prompt,response))
    return history

if __name__ == "__main__":
    remote_host = "https://lunch-wednesday-priorities-sin.trycloudflare.com/"

    client = ollama.Client(host=remote_host)

    start_chat(client=client,model="gemma3")
