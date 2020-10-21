
def Memed(panvel, usuario, senha):
    return """ 
    <div>
        <h3>Olá {0}</h3>
        <p>
            Agora você pode fazer a <strong>captação eletrônica</strong> pela <strong>Memed!</strong>
        </p>
        
        <p>Segue seus dados para acesso:</p>
        <table style="border-collapse:collapse; text-align:center">
            <tbody>
                <tr style="border:1px solid black">
                    <td style="padding:6px; border:1px solid black; background-color:#3486eb; color:white">
                        <strong>Usuário</strong>
                    </td>
                    <td style="padding:6px; border:1px solid black; background-color:#3486eb; color:white">
                        <strong>Senha</strong>
                    </td>
                    <td style="padding:6px; border:1px solid black; background-color:#3486eb; color:white">
                        <strong>Acesso a plataforma</strong>
                    </td>
                </tr>
                <tr style="border:1px solid black">
                    <td style="padding:10px; border:1px solid black">{1}</td>
                    <td style="padding:10px; border:1px solid black">{2}</td>
                    <td style="padding:10px; border:1px solid black">
                        <a href="https://memed.com.br/receita/login">Acesse aqui!</a>
                    </td>
                </tr>
            </tbody>
        </table>
        <br>
        <h4>
            Como faço o acesso?<br>
            <p style="font-weight:normal">
                Você deve acessar o site, digitar o código da receita, e utilizar o login e senha descritos neste e-mail. <br>
                Acesso: <a href="https://memed.com.br/receita/login">https://memed.com.br/receita/login</a>
            </p>
        </h4>
        <h4>
            Ainda com dúvida? <br>
            <p style="font-weight:normal">
                Converse com o Eliot, nosso ChatBot da CS, <a href="https://s3.amazonaws.com/demo-webchat/dimed-interno/index.html">clicando aqui!</a> 
                <br>
                Inicie uma conversa pelo <strong>balão de fala que fica no canto inferior direito</strong> 
                <br>
                Preencha o campo <strong><i>Nome</i></strong> e o campo <strong><i>Usuário Omni/Pharmaweb</i><br></strong>e digite <strong><i>Receita Digital</i></strong> para receber mais orientações sobre o processo. 
            </p>
        </h4>
    </div>
    """.format(panvel, usuario, senha)

def Nexodata(panvel, usuario, senha):
    return """
    <div>
        <p>
            <strong>Quem é Nexodata?</strong> 
            <br><br>A <span>Nexodata</span> permite que o médico realize as receitas digitalmente e está presente nos principais sistemas de saúde e nas maiores redes de hospitais e clínicas do país. Fazemos isso para conectar farmácias a milhões de pacientes de forma rápida, segura, certificada e inteligente.
        </p>
        
        <p>
            <strong>Como acessar a receita digital?</strong> 
            <br>
            <br>
            Para acessar o Portal, basta entrar em 
            <a href="https://farmacias.nexodata.com.br" target="_blank">https://farmacias.nexodata.com.br</a> 
            e fazer o login.
            <br>
            O seu <strong>usuário</strong> é: <strong>{0}</strong> 
            <br>
            E a sua <strong>senha</strong> é: <strong>{1}</strong> 
        </p>
        
        <p>
            Você recebeu um <strong>Login de Administrador</strong> e por isso, poderá cadastrar seus profissionais, caso queira. Para saber mais, acesse nosso FAQ (em anexo) e vá até a pergunta número 
        </p>
        
        <p style="color:red">Informações importantes:</p>
        
        <p><i><strong>Recomendamos fortemente</strong> que deixem a senha e o login salvos em todos os computadores. Isso facilitará a dinâmica da farmácia, no momento que o cliente chegar com uma receita digital. </i></p>
        
        <p>
            <i>
                <strong>Dicas:</strong>
            </i>
        </p>
        
        <p>
            <i>
                Salve também, na área de trabalho do computador da loja ou em favoritos, 
                o link do Portal da Nexodata, para que o acesso de todos os atendentes e farmacêuticos seja rápido.
            </i>
        </p>
        
        <p>
            <i>
                <strong>Ainda com dúvida?</strong> 
                
                <br>
                Converse com o Eliot, nosso ChatBot da CS, 
                <a href="https://s3.amazonaws.com/demo-webchat/dimed-interno/index.html" target="_blank">clicando aqui</a>!
                Inicie uma conversa pelo <strong>balão de fala que fica no canto inferior direito</strong> Preencha o campo 
                <strong>Nome</strong> e o campo <strong>Usuário Omni/Pharmaweb</strong> e digite <strong><i>Receita Digital</i></strong>
                para receber mais orientações sobre o processo. 
            </i>
        </p>
        <p>
            <i>
                Ou Acesse o portal da Nexodata pelo link: <a href="https://nexodata.zendesk.com/hc/pt-br" target="_blank">https://nexodata.zendesk.com/hc/pt-br</a> 
            </i>
        </p>
        <p>
            <i>
                Ou Entre em contato com a CS pelo ramal interno 2101, ou externo (51) 3220-2101, opção 1. 
            </i>
        </p>
    </div>
    """.format(usuario, senha)

def Indisponibilidade():
    return """
        <p class="x_MsoNormal"><span style="font-size:12.0pt; font-family:&quot;Calibri Light&quot;,sans-serif">Olá, </span></p>
        <p class="x_MsoNormal"><span style="font-size:12.0pt; font-family:&quot;Calibri Light&quot;,sans-serif">Informamos que, durante a madrugada de sábado para domingo, 26 e 27/09, haverá uma sequência de testes em nossos servidores e infraestrutura de datacenter, que acabará afetando algumas funcionalidades em sua filial durante esse período. </span></p>
        <p class="x_MsoNormal"><b><span style="font-size:14.0pt; font-family:&quot;Calibri Light&quot;,sans-serif; color:red">Orientamos que realize vendas off-line&nbsp; durante esse período, com vendas somente pelo POS.</span></b></p>
        <p class="x_MsoNormal"><span style="font-size:12.0pt; font-family:&quot;Calibri Light&quot;,sans-serif">Lembramos que vendas realizadas nessa modalidade não conseguem oferecer os descontos de PBM ou Convênios. </span></p>
        <p class="x_MsoNormal"><b><span style="font-size:12.0pt; font-family:&quot;Calibri Light&quot;,sans-serif">A previsão é que essa bateria de testes seja realizada entre a 01h00 e às 06h00 de 27/09.</span></b></p>
        <p class="x_MsoNormal"><span style="font-size:12.0pt; font-family:&quot;Calibri Light&quot;,sans-serif">O serviço será restabelecido, após esse horário, sem aviso, para toda a rede.</span></p>
        <p class="x_MsoNormal"><span style="font-size:12.0pt; font-family:&quot;Calibri Light&quot;,sans-serif">Caso surjam dúvidas, a Central de Serviços estará operando normalmente durante todo o período.</span></p>
        <br><br>
    """