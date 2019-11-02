# Crawly Challenge
Repositório com o código do desafio crawly.

[![Build Status](https://travis-ci.org/abispo/crawly-challenge.svg?branch=master)](https://travis-ci.org/abispo/crawly-challenge)
[![codecov](https://codecov.io/gh/abispo/crawly-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/abispo/crawly-challenge)
![GitHub Pipenv locked Python version (branch)](https://img.shields.io/github/pipenv/locked/python-version/abispo/crawly-challenge/master)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

## Baixando o projeto
Execute os comandos abaixo no terminal:
```bash
git clone https://github.com/abispo/crawly-challenge.git
cd crawly-challenge
```

Crie o arquivo `.env` no diretório raiz do projeto com o seguinte conteúdo:
```
CRAWLY_APP_URL=http://applicant-test.us-east-1.elasticbeanstalk.com
```

O projeto consiste de uma API que retorna o resultado de um crawling em uma página. Depois do projeto instalado e executando, para fazer uma requisição você pode digitar no terminal:
```bash
curl -X GET http://127.0.0.1:8000
```

Ou acessar diretamente o link `http://127.0.0.1:8000` pelo navegador.

Ou ainda acessar a documentação da API em `http://127.0.0.1:8000/docs` ou `http://127.0.0.1:8000/redoc`.

## Executando o projeto usando Docker

> **Requisitos:**
> - Docker 19.03.4
> - docker-compose 1.24.1

Execute o comando abaixo no terminal:
```bash
docker-compose up
```

### Executando os testes pelo docker
Execute o comando abaixo no terminal:
```bash
docker exec -it crawly_challenge pipenv run pytest --cov tests/ --disable-warnings
```

## Executando o projeto usando Python com pipenv
> **Requisitos:**
> - Python 3.6
> - pip 9.0.1
> - pipenv 2018.11.26

Crie o arquivo `.env` no diretório raiz do projeto com o seguinte conteúdo:
```
CRAWLY_APP_URL=http://applicant-test.us-east-1.elasticbeanstalk.com
```

Execute os comandos abaixo no terminal:
```bash
pipenv install --dev
pipenv run uvicorn app.main:app --reload
```

### Executando os testes pelo pipenv
Execute o comando abaixo no terminal:
```bash
pipenv run pytest --cov tests/ --disable-warnings
```
