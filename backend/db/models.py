import uuid
from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(256), unique=True, nullable=False)
    display_name = Column(String(256), nullable=False)


class Chain(Base):
    __tablename__ = "chain"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    root_id = Column(UUID(as_uuid=True), ForeignKey("ring.id"))
    name = Column(String(256), nullable=False)


class Ring(Base):
    __tablename__ = "ring"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("ring.id"))
    chain_id = Column(UUID(as_uuid=True), ForeignKey("chain.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(256), nullable=False)
    color = Column(String(64), nullable=False)


class Key(Base):
    __tablename__ = "key"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("ring.id"))
    chain_id = Column(UUID(as_uuid=True), ForeignKey("chain.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(256), nullable=False)
    color = Column(String(64), nullable=False)


class Charm(Base):
    __tablename__ = "charm"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("ring.id"))
    chain_id = Column(UUID(as_uuid=True), ForeignKey("chain.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(256), nullable=False)
    type = Column(String(128), nullable=False)
