<div align="center">
    <h1> 💧📍 Hack4Cities - Conectando Cidades e Pessoas 🌆 </h1>
    <img alt="Fiber sensor blue logo" src="https://raw.githubusercontent.com/itsaleplets/fiber-sensors/Main/src/images/blue-logo.png" width="200px" />   
</div>
<br>
A Fiber Sensors é uma inovação tecnológica que utiliza circuitos ópticos unidos na tubulação hídrica para detecção de vazamentos. Nossa solução dispõe características únicas que nenhuma outra tecnologia pode oferecer, como: análise em tempo real e remota de toda malha hídrica capaz de detectar pequenos vazamentos, convergência de todos os dados um uma única interface e, além disso, nossa solução é de baixo custo.

<br>
### Ferramentas

A parte back-end do projeto foi construída em Python com a leitura do arquivo da maquina de sensor e utilizando Django para a geração do back-end para geração da API para a aplicação web.

[Link para o Front-end](https://github.com/itsaleplets/fiber-sensors)

## :hammer: Instalação

Com o Python >= 3.0 instalado


Dentro da pasta do projeto execute

Instalação dos pacotes:

```
pip install -r requirements.txt
```

Gerando o xml do arquivo SOR da maquina de sensor:

```
pyOTDR sensor.SOR XML
```

Rodando as Migrations:

```
python manage.py makemigrations
```

Rodando a Migrate:

```
python manage.py migrate
```

Criando Super Usuario

```
python manage.py createsuperuser
```

Rodando a Aplicação Back-End:

```
python manage.py runserver
```