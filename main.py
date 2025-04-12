import subprocess

conversation_history = []

def chat_with_llama2(prompt):
    global conversation_history
    conversation_history.append(f"You: {prompt}")

    full_prompt = "\n".join(conversation_history) + "\nAI:"

    command = ["ollama", "run", "llama2", full_prompt]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        response = result.stdout.strip()

        conversation_history.append(f"AI: {response}")
        return response
    except subprocess.TimeoutExpired:
        return "❌ Ollama took too long to respond!"
    except subprocess.CalledProcessError as e:
        return f"❌ Error: {e.stderr}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat_with_llama2(user_input)
        print(f"🤖 AI: {response}")
