# MTZ_EFD_MANUTENCAO-GERACAO_ESPECIAL

> Fonte: MTZ_EFD_MANUTENCAO-GERACAO_ESPECIAL.doc

Módulo SPED Fiscal – Geração Meio Magnético (Especial)

Módulo: SPED ( EFD – Escrituração Fiscal Digital
Menu: Geração ( Meio Magnético (Meio Magnético (Especial)

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS-3736-A	Data do Saldo Inicial LPD	Novo parâmetro para informação da Data do Saldo Inicial LPD	19/09/2012		OS-3838	Nova versão de leiaute	Atualização legal – Ato cotepe 57 de Nov/2012 – Novo Código de leiaute.	05/12/2012		OS3983	Nova versão de leiaute	Atualização legal – Ato Cotepe 14/2013 – Novo Código de leiaute
(ver RN03).	26/04/2013		OS4261	Atualização da versão de leiaute	Atualização legal – Ato Cotepe 52/13	06/12/2013		OS4535	Nova versão de leiaute	Atualização legal – Ato Cotepe 22/2014 – Novo Código de leiaute.	14/08/2014		OS4609	Nova versão de leiaute	Atualização legal – Ato Cotepe 49/2014 – Novo Código de leiaute (ver RN03).	05/12/2014		MFS8017	Ato Cotepe 7/2016	Possibilitar ao cliente gerar a versão 1.10 para testes no ano de 2016	14/11/2016		MFS13290	Ato Cotepe ICMS 48/2017	Possibilitar ao cliente gerar a versão 1.11 para testes no ano de 2018	21/09/2017		MFS-20986	Ato Cotepe ICMS 44/2018	Possibilitar ao cliente gerar a versão 1.12 para testes no ano de 2019	04/10/2018		MFS31406	Ato Cotepe ICMS 65/2019	Possibilitar ao cliente gerar a versão 1.13 para testes no ano de 2020	28/11/2019		MFS45380	Nova versão de layout	Atualização legal – Ato Cotepe 44/2020 – Nova versão de layout 1.14 (ver RN02).	21/10/2020		MFS73692	Nova versão de layout	Atualização legal – Ato Cotepe 62/2021 – Nova versão de layout 1.15 (ver RN02).	13/10/2021		MFS85388	Nova versão de layout	Atualização legal – Ato Cotepe 21/2022 – Nova versão de layout 1.16 (ver RN02).	11/05/2022		MFS579421	Nova versão de layout	Atualização legal – Ato Cotepe 134/2023 Nova versão de layout 1.17 (ver RN02).	19/10/2023		MFS690861	Nova versão de layout	Atualização legal – Ato Cotepe 131/2024 Nova versão de layout 1.18 (ver RN02).	01/10/2024		MFS861835	Nova versão de layout	Atualização legal – Ato Cotepe 79/2025 Nova versão de layout 1.19 (ver RN02).	11/08/2025		
REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	Regras gerais

(espaço reservado para regras genéricas, que não dizem respeito a campos específicos)

		RN01	“Campo Data do Saldo Inicial LPD (Cotepe 41)”

O campo Data do Saldo Inicial LPD (Cotepe 41) será um campo do tipo Data, formato DD/MM/AAAA, de parametrização não obrigatória. Quando informado será considerado na geração do campo 04 – ESTQ_INI do Registro 1391 do SPED Fiscal.
	OS-3736-A		RN02	Campo “Leiaute”

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

Alteração da MFS-73692:
Incluída a nova versão de leiaute 1.15, referente ao Ato Cotepe ICMS 62/2021. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2022. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2022, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

Alteração da MFS-85388:
Incluída a nova versão de leiaute 1.16, referente ao Ato Cotepe ICMS 21/2022. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2023. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2023, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.


Alteração da MFS579421:
Incluída a nova versão de leiaute 1.17, referente ao Ato Cotepe ICMS 134/2023. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2024. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2024, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

Alteração da MFS690861:
Incluída a nova versão de leiaute 1.18, referente ao Ato Cotepe ICMS 131/2024. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2025. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2025, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

Alteração da MFS861835:
Incluída a nova versão de leiaute 1.19, referente ao Ato Cotepe ICMS 79/2025. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2026. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2026, será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados. Deseja continuar mesmo assim?” e o cliente poderá escolher entre continuar a geração Sim ou Não. Caso seja selecionado Não, a geração não será iniciada.

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
MFS73692
MFS85388