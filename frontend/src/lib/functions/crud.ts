// Types
export interface UserCreate {
  email: string;
  display_name: string;
}

export interface UserRead {
  id: string;
  email: string;
  display_name: string;
}

export interface ChainCreate {
  user_id: string;
  name: string;
}

export interface ChainRead {
  id: string;
  user_id: string;
  name: string;
  root_id: string | null;
}

export interface RingCreate {
  chain_id: string;
  name: string;
  color: string;
  parent_id?: string | null;
}

export interface RingRead {
  id: string;
  chain_id: string;
  name: string;
  color: string;
  parent_id: string | null;
}

export interface KeyCreate {
  chain_id: string;
  name: string;
  color: string;
  parent_id?: string | null;
}

export interface KeyRead {
  id: string;
  chain_id: string;
  name: string;
  color: string;
  parent_id: string | null;
}

export interface CharmCreate {
  chain_id: string;
  name: string;
  type: string;
  parent_id?: string | null;
}

export interface CharmRead {
  id: string;
  chain_id: string;
  name: string;
  type: string;
  parent_id: string | null;
}

// API Client
class KeychainAPI {
  private baseUrl: string;

  constructor(baseUrl: string = "http://localhost:8000") {
    this.baseUrl = baseUrl;
  }

  private async request<T>(
    endpoint: string,
    options?: RequestInit
  ): Promise<T> {
    const res = await fetch(`${this.baseUrl}${endpoint}`, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        ...options?.headers,
      },
    });

    if (!res.ok) {
      const error = await res.json().catch(() => ({ detail: res.statusText }));
      throw new Error(error.detail || `HTTP ${res.status}`);
    }

    // Some endpoints (DELETE) return 204 No Content. Avoid calling res.json()
    // when there's no body.
    if (res.status === 204) {
      return undefined as unknown as T;
    }

    return res.json();
  }

  // Status
  async getStatus(): Promise<{ service: string; status: string }> {
    return this.request("/");
  }

  // Users
  async createUser(user: UserCreate): Promise<UserRead> {
    return this.request("/users", {
      method: "POST",
      body: JSON.stringify(user),
    });
  }

  async getUser(userId: string): Promise<UserRead> {
    return this.request(`/users/${userId}`);
  }

  async getUserByEmail(email: string): Promise<UserRead> {
    const users = await this.request<UserRead[]>(
      `/users?email=${encodeURIComponent(email)}`
    );
    if (users.length === 0) {
      throw new Error("User not found");
    }
    return users[0];
  }

  async listUsers(): Promise<UserRead[]> {
    return this.request("/users");
  }

  // Chains
  async createChain(chain: ChainCreate): Promise<ChainRead> {
    return this.request("/chains", {
      method: "POST",
      body: JSON.stringify(chain),
    });
  }

  async getChain(chainId: string): Promise<ChainRead> {
    return this.request(`/chains/${chainId}`);
  }

  async listChains(userId: string): Promise<ChainRead[]> {
    return this.request(`/chains?user_id=${userId}`);
  }

  // Rings
  async createRing(ring: RingCreate): Promise<RingRead> {
    return this.request("/rings", {
      method: "POST",
      body: JSON.stringify(ring),
    });
  }

  async getRing(ringId: string): Promise<RingRead> {
    return this.request(`/rings/${ringId}`);
  }

  async listRings(params?: {
    chain_id?: string;
    parent_id?: string;
  }): Promise<RingRead[]> {
    const query = new URLSearchParams();
    if (params?.chain_id) query.set("chain_id", params.chain_id);
    if (params?.parent_id) query.set("parent_id", params.parent_id);
    const queryStr = query.toString();
    return this.request(`/rings${queryStr ? `?${queryStr}` : ""}`);
  }

  // Keys
  async createKey(key: KeyCreate): Promise<KeyRead> {
    return this.request("/keys", {
      method: "POST",
      body: JSON.stringify(key),
    });
  }

  async getKey(keyId: string): Promise<KeyRead> {
    return this.request(`/keys/${keyId}`);
  }

  async listKeys(params?: {
    chain_id?: string;
    parent_id?: string;
  }): Promise<KeyRead[]> {
    const query = new URLSearchParams();
    if (params?.chain_id) query.set("chain_id", params.chain_id);
    if (params?.parent_id) query.set("parent_id", params.parent_id);
    const queryStr = query.toString();
    return this.request(`/keys${queryStr ? `?${queryStr}` : ""}`);
  }

  // Charms
  async createCharm(charm: CharmCreate): Promise<CharmRead> {
    return this.request("/charms", {
      method: "POST",
      body: JSON.stringify(charm),
    });
  }

  async getCharm(charmId: string): Promise<CharmRead> {
    return this.request(`/charms/${charmId}`);
  }

  async listCharms(params?: {
    chain_id?: string;
    parent_id?: string;
  }): Promise<CharmRead[]> {
    const query = new URLSearchParams();
    if (params?.chain_id) query.set("chain_id", params.chain_id);
    if (params?.parent_id) query.set("parent_id", params.parent_id);
    const queryStr = query.toString();
    return this.request(`/charms${queryStr ? `?${queryStr}` : ""}`);
  }

  // DELETE helpers
  async deleteRing(ringId: string): Promise<void> {
    return this.request<void>(`/rings/${ringId}`, { method: "DELETE" });
  }

  async deleteKey(keyId: string): Promise<void> {
    return this.request<void>(`/keys/${keyId}`, { method: "DELETE" });
  }

  async deleteCharm(charmId: string): Promise<void> {
    return this.request<void>(`/charms/${charmId}`, { method: "DELETE" });
  }
}

// Export the class
export { KeychainAPI };

// Usage example:
// const api = new KeychainAPI('http://localhost:8000');
// const user = await api.createUser({ email: 'test@example.com', display_name: 'Test' });
// const chain = await api.createChain({ user_id: user.id, name: 'My Chain' });
// const rings = await api.listRings({ chain_id: chain.id });
