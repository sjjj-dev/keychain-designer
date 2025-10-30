<script lang="ts">
  interface Props {
    onDrop: (data: any) => void;
  }

  let { onDrop }: Props = $props();

  let isHovering = $state(false);

  function handleDragOver(e: DragEvent) {
    e.preventDefault();
    isHovering = true;
  }

  function handleDragLeave(e: DragEvent) {
    isHovering = false;
  }

  function handleDrop(e: DragEvent) {
    e.preventDefault();
    isHovering = false;

    const data = JSON.parse(e.dataTransfer!.getData("application/json"));
    onDrop(data);
  }
</script>

<div
  class="w-16 h-16 border-2 border-dashed rounded-lg flex items-center justify-center transition-colors cursor-pointer"
  class:border-gray-600={!isHovering}
  class:border-blue-400={isHovering}
  class:bg-blue-900={isHovering}
  class:hover:border-blue-400={!isHovering}
  role="button"
  tabindex="0"
  aria-label="Drop items here"
  ondragover={handleDragOver}
  ondragleave={handleDragLeave}
  ondrop={handleDrop}
>
  <svg
    class="w-8 h-8 text-gray-600 pointer-events-none"
    fill="none"
    stroke="currentColor"
    viewBox="0 0 24 24"
  >
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
      d="M12 4v16m8-8H4"
    />
  </svg>
</div>
