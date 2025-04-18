<script>
  import { Tabs, TabItem } from "flowbite-svelte";
  import Suggestion from "./Agents/Suggestion.svelte";
  import Testing from "./Agents/Testing.svelte";
</script>

<Tabs style="color: #0076CE !important;">
  <TabItem open title="Agent Suggestions">
    <Suggestion />
  </TabItem>
  <TabItem title="Testing Agent">
    <Testing />
  </TabItem>
</Tabs>
