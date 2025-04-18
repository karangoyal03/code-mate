import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
// import monacoEditorPlugin from "vite-plugin-monaco-editor";

// console.log("Vite config loaded",monacoEditorPlugin);

export default defineConfig({
  plugins: [tailwindcss(), svelte()],
  optimizeDeps: {
    include: ["monaco-editor"],
  },
});
