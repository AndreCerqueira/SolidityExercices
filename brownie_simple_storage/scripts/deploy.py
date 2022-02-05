from brownie import accounts, config, SimpleStorage, network


def deply_simple_storage():
    account = get_account()

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    # account = accounts.load("andre-account")
    # account = accounts.add(config["wallets"]["from_key"])
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deply_simple_storage()
