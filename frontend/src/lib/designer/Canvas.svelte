<script lang="ts">
  import type { Ring } from "../functions/types";
  import { addChainItem, getTree } from "../functions/utils";
  import DropZone from "./DropZone.svelte";

  let { chainTree } = $props();

  // Static asset paths for SVGs
  const ringImg = "/src/assets/rings/ring.svg";
  const keyImg = "/src/assets/keys/key.svg";
  const charmImgs: Record<string, string> = {
    HEART: "/src/assets/charms/heart.svg",
    STAR: "/src/assets/charms/star.svg",
    DIAMOND: "/src/assets/charms/diamond.svg",
    MOON: "/src/assets/charms/moon.svg",
    default: "/src/assets/charms/diamond.svg",
  };

  function getCharmImg(type: string): string {
    return charmImgs[type] || charmImgs.default;
  }

  async function handleItemDrop(ring: Ring, item: any) {
    if (item.create.color) {
      await addChainItem(
        ring.id,
        ring.chain_id,
        item.itemType,
        item.create.name,
        item.create.color,
        null
      );
    } else if (item.create.type) {
      await addChainItem(
        ring.id,
        ring.chain_id,
        item.itemType,
        item.create.name,
        null,
        item.create.type
      );
    }

    // Reload the chain tree to reflect the new item
    chainTree = await getTree(ring.chain_id);
  }

  async function handleDelete(itemType: string, id: string, chainId: string) {
    return;
  }
</script>

{#snippet RingNode(ring: Ring)}
  <div class="relative flex flex-col items-center my-4">
    <!-- Ring itself -->
    <div class="flex flex-col items-center">
      <img src={ringImg} alt="Ring" class="w-16 h-16" />
      <div class="text-white text-sm font-bold mt-1">{ring.name}</div>
    </div>

    <!-- Keys, Charms, and Child Rings -->
    <div class="flex flex-row gap-6 mt-2">
      <!-- Drop Zone -->
      <DropZone onDrop={(item) => handleItemDrop(ring, item)} />

      <!-- Keys -->
      {#each ring.keys as key (key.id)}
        <div class="relative flex flex-col items-center mb-2">
          <button
            class="absolute -top-2 -right-2 bg-red-600 text-white rounded-full w-5 h-5 text-xs flex items-center justify-center"
            onclick={() => handleDelete("key", key.id, ring.chain_id)}
            aria-label="Delete key"
            title="Delete"
          >
            ×
          </button>
          <img src={keyImg} alt="Key" class="w-12 h-12" />
          <div class="text-white text-xs mt-1">{key.name}</div>
        </div>
      {/each}

      <!-- Charms -->
      {#each ring.charms as charm (charm.id)}
        <div class="relative flex flex-col items-center mb-2">
          <button
            class="absolute -top-2 -right-2 bg-red-600 text-white rounded-full w-5 h-5 text-xs flex items-center justify-center"
            onclick={() => handleDelete("charm", charm.id, ring.chain_id)}
            aria-label="Delete charm"
            title="Delete"
          >
            ×
          </button>
          <img
            src={getCharmImg(charm.type)}
            alt={charm.type}
            class="w-12 h-12"
          />
          <div class="text-white text-xs mt-1">{charm.name}</div>
        </div>
      {/each}

      <!-- Child Rings (Recursive) -->
      {#each ring.rings as childRing (childRing.id)}
        {@render RingNode(childRing)}
      {/each}
    </div>
  </div>
{/snippet}

<div
  class="canvas-area w-full h-full bg-gray-900 flex flex-col items-center overflow-auto p-8"
>
  {#if chainTree}
    {@render RingNode(chainTree)}
  {:else}
    <div class="text-white">No chain loaded.</div>
  {/if}
</div>
