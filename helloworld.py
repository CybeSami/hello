import time
from tqdm import tqdm  

def hello_animation():
    message = "+++++++++++"
    for char in tqdm(message, desc="Affichage du message"):
        print(char, end='', flush=True)
        time.sleep(0.1)
    print("\nHello World !")

if __name__ == "__main__":
    hello_animation()
