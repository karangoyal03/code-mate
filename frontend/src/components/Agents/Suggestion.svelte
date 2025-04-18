<script>
  import { code } from "../../store/codeStore.js";
  let data = "";
  async function fetchSuggestions() {
    const response = await fetch("http://localhost:8080/get-suggestions", {
      method: "POST",
      body: JSON.stringify({
        code: $code,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    // data = await response.json();
    // data = data.choices[0].message.content;
    //   return data;
    if (response.ok) {
      const reader = response.body
        ?.pipeThrough(new TextDecoderStream())
        .pipeThrough(splitstream("\n"))
        .getReader();
      newData = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const line = value.trim();
        if (line.startsWith("data: ")) {
          const jsonString = line.replace("/^data: /", "");
          if (jsonString === "[DONE]") break;
          try {
            let result = JSON.parse(jsonString);
            const content = result.choices?.[0]?.message.content || "";
            newData += content;
            data += newData;
          } catch (e) {
            console.error("Error parsing JSON:", e);
          }
        }
      }
    }
  }
</script>

<div>
  <p class="text-sm text-gray-500 dark:text-gray-400">
    <button onclick={fetchSuggestions}>Agent Suggestions</button>
    {data}
  </p>
</div>
