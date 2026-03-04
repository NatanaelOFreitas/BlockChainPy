import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        #Cria um novo bloco e adiciona à chain
        pass

    def new_transaction(self,sender, recipient, amount):
        #Adiciona uma nova transação à lista de transações
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })
        return self.last_block["index"] + 1

    @staticmethod
    def Hash(block):
        #Passa um block pela função Hash
        pass

    @property
    def last_block(self):
        #retorna o último bloco adiocinado à chain
        pass