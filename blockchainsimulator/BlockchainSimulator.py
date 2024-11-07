from flask import Flask, render_template, jsonify, request
import hashlib as hasher
import datetime as date
import json

# Define the Block class and blockchain functions
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))

# Flask web app
app = Flask(__name__)

this_nodes_transactions = []

@app.route('/')
def home():
    return render_template('index.html', blockchain=blockchain)

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain[-1]
    
    # Handle the genesis block case where last_block.data is a string, not a dict
    if isinstance(last_block.data, str):
        last_proof = 0  # Since it's the genesis block, we can set the proof of work to 0.
    else:
        last_proof = last_block.data.get('proof-of-work', 0)
    
    proof = proof_of_work(last_proof)
    
    this_nodes_transactions.append(
        {"from": "network", "to": "miner_address", "amount": 1}
    )

    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(this_nodes_transactions)
    }

    new_block_index = last_block.index + 1
    new_block_timestamp = date.datetime.now()
    last_block_hash = last_block.hash

    this_nodes_transactions.clear()

    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )

    blockchain.append(mined_block)

    # Render the mining result page with the new block's information
    return render_template('mine_result.html', block=mined_block)

@app.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    result = []
    for block in chain_to_send:
        result.append({
            "index": str(block.index),
            "timestamp": str(block.timestamp),
            "data": str(block.data),
            "hash": block.hash
        })
    return render_template('blocks.html', blockchain=blockchain)

def proof_of_work(last_proof):
    # If last_proof is zero, start incrementor from 1 to avoid division by zero.
    incrementor = last_proof + 1 if last_proof != 0 else 1
    
    # If last_proof is zero, skip the modulo check with last_proof
    while not (incrementor % 9 == 0 and (last_proof == 0 or incrementor % last_proof == 0)):
        incrementor += 1

    return incrementor

if __name__ == '__main__':
    app.run(debug=True)
