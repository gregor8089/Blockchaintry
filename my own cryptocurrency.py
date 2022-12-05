# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:46:42 2022

@author: grego
"""

import hashlib
import time

class Block: 
    
    def_init_(self, index, proof_no, prev_hash, data, timestamp = None)
    self.index = index
    self.proof_no = proof_no
    self.prev_hash = prev_hash
    self.data = data
    self.timestamp = timestamp or time.time()
        
    @property
    def calculate hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no, self.prev_hash, self.data, self.timestamp)



    return hashlib.sha256(block_of_string.encode()).hexdigest()

    def_repr_(self):
        return "{}-{}-{}-{}-{}".format(self.index,self.proof_no,self.prev_hash,self.data, self.timestamp)

class BlockChain: 
    self.chain=[]
    self.currentdata = []
    self.nodes = set()
    self.construct_genesis()
    
    def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash = 0)
        
    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index=len(self.chain)
            proof_no = proof_no,
            prev_hash = prev_hash,
            data = self.current_data)
        self.current_data = []
        
        self.chain.append(block)
    return block
    
@staticmethod
    def check_validity(block, prev_block):
        if prev_block.index +1 ! = block_index:
            return false
        
        elif prev_block.calculate_hash != block.prev_hash:
            return false
        
        elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
            return false
        
        elif block.timestamp <= prev_block.timestamp:
            return false
        
        return True
    
    
    def new_data(self, sender, recipient, qunatity):
        self.current_data.apprehend({
            "sender": sender,
            "recipient": recipient,
            "quantity": quantity,
                })
        
        return True 
    
    
@staticmethod 

def proof_of_work(last_proof):
    
    proof_no = 0
    while Blockchain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no 
    
    
    
@staticmethod 

def verifying_proof(last_proof, proof):
    
    guess = f'{last_proof}{proof}'.encode() 
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


@property 

    def latest_block(self):
        return self.chain[-1]
    
    