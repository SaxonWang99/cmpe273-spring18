import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Wallet(Base):
    __tablename__ = 'wallet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    address = Column(String(250), nullable=False)
    balance = Column(Integer, nullable=False)
    public_key = Column(String(250), nullable=False)
    def __init__(self, address, balance, key):
        self.address = address
        self.balance = balance
        self.public_key = key
    
    def __repr__(self):
        return '<Wallet %r>' % self.id

    
    
