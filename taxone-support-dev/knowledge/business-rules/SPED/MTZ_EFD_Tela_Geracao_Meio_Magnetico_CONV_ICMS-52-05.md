# MTZ_EFD_Tela_Geracao_Meio_Magnetico_CONV_ICMS-52-05

> Fonte: MTZ_EFD_Tela_Geracao_Meio_Magnetico_CONV_ICMS-52-05.doc

Módulo SPED Fiscal – Geração Conv. ICMS 52/05

Módulo: SPED ( EFD – Escrituração Fiscal Digital
Menu: Geração Conv. ICMS 52/05( Meio Magnético	

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS-3838	Nova versão de leiaute	Atualização legal – Ato cotepe 57 de Nov/2012 – Novo Código de leiaute.	05/12/2012		OS3983	Nova versão de leiaute	Atualização legal – Ato Cotepe 14/2013 – Novo Código de leiaute.	26/04/2013		OS4261	Atualização da versão de leiaute	Atualização legal – Ato Cotepe 52/13	06/12/2013		OS4535	Nova versão de leiaute	Atualização legal – Ato Cotepe 22/2014 – Novo Código de leiaute
(ver RN03).	14/08/2014		OS4609	Nova versão de leiaute	Atualização legal – Ato Cotepe 49/2014 – Novo Código de leiaute
(ver RN03).	05/12/2014		MFS8017	Ato Cotepe 7/2016	Possibilitar ao cliente gerar a versão 1.10 para testes no ano de 2016	14/11/2016		MFS13290	Ato Cotepe ICMS 48/2017	Possibilitar ao cliente gerar a versão 1.11 para testes no ano de 2018	21/09/2017		MFS-20986	Ato Cotepe ICMS 44/2018	Possibilitar ao cliente gerar a versão 1.12 para testes no ano de 2019	04/10/2018		MFS31406	Ato Cotepe ICMS 65/2019	Possibilitar ao cliente gerar a versão 1.13 para testes no ano de 2020	28/11/2019		MFS45380	Nova versão de layout	Atualização legal – Ato Cotepe 44/2020 – Nova versão de layout 1.14 (ver RN01).	21/10/2020		MFS73692	Nova versão de layout p/ jan/2022		MFS85388	Nova versão de layout p/ jan/2023		
REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	Regras gerais

(espaço reservado para regras genéricas, que não dizem respeito a campos específicos)
		RN01	Campo “Leiaute”

Incluir no campo “Leiaute” a opção “Escrituração Fiscal Digital – Ato Cotepe ICMS 57/2012 – Versão 1.0.6”
O posicionamento deste registro deve seguir a ordem de versão, ficando logo abaixo da opção de versão “1.0.5”.

Este novo leiaute entra em vigor a partir do dia 01/01/2013. 

Se o usuário selecionar esta nova opção (Layout versão 1.0.6) e inserir nos campos “Data Inicial” e “Data final” um período anterior ao ano de 2013, então o sistema deve apresentar a mensagem: 
“Leiaute incompatível com o período dos dados a serem apresentados.”

Incluir no campo “Leiaute” a opção “Escrituração Fiscal Digital – Ato Cotepe ICMS 14/2013 e 52/2013 – Versão 1.0.7”
O posicionamento deste registro deve seguir a ordem de versão, ficando logo abaixo da opção de versão “1.0.6”.

Este novo leiaute entra em vigor a partir do dia 01/04/2013. 

Se o usuário selecionar esta nova opção (Layout versão 1.0.7) e inserir nos campos “Data Inicial” e “Data final” um período anterior a 01/04/2013, então o sistema deve apresentar a mensagem: 
“Leiaute incompatível com o período dos dados a serem apresentados.”

Alteração da OS4535:
Incluída a nova versão de leiaute 1.0.8 (“Escrituração Fiscal Digital-Ato Cotepe ICMS 22/2014-Versão 1.0.8”), com validade a partir de Jan/2015. Se o usuário selecionar a versão 1.0.8, e informar nos campos “Data Inicial” e “Data final” um período anterior a Janeiro/2015, então será demonstrada a mensagem padrão “Leiaute incompatível com o período dos dados a serem apresentados” e a geração não será iniciada até que o usuário modifique os parâmetros informados.

Alteração da OS4609:
Incluída a nova versão de leiaute 1.0.9 (“Escrituração Fiscal Digital-Ato Cotepe ICMS 49/2014-Versão 1.0.9”), com validade a partir de Jan/2016. Se o usuário selecionar a versão 1.0.9, e informar nos campos “Data Inicial” e “Data final” um período anterior a Janeiro/2016, então será demonstrada a mensagem padrão “Leiaute incompatível com o período dos dados a serem apresentados” e a geração não será iniciada até que o usuário modifique os parâmetros informados.

Alteração da MFS8017:
Incluída a nova versão de leiaute 1.10, referente ao Ato Cotepe ICMS 07/2016. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2017. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2017, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

Alteração da MFS13290:
Incluída a nova versão de leiaute 1.11, referente ao Ato Cotepe ICMS 48/2017. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2018. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2018, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

Alteração da MFS-20986:
Incluída a nova versão de leiaute 1.12, referente ao Ato Cotepe ICMS 44/2018. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2019. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2019, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

Alteração da MFS-31406:
Incluída a nova versão de leiaute 1.13, referente ao Ato Cotepe ICMS 65/2019. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2020. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2020, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

Alteração da MFS-45380:
Incluída a nova versão de leiaute 1.14, referente ao Ato Cotepe ICMS 44/2020. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2021. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2021, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

	OS-3838
OS3983
OS4261
OS4535
OS4609
MFS8017
MFS13290
MFS-20986
MFS31406
MFS45380