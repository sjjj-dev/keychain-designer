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
