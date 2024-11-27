import subprocess
import subprocess
import re

# Function to remove ANSI escape codes
def strip_ansi_codes(text):
    ansi_escape = re.compile(r'(\x1b\[|\x9b)[0-?]*[ -/]*[@-~]|\x1b[@-_]')
    return ansi_escape.sub('', text)

def run_llama(model_name, user_message):
    try:
        # Call the `ollama` CLI
        process = subprocess.Popen(
            ["ollama", "run", model_name],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Send the input and capture output
        stdout, stderr = process.communicate(input=user_message)

        # Clean STDERR (for debugging or logging if needed)
        cleaned_stderr = strip_ansi_codes(stderr)

        # Clean and prepare the response
        final_response = stdout.strip()

        # Return both the response and any debug information
        return {"response": final_response, "debug": cleaned_stderr}
    except Exception as e:
        return {"error": str(e)}

# For testing the script directly
if __name__ == "__main__":
    MODEL_NAME = "llama3.2:1b"
    USER_MESSAGE = "hey"
    result = run_llama(MODEL_NAME, USER_MESSAGE)
    print(result)
