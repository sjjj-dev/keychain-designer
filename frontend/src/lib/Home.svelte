<script lang="ts">
  import { Button } from "flowbite-svelte";
  import { goto } from "@mateothegreat/svelte5-router";

  function handleLoginClick() {
    goto("/login");
  }

  function handleSignupClick() {
    goto("/signup");
  }
</script>

<main class="flex flex-col items-center justify-center min-h-screen">
  <div class="w-full max-w-md">
    <h1 class="text-3xl font-bold text-center mb-2 text-blue-600">
      Keychain Designer
    </h1>
    <p class="text-xl font-semibold text-center mb-8 text-gray-700">
      Create, customize, and organize your perfect keychain
    </p>

    <div class="flex flex-col gap-4">
      <Button color="blue" size="lg" class="w-full" onclick={handleLoginClick}>
        Login
      </Button>
      <Button color="dark" size="lg" class="w-full" onclick={handleSignupClick}>
        Sign Up
      </Button>
    </div>
  </div>
</main>

<style>
</style>
