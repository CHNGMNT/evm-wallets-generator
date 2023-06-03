from data import *
from termcolor import cprint

num_wallets = 1   # количество кошельков

wallets = generate_wallets(num_wallets)

save_wallets_to_files(wallets)
save_wallets_to_csv(wallets)

if __name__ == '__main__':
    cprint(text1, 'red')
    cprint(f"Генерация {num_wallets} кошельков завершена.\n\nКошельки сохранены в папку results\n", 'cyan')