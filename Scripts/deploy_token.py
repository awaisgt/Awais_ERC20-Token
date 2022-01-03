from brownie import accounts,AwaisGT,network
import os
import time


def main():
    initial_supply = 100000 #100000 tokens
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    token_object = AwaisGT.deploy(initial_supply,{"from":account},publish_source = True)
    

