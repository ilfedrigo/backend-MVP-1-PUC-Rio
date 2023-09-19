# Brain Notes - Back-end

Este projeto faz parte da entrega do MVP da primeira Sprint em Desenvolvimento em Full Stack Básico do curso de pós-graduação **Desenvolvimento Full Stack** pela PUC-Rio.

O objetivo deste projeto é colocar em prática os conceitos aprendidos ao longo das últimas 11 semanas nas disciplinas de **Programação Orientada e Objetos**, **Banco de Dados** e **Desenvolvimento Full Stack Básico**.

---
## Como executar 

> Após clonar o repositório é necessário iniciar um ambiente virtual do tipo [virtualenv] 

Para executar o **Brain Notes** será necessário instalar as dependências da aplicação, as mesmas estão listadas no arquivo `requirements.txt` e podem ser instaladas através do comando:

```
(nome_do_ambiente_virtual)$ pip3 install -r requirements.txt
```

Após executar o comando acima, todas as as dependências/bibliotecas, descritas no arquivo `requirements.txt` estarão instaladas.

Feito isso, basta executar o comando abaixo para iniciar a API:

```
(nome_do_ambiente_virtual)$ flask run --host http://127.0.0.1 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(nome_do_ambiente_virtual)$ flask run --host 0.0.0.0 --port 5000 --reload
```