# Sistema de login Mini-Game RPG

  Esse foi um projeto feito inteiramente por mim, Douglas Freitas, para a Infinity School como uma simulação de um sistema de login 
para um Mini-Game-RPG. O projeto teve um tempo de desenvolvimento de 56 dias juntamente com o tempo de planejamento e pesquisa sobre
tecnologias e possibilidades.

## Tecnologias Utilizadas:

  O projeto foi desenvolvido inteiramente em Python e MySQL utilizando as bibliotecas:

  - ### Flet
Que utiliza a linguagem Flutter por detrás dos panos para a criação de interfaces modernas e atrativas para o usuário.

  - ### mysql-connector-python
Uma biblioteca que permite a conexão entre Python e MySQL por meio de scripts simples para realizar consultas e operações no banco de dados.

  - ### bycrypt
Uma biblioteca usada para transformar strings como, senhas, em hashs de bytes, para melhor segurança ao salvar as senhas em banco de dados. 

## Sobre o Projeto

O projeto consiste em um sistema de login e customização de personagem simples. Inicia-se com as opções de _Login_ onde o usuário que já
tem uma conta e personagens criados pode fazer seu login com seu **usuário** e **senha** corretos, para ser direcionado à página principal.
Ou _Criar Conta_ onde o usuário deve inserir seu **nome**, **usuário**, e confirmar sua **senha**, para então ser direcionado a página de 
criação de personagem, na qual ele customiza totalmente seu personagem, escolhendo todas suas características físicas e outros 
aspectos como, _foto_, _história_, _inteligência_ e etc...

Todas as informações são armazenadas com segurança no banco de dados para serem acessadas depois. Na página principal
o usuário tem as opções de _jogar_ e _ver ranking_ que estão temporariamente desabilitados, já que isso não faz parte do briefing do projeto.
Além disso, há opções para fazer LogOut ou visualizar as características do personagem. Sempre mantendo a **simplicidade** e o **design** 
atrativo para o usuário.

### Desenvolvimento
O desenvolvimento do projeto foi tranquilo, porém mais demorado do que o esperado devido a problemas e bugs ocasionados pela minha pouca 
experiência com projetos completos como este. Desde o início, pesquisei sobre novas implementações para tornar o projeto o mais profissional 
possível. Desenvolvi o projeto inteiramente em inglês para me familiarizar com as nomenclaturas e a escrita técnica.

A experiência que ganhei com esse projeto foi imensurável. Fiz tudo sozinho, utilizando a ajuda de **IAs** apenas para **aprender** novas tecnologias
e implementações, e **nunca para escrever** o código por mim.

### Detalhes
Procurei fazer um código que facilitasse minha própria compreensão e depuração do mesmo, criando classes e várias funções em diferentes 
arquivos para manter a organização e o fácil entendimento desde o início.

 - **Logs:** Criei um simples sistema de _logs_ de ações que estão sendo executadas no momento pelo terminal. Para que eu pudesse ver onde o
   código está travando ou _bugando_
 - **Classes:** Para armazenar as informações dos usuários e personagens, eu optei por usar classes para encapsular informações
   sensíveis dos mesmos.
 - **Usuário logado:** Optei por identificar o usuário que está atualmente usando o app, com uma variável que é carregada com seu ID
   assim que seu login é confirmado. E que é importada e usada para fazer todas as operações no Banco de Dados relacionadas ao usuário

## Como usar

Para usar o app e roda-lo na sua máquina, primeiro teremos que criar o banco de dados utilizando o MySQL Workbench, ou outro app de sua 
preferência que suporte o _mysql-connector-python_. Após fazer a instalação dos arquivos de código, procure pelo arquivo _create_database.sql_
que está em _app/database/create_database.sql_ e execute todo o seu código no seu MySQl-Workbench para criar o banco de dados com sucesso.

Após isso, vamos instalar as dependências necessárias para fazer o projeto funcionar. 
Primeiro, crie um ambiente virtual executando o seguinte comando no terminal:

```Python
python -m venv venv
# Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

Depois de ter seu ambiente virtual criado e ativado, vamos instalar as dependências necessárias localizadas no arquivo _requirements.txt_
executando o seguinte código no terminal:

```Python
pip install -r requirements.txt
```

Por fim, vamos configurar a conexão com o Banco de dados. Localize o arquivo _connections.py_ que está em app/database/connections.py
e localize a função _create_conn()_. Na parte:

```Python
connection = mysql.connector.connect(
            host='127.0.0.1',       
            database='RPG',         
            user='root',            
            password='admin' 
        )
```

troque as informações _host_, _user_ e _password_ conforme as suas próprias. 

#### Finalmente, você tem o projeto pronto para uso! Basta executar o arquivo main.py localizado no diretório raiz do projeto!
## Aproveite!
