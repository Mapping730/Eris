from flask import Flask, request, jsonify, render_template
from run_llama import run_llama  # Import the function from run_llama.py

app = Flask(__name__)

MODEL_NAME = "llama3.2:1b"  # Replace with your model name

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    try:
        # Call the run_llama function
        result = run_llama(MODEL_NAME, user_message)

        # Check for errors in the result
        if "error" in result:
            return jsonify({"error": result["error"]})
        return jsonify({"response": result["response"], "debug": result["debug"]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
