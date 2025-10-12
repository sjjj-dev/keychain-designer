// Fake chain data for frontend dev/testing, matching backend models
import { writable } from 'svelte/store';

// Types matching backend
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

// Dummy UUIDs for structure
const userId = '11111111-1111-1111-1111-111111111111';
const chainId = '22222222-2222-2222-2222-222222222222';
const rootRingId = '33333333-3333-3333-3333-333333333333';
const childRing1Id = '44444444-4444-4444-4444-444444444444';
const childRing2Id = '55555555-5555-5555-5555-555555555555';
const grandchildRingId = '66666666-6666-6666-6666-666666666666';

export const fakeChain: Chain = {
	id: chainId,
	user_id: userId,
	root_id: rootRingId,
	name: 'Sample Chain',
};

export const fakeChainTree: Ring = {
	id: rootRingId,
	parent_id: null,
	chain_id: chainId,
	name: 'Root Ring',
	color: 'SILVER',
	rings: [
		{
			id: childRing1Id,
			parent_id: rootRingId,
			chain_id: chainId,
			name: 'Child Ring 1',
			color: 'GOLD',
			rings: [
				{
					id: grandchildRingId,
					parent_id: childRing1Id,
					chain_id: chainId,
					name: 'Grandchild Ring',
					color: 'SILVER',
					rings: [],
					keys: [
						{
							id: '77777777-7777-7777-7777-777777777777',
							parent_id: grandchildRingId,
							chain_id: chainId,
							name: 'Grandchild Key',
							color: 'BLUE',
						},
					],
					charms: [],
				},
			],
			keys: [
				{
					id: '88888888-8888-8888-8888-888888888888',
					parent_id: childRing1Id,
					chain_id: chainId,
					name: 'Child1 Key',
					color: 'GREEN',
				},
			],
			charms: [],
		},
		{
			id: childRing2Id,
			parent_id: rootRingId,
			chain_id: chainId,
			name: 'Child Ring 2',
			color: 'BRONZE',
			rings: [],
			keys: [],
			charms: [
				{
					id: '99999999-9999-9999-9999-999999999999',
					parent_id: childRing2Id,
					chain_id: chainId,
					name: 'Child2 Charm',
					type: 'HEART',
				},
			],
		},
	],
	keys: [
		{
			id: 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
			parent_id: rootRingId,
			chain_id: chainId,
			name: 'Root Key',
			color: 'RED',
		},
	],
	charms: [
		{
			id: 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
			parent_id: rootRingId,
			chain_id: chainId,
			name: 'Root Charm',
			type: 'STAR',
		},
	],
};

// Svelte store for the current chain tree (for dev/testing)
export const chainTreeStore = writable<Ring>(fakeChainTree);
