# Trabalho de Engenharia de Software II / Teste de Software

## Integrantes

- Davi Braga Tolentino Veloso
- Guilherme Versiani Raposo
- Lais Guimaraes Lima Gomes

## Sistema Desenvolvido

O sistema permite fazer upload de arquivos de até 30MiB = 31457280 bytes. Há um sistema de busca, que indexa os arquivos. Um arquivo pode ser protegido por senha ou não. Se protegido por senha, o arquivo não é levado em conta pela máquina de busca.

Funcionalidades extras:
- Ver em tempo real os uploads mais recentes

## Tecnologias Utilizadas

`html`, `css`, `javascript`: frontend
`Python 3.x`: backend
`pytest`: framework de test
E outras bibliotecas python, como `flask`

## Instruções de Execução

Para instalar as dependências:

`pip install -r requirements.txt`

Para rodar:

`python Project/src/main.py`

No Windows, basta digitar `run` para chamar o batch file que roda esse comando.