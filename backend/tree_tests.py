from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid

from backend.db import crud, tree
from backend.db import models
from backend.db import session
from backend.db.models import Base


def build_sample_chain(session, user):
    # Create a chain and a root ring
    chain = crud.create_chain(session, user_id=user.id, name="Sample Chain")
    root = crud.create_ring(session, chain_id=chain.id, name="Root Ring", color="SILVER")
    # Set root_id on chain
    crud.update_chain(session, chain_id=chain.id, root_id=root.id)

    # Create child rings
    child1 = crud.create_ring(session, chain_id=chain.id, name="Child Ring 1", color="GOLD", parent_id=root.id)
    child2 = crud.create_ring(
        session,
        chain_id=chain.id,
        name="Child Ring 2",
        color="BRONZE",
        parent_id=root.id,
    )

    # Grandchild under child1
    grandchild = crud.create_ring(
        session,
        chain_id=chain.id,
        name="Grandchild Ring",
        color="SILVER",
        parent_id=child1.id,
    )

    # Keys attached to various rings
    key_root = crud.create_key(session, chain_id=chain.id, name="Root Key", color="RED", parent_id=root.id)
    key_child1 = crud.create_key(
        session,
        chain_id=chain.id,
        name="Child1 Key",
        color="GREEN",
        parent_id=child1.id,
    )
    key_grandchild = crud.create_key(
        session,
        chain_id=chain.id,
        name="Grandchild Key",
        color="BLUE",
        parent_id=grandchild.id,
    )

    # Charms attached to various rings
    charm_root = crud.create_charm(session, chain_id=chain.id, name="Root Charm", type="Star", parent_id=root.id)
    charm_child2 = crud.create_charm(
        session,
        chain_id=chain.id,
        name="Child2 Charm",
        type="Heart",
        parent_id=child2.id,
    )

    return chain


def print_tree(node, indent=0):
    pad = "  " * indent
    print(f"{pad}- Ring: {node.ring.name} (id={node.ring.id}) color={getattr(node.ring, 'color', None)}")
    for k in node.keys:
        print(f"{pad}  * Key: {k.name} (id={k.id}) color={k.color}")
    for c in node.charms:
        print(f"{pad}  * Charm: {c.name} (id={c.id}) type={c.type}")
    for child in node.children:
        print_tree(child, indent + 1)


def main():

    # Connect to postgres database

    engine = session.get_engine()
    db_session = session.get_session()
    models.Base.metadata.create_all(bind=engine)

    user = crud.create_user(
        db_session,
        email=f"tester+{uuid.uuid4().hex}@example.com",
        display_name="Tester",
    )
    chain = build_sample_chain(db_session, user)
    tree_root = tree.get_chain_tree(db_session, chain.id)
    if not tree_root:
        print("Failed to build tree")
        return

    print("Constructed tree:")
    print_tree(tree_root)

    # Basic verifications
    # root should have 2 child rings
    assert len(tree_root.children) == 2, "Expected 2 child rings under root"
    # root should have at least one key and one charm
    assert len(tree_root.keys) >= 1
    assert len(tree_root.charms) >= 1
    crud.delete_user(db_session, user_id=user.id)

    print("Sample chain created and basic checks passed.")
    db_session.close()


if __name__ == "__main__":
    main()
