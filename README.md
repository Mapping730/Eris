### **`README.md`**

# **Eris Chat - Local ChatGPT-like Interface**

Eris is a lightweight, Flask-based application that provides a **ChatGPT-like interface** for interacting with locally hosted LLaMA models using the `ollama` CLI. This project serves as a proof of concept to replicate the experience of OpenAI’s ChatGPT or OpenWebUI with additional flexibility to integrate local models.

---

## **Features**
- **Chat Interface**:
  - A clean, responsive web interface for chatting with your LLaMA model.
  - Includes advanced parameter controls to adjust model behavior in real time.
- **Local LLaMA Integration**:
  - Uses the `ollama` CLI to interact with a locally hosted LLaMA model.
- **Debugging Tools**:
  - Provides detailed logging of raw and cleaned outputs for better troubleshooting.
- **Modular Design**:
  - Clean separation of responsibilities between the Flask app (`app.py`) and model handling logic (`run_llama.py`).

---

## **How It Works**
1. **Model Interaction**:
   - User messages are sent to the `ollama` CLI through `run_llama.py`.
   - The script handles the model's input and cleans the output, removing ANSI escape codes or other unwanted artifacts.
2. **Web Interface**:
   - Built using Flask, the web UI allows users to interact with the model seamlessly.
   - Messages are displayed dynamically with user input at the bottom of the chat history.
3. **Advanced Parameters**:
   - Adjust parameters like `temperature`, `top_p`, and `system_prompt` directly through the web interface.

---

## **Setup Instructions**
### **Prerequisites**
- Python 3.11 or later
- `ollama` CLI installed and configured with your LLaMA model
- Flask (`pip install flask`)

### **Installation**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Eris
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Ensure your LLaMA model is set up and available:
   ```bash
   ollama pull llama3.2:1b
   ```

---

## **Usage**
1. Start the `ollama` server:
   ```bash
   ollama serve
   ```
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
4. Start chatting!

---

## **File Structure**
```
Eris/
│
├── app.py             # Flask application
├── run_llama.py       # Script for interacting with the ollama CLI
├── templates/
│   └── index.html     # Frontend HTML for the chat interface
├── static/
│   ├── style.css      # Stylesheet for the UI
│   └── script.js      # JavaScript for frontend interactivity
├── README.md          # Project documentation
```

---

## **Future Improvements**
1. **Enhanced Interface**:
   - Add support for markdown rendering in the chat history (e.g., code blocks, bold text).
   - Include more visual feedback, like typing indicators or a progress spinner.
2. **Model Customization**:
   - Allow real-time model swapping for users with multiple LLaMA versions.
3. **Database Integration**:
   - Save chat history for later review or analysis.
4. **API Expansion**:
   - Provide a RESTful API for external apps to interact with the model.
5. **Dockerization**:
   - Package the entire setup into a Docker container for easier deployment.

---

## **Contributing**
Feel free to fork the repository and submit pull requests! Contributions are welcome, whether they are bug fixes, new features, or documentation improvements.

---

## **License**
This project is open source and licensed under the [MIT License](LICENSE).

---

Let me know if you’d like me to adjust this further! 🚀
