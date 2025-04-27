<script>
  import { code } from "../../store/codeStore.js";
  let data = "";

  async function fetchSuggestions() {
    const response = await fetch("http://localhost:8080/get-suggestions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code: $code }),
    });

    if (!response.ok || !response.body) {
      console.error("No response body");
      return;
    }
    console.log("Response body:", response.json()); // Debugging line
    // const reader = response.body.getReader();
    // const decoder = new TextDecoder("utf-8");

    // let buffer = "";

    // while (true) {
    //   const { done, value } = await reader.read();
    //   if (done) break;

    //   buffer += decoder.decode(value, { stream: true });

    //   console.log("Buffer:", buffer); // Debugging line

    //   // Split by newlines
    //   const lines = buffer.split("\n");
    //   buffer = lines.pop(); // Keep the last unfinished line

    //   for (let line of lines) {
    //     line = line.trim();
    //     if (!line.startsWith("data: ")) continue;

    //     const jsonString = line.slice(6); // remove 'data: '
    //     if (jsonString === "[DONE]") return;

    //     try {
    //       const parsed = JSON.parse(jsonString);
    //       const content = parsed.text || "";
    //       data += content;
    //     } catch (err) {
    //       console.error("Parse error:", err, jsonString);
    //     }
    //   }
    // }
  }
</script>

<div>
  <button on:click={fetchSuggestions}>Get Suggestions</button>
  <pre class="whitespace-pre-wrap">{data}</pre>
</div>
