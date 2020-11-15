# NoCall

Esse prejeto tem o objetivo de substituir marcações de entrada e saída de usuários via telefone
por marcações web.


Contexto:

Técnicos de diversas empresas ligam para dizer que estão acessando ou saindo de um determinado local.


Informações necessárias(dados relevantes):

-Data e Hora
-Nome do técnico
-Local
-Ticket/Chamado
-localização


Plugins:

-Geolocalição (Google Maps)


Ferramentas Utilizadas:

-Django3    
-MongoDB (salvar os logs)
-PostgreSql (Banco principal)


Comandos Uteis

Criar Ambiente Virtual: 
virtualenv --version
virtualenv nomedaenv

requirements.txt
Usado pra instalar dependencias do python (Django e Psycopg)
pip install -r requirements.txt