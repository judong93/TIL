import hashlib

blockchain = []
data = ['2nd', '3rd']

def make_genesis_block():
    data = b'Genesis'
    prev_hash = b''
    nonce = 0
    current_hash = make_hash(data, b'nonce', prev_hash)
    blockchain.append((nonce, data, prev_hash, current_hash))

def make_hash(data, nonce, prev_hash) -> bytes:
    return hashlib.sha256(data + nonce + prev_hash).hexdigest()

def add_block(data: str, nonce):
    _, _, _, prev_hash = blockchain[-1]
    while True:
        nonce += 1
        encoded_data = data.encode()
        encoded_nonce = str(nonce).encode()
        current_hash = make_hash(encoded_data, encoded_nonce , b'prev_hash')
        if current_hash[:5] == '00000':
            blockchain.append((nonce, data, prev_hash, current_hash))
            break

make_genesis_block()
for i in data:
    nonce = -1
    add_block(i, -1)
for j in blockchain:
    print(f'nonce: {j[0]}')
    print(f'data: {j[1]}')
    print(f'prevhash: {j[2]}')
    print(f'hash: {j[3]}')
    print()

