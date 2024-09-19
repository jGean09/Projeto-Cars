# Projeto de Gestão de Carros

Este projeto é uma aplicação web desenvolvida com Django para a gestão de informações sobre carros e suas marcas. Ele faz parte de um curso de Django Master, que visa aprofundar o conhecimento em desenvolvimento de aplicações web com Django.

## Funcionalidades

- **Cadastro de Marcas:** Permite a criação e gerenciamento de marcas de carros.
- **Cadastro de Carros:** Permite o registro e atualização das informações de carros, incluindo marca, ano de fábrica, ano do modelo, placa, valor e foto.

## Modelos

### Brand

O modelo `Brand` representa uma marca de carro e possui os seguintes campos:

- `id` (AutoField, chave primária): Identificador único da marca.
- `name` (CharField): Nome da marca.

#### Métodos

- `__str__(self)`: Retorna o nome da marca.

### Car

O modelo `Car` representa um carro e possui os seguintes campos:

- `id` (AutoField, chave primária): Identificador único do carro.
- `model` (CharField): Modelo do carro.
- `brand` (ForeignKey): Relação com o modelo `Brand`. Define a marca do carro e é protegido contra exclusão.
- `factory_year` (IntegerField): Ano de fabricação do carro.
- `model_year` (IntegerField): Ano do modelo do carro.
- `plate` (CharField): Placa do carro.
- `value` (FloatField): Valor do carro.
- `photo` (ImageField): Foto do carro, armazenada na pasta `cars/`.

#### Métodos

- `__str__(self)`: Retorna o modelo do carro.

## Requisitos

- Python 3.x
- Django 3.x ou superior
- 
## Nota
Este projeto é baseado no curso Django Master, que fornece uma base sólida para o desenvolvimento de aplicações web robustas usando Django.




