<script lang="ts">
  import { Button } from "flowbite-svelte";
  import { goto } from "@mateothegreat/svelte5-router";
  import { auth } from "./stores/authStore";
  import { onMount } from "svelte";
  import { get } from "svelte/store";
  import { KeychainAPI } from "./functions/crud";

  const api = new KeychainAPI("http://localhost:8000");

  let keychains = $state([]);

  onMount(() => {
    if (!get(auth).loggedIn) {
      goto("/");
    }
    getChains();
  });

  function openDesigner(id?: string) {
    goto(`/designer/${id}`);
  }

  async function getChains() {
    let chains = await api.listChains("4d0b150a-e5d0-4ed6-8ecd-c43c34f4866f");
    for (let chain of chains) {
      keychains.push({ id: chain.id, name: chain.name });
    }
  }
</script>

<main class="flex flex-col items-center justify-center min-h-screen">
  <h1 class="text-2xl text-blue-500 font-bold mb-4">Your Keychains</h1>
  <div class="flex flex-col gap-2 w-64 mb-4">
    <Button color="blue" class="w-full" onclick={() => openDesigner() as any}
      >+ Create New Keychain</Button
    >
    {#each keychains as kc}
      <Button color="light" class="w-full" onclick={() => openDesigner(kc.id)}
        >{kc.name}</Button
      >
    {/each}
  </div>
  <Button color="red" onclick={() => goto("/") as any}>Logout</Button>
</main>

<style>
</style>
