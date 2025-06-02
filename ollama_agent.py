import subprocess

def query_ai(prompt):
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()
