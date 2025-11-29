const statusLabel = document.getElementById("status-label");
const listenBtn = document.getElementById("listen-btn");
const stopBtn = document.getElementById("stop-btn");
const logDiv = document.getElementById("log");

function addLog(speaker, text) {
  const line = document.createElement("div");
  line.className = "log-line";
  line.innerHTML = `<span class="label">${speaker}:</span> ${text}`;
  logDiv.appendChild(line);
  logDiv.scrollTop = logDiv.scrollHeight;
}

let isListening = false;

listenBtn.addEventListener("click", async () => {
  if (isListening) return; // Already listening

  isListening = true;
  listenBtn.disabled = true;
  statusLabel.textContent = "Listening…";
  addLog("FRIDAY", "I'm listening. Please speak...");

  try {
    const response = await fetch("http://127.0.0.1:9000/api/listen");
    const data = await response.json();

    if (data.user) {
      addLog("You", data.user);
    } else {
      addLog("You", "(no speech detected)");
    }

    addLog("FRIDAY", data.friday || "(no response)");
  } catch (err) {
    console.error(err);
    addLog("FRIDAY", "Error talking to backend.");
  } finally {
    isListening = false;
    listenBtn.disabled = false;
    statusLabel.textContent = "Idle";
  }
});

stopBtn.addEventListener("click", () => {
  // This cannot cancel the backend listen (already running),
  // but we can mark the UI as idle.
  statusLabel.textContent = "Idle";
  addLog("FRIDAY", "Stop pressed (will apply to next command).");
});
