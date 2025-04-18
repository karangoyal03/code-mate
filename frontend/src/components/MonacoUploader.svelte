<script lang="ts">
  import { onMount } from "svelte";
  import * as monaco from "monaco-editor";
  import { code } from "../store/codeStore.js"; 

  let editorContainer: HTMLDivElement;
  let fileContent: string = "";
  let editor: monaco.editor.IStandaloneCodeEditor | null = null;

  function handleFileUpload(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      fileContent = e.target?.result as string;
      code.set(fileContent);
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
    editor.onDidChangeModelContent(() => {
      const value = editor?.getValue() || "";
      code.set(value);
    });
    const unsubscribe = code.subscribe((val) => {
      if (editor && editor.getValue() !== val) {
        editor.setValue(val);
      }
    });
    return () => unsubscribe();
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
    height: 90vh;
    width: 100%;
    border: 1px solid #ccc;
  }
</style>
