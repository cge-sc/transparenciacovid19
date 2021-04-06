# Transparência Covid-19 

Código fonte da página de transparência sobre enfrentamento da Covid-19 no Estado de Santa Catarina - [transparenciacovid19.sc.gov.br](http://transparenciacovid19.sc.gov.br/)

## Objetivo
O site foi criado pela [CGE/SC](https://cge.sc.gov.br/) tendo como objetivo principal disponibilizar informações de forma simples e com foco nos gastos públicos catarinense e demais atividades relacionadas à transparência no enfrentamento da pandemia do novo coronavírus (Sars-CoV-2).

## Tecnologia
Foi aproveitado muito do HTML e CSS do Portal da Transparência [transparencia.sc.gov.br](http://www.transparencia.sc.gov.br/), sendo necessários alguns ajustes. Desta forma mantém um alinhamento ao portal, através de uma identidade visual semelhante e facilita a navegação daqueles que já utilizam esta página.

Para fazer o roteamento das páginas foi usado o [Flask](https://flask.palletsprojects.com/) por ser um microframework Python leve e escalável. Optou-se por criar o roteamento dentro do arquivo app.py, uma vez que são poucas páginas dentro do site. 

O [Jinja](https://jinja.palletsprojects.com/) serve para otimizar a escrita de HTML, permitindo assim isolar trechos que possam ser reutilizados, tais como cabeçalhos e rodapés. 
Os gráficos disponibilziados dentro da página foram criados usando o [Metabase](https://www.metabase.com/) para agilizar o processo de criação.
Foi utilizada a hospedagem na [Heroku](https://www.heroku.com/), nuvem, como ambiente de homologação, permitindo assim uma agilidade nas entregas das versões, tanto de novas funcionalidades quanto de correções e ajustes.

## Ambiente de desenvolvimento
### Criar e ativar o ambiente virtual
pip3 install virtualenv
virtualenv env
source env/bin/activate

### Instalar as dependências
pip3 install flask

### Criar o arquivo Procfile para a Heroku saber o que fazer
touch Procfile

### Incluir a linha abaixo no arquivo Procfile
web: gunicorn app:app

### Congelar as dependências e salvar no arquivo requirements.txt
pip3 freeze > requirements.txt

### Rodar em ambiente de desenvlvimento

## Ambiente de homologação
### Conectar o usuário à Heroku. Abre uma aba no navegador para usuário e senha na Heroku.
heroku login

### Criar o app na Heroku
heroku create transparenciacovid9

### Configurar o ambiente para Python com o buildpack da Heroku
heroku buildpacks:set heroku/python

### Verificar se está apontando para transparenciacovid19
heroku remote -v

Caso não esteja, rodar o comando abaixo:

heroku git:remote -a transparenciacovid19

### Operações para subir o projeto no Github e rodar na Heroku
git init

git add .

git commit -m “Texto da versão”

git push heroku master