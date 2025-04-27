<script>
  let mediaRecorder;
  let audioChunks = [];
  let audioBlob = null;
  let isRecording = false;

  async function sendAudio(audioBlob) {
    try {
      const response = await fetch("http://localhost:8080/transcribe", {
        method: "POST",
        // Remove 'mode: 'no-cors'' to allow reading the response
        headers: {
          "Content-Type": "audio/webm",
        },
        body: audioBlob,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const result = await response.json();
      console.log("Transcribed Text:", result.text);
      return result.text;
    } catch (error) {
      console.error("Error sending audio:", error);
      return null;
    }
  }
  async function toggleRecording() {
    if (isRecording) {
      mediaRecorder.stop();
      isRecording = false;
      sendAudio(audioBlob);
    } else {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };

      mediaRecorder.onstop = () => {
        audioBlob = new Blob(audioChunks, { type: "audio/webm" });
        audioChunks = [];
      };

      mediaRecorder.start();
      isRecording = true;
    }
  }
</script>

<button on:click={toggleRecording}>
  {isRecording ? "Stop Recording" : "Start Recording"}
</button>
