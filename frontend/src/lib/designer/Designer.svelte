<script lang="ts">
  import { Button } from "flowbite-svelte";
  import { goto } from "@mateothegreat/svelte5-router";
  import { auth } from "../stores/authStore";
  import { onMount } from "svelte";
  import { get } from "svelte/store";
  import { KeychainAPI } from "../functions/crud";

  import LayerMenu from "./LayerMenu.svelte";
  import ItemMenu from "./ItemMenu.svelte";
  import Canvas from "./Canvas.svelte";

  const api = new KeychainAPI("http://localhost:8000");

  let { route } = $props();

  onMount(() => {
    if (!get(auth).loggedIn) {
      goto("/");
    }
    let chainId = route.result.path.params.id;
    getTree(chainId);
  });

  async function getTree(chainId: string) {
    let chain = await api.getChain(chainId);
    console.log(`Designer ID: ${JSON.stringify(chain)}`);
  }
</script>

<main class="grid grid-cols-6 min-h-screen relative">
  <!-- Top left: Buttons -->
  <div class="absolute top-4 left-4 z-10 flex flex-col gap-2">
    <Button
      color="blue"
      class="mb-2 w-32"
      onclick={() => goto("/dashboard") as any}>Back to List</Button
    >
    <Button color="red" class="w-32" onclick={() => goto("/") as any}
      >Logout</Button
    >
  </div>
  <!-- Left: ItemMenu -->
  <div class="col-span-1 flex items-center justify-start pl-8">
    <ItemMenu />
  </div>
  <!-- Center: Canvas -->
  <div class="col-span-4 flex flex-col items-center justify-center">
    <Canvas />
  </div>
  <!-- Right: LayerMenu -->
  <div class="col-span-1 flex items-center justify-end pr-8">
    <LayerMenu />
  </div>
</main>

<style>
</style>
