import time
from tqdm import tqdm  

def hello_animation():
    message = "Hello, World!"
    for char in tqdm(message, desc="Affichage du message"):
        print(char, end='', flush=True)
        time.sleep(0.1)
    print("\nMessage affiché avec succès!")

if __name__ == "__main__":
    hello_animation()
