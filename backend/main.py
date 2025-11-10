from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uuid

from backend import db
from backend.db import crud
from backend.db.session import get_session, get_engine
from backend.schemas import (
    UserCreate,
    UserRead,
    ChainCreate,
    ChainRead,
    RingCreate,
    RingRead,
    KeyCreate,
    KeyRead,
    CharmCreate,
    CharmRead,
)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your Svelte dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/", response_model=dict)
def get_status():
    return {"service": "keychain_designer", "status": "ok"}


# -----------------
# Users
# -----------------


@app.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    existing = crud.get_user_by_email(db, email=user.email)
    if existing:
        raise HTTPException(status_code=409, detail="email already registered")
    created = crud.create_user(db, email=user.email, display_name=user.display_name)
    return created


@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: uuid.UUID, db: Session = Depends(get_session)):
    u = crud.get_user(db, user_id=user_id)
    if not u:
        raise HTTPException(status_code=404, detail="user not found")
    return u


@app.get("/users", response_model=List[UserRead])
def list_users(db: Session = Depends(get_session)):
    return crud.get_all_users(db)


# -----------------
# Chains
# -----------------


@app.post("/chains", response_model=ChainRead, status_code=status.HTTP_201_CREATED)
def create_chain(chain: ChainCreate, db: Session = Depends(get_session)):
    # Ensure user exists
    if not crud.get_user(db, user_id=chain.user_id):
        raise HTTPException(status_code=404, detail="user not found")
    created = crud.create_chain(db, user_id=chain.user_id, name=chain.name)
    return created


@app.get("/chains/{chain_id}", response_model=ChainRead)
def get_chain(chain_id: uuid.UUID, db: Session = Depends(get_session)):
    chain = crud.get_chain(db, chain_id=chain_id)
    if not chain:
        raise HTTPException(status_code=404, detail="chain not found")
    return chain


@app.get("/chains", response_model=List[ChainRead])
def list_chains(user_id: uuid.UUID, db: Session = Depends(get_session)):
    return crud.get_chains(db, user_id=user_id)


# -----------------
# Rings / Keys / Charms
# -----------------


@app.post("/rings", response_model=RingRead, status_code=status.HTTP_201_CREATED)
def create_ring(r: RingCreate, db: Session = Depends(get_session)):
    # Validate chain exists
    if not crud.get_chain(db, chain_id=r.chain_id):
        raise HTTPException(status_code=404, detail="chain not found")
    created = crud.create_ring(db, chain_id=r.chain_id, name=r.name, color=r.color, parent_id=r.parent_id)
    # If this is the first ring in the chain, set it as the root
    if not created.parent_id and not crud.get_chain(db, chain_id=r.chain_id).root_id:
        crud.update_chain(db, chain_id=r.chain_id, root_id=created.id)
    return created


@app.get("/rings/{ring_id}", response_model=RingRead)
def get_ring(ring_id: uuid.UUID, db: Session = Depends(get_session)):
    ring = crud.get_ring(db, ring_id=ring_id)
    if not ring:
        raise HTTPException(status_code=404, detail="ring not found")
    return ring


@app.get("/rings", response_model=List[RingRead])
def list_rings(
    chain_id: uuid.UUID | None = None,
    parent_id: uuid.UUID | None = None,
    db: Session = Depends(get_session),
):
    return crud.get_rings(db, chain_id=chain_id, parent_id=parent_id)


@app.delete("/rings/{ring_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ring(ring_id: uuid.UUID, db: Session = Depends(get_session)):
    if not crud.get_ring(db, ring_id=ring_id):
        raise HTTPException(status_code=404, detail="ring not found")
    crud.delete_ring(db, ring_id=ring_id)
    return


@app.post("/keys", response_model=KeyRead, status_code=status.HTTP_201_CREATED)
def create_key(k: KeyCreate, db: Session = Depends(get_session)):
    if not crud.get_chain(db, chain_id=k.chain_id):
        raise HTTPException(status_code=404, detail="chain not found")
    created = crud.create_key(db, chain_id=k.chain_id, name=k.name, color=k.color, parent_id=k.parent_id)
    return created


@app.get("/keys/{key_id}", response_model=KeyRead)
def get_key(key_id: uuid.UUID, db: Session = Depends(get_session)):
    key = crud.get_key(db, key_id=key_id)
    if not key:
        raise HTTPException(status_code=404, detail="key not found")
    return key


@app.get("/keys", response_model=List[KeyRead])
def list_keys(
    chain_id: uuid.UUID | None = None,
    parent_id: uuid.UUID | None = None,
    db: Session = Depends(get_session),
):
    return crud.get_keys(db, chain_id=chain_id, parent_id=parent_id)


@app.delete("/keys/{key_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_key(key_id: uuid.UUID, db: Session = Depends(get_session)):
    if not crud.get_key(db, key_id=key_id):
        raise HTTPException(status_code=404, detail="key not found")
    crud.delete_key(db, key_id=key_id)
    return


@app.post("/charms", response_model=CharmRead, status_code=status.HTTP_201_CREATED)
def create_charm(c: CharmCreate, db: Session = Depends(get_session)):
    if not crud.get_chain(db, chain_id=c.chain_id):
        raise HTTPException(status_code=404, detail="chain not found")
    created = crud.create_charm(db, chain_id=c.chain_id, name=c.name, type=c.type, parent_id=c.parent_id)
    return created


@app.get("/charms/{charm_id}", response_model=CharmRead)
def get_charm(charm_id: uuid.UUID, db: Session = Depends(get_session)):
    charm = crud.get_charm(db, charm_id=charm_id)
    if not charm:
        raise HTTPException(status_code=404, detail="charm not found")
    return charm


@app.get("/charms", response_model=List[CharmRead])
def list_charms(
    chain_id: uuid.UUID | None = None,
    parent_id: uuid.UUID | None = None,
    db: Session = Depends(get_session),
):
    return crud.get_charms(db, chain_id=chain_id, parent_id=parent_id)


@app.delete("/charms/{charm_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_charm(charm_id: uuid.UUID, db: Session = Depends(get_session)):
    if not crud.get_charm(db, charm_id=charm_id):
        raise HTTPException(status_code=404, detail="charm not found")
    crud.delete_charm(db, charm_id=charm_id)
    return
