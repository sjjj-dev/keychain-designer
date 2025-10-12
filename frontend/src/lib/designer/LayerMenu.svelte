<script lang="ts">
  import {
    chainTreeStore,
    type Ring,
    type Key,
    type Charm,
  } from "../stores/chainStore";
  import { derived } from "svelte/store";

  // Subscribe to the current chain tree
  let chainTree: Ring | null = null;
  const unsubscribe = chainTreeStore.subscribe((val) => {
    chainTree = val;
  });

  // Cleanup on destroy
  import { onDestroy } from "svelte";
  onDestroy(unsubscribe);

  // Recursive render function
  function renderRing(ring: Ring, indent = 0): any[] {
    const pad = "&nbsp;".repeat(indent * 4);
    let out = [`<div>${pad}<b>Ring:</b> ${ring.name}</div>`];
    for (const key of ring.keys) {
      out.push(`<div>${pad}&nbsp;&nbsp;Key: ${key.name}</div>`);
    }
    for (const charm of ring.charms) {
      out.push(`<div>${pad}&nbsp;&nbsp;Charm: ${charm.name}</div>`);
    }
    for (const child of ring.rings) {
      out = out.concat(renderRing(child, indent + 1));
    }
    return out;
  }
</script>

<div
  class="layer-menu p-2 text-white font-mono text-sm bg-gray-800 rounded max-h-96 overflow-auto"
>
  {#if chainTree}
    {@html renderRing(chainTree).join("")}
  {:else}
    <div>No chain loaded.</div>
  {/if}
</div>
