import subprocess
import re

MODEL_NAME = "llama3.2:1b"
USER_MESSAGE = "hey"  # Replace with your test input

# Improved function to remove all ANSI escape sequences and cursor control codes
def strip_ansi_codes(text):
    ansi_escape = re.compile(r'(\x1b\[|\x9b)[0-?]*[ -/]*[@-~]|\x1b[@-_]')
    return ansi_escape.sub('', text)

def debug_ollama():
    print("=== STEP 1: Preparing to Run `ollama` ===")
    try:
        # Attempt to call the ollama CLI
        print(f"Model Name: {MODEL_NAME}")
        print(f"User Message: {USER_MESSAGE}")

        process = subprocess.Popen(
            ["ollama", "run", MODEL_NAME],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("=== STEP 2: Subprocess Started Successfully ===")

        # Send the input and capture output
        stdout, stderr = process.communicate(input=USER_MESSAGE)

        print("\n=== STEP 3: Capturing Output ===")
        print("\n--- RAW STDOUT ---")
        print(repr(stdout))  # Raw model response

        print("\n--- RAW STDERR (Before Cleaning) ---")
        print(repr(stderr))

        # Clean up STDERR
        cleaned_stderr = strip_ansi_codes(stderr)
        print("\n--- CLEANED STDERR ---")
        print(cleaned_stderr)

        # Final response to use (STDOUT or cleaned STDERR if needed)
        final_response = stdout.strip()
        print("\n--- FINAL RESPONSE ---")
        print(final_response)

    except Exception as e:
        print("\n=== STEP 5: Exception Encountered ===")
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    debug_ollama()
