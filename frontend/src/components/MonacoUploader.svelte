<script lang="ts">
  import { onMount } from "svelte";
  import * as monaco from "monaco-editor";

  let editorContainer: HTMLDivElement;
  let fileContent: string = "";
  let editor: monaco.editor.IStandaloneCodeEditor | null = null;

  function handleFileUpload(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      fileContent = e.target?.result as string;
      if (editor) {
        editor.setValue(fileContent);
      }
    };
    reader.readAsText(file);
  }

  onMount(() => {
    editor = monaco.editor.create(editorContainer, {
      value: fileContent,
      language: "javascript",
      theme: "vs-light",
      automaticLayout: true,
    });
  });
  console.log("content", editor);
</script>

<div class="p-4">
  <input
    type="file"
    accept=".txt,.js,.ts,.json,.html,.css"
    on:change={handleFileUpload}
    class="mb-4"
  />
  <div bind:this={editorContainer} class="editor-container"></div>
</div>

<style>
  .editor-container {
    height: 70vh;
    width: 100%;
    border: 1px solid #ccc;
  }
</style>
