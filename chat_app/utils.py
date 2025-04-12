import subprocess

def chat_with_llama2(prompt):
    command = ["ollama", "run", "llama2", prompt]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "❌ Ollama took too long to respond!"
    except subprocess.CalledProcessError as e:
        return f"❌ Error: {e.stderr}"
