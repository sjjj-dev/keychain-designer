<script lang="ts">
  // Import SVGs as static assets
  // Vite will resolve these imports at build time
  import ringImg from "../../assets/rings/ring.svg";
  import keyImg from "../../assets/keys/key.svg";
  import charmDiamond from "../../assets/charms/diamond.svg";
  import charmHeart from "../../assets/charms/heart.svg";
  import charmMoon from "../../assets/charms/moon.svg";
  import charmStar from "../../assets/charms/star.svg";

  const ringSvgs = [{ name: "Ring", src: ringImg }];
  const keySvgs = [{ name: "Key", src: keyImg }];
  const charmSvgs = [
    { name: "Diamond", src: charmDiamond },
    { name: "Heart", src: charmHeart },
    { name: "Moon", src: charmMoon },
    { name: "Star", src: charmStar },
  ];
</script>

<div class="item-menu space-y-6 p-4 bg-gray-800 rounded text-white">
  <div>
    <div class="font-bold mb-1">Rings</div>
    <div class="flex flex-row gap-3 items-center">
      {#each ringSvgs as ring}
        <img
          src={ring.src}
          alt={ring.name}
          class="w-12 h-12 bg-gray-700 rounded p-1"
        />
      {/each}
    </div>
  </div>
  <div>
    <div class="font-bold mb-1">Keys</div>
    <div class="flex flex-row gap-3 items-center">
      {#each keySvgs as key}
        <img
          src={key.src}
          alt={key.name}
          class="w-12 h-12 bg-gray-700 rounded p-1"
        />
      {/each}
    </div>
  </div>
  <div>
    <div class="font-bold mb-1">Charms</div>
    <div class="flex flex-col gap-3 items-center">
      {#each charmSvgs as charm}
        <img
          src={charm.src}
          alt={charm.name}
          class="w-12 h-12 bg-gray-700 rounded p-1"
        />
      {/each}
    </div>
  </div>
</div>
