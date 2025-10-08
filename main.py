from ollama import chat, ChatResponse

def chat_with_ollama(model: str) -> None:
    """
    Simple interactive chat with a local Ollama model.
    """
    print(f"💬 Starting chat with Ollama model: {model}")
    print("Type 'exit' to end.\n")

    messages = []

    while True:
        user_input = input("You: ")
        user_input = user_input.strip().lower()
        if user_input in {"exit", "quit"}:
            print("👋 Ending chat.")
            break

        messages.append({"role": "user", "content": user_input})
        response: ChatResponse = chat(model=model, messages=messages)

        reply = response.message.content
        print(f"{model}: {reply}\n")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    chat_with_ollama("gemma3")
