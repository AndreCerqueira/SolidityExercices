from brownie import AndresCoin, config
from scripts.utils import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy():
    account = get_account()
    my_token = AndresCoin.deploy(initial_supply, {"from": account})
    print("deu: " + my_token.name())
    pass


def main():
    deploy()
