# Automação: Enviar e-mails

## Solução
Foi desenvolvido por mim, um script na linguagem Python para a automação destes envios, poupando o tempo de qualquer responsável por esta função, o script faz a leitura dos dados em um arquivo de extensão CSV, monta o corpo do e-mail, e utiliza de um servidor smtp local para a propagação envio em massa.

### Requisitos técnicos:
- Python >= 3.8.3
- Servidor SMTP
### Estrutura do projeto:
- data/
	-	data_example.csv
 - main.py

### data/
Nesta pasta é armazenado em arquivos CSV os dados necessários que cada e-mail deve conter, por exemplo: nome da panvel, login, senha, e-mail. 

#### O que são arquivos CSV?
> Os arquivos CSV (do inglês "Character-separated values" ou "valores separados por um delimitador") servem para armazenar dados tabulares (números e texto) em texto simples. O "texto simples" significa que o arquivo é uma sequência de caracteres puros, sem qualquer informação escondida que o computador tenha que processar.  Um arquivo CSV abriga um sem número de "registros", separados por quebras de linha (cada "registro" permanece numa linha do arquivo) e cada registro possui um ou mais "campos", separados por um delimitador, os mais comuns sendo a vírgula (","), o ponto e vírgula (";") e o caractere "invisível" que surge ao se pressionar a tecla "tab". 
> 
 Citação retirada de: https://ceweb.br/guias/dados-abertos/capitulo-35/#:~:text=Os%20arquivos%20CSV%20(do%20ingl%C3%AAs,e%20texto)%20em%20texto%20simples.&text=Arquivos%20CSV%20s%C3%A3o%20simples%20e,que%20lidam%20com%20dados%20estruturados.

### main.py
Esse é o script principal, nele é feito a leitura do arquivo, a geração do e-mail e o envio. Também separei por funções a responsabilidade de envio para cada plataforma. 
No final deste script, é necessário chamar a função declarada para que seja disparado os e-mails.

Exemplo:

1 - Popular o arquivo CSV da plataforma (data_example.csv)
obs: nesta estrutura separei por |E-mail|Usuario|senha

![data](https://raw.githubusercontent.com/wlousado/enviar-email/master/screenshot/data_example.png)

2 - É preciso chamar a função main para que seja invocada e faça o seu papel.
obs: Você precisa configurar essa função conforme seu ambiente,
alterando os destinatários, cópias, e servidor smtp

3 - Resultado final:

![email](https://raw.githubusercontent.com/wlousado/enviar-email/master/screenshot/e-mail.png)


Dúvidas estou a disposição!
Obrigado.


