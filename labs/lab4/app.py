import sys
from datetime import date
import json
from sqlalchemy.orm import relationship
from model import Wallet,Base
from sqlalchemy import create_engine
from flask import Flask, jsonify, abort
from flask import request
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
session = db.session
#engine = create_engine('sqlite:///assignment2.db')
#Base.metadata.create_all(engine)

def session_factory():
    from sqlalchemy.orm import sessionmaker
    DBSession = sessionmaker(bind=engine)
    return DBSession()

@app.route('/api/wallets', methods=['POST'])
def create_wallets():
    if get_wallets_count() == 0:
        walletA = Wallet("0x12345", 1000,"345w24qc4fa4t34raert")
        walletB = Wallet("0x67890", 2000,"345w24qc4fa4dfddxxgg")
        session.add(walletA)
        session.add(walletB)
        session.commit()
    return jsonify( { 'result': 'OK' } )

@app.route('/api/wallet/<int:id>', methods=['GET'])
def get_wallet(id):
    wallet_query = session.query(Wallet)
    row = wallet_query.get(id)
    return json.dumps({'id':row.id,'address':row.address,'balance':row.balance})

def get_wallets_count():
    wallet_query = session.query(Wallet)
    return len(wallet_query.all())

@app.route('/api/wallets', methods=['GET'])
def get_wallets():
    wallet_query = session.query(Wallet)
    rs = wallet_query.all()
    
    return json.dumps([{'id':row.id,'address':row.address,'balance':row.balance} for row in rs])

@app.route('/api/wallet/<int:id>', methods=['PUT'])
def update_wallets(id):
    wallet = session.query(Wallet).get(id)
    if wallet is None:
        abort(400)
    
    wallet.balance = int(request.form["balance"])
    wallet.address = request.form["address"]
    session.commit()
    return jsonify( { 'result': 'OK' } )


@app.route('/api/wallet/<int:id>', methods=['DELETE'])
def delete_wallets(id):
    wallet = session.query(Wallet).get(id)
    if wallet is None:
        abort(400)
    session.delete(wallet)
    session.commit()
    return jsonify( { 'result': 'OK' } )


if __name__ == "__main__":
    app.run()
    #session = session_factory
    #wallets = get_wallets(session)
    #if len(wallets) == 0:
        #create_wallets(session)
    #wallets = get_wallets(session)

    #for wallet in wallets:
        #print(wallet)