<script lang="ts">
  import Home from "./lib/Home.svelte";
  import Dashboard from "./lib/Dashboard.svelte";
  import Designer from "./lib/designer/Designer.svelte";
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
    {
      path: "/designer/(?<id>[a-z0-9-]{36})",
      component: Designer,
    },
  ];
</script>

<main>
  <Router {routes} />
</main>

<style>
</style>
