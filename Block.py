import datetime
import hashlib #to hash the blocks
import json     
from flask import Flask, jsonify # jsonify is to get the state of the block


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    #essential keys of Block
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) +1,
        'timestamp': str(datetime.datetime.now()),
        'proof': proof,
        'previous_hash': previous_hash,
        }

        self.chain.append(block)
        return block

    def get_previous_block(self):   #get the last block of the cuurent chain
        return self.chain[-1]          #it get us to the previous Block

    #proof of work is hard to find and easy to verify because if proof of work would be would be easy it would be easy 
    #for miners to find the block and so that the cryptocurruency don't loose thier values
    #and they are easy to verify because so that the other miners can verify the transactions
    
    def proof_of_work(self, previous_proof):
        new_proof=1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof +=1
        return new_proof

    def hash(self, block):      #
        encoded_block = json.dumps(block, sort_keys = True).encode      #we are taking json beacuse in later crypto making we will import it using json
        return hashlib.sha256(encoded_block).hexdigest()                                                         #sort keys because our block dictonaries are sorted
    
    def is_change_valid(self, chain):
        previous_block = chain[0]           #
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    
