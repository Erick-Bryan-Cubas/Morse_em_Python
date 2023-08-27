import time
from playsound import playsound # pip install playsound==1.2.2

dict_tradutor = {'A': '.-',   'B': '-...',    'C': '-.-.',    'D': '-..',
       'E': '.',    'F': '..-.',    'G': '--.',     'H': '....',
       'I': '..',   'J': '.---',    'K': '-.-',     'L': '.-..',
       'M': '--',   'N': '-.',      'O': '---',     'P': '.--.',
       'Q': '--.-', 'R': '.-.',     'S': '...',     'T': '-',
       'U': '..-',  'V': '...-',    'W': '.--',     'X': '-..-',
       'Y': '-.--', 'Z': '--..',

       '0': '-----',    '1': '.----',   '2': '..---',   '3': '...--',
       '4': '....-',    '5': '.....',   '6': '-....',   '7': '--...',
       '8': '---..',    '9': '----.',   ' ': '/'
        }

mensagem = str(input("Texto para ser codificado em morse:").upper())
mensagem = " ".join(dict_tradutor[c] for c in mensagem.upper())
# print(mensagem)

def reproduzir_codigo_morse(mensagem):
    for c in mensagem:
        if c == ".":
            playsound("bip_short.mp3")
            time.sleep(0.3)
        elif c == "-":
            playsound("bip_long.mp3")
            time.sleep(0.3)
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("Caractere inválido detectado!")
            
print(mensagem)
reproduzir_codigo_morse(mensagem)

dict_reverso = {v: k for k, v in dict_tradutor.items()}
mensagem_reversa = "".join(dict_reverso[c] for c in mensagem.split(" "))
print(f"Mensagem reversa: {mensagem_reversa}")