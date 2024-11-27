document.getElementById("send-btn").addEventListener("click", async () => {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    const chatBox = document.getElementById("chat-box");

    // Add user message
    const userMessage = document.createElement("div");
    userMessage.classList.add("user");
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    // Scroll to show the latest message
    chatBox.scrollTop = chatBox.scrollHeight;

    // Simulate AI response
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();

    // Add AI message
    const aiMessage = document.createElement("div");
    aiMessage.classList.add("ai");
    aiMessage.textContent = data.response;
    chatBox.appendChild(aiMessage);

    // Scroll to show the latest message again
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear input box
    document.getElementById("user-input").value = "";
});
