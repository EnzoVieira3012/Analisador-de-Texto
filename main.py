import re


def analyze_text(text):
    # Contar caracteres
    num_characters = len(text)

    # Contar frases (considera que uma frase termina com '.', '!', ou '?')
    num_sentences = len(re.findall(r'[.!?]', text))

    # Contar palavras
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)

    # Contar palavras por frase
    if num_sentences > 0:
        avg_words_per_sentence = num_words / num_sentences
    else:
        avg_words_per_sentence = 0

    # Contar caracteres por palavra
    if num_words > 0:
        avg_characters_per_word = num_characters / num_words
    else:
        avg_characters_per_word = 0

    # Exibir estatísticas
    print("\nEstatísticas do Texto:")
    print(f"Número de caracteres: {num_characters}")
    print(f"Número de frases: {num_sentences}")
    print(f"Número de palavras: {num_words}")
    print(f"Média de palavras por frase: {avg_words_per_sentence:.2f}")
    print(f"Média de caracteres por palavra: {avg_characters_per_word:.2f}")


def main():
    print("Bem-vindo ao analisador de texto!")

    while True:
        text = input("\nDigite o texto para análise (ou 'sair' para encerrar): ")
        if text.lower() == 'sair':
            print("Saindo...")
            break

        analyze_text(text)


if __name__ == "__main__":
    main()
