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
    getChains(get(auth).user_id);
  });

  async function openDesigner(id: string | null = null) {
    if (!id) {
      id = (
        await api.createChain({
          user_id: get(auth).user_id,
          name: "New Keychain",
        })
      ).id;
    }
    goto(`/designer/${id}`);
  }

  async function getChains(userId: string) {
    let chains = await api.listChains(userId);
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
      <Button color="dark" class="w-full" onclick={() => openDesigner(kc.id)}
        >{kc.name}</Button
      >
    {/each}
  </div>
  <Button color="red" onclick={() => goto("/") as any}>Logout</Button>
</main>

<style>
</style>
