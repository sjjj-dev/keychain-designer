<script lang="ts">
  import type { Ring } from "../functions/types";
  let { chainTree } = $props();
</script>

{#snippet RingNode(ring: Ring, indent: number = 0)}
  {@const padding = indent * 4}

  <div style="padding-left: {padding * 4}px;">
    <b>Ring:</b>
    {ring.name}
  </div>

  {#each ring.keys as key (key.id)}
    <div style="padding-left: {(padding + 2) * 4}px;">
      Key: {key.name}
    </div>
  {/each}

  {#each ring.charms as charm (charm.id)}
    <div style="padding-left: {(padding + 2) * 4}px;">
      Charm: {charm.name}
    </div>
  {/each}

  {#each ring.rings as childRing (childRing.id)}
    {@render RingNode(childRing, indent + 1)}
  {/each}
{/snippet}

<div
  class="layer-menu p-2 text-white font-mono text-sm bg-gray-800 rounded max-h-96 overflow-auto"
>
  {#if chainTree}
    {@render RingNode(chainTree)}
  {:else}
    <div>No chain loaded.</div>
  {/if}
</div>

<style>
</style>
