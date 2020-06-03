import hashlib
import datetime


class Block:

    def __init__(self, data, previous_hash = None):
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.prev = None
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.index = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def get_index(self):
        return self.index


class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head is None:
            block = Block(data)
            block.index = 0
            self.head = block
            self.tail = self.head
            return
        else:
            block = Block(data)
            former_tail = self.tail
            former_index = former_tail.get_index()
            self.tail = block
            self.tail.prev = former_tail
            self.tail.previous_hash = former_tail.get_hash()
            self.tail.index = former_index + 1

#Test case 1
block = Block("WenyenHuang")
chain_1 = Blockchain()
chain_1.append("Wenyen")
chain_1.append("Amy")
chain_1.append("Jenny")
print(chain_1.tail.hash)
print(chain_1.tail.previous_hash)
print(chain_1.tail.prev.hash)
print(chain_1.tail.prev.data)
print(chain_1.tail.prev.previous_hash)
print(chain_1.head.hash)

#Test case 2 - Edge Cases
block = Block("A")
chain_2 = Blockchain()
chain_2.append("")

print(type(chain_2))
print(chain_2.tail.hash)
print(chain_2.tail.previous_hash)
print(chain_2.head.hash)

#Test case 3 - Edge Cases
block = Block("")
chain_3 = Blockchain()
chain_3.append(" ")

print(type(chain_3))
print(chain_3.tail.hash)
print(chain_3.tail.previous_hash)
print(chain_3.head.hash)
