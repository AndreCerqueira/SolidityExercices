from solcx import compile_standard, install_solc
import json
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Our Solidity
install_solc('0.6.0')
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Connect to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xBb18a1E4Ee81d7F8d98e5D66655d4e342fB9e0c8"
# vvvv Don't do this
private_key = os.getenv("PRIVATE_KEY")

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the latest transaction
nonce = w3.eth.getTransactionCount(my_address)

# 1. Build a transaction
transaction = SimpleStorage.constructor().buildTransaction({
    "gasPrice": w3.eth.gas_price,
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce
})

# 2. Sign a transaction
signed_txn = w3.eth.account.sign_transaction(
    transaction, private_key=private_key)


# 3. Send a transaction
print("Deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!!")

# Working with the contract, always need
# Contract Address
# Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Call / Transact
print(simple_storage.functions.retrieve().call())


print("Updating Contract...")
store_transaction = simple_storage.functions.store(15).buildTransaction({
    "gasPrice": w3.eth.gas_price,
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce + 1
})

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key)

send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)

print("Updated!!")

print(simple_storage.functions.retrieve().call())
