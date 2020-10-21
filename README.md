# Automação: Enviar e-mails

Com a chegada de novas plataformas para captação de receita, surgiu a necessidade de notificar as filiais com seus respectivos login e senha para acesso para captar a receita nas mesmas. Entretanto cada login e senha são únicos e destinado apenas a filial respectiva, sendo assim, fazendo necessário enviar e-mails individuais para cada filial, respeitando e cumprindo com o sigilo e normas da segurança da informação.

## Solução
Foi desenvolvido por mim, um script na linguagem Python para a automação destes envios, poupando o tempo de qualquer responsável por esta função, o script faz a leitura dos dados em um arquivo de extensão CSV, monta o corpo do e-mail, e utiliza de um servidor smtp local para a propagação envio em massa.

### Requisitos técnicos:
- Python >= 3.8.3
### Estrutura do projeto:
- data/
	-	indisponibilidade.csv
	-	memed.csv
	-	nexodata.csv
- view/
	- html.py
 - main.py

### data/
Nesta pasta é armazenado em arquivos CSV os dados necessários que cada e-mail deve conter, por exemplo: nome da panvel, login, senha, e-mail. 

#### O que são arquivos CSV?
> Os arquivos CSV (do inglês "Character-separated values" ou "valores separados por um delimitador") servem para armazenar dados tabulares (números e texto) em texto simples. O "texto simples" significa que o arquivo é uma sequência de caracteres puros, sem qualquer informação escondida que o computador tenha que processar.  Um arquivo CSV abriga um sem número de "registros", separados por quebras de linha (cada "registro" permanece numa linha do arquivo) e cada registro possui um ou mais "campos", separados por um delimitador, os mais comuns sendo a vírgula (","), o ponto e vírgula (";") e o caractere "invisível" que surge ao se pressionar a tecla "tab". 
> 
 Citação retirada de: https://ceweb.br/guias/dados-abertos/capitulo-35/#:~:text=Os%20arquivos%20CSV%20(do%20ingl%C3%AAs,e%20texto)%20em%20texto%20simples.&text=Arquivos%20CSV%20s%C3%A3o%20simples%20e,que%20lidam%20com%20dados%20estruturados.

### view/
Nesta pasta é armazenado scripts para gerar o corpo de e-mail, lembrando que podemos criar um corpo de e-mail utilizando texto simples, ou notação HTML com CSS Inline.

 - html.py
	 - Separei a responsabilidade de gerar e-mails por funções, cada função gera o padrão que será enviado a 		loja. Para isso, as funções recebem parâmetros, estes parâmetros serão utilizando para gerar o e-mail e por fim, a função retorna o conteúdo do e-mail atualizado com as informações que recebeu por parâmetro

### main.py
Esse é o script principal, nele é feito a leitura do arquivo, a geração do e-mail e o envio. Também separei por funções a responsabilidade de envio para cada plataforma. 
No final deste script, é necessário chamar a função declarada para que seja disparado os e-mails.

Exemplo:

1 - Cadastro e solicitação do Apoio Farmacêutico:

![Exemplo1](http://gitlab.dimed.com.br/wlousado/enviaemail/-/raw/master/screenshot/ex1.png)

2 - Popular o arquivo CSV da plataforma (nexodata.csv)
obs: nesta estrutura separei por |Nome da farmácia|Usuario/email|senha

![Exemplo2](http://gitlab.dimed.com.br/wlousado/enviaemail/-/raw/master/screenshot/ex2.png)

3 - É preciso chamar a função responsável para que seja invocada e faça o seu papel,
então após nos certificarmos que está tudo OK, e na ultima linha chamamos a função.
![Exemplo3](http://gitlab.dimed.com.br/wlousado/enviaemail/-/raw/master/screenshot/ex3.png)

4 - Ultimo passo é executar o script.

obs: Foi possível chamar o interpretador via linha de comando, pois o mesmo
se encontra no Path (variável de ambiente do windows), mas é possível utilizar
qualquer chamada de interpretador desde que execute na versão 3.8.3 ou maior.

![Exemplo4](http://gitlab.dimed.com.br/wlousado/enviaemail/-/raw/master/screenshot/ex4.png)


5 - Resultado final:
![Exemplo5](http://gitlab.dimed.com.br/wlousado/enviaemail/-/raw/master/screenshot/ex5.png)





Dúvidas estou a disposição!
Obrigado.


