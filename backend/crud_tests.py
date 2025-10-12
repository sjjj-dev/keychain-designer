from backend.db import models, crud, session
import random
import string

engine = session.get_engine()
db_session = session.get_session()
models.Base.metadata.create_all(bind=engine)


# Randomly generate user data and create
def random_email():
    return "".join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"


def random_display_name():
    return "".join(random.choices(string.ascii_letters, k=10))


# Create 5 random users
for _ in range(5):
    email = random_email()
    display_name = random_display_name()
    crud.create_user(db_session, email=email, display_name=display_name)

    # Read user
    user = crud.get_user(db_session, user_id=crud.get_user_by_email(db_session, email=email).id)
    print(f"Created User ID: {user.id}, Email: {user.email}, Display Name: {user.display_name}")

    # Update user
    new_display_name = random_display_name()
    crud.update_user(db_session, user_id=user.id, display_name=new_display_name)
    updated_user = crud.get_user(db_session, user_id=user.id)
    print(f"Updated User ID: {updated_user.id}, Email: {updated_user.email}, Display Name: {updated_user.display_name}")

# Read all users and delete them
users = crud.get_all_users(db_session)
for user in users:
    print(f"User ID: {user.id}, Email: {user.email}, Display Name: {user.display_name}")
    # Delete user
    success = crud.delete_user(db_session, user_id=user.id)
    if success:
        print(f"Deleted User ID: {user.id}")


# Create a user for foreign keys
email = random_email()
display_name = random_display_name()
user = crud.create_user(db_session, email=email, display_name=display_name)

# Chain CRUD
chain = crud.create_chain(db_session, user_id=user.id, name="Test Chain")
print(f"Created Chain ID: {chain.id}, Name: {chain.name}, User ID: {chain.user_id}")

chain = crud.get_chain(db_session, chain_id=chain.id)
print(f"Read Chain ID: {chain.id}, Name: {chain.name}")

crud.update_chain(db_session, chain_id=chain.id, name="Updated Chain")
chain = crud.get_chain(db_session, chain_id=chain.id)
print(f"Updated Chain ID: {chain.id}, Name: {chain.name}")

crud.delete_chain(db_session, chain_id=chain.id)
print(f"Deleted Chain ID: {chain.id}")


# Ring CRUD
chain = crud.create_chain(db_session, user_id=user.id, name="Chain for Ring")
ring = crud.create_ring(db_session, chain_id=chain.id, name="Test Ring", color="SILVER")
print(f"Created Ring ID: {ring.id}, Name: {ring.name}, Color: {ring.color}")

ring = crud.get_ring(db_session, ring_id=ring.id)
print(f"Read Ring ID: {ring.id}, Name: {ring.name}")
rings = crud.get_rings(db_session, chain_id=chain.id)
print(f"All Rings in Chain ID {chain.id}: {[r.id for r in rings]}")

crud.update_ring(db_session, ring_id=ring.id, name="Updated Ring", color="GOLD")
ring = crud.get_ring(db_session, ring_id=ring.id)
print(f"Updated Ring ID: {ring.id}, Name: {ring.name}, Color: {ring.color}")

crud.delete_ring(db_session, ring_id=ring.id)
print(f"Deleted Ring ID: {ring.id}")


# Key CRUD
ring = crud.create_ring(db_session, chain_id=chain.id, name="Ring for Key", color="SILVER")
key = crud.create_key(db_session, chain_id=chain.id, name="Test Key", color="RED", parent_id=ring.id)
print(f"Created Key ID: {key.id}, Name: {key.name}, Color: {key.color}")

key = crud.get_key(db_session, key_id=key.id)
print(f"Read Key ID: {key.id}, Name: {key.name}")
keys = crud.get_keys(db_session, chain_id=chain.id)
print(f"All Keys in Chain ID {chain.id}: {[k.id for k in keys]}")

crud.update_key(db_session, key_id=key.id, name="Updated Key", color="GREEN")
key = crud.get_key(db_session, key_id=key.id)
print(f"Updated Key ID: {key.id}, Name: {key.name}, Color: {key.color}")

crud.delete_key(db_session, key_id=key.id)
print(f"Deleted Key ID: {key.id}")


# Charm CRUD
charm = crud.create_charm(db_session, chain_id=chain.id, name="Test Charm", type="Star", parent_id=ring.id)
print(f"Created Charm ID: {charm.id}, Name: {charm.name}, Type: {charm.type}")

charm = crud.get_charm(db_session, charm_id=charm.id)
print(f"Read Charm ID: {charm.id}, Name: {charm.name}")
charms = crud.get_charms(db_session, chain_id=chain.id)
print(f"All Charms in Chain ID {chain.id}: {[c.id for c in charms]}")

crud.update_charm(db_session, charm_id=charm.id, name="Updated Charm", type="Heart")
charm = crud.get_charm(db_session, charm_id=charm.id)
print(f"Updated Charm ID: {charm.id}, Name: {charm.name}, Type: {charm.type}")

crud.delete_charm(db_session, charm_id=charm.id)
print(f"Deleted Charm ID: {charm.id}")
