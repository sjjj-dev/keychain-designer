import { writable } from "svelte/store";

// Simple auth store: { loggedIn: boolean, username: string|null }
export const auth = writable({
  loggedIn: false,
  username: null,
  password: null,
});
