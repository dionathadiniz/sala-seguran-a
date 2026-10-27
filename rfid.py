
from mfrc522 import SimpleMFRC522


def ler_tag():
    leitor = SimpleMFRC522()

    try:
        print("Aproxime o crachá do leitor RFID...")
        uid, texto = leitor.read()

        print(f"UID detectado: {uid}")
        return str(uid)

    except Exception as erro:
        print(f"Erro ao ler a tag: {erro}")
        return None


if __name__ == "__main__":
    ler_tag()
