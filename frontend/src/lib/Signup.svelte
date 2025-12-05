<script lang="ts">
  import { Button, Input } from "flowbite-svelte";
  import { goto } from "@mateothegreat/svelte5-router";
  import { auth } from "./stores/authStore";

  let username = "";
  let email = "";
  let displayName = "";
  let error = "";
  let isLoading = false;

  async function handleSignup(e: Event) {
    e.preventDefault();
    error = "";

    if (!username.trim()) {
      error = "Please enter a username.";
      return;
    }

    if (!email.trim()) {
      error = "Please enter an email.";
      return;
    }

    if (!displayName.trim()) {
      error = "Please enter a display name.";
      return;
    }

    isLoading = true;
    try {
      // TODO: Call actual signup endpoint
      auth.set({ loggedIn: true, username, password: "" });
      goto("/dashboard");
    } catch (err) {
      error = err instanceof Error ? err.message : "Signup failed";
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
    <h2 class="text-xl font-semibold text-center mb-8 text-gray-700">
      Sign Up
    </h2>

    <form class="flex flex-col gap-4" on:submit|preventDefault={handleSignup}>
      <div>
        <label
          for="username"
          class="block text-sm font-medium text-gray-700 mb-2"
        >
          Username
        </label>
        <Input
          id="username"
          type="text"
          placeholder="Choose a username"
          bind:value={username}
          disabled={isLoading}
        />
      </div>

      <div>
        <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
          Email
        </label>
        <Input
          id="email"
          type="email"
          placeholder="Enter your email"
          bind:value={email}
          disabled={isLoading}
        />
      </div>

      <div>
        <label
          for="displayName"
          class="block text-sm font-medium text-gray-700 mb-2"
        >
          Display Name
        </label>
        <Input
          id="displayName"
          type="text"
          placeholder="Enter your display name"
          bind:value={displayName}
          disabled={isLoading}
        />
      </div>

      {#if error}
        <div class="text-red-600 text-sm bg-red-50 p-3 rounded">{error}</div>
      {/if}

      <Button color="blue" type="submit" disabled={isLoading} class="w-full">
        {isLoading ? "Creating account..." : "Sign Up"}
      </Button>
    </form>

    <div class="text-center mt-6">
      <p class="text-gray-600">
        Already have an account?
        <a href="/" class="text-blue-600 hover:text-blue-800 font-semibold">
          Log in
        </a>
      </p>
    </div>
  </div>
</main>

<style>
</style>
