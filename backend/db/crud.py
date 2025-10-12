from sqlalchemy.orm import Session
import uuid
from backend.db.models import User, Chain, Ring, Key, Charm
from backend.db import constants

# Basic CRUD operations for User, Chain, Ring, Key, and Charm


# User CRUD operations
def create_user(db: Session, email: str, display_name: str) -> User | None:
    user = User(email=email, display_name=display_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: uuid.UUID) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()


def update_user(
    db: Session,
    user_id: uuid.UUID,
    email: str | None = None,
    display_name: str | None = None,
) -> User | None:
    user = get_user(db, user_id)
    if user:
        if email:
            user.email = email
        if display_name:
            user.display_name = display_name
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: uuid.UUID) -> bool:
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


# Chain CRUD operations
def create_chain(
    db: Session,
    user_id: uuid.UUID,
    name: str = "chain",
    root_id: uuid.UUID | None = None,
) -> Chain | None:
    chain = Chain(user_id=user_id, name=name, root_id=root_id)
    db.add(chain)
    db.commit()
    db.refresh(chain)
    return chain


def get_chain(db: Session, chain_id: uuid.UUID) -> Chain | None:
    return db.query(Chain).filter(Chain.id == chain_id).first()


def get_chains(db: Session, user_id: uuid.UUID | None = None) -> list[Chain]:
    """Return chains optionally filtered by user_id."""
    query = db.query(Chain)
    if user_id:
        query = query.filter(Chain.user_id == user_id)
    return query.all()


def update_chain(
    db: Session, chain_id: uuid.UUID, name: str | None = None, root_id: uuid.UUID | None = None
) -> Chain | None:
    chain = get_chain(db, chain_id)
    if chain:
        if name:
            chain.name = name
        if root_id:
            chain.root_id = root_id
        db.commit()
        db.refresh(chain)
    return chain


def delete_chain(db: Session, chain_id: uuid.UUID) -> bool:
    chain = get_chain(db, chain_id)
    if chain:
        db.delete(chain)
        db.commit()
        return True
    return False


# Chain CRUD operations
def create_ring(
    db: Session,
    chain_id: uuid.UUID,
    name: str = "ring",
    color: str = constants.RING_COLORS[0],
    parent_id: uuid.UUID | None = None,
) -> Ring | None:
    ring = Ring(chain_id=chain_id, name=name, color=color, parent_id=parent_id)
    db.add(ring)
    db.commit()
    db.refresh(ring)
    return ring


def get_ring(db: Session, ring_id: uuid.UUID) -> Ring | None:
    return db.query(Ring).filter(Ring.id == ring_id).first()


def get_rings(db: Session, chain_id: uuid.UUID | None = None, parent_id: uuid.UUID | None = None) -> list[Ring]:
    """Return rings optionally filtered by chain_id and/or parent_id."""
    query = db.query(Ring)
    if chain_id:
        query = query.filter(Ring.chain_id == chain_id)
    if parent_id is not None:
        query = query.filter(Ring.parent_id == parent_id)
    return query.all()


def update_ring(
    db: Session,
    ring_id: uuid.UUID,
    name: str | None = None,
    color: str | None = None,
    parent_id: uuid.UUID | None = None,
) -> Ring | None:
    ring = get_ring(db, ring_id)
    if ring:
        if name:
            ring.name = name
        if color:
            ring.color = color
        if parent_id is not None:
            ring.parent_id = parent_id
        db.commit()
        db.refresh(ring)
    return ring


def delete_ring(db: Session, ring_id: uuid.UUID) -> bool:
    ring = get_ring(db, ring_id)
    if ring:
        db.delete(ring)
        db.commit()
        return True
    return False


# Key CRUD operations
def create_key(
    db: Session,
    chain_id: uuid.UUID,
    name: str = "key",
    color: str = constants.KEY_COLORS[0],
    parent_id: uuid.UUID | None = None,
) -> Key | None:
    key = Key(chain_id=chain_id, name=name, color=color, parent_id=parent_id)
    db.add(key)
    db.commit()
    db.refresh(key)
    return key


def get_key(db: Session, key_id: uuid.UUID) -> Key | None:
    return db.query(Key).filter(Key.id == key_id).first()


def get_keys(db: Session, chain_id: uuid.UUID | None = None, parent_id: uuid.UUID | None = None) -> list[Key]:
    """Return keys optionally filtered by chain_id and/or parent_id."""
    query = db.query(Key)
    if chain_id:
        query = query.filter(Key.chain_id == chain_id)
    if parent_id is not None:
        query = query.filter(Key.parent_id == parent_id)
    return query.all()


def update_key(
    db: Session,
    key_id: uuid.UUID,
    name: str | None = None,
    color: str | None = None,
    parent_id: uuid.UUID | None = None,
) -> Key | None:
    key = get_key(db, key_id)
    if key:
        if name:
            key.name = name
        if color:
            key.color = color
        if parent_id is not None:
            key.parent_id = parent_id
        db.commit()
        db.refresh(key)
    return key


def delete_key(db: Session, key_id: uuid.UUID) -> bool:
    key = get_key(db, key_id)
    if key:
        db.delete(key)
        db.commit()
        return True
    return False


# Charm CRUD operations
def create_charm(
    db: Session,
    chain_id: uuid.UUID,
    name: str = "charm",
    type: str = constants.CHARM_TYPES[0],
    parent_id: uuid.UUID | None = None,
) -> Charm | None:
    charm = Charm(chain_id=chain_id, name=name, type=type, parent_id=parent_id)
    db.add(charm)
    db.commit()
    db.refresh(charm)
    return charm


def get_charm(db: Session, charm_id: uuid.UUID) -> Charm | None:
    return db.query(Charm).filter(Charm.id == charm_id).first()


def get_charms(db: Session, chain_id: uuid.UUID | None = None, parent_id: uuid.UUID | None = None) -> list[Charm]:
    """Return charms optionally filtered by chain_id and/or parent_id."""
    query = db.query(Charm)
    if chain_id:
        query = query.filter(Charm.chain_id == chain_id)
    if parent_id is not None:
        query = query.filter(Charm.parent_id == parent_id)
    return query.all()


def update_charm(
    db: Session,
    charm_id: uuid.UUID,
    name: str | None = None,
    type: str | None = None,
    parent_id: uuid.UUID | None = None,
) -> Charm | None:
    charm = get_charm(db, charm_id)
    if charm:
        if name:
            charm.name = name
        if type:
            charm.type = type
        if parent_id is not None:
            charm.parent_id = parent_id
        db.commit()
        db.refresh(charm)
    return charm


def delete_charm(db: Session, charm_id: uuid.UUID) -> bool:
    charm = get_charm(db, charm_id)
    if charm:
        db.delete(charm)
        db.commit()
        return True
    return False
