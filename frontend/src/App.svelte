<script lang="ts">
  import Home from "./lib/Home.svelte";
  import Dashboard from "./lib/user/Dashboard.svelte";
  import Designer from "./lib/designer/Designer.svelte";
  import { Button } from "flowbite-svelte";
  import { Router, type RouteConfig } from "@mateothegreat/svelte5-router";

  const routes: RouteConfig[] = [
    {
      path: "/",
      component: Home,
    },
    {
      path: "/dashboard",
      component: Dashboard,
    },
    {
      path: "/designer",
      component: Designer,
    },
  ];
</script>

<main>
  <Router {routes} />
</main>

<style>
</style>
