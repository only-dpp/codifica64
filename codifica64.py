import base64


def codificar_base64(texto):
    texto_bytes = texto.encode('utf-8')
    bytes_codificados = base64.b64encode(texto_bytes)
    texto_codificado = bytes_codificados.decode('utf-8')
    return texto_codificado

def decodificar_base64(texto_codificado):
    bytes_codificados = texto_codificado.encode('utf-8')
    try:
        bytes_decodificados = base64.b64decode(bytes_codificados)
        texto_decodificado = bytes_decodificados.decode('utf-8')
        return texto_decodificado
    except base64.binascii.Error:
        raise base64.binascii.Error("O texto fornecido não parece ser uma codificação Base64 :/")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("O resultado da decodificação Base64 não está em formato UTF-8.")

if __name__ == "__main__":
    while True:
        print("\nescolha uma ação:")
        print("1. codificar texto para Base64")
        print("2. decodificar texto de Base64")
        print("3. Sair")

        escolha = input("Digita sua escolha (1, 2 ou 3): ")

        try:
            if escolha == '1':
                texto_original = input("Digite o texto a ser codificado: ")
                texto_codificado = codificar_base64(texto_original)
                print(f"Texto codificado em Base64: {texto_codificado}")
            elif escolha == '2':
                texto_codificado = input("Digite o texto Base64 a ser decodificado: ")
                try:
                    texto_decoficado = decodificar_base64(texto_codificado)
                    print(f"Texto decoficado: {texto_decoficado}")
                except (base64.binascii.Error, UnicodeDecodeError) as e:
                    print(f"Erro ao decodificar: {e}")
            elif escolha == '3':
                print("Você escolheu Sair.")
                break
            else:
                print("Escolha inválida. Por favor, digite 1, 2 ou 3.")
        except KeyboardInterrupt:
            print("\nVocê escolheu sair.")
            break
