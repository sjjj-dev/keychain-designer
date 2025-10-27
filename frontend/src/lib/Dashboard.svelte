<script lang="ts">
  import { Button } from "flowbite-svelte";
  import { goto } from "@mateothegreat/svelte5-router";
  import { auth } from "./stores/authStore";
  import { onMount } from "svelte";
  import { get } from "svelte/store";

  // Dummy keychains
  let keychains = [
    { id: 1, name: "Work Keys" },
    { id: 2, name: "Home Keys" },
    { id: 3, name: "Gym Keys" },
  ];

  onMount(() => {
    if (!get(auth).loggedIn) {
      goto("/");
    }
  });

  function openDesigner(id?: number) {
    // Optionally pass id in the future
    goto("/designer");
  }
</script>

<main class="flex flex-col items-center justify-center min-h-screen">
  <h1 class="text-2xl text-blue-500 font-bold mb-4">Your Keychains</h1>
  <div class="flex flex-col gap-2 w-64 mb-4">
    <Button color="blue" class="w-full" onclick={() => openDesigner() as any}
      >+ Create New Keychain</Button
    >
    {#each keychains as kc}
      <Button
        color="light"
        class="w-full"
        onclick={() => openDesigner(kc.id) as any}>{kc.name}</Button
      >
    {/each}
  </div>
  <Button color="red" onclick={() => goto("/") as any}>Logout</Button>
</main>

<style>
</style>
