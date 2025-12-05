import { writable } from "svelte/store";

// Simple auth store: { loggedIn: boolean, username: string|null }
export const auth = writable({
  loggedIn: false,
  user_id: null,
  password: null,
});
