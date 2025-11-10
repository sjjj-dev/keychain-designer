<script lang="ts">
  import ringImg from "../../assets/rings/ring.svg";
  import keyImg from "../../assets/keys/key.svg";
  import charmDiamond from "../../assets/charms/diamond.svg";
  import charmHeart from "../../assets/charms/heart.svg";
  import charmMoon from "../../assets/charms/moon.svg";
  import charmStar from "../../assets/charms/star.svg";

  const DEFAULT_RING_COLOR = "SILVER";
  const DEFAULT_KEY_COLOR = "RED";
  const DEFAULT_CHARM_TYPE = "HEART";

  const ringSvgs: { name: string; src: string }[] = [
    { name: "Ring", src: ringImg },
  ];
  const keySvgs: { name: string; src: string }[] = [
    { name: "Key", src: keyImg },
  ];
  const charmSvgs = [
    { name: "Diamond", src: charmDiamond },
    { name: "Heart", src: charmHeart },
    { name: "Moon", src: charmMoon },
    { name: "Star", src: charmStar },
  ];

  // Build the payload that will be attached to the drag event. The consumer
  // (drop handler) should fill in runtime values like chain_id and parent_id
  // before calling the API.
  function handleDragStart(e: DragEvent, payload: Record<string, any>) {
    e.dataTransfer!.effectAllowed = "copy";
    e.dataTransfer!.setData("application/json", JSON.stringify(payload));
  }
</script>

<div class="item-menu space-y-6 p-4 bg-gray-800 rounded text-white">
  <div>
    <div class="font-bold mb-1">Rings</div>
    <div class="flex flex-row gap-3 items-center">
      {#each ringSvgs as ring}
        <img
          src={ring.src}
          alt={ring.name}
          class="w-12 h-12 bg-gray-700 rounded p-1 cursor-move"
          draggable="true"
          ondragstart={(e) =>
            handleDragStart(e, {
              itemType: "ring",
              create: {
                name: ring.name,
                color: DEFAULT_RING_COLOR,
              },
            })}
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
          class="w-12 h-12 bg-gray-700 rounded p-1 cursor-move"
          draggable="true"
          ondragstart={(e) =>
            handleDragStart(e, {
              itemType: "key",
              create: {
                name: key.name,
                color: DEFAULT_KEY_COLOR,
              },
            })}
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
          class="w-12 h-12 bg-gray-700 rounded p-1 cursor-move"
          draggable="true"
          ondragstart={(e) =>
            handleDragStart(e, {
              itemType: "charm",
              create: {
                name: charm.name,
                type: DEFAULT_CHARM_TYPE,
              },
            })}
        />
      {/each}
    </div>
  </div>
</div>
