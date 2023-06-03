import os
import csv
from web3 import Web3
from eth_account import Account
from mnemonic import Mnemonic

w3 = Web3()

def generate_wallets(num_wallets):
    wallets = []
    for _ in range(num_wallets):
        account = w3.eth.account.create()
        mnemonic = Mnemonic('english').generate(strength=128).split()
        wallets.append({
            'address': account.address,
            'private_key': account.privateKey.hex(),
            'mnemonic': mnemonic
        })
    return wallets


def save_wallets_to_files(wallets):
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)
    addresses_file = os.path.join(results_dir, 'addresses.txt')
    private_keys_file = os.path.join(results_dir, 'private_keys.txt')
    mnemonics_file = os.path.join(results_dir, 'mnemonics.txt')
    
    with open(addresses_file, 'w') as f_addresses, \
            open(private_keys_file, 'w') as f_private_keys, \
            open(mnemonics_file, 'w') as f_mnemonics:
        for wallet in wallets:
            f_addresses.write(wallet['address'] + '\n')
            f_private_keys.write(wallet['private_key'] + '\n')
            f_mnemonics.write(' '.join(wallet['mnemonic']) + '\n')


def save_wallets_to_csv(wallets):
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)
    csv_file = os.path.join(results_dir, 'wallets.csv')

    with open(csv_file, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['Number', 'Address', 'Private Key', 'Mnemonic'])
        for i, wallet in enumerate(wallets, start=1):
            writer.writerow([i, wallet['address'], wallet['private_key'], wallet['mnemonic']])

text1 = '''
         ___  ___  ___  __   _____    ___  _   _ _____ 
        |  \/  | /   |/  | /  ___|  /   || \ | |  _  |
        | .  . |/ /| |`| | \ `--.  / /| ||  \| | | | |
        | |\/| / /_| | | |  `--. \/ /_| || . ` | | | |
        | |  | \___  |_| |_/\__/ /\___  || |\  \ \_/ /
        \_|  |_/   |_/\___/\____/     |_/\_| \_/\___/ 
  
              https://github.com/vittoriomaisano
              '''
