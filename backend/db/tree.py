from sqlalchemy.orm import Session
import uuid
from backend.db.models import Chain, Ring, Key, Charm

# Organizes chain data in a tree structure with rings, keys, and charms by querying the database


class RingNode:
    def __init__(self, ring: Ring):
        self.ring = ring
        self.children: list[RingNode] = []  # List of child RingNodes
        self.keys: list[Key] = []  # List of Keys
        self.charms: list[Charm] = []  # List of Charms


def build_ring_tree(db: Session, ring: Ring) -> RingNode:
    node = RingNode(ring)
    # Fetch child rings
    child_rings = db.query(Ring).filter(Ring.parent_id == ring.id).all()
    for child_ring in child_rings:
        child_node = build_ring_tree(db, child_ring)
        node.children.append(child_node)
    # Fetch keys
    node.keys = db.query(Key).filter(Key.parent_id == ring.id).all()
    # Fetch charms
    node.charms = db.query(Charm).filter(Charm.parent_id == ring.id).all()
    return node


def get_chain_tree(db: Session, chain_id: uuid.UUID) -> RingNode | None:
    chain = db.query(Chain).filter(Chain.id == chain_id).first()
    if not chain or not chain.root_id:
        return None
    root_ring = db.query(Ring).filter(Ring.id == chain.root_id).first()
    if not root_ring:
        return None
    return build_ring_tree(db, root_ring)
