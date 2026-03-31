# MTZ_EFD_MANUTENCAO-GERACAO

> Fonte: MTZ_EFD_MANUTENCAO-GERACAO.doc

Módulo SPED Fiscal – Geração 

Módulo: SPED ( EFD – Escrituração Fiscal Digital
Menu: Geração ( Meio Magnético

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS-2388-A7	Perfil por estabelecimento	Novo tratamento para quando houver perfil por estabelecimento	29/06/2011		OS-3736	Data do Saldo Inicial LPD	Novo parâmetro para informação da Data do Saldo Inicial LPD	04/09/2012		OS-3838	Nova versão de leiaute	Atualização legal – Ato cotepe 57 de Nov/2012 – Novo Código de leiaute.	05/12/2012		OS3983	Nova versão de leiaute	Atualização legal – Ato Cotepe 14/2013 – Novo Código de leiaute.	26/04/2013		OS4261	Atualização da versão de leiaute	Atualização legal – Ato Cotepe 52/13	06/12/2013		OS4535	Nova versão de leiaute	Atualização legal – Ato Cotepe 22/2014 – Novo Código de leiaute
(ver RN03).	14/08/2014		OS4508	Alteração p/ Multiempresa	Alteração da geração da EFD para possibilitar a geração multiempresa, e também filtro dos estabelecimentos por UF (ver RN04, RN05 e RN06)	02/09/2014		OS4609	Nova versão de leiaute	Atualização legal – Ato Cotepe 49/2014 – Novo Código de leiaute (ver RN03).	05/12/2014		MFS4992	Ato Cotepe 7/2016	Criação dos novos registros do Bloco K, e da nova versão de layout 1.10. Ver RN03.	(27/06/2016)		MFS8017	Ato Cotepe 7/2016	Possibilitar ao cliente gerar a versão 1.10 para testes no ano de 2016	14/11/2016		MFS13290	Ato Cotepe ICMS 48/2017	Possibilitar ao cliente gerar a versão 1.11 para testes no ano de 2018	21/09/2017		MFS-20986	Ato Cotepe ICMS 44/2018	Possibilitar ao cliente gerar a versão 1.12 para testes no ano de 2019	04/10/2018		MFS31406	Ato Cotepe ICMS 65/2019	Possibilitar ao cliente gerar a versão 1.13 para testes no ano de 2020	28/11/2019		MFS45380	Nova versão de layout	Atualização legal – Ato Cotepe 44/2020 – Nova versão de layout 1.14 (ver RN03).	21/10/2020		MFS73692	Nova versão de layout	Atualização legal – Ato Cotepe 62/2021 – Nova versão de layout 1.15 (ver RN03).	13/10/2021		MFS76273	Andréa Rocha	Tratamento da mensagem de erro referente ao tipo de apuração de ICMS/IPI para as empresas prestadoras de serviço do DF	21/12/2021		MFS85388	Nova versão de layout	Atualização legal – Ato Cotepe 21/2022 – Nova versão de layout 1.16 (ver RN03).	11/05/2022		MFS579421	Nova versão de layout	Atualização legal – Ato Cotepe 134/2023 Nova versão de layout 1.17 (ver RN03).	19/10/2023		MFS690861	Nova versão de layout	Atualização legal – Ato Cotepe 131/2024 Nova versão de layout 1.18 (ver RN03).	01/10/2024		MFS861835	Nova versão de layout	Atualização legal – Ato Cotepe 79/2025 Nova versão de layout 1.19 (ver RN03).	11/08/2025		
REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	Regras gerais

(espaço reservado para regras genéricas, que não dizem respeito a campos específicos)

Alteração da OS4508:

Com a alteração para geração multiempresa (ver RN04, RN05 e RN06), o nome do arquivo será gerado da seguinte forma:

Na geração “normal” ( 999999_CODESTAB_MM_YYYY.TXT
                                 (número do processo (opcional) + código do estabelecimento _mês + ano + “EFD”)

Na geração multiempresa ( 999999_CODEMPRESA_CODESTAB_MM_YYYY.TXT
                  (número do processo (opcional) + código da empresa + código do estabelecimento _mês + ano + “EFD”)

O procedimento é devido à possibilidade de existência de mesmo código de estabelecimento para empresas distintas. 

		RN01	“Novo tratamento para quando houver perfil por estabelecimento”

Se houver parametrização em “Perfil por estabelecimento” então o a tela de geração do SPED deverá listar apenas os estabelecimentos  associados.

Se não houver parametrização em “Perfil por estabelecimento” então o a tela de geração do SPED continuará buscando todos estabelecimentos associados à empresa, da forma como já é feito hoje. Não alterar o produto.	OS2388-A7		RN02	“Campo Data do Saldo Inicial LPD (Cotepe 41)”

O campo Data do Saldo Inicial LPD (Cotepe 41) será um campo do tipo Data, formato DD/MM/AAAA, de parametrização não obrigatória. Quando informado será considerado na geração do campo 04 – ESTQ_INI do Registro 1391 do SPED Fiscal.
	OS3736		RN03	Campo “Leiaute”

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

Alteração da MFS4992:
Incluída a nova versão de leiaute 1.10, referente ao Ato Cotepe ICMS 07/2016. Esta versão só poderá ser utilizada para períodos a partir de 01/01/2017. Assim, seguindo o padrão, caso o usuário selecione esta versão, e informe um período anterior à JAN/2017, a geração não será iniciada, e será exibida a seguinte mensagem: “Leiaute incompatível com o período dos dados a serem apresentados”.

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

	OS3838
OS3983
OS4261
OS4535
OS4609
MFS4992
MFS8017
MFS13290
MFS-20986
MFS31406
MFS45380
MFS73692
MFS85388		
RN04
	Parâmetro “Geração Multiempresa”:  (criado na OS4508)

Parâmetro do tipo checkbox
Default = desmarcado

Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado na RN06.
	OS4508		RN05	Parâmetro “UF”:                        (criado na OS4508)

Parâmetro do tipo listbox que apresenta a lista das UF’s (tabela ESTADO) + opção “Todas”.
Default = “Todas”

Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado na RN06.
 	OS4508		RN06	
Funcionamento da lista dos Estabelecimentos:

Originalmente, este campo apresentava todos os estabelecimentos da empresa do login. Se o parâmetro “Geração p/ Insc.Estadual Única” marcado, seriam considerados apenas os estabelecimentos centralizadores de I.E.U. (conforme a parametrização do módulo de controle das obrigações estaduais).  

Posteriormente, com a criação da parametrização “Perfil por Estabelecimento”, as regras originais permaneceram, e foi inserida mais uma regra, conforme descrito na RN01:

      Se existir dados na parametrização “Perfil por Estabelecimento”:
           Neste caso, passou a considerar apenas os estabelecimentos parametrizados para o perfil informado;
      Senão
           Neste caso, continuou mostrando todos os estabelecimentos;
 
Alteração da OS4508:

A partir da inclusão dos parâmetros “Geração Multiempresa” e “UF” (parâmetros criados na OS4508), a lista passou a funcionar da seguinte forma:

Se parâmetro “Geração Multiempresa” desmarcado:
 
     Na lista será demonstrado apenas o código e a razão social de cada estabelecimento (= versão original).

     Ordenação das linhas: código do estabelecimento.
     A opção “Selecionar” permite ao usuário escolher um estabelecimento, dentre os que foram disponibilizados
     para seleção.

     Serão demonstrados apenas os estabelecimentos que atendam aos seguintes critérios:

     - Estabelecimentos da empresa do login;
     - Se existir dados na parametrização “Perfil por Estabelecimento”: 
             Considera apenas os estabelecimentos parametrizados para o perfil informado;
       Senão
             Considera todos os estabelecimentos normalmente;
     - Se parâmetro “Geração p/ Insc. Estadual Única” marcado:
             Considera apenas os estabelecimentos centralizadores, de acordo com a parametrização da
             Inscrição Estadual Única do módulo de controle das obrigações estaduais;
       Senão
             Considera todos os estabelecimentos normalmente;
     - Se parâmetro “UF” <>  “Todas”:
             Considera apenas os estabelecimentos da UF informada em tela;
       Senão
             Considera todos os estabelecimentos normalmente;
   
      (esta opção equivale ao funcionamento anterior à OS4508, mas incluindo apenas o filtro por UF)
Se parâmetro “Geração Multiempresa” marcado:

     Na lista será demonstrado o código e a razão social de cada estabelecimento, e também o código e a razão social
     da empresa, com objetivo de possibilitar a identificação dos estabelecimentos:

                   XXX - XXXXXXXXXXXXXXXXXX – XXXXXX - XXXXXXXXXXXXXXXXXXXXXXXXXX
                         (cód. e razão social da empresa + cód. e razão social do estabelecimento)

     Ordenação das linhas: código da empresa + código do estabelecimento.
     A opção “Selecionar” permite ao usuário escolher uma empresa/estabelecimento, dentre os que foram
     disponibilizados para seleção.

     Serão demonstrados apenas os estabelecimentos que atendam aos seguintes critérios:

     - Estabelecimentos de todas as empresas as quais o usuário do login tenha acesso (controle User x Company do 
        Powerlock);
     - Se existir dados na parametrização “Perfil por Estabelecimento”: 
             Considera apenas os estabelecimentos parametrizados para o perfil informado;
       Senão
             Considera todos os estabelecimentos normalmente;
     - Se parâmetro “Geração p/ Insc. Estadual Única” marcado:
             Considera apenas os estabelecimentos centralizadores, de acordo com a parametrização da
             Inscrição Estadual Única do módulo de controle das obrigações estaduais;
       Senão
             Considera todos os estabelecimentos normalmente;
     - Se parâmetro “UF” <>  “Todas”:
             Considera apenas os estabelecimentos da UF informada em tela;
       Senão
             Considera todos os estabelecimentos normalmente;

Obs: No caso da geração multiempresa, as regras da geração do arquivo não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do arquivo existirão estabelecimentos de empresas distintas. Além disso, o nome do arquivo gerado terá a informação do código da empresa, como descrito na RN00. 
	OS4508		RN07	[MFS76273] Tratamento da regra para contribuintes do Distrito Federal que são prestadores de serviços e não tem apuração do ICMS.

Tratamento de mensagens de erro a serem dadas antes de iniciar a geração:

Quando o estabelecimento não tem o campo ''Tipo de Apuração do ICMS'' preenchido no cadastro do Estabelecimento (campo 71 da SAFX2064), a UF do Estabelecimento = ‘DF’ (campo 18 da SAFX2064) e o Tipo de Atividade do Estabelecimento = ‘2 – Prestador de Seviço’ (campo 70 da SAFX2064), não será exibida a mensagem de erro para o campo tipo de apuração do ICMS, pois o estabelecimento não é obrigado a ter uma apuração de ICMS gerada.

Caso contrário, será exibida a seguinte mensagem:

“Para gerar os registros do Bloco E referentes à apuração do ICMS, é necessário informar o tipo de apuração utilizada. O campo ''Tipo de Apuração do ICMS'' deve ser informado para todos os Estabelecimentos selecionados. (módulo Parâmetros, item Preliminares -> Empresa / Estabelecimento).”

Quando o estabelecimento não tem o campo ''Tipo de Apuração do IPI preenchido no cadastro do Estabelecimento (campo 71 da SAFX2064), a UF do Estabelecimento = ‘DF’ (campo 18 da SAFX2064) e o Tipo de Atividade do Estabelecimento = ‘2 – Prestador de Seviço’ (campo 70 da SAFX2064), não será exibida a mensagem de erro para o campo tipo de apuração do IPI, pois o estabelecimento não é obrigado a ter uma apuração de IPI gerada.

Caso contrário, será exibida a seguinte mensagem:

“Para gerar os registros do Bloco E referentes à apuração do IPI, é necessário informar o tipo de apuração utilizada. O campo ''Tipo de Apuração do IPI'' deve ser informado para todos os Estabelecimentos selecionados. (módulo Parâmetros, item Preliminares -> Empresa / Estabelecimento).”
	MFS76273		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN