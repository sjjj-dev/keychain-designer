<script lang="ts">
  import { chainTreeStore, type Ring } from "../stores/chainStore";
  import { onDestroy } from "svelte";

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

  let chainTree: Ring | null = null;
  const unsubscribe = chainTreeStore.subscribe((val) => {
    chainTree = val;
  });
  onDestroy(unsubscribe);

  // Helper to get charm SVG
  function getCharmImg(type: string) {
    return charmImgs[type] || charmImgs["default"];
  }

  // Recursive function to render a ring and its children
  export function renderRing(ring: Ring) {
    return `
      <div class="flex flex-col items-center my-4">
        <div class="flex flex-col items-center">
          <img src="${ringImg}" alt="Ring" class="w-16 h-16" />
          <div class="text-white text-sm font-bold mt-1">${ring.name}</div>
        </div>
        <div class="flex flex-row gap-6 mt-2">
          ${ring.keys
            .map(
              (key) => `
            <div class="flex flex-col items-center mb-2">
              <img src="${keyImg}" alt="Key" class="w-12 h-12" />
              <div class="text-white text-xs mt-1">${key.name}</div>
            </div>
          `
            )
            .join("")}
          ${ring.charms
            .map(
              (charm) => `
            <div class="flex flex-col items-center mb-2">
              <img src="${getCharmImg(charm.type)}" alt="${charm.type}" class="w-12 h-12" />
              <div class="text-white text-xs mt-1">${charm.name}</div>
            </div>
          `
            )
            .join("")}
          ${ring.rings.map((child) => renderRing(child)).join("")}
        </div>
      </div>
    `;
  }
</script>

<div
  class="canvas-area w-full h-full bg-gray-900 flex flex-col items-center overflow-auto p-8"
>
  {#if chainTree}
    {#if chainTree}
      {@html renderRing(chainTree)}
    {/if}
  {:else}
    <div class="text-white">No chain loaded.</div>
  {/if}
</div>

<!-- Recursive rendering using Svelte blocks -->
{#if false}<!-- This block is just to allow the function below to be in the file -->{/if}
{@html ""}
<!-- Svelte requires at least one markup node outside <script> -->
