import { KeychainAPI } from "./crud";
import type { Charm, Key, Ring } from "./types";

const api = new KeychainAPI("http://localhost:8000");

async function getSubTree(ringId: string): Promise<Ring> {
  let ring = await api.getRing(ringId);
  let keys: Key[] = (await api.listKeys({ parent_id: ringId })) as Key[];
  let charms: Charm[] = (await api.listCharms({
    parent_id: ringId,
  })) as Charm[];
  let childRings = await api.listRings({ parent_id: ringId });
  let subTrees: Ring[] = [];
  for (let childRing of childRings) {
    subTrees.push(await getSubTree(childRing.id));
  }
  return {
    id: ring.id,
    parent_id: ring.parent_id,
    chain_id: ring.chain_id,
    name: ring.name,
    color: ring.color,
    rings: subTrees,
    keys: keys,
    charms: charms,
  };
}

export async function getTree(chainId: string): Promise<Ring> {
  console.log(`Getting tree for chain ID: ${chainId}`);
  let chain = await api.getChain(chainId);
  let rootId = chain.root_id;
  let tree = await getSubTree(rootId);
  console.log(`Tree: ${JSON.stringify(tree)}`);
  return tree;
}

export async function createRootRing(
  chainId: string,
  color: string | null
): Promise<Ring> {
  console.log(`Creating root ring for chain ID: ${chainId}`);
  let ring = await api.createRing({
    parent_id: null,
    chain_id: chainId,
    name: "Root Ring",
    color: color,
  });
  console.log(`Created root ring: ${JSON.stringify(ring)}`);
  return ring as Ring;
}

export async function addChainItem(
  parentId: string,
  chainId: string,
  itemType: "ring" | "key" | "charm",
  name: string,
  color: string | null,
  type: string | null
): Promise<void> {
  console.log(
    `Adding item of type ${itemType} with name ${name} to parent ID ${parentId} in chain ID ${chainId}`
  );
  if (itemType === "ring") {
    await api.createRing({
      parent_id: parentId,
      chain_id: chainId,
      name: name,
      color: color!,
    });
  } else if (itemType === "key") {
    await api.createKey({
      parent_id: parentId,
      chain_id: chainId,
      name: name,
      color: color!,
    });
  } else if (itemType === "charm") {
    await api.createCharm({
      parent_id: parentId,
      chain_id: chainId,
      name: name,
      type: type!,
    });
  } else {
    throw new Error(`Unknown item type: ${itemType}`);
  }
}

export async function deleteChainItem(
  itemType: "ring" | "key" | "charm",
  itemId: string
): Promise<void> {
  console.log(`Deleting item of type ${itemType} with ID ${itemId}`);
  if (itemType === "ring") {
    await api.deleteRing(itemId);
  } else if (itemType === "key") {
    await api.deleteKey(itemId);
  } else if (itemType === "charm") {
    await api.deleteCharm(itemId);
  } else {
    throw new Error(`Unknown item type: ${itemType}`);
  }
}
