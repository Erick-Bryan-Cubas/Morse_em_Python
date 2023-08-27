# Codificador e Reprodutor de Código Morse

Este repositório contém um simples programa em Python para codificar mensagens em código Morse e reproduzir o som correspondente às sequências de pontos e traços. Isso é realizado utilizando arquivos de som curtos e longos para representar os símbolos do código Morse.

## Pré-requisitos

Certifique-se de que você tenha o Python instalado em seu sistema. Você também precisará da biblioteca `playsound` para reproduzir os arquivos de som. Você pode instalá-la usando o seguinte comando:

```
pip install playsound==1.2.2
```

## Funcionamento

1. O programa inicia lendo uma mensagem em texto inserida pelo usuário.
2. A mensagem é convertida para letras maiúsculas e, em seguida, cada caractere é traduzido para o código Morse utilizando um dicionário pré-definido.
3. A sequência de código Morse é reproduzida como som, onde os pontos são representados por um som curto ("bip_short.mp3") e os traços são representados por um som longo ("bip_long.mp3"). Intervalos de tempo apropriados são inseridos entre cada som para que a sequência seja discernível.
4. Caracteres de espaço e barra ("/") são interpretados como intervalos de palavras.
5. Caracteres não reconhecidos são tratados como inválidos e uma mensagem de erro é exibida.
6. A sequência de código Morse é impressa no console.
7. A mensagem em código Morse é traduzida de volta para o texto original utilizando um dicionário reverso.
8. A mensagem traduzida é exibida no console.

## Utilização

1. Execute o programa em um ambiente Python.
2. Insira o texto que deseja codificar em código Morse.
3. A sequência de código Morse será reproduzida como som e exibida no console.
4. A mensagem traduzida de volta para o texto original também será exibida.

## Contribuições

Sinta-se à vontade para contribuir para este repositório. Você pode melhorar o código, adicionar recursos adicionais, aprimorar a interface do usuário ou corrigir possíveis problemas. Basta enviar um pull request e ficaremos felizes em revisar suas contribuições.

Esperamos que este programa seja educativo e útil para quem deseja aprender sobre código Morse e manipulação de som em Python. Divirta-se codificando e reproduzindo mensagens em código Morse!

**Nota:** Certifique-se de fornecer os arquivos de som "bip_short.mp3" e "bip_long.mp3" no diretório do projeto para que o programa possa reproduzir os sons corretamente. Esses arquivos podem ser obtidos ou criados de acordo com a sua preferência.
