// Types matching backend
export type User = {
  id: string;
  username: string;
  password_hash: string;
};

export type Chain = {
  id: string;
  user_id: string;
  root_id: string;
  name: string;
};

export type Ring = {
  id: string;
  parent_id: string | null;
  chain_id: string;
  name: string;
  color: string;
  rings: Ring[];
  keys: Key[];
  charms: Charm[];
};

export type Key = {
  id: string;
  parent_id: string;
  chain_id: string;
  name: string;
  color: string;
};

export type Charm = {
  id: string;
  parent_id: string;
  chain_id: string;
  name: string;
  type: string;
};

export type ChainItem = Ring | Key | Charm;
