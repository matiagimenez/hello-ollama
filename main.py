from ollama import ChatResponse, chat

from utils import Tokenizer


def chat_with_ollama(model: str) -> None:
    """
    Simple interactive chat with a local Ollama model.
    """
    print(f"💬 Starting chat with Ollama model: {model}")
    print("Type 'exit' to end.\n")

    messages = []
    tokenizer = Tokenizer(encoding="cl100k_base")

    while True:
        user_input = input("You: ")
        user_input = user_input.strip().lower()

        if user_input in {"exit", "quit"}:
            print("👋 Ending chat.")
            break

        messages.append({"role": "user", "content": user_input})
        response: ChatResponse = chat(model=model, messages=messages)

        reply = response.message.content
        output_tokens = tokenizer.tokenize(reply)
        print(f"{model} ({len(output_tokens)} output tokens): {reply}\n")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    chat_with_ollama("gemma3")
