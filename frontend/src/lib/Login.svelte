<script lang="ts">
  import { Button, Input } from "flowbite-svelte";
  import { goto } from "@mateothegreat/svelte5-router";
  import { auth } from "./stores/authStore";
  import { KeychainAPI } from "./functions/crud";

  const api = new KeychainAPI("http://localhost:8000");

  let email = "";
  let error = "";
  let isLoading = false;

  async function handleLogin(e: Event) {
    e.preventDefault();
    error = "";

    if (!email.trim()) {
      error = "Please enter a email.";
      return;
    }

    isLoading = true;
    try {
      const user = await api.getUserByEmail(email);
      auth.set({ loggedIn: true, user_id: user.id, password: "" });
      goto("/dashboard");
    } catch (err) {
      error = err instanceof Error ? err.message : "Login failed";
    } finally {
      isLoading = false;
    }
  }
</script>

<main class="flex flex-col items-center justify-center min-h-screen">
  <div class="w-full max-w-md">
    <h1 class="text-3xl font-bold text-center mb-2 text-blue-600">
      Keychain Designer
    </h1>
    <h2 class="text-xl font-semibold text-center mb-8 text-gray-700">Login</h2>

    <form class="flex flex-col gap-4" on:submit|preventDefault={handleLogin}>
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
          Email
        </label>
        <Input
          id="email"
          type="text"
          placeholder="Enter your email"
          bind:value={email}
          disabled={isLoading}
        />
      </div>

      {#if error}
        <div class="text-red-600 text-sm bg-red-50 p-3 rounded">{error}</div>
      {/if}

      <Button color="blue" type="submit" disabled={isLoading} class="w-full">
        {isLoading ? "Logging in..." : "Login"}
      </Button>
    </form>

    <div class="text-center mt-6">
      <p class="text-gray-600">
        Don't have an account?
        <a
          href="/signup"
          class="text-blue-600 hover:text-blue-800 font-semibold"
        >
          Sign up
        </a>
      </p>
    </div>
  </div>
</main>

<style>
</style>
