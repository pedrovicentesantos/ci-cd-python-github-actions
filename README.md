# Projeto

Aplicação Web em Python usando Flask para exibir imagens de gatos ou cachorros, de acordo com a rota chamada.

Utiliza duas APIs para obter imagens aleatórias:

- [https://api.thecatapi.com/v1/images/search](https://api.thecatapi.com/v1/images/search)
- [https://api.thedogapi.com/v1/images/search](https://api.thedogapi.com/v1/images/search)

## Rotas

- /

  - Rota principal, que retorna imagem aleatória de um gato

- /dog
  - Rota que retorna imagem aleatória de um cachorro

## Instalação

É possível testar a aplicação localmente.

Para isso, deve-se clonar o repositório e entrar na pasta do projeto:

```
git clone https://github.com/pedrovicentesantos/ci-cd-python-github-actions
cd ci-cd-python-github-actions
```

O segundo passo é instalar as dependências necessárias para o projeto funcionar, usando o seguinte comando:

```
pip install -r requirements.txt
```

Feito isto, basta rodar o seguinte comando iniciar a aplicação:

```
flask run
```

Depois deste comando, a aplicação já estará funcionando e é possível acessá-la pelo servidor local:

```
localhost:5000
```

Como a aplicação possui testes, eles podem ser rodados com o seguinte comando:

```
python -m pytest tests
```

## Pipelines

A aplicação possui dois pipelines, uma para cada Pull Request na branch Main e um para cada Push na branch Main.

Ambos os pipelines instalam as dependências necessárias, passam a pasta com o código principal por um lint e rodam testes com o framework `pytest`.
