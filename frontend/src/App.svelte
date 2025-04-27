<script lang="ts">
  import { AlignCenterOutline } from "flowbite-svelte-icons";
  import "./app.css";
  import MonacoUploader from "./components/MonacoUploader.svelte";
  import Navbar from "./components/navbar.svelte";
  import Agent from "./components/Agent.svelte";
  import Bottom from "./components/Bottom.svelte";
  import Voice from "./components/Voice.svelte";
</script>

<main>
  <Navbar />
  <div class="flex h-screen">
    <div class="w-[70%] bg-blue-100">
      <MonacoUploader />
    </div>

    <div class="w-[30%] h-screen bg-light-100 overflow-auto">
      <Agent />
    </div>
  </div>
  <Voice />
  <Bottom />
</main>
