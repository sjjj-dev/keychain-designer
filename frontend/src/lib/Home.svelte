<script lang="ts">
  import { Button, Input } from "flowbite-svelte";
  import { goto } from "@mateothegreat/svelte5-router";
  import { auth } from "./stores/authStore";
  let username = "";
  let error = "";

  function handleLogin(e: Event) {
    e.preventDefault();
    if (username.trim()) {
      auth.set({ loggedIn: true, username });
      goto("/dashboard");
    } else {
      error = "Please enter username.";
    }
  }
</script>

<main class="flex flex-col items-center justify-center min-h-screen">
  <h1 class="text-2xl text-blue-500 font-bold mb-4">Keychain Designer Login</h1>
  <form class="flex flex-col gap-3 w-64" on:submit|preventDefault={handleLogin}>
    <Input
      class="border rounded px-2 py-1"
      type="text"
      placeholder="Username"
      bind:value={username}
    />
    {#if error}
      <div class="text-red-600 text-sm">{error}</div>
    {/if}
    <Button color="blue" type="submit">Login</Button>
  </form>
</main>

<style>
</style>
