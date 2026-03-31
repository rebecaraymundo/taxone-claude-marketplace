# MTZ-eSocial-Relatorio-Conferencia-dos-Cadastros

> Fonte: MTZ-eSocial-Relatorio-Conferencia-dos-Cadastros.docx






THOMSON REUTERS

Módulo eSocial

Relatório de Conferência da Geração dos Cadastros



Localização: Menu SPED, módulo Informações p/o eSocial, menu Relatórios  Conferência da Geração dos Cadastros


DOCUMENTO DE REQUISITO



Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4
4.	Emissão do Relatório	5
5.	Relatório do Evento S-1005 (Estabelecimentos)	6
6.	Relatório do Evento S-1010 (Rubricas)	11
7.	Relatório do Evento S-1020 (Lotações)	16
8.	Relatório do Evento S-1070 (Processos)	16



Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.











## Regras Gerais


O relatório de conferência dos cadastros é gerado a partir das tabelas auxiliares alimentadas na geração dos dados (menu Geração > Geração dos Cadastros). O objetivo é que o usuário possa conferir exatamente as informações que serão utilizadas para gerar os arquivos XML.

## Layout da Tela






Botões da barra de menu:




## Regras de Funcionamento dos Campos





## Emissão do Relatório


Será gerado um relatório para cada um dos estabelecimentos selecionados no campo “Estabelecimentos Centralizadores”.

O relatório a ser gerado será a opção escolhida pelo usuário no campo “Eventos”, observando que o campo só permite a emissão de um modelo de relatório por vez.

As regras da recuperação dos dados e o layout, dependem da opção de relatório escolhida, da seguinte forma:



## Relatório do Evento S-1005 (Estabelecimentos)


Origem dos dados: Tabelas auxiliares geradas no menu “Geração dos Cadastros”.


Recuperação dos dados: Para o relatório de cada estabelecimento selecionado em tela, os eventos serão recuperados da seguinte forma:

- Considerar todos os eventos S-1005 que tenham sido gerados previamente (no menu “Geração dos Cadastros”) para o
estabelecimento centralizador em questão;

- O mês/ano do campo iniValid (registro ideEstab) do evento deve ser >= mês/ano do Período Inicial e <= mês/ano do
Período Final informados em tela;

Layout: Vide planilha “Layout Conferência dos Cadastros”, aba “S1005-Estabelecimentos”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:




Linhas de detalhe “Informações do Estabelecimento”:





## Relatório do Evento S-1010 (Rubricas)



Origem dos dados: Tabelas auxiliares geradas no menu “Geração dos Cadastros”.


Recuperação dos dados: Para o relatório de cada estabelecimento, os eventos serão recuperados da seguinte forma:

- Considerar todos os eventos S-1010 que tenham sido gerados previamente (no menu “Geração dos Cadastros”) para o
estabelecimento centralizador em questão;

- O mês/ano do campo iniValid (registro ideRubrica) do evento deve ser >= mês/ano do Período Inicial e <= mês/ano do
Período Final informados em tela;


Layout: Vide planilha “Layout Conferência dos Cadastros”, aba “S1010-Rubricas”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:






Linhas de detalhe “Informações de Identificação da Rubrica”:





Linhas de detalhe “Informações de Processos”:

A linha com o título “Informações de Processos” será impressa apenas quando existir pelo menos um dos processos no evento da rubrica: o processo referente à Contribuição Previdenciária, ou o processo referente ao IRRF.

OBS: Como a geração dos dados dos cadastros não gera processos referentes ao FGTS e à Contribuição Sindical, os campos destes processos não são tratados no relatório, apesar de constarem no layout deste evento (como campos não obrigatórios).




## Relatório do Evento S-1020 (Lotações)



Origem dos dados: Tabelas auxiliares geradas no menu “Geração dos Cadastros”.


Recuperação dos dados: Para o relatório de cada estabelecimento, os eventos serão recuperados da seguinte forma:

- Considerar todos os eventos S-1020 que tenham sido gerados previamente (no menu “Geração dos Cadastros”) para o
estabelecimento centralizador em questão;

- O mês/ano do campo iniValid (registro ideLotacao) do evento deve ser >= mês/ano do Período Inicial e <= mês/ano do
Período Final informados em tela;


Layout: Vide planilha “Layout Conferência dos Cadastros”, aba “S1020-Lotacoes”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:




Linhas de detalhe “Informações de Identificação da Lotação”:




Linha de detalhe “Informações de Processos”:

A linha com o título “Informações de Processos” será impressa apenas quando existir o registro procJudTerceiro. Quando este registro não existir no evento, esta linha não será impressa, assim como a linha que apresenta as informações do processo.


Linha de detalhe “Informações do Operador Portuário”:

A linha com o título “Informações do Operador Portuário” será impressa apenas quando existir o registro dadosOpPort. Quando este registro não existir no evento, esta linha não será impressa, assim como a linha que apresenta as informações do processo.


## Relatório do Evento S-1070 (Processos)


Origem dos dados: Tabelas auxiliares geradas no menu “Geração dos Cadastros”.


Recuperação dos dados: Para o relatório de cada estabelecimento, os eventos serão recuperados da seguinte forma:

- Considerar todos os eventos S-1070 que tenham sido gerados previamente (no menu “Geração dos Cadastros”) para o
estabelecimento centralizador em questão;

- O mês/ano do campo iniValid (registro ideProcesso) do evento deve ser >= mês/ano do Período Inicial e <= mês/ano do
Período Final informados em tela;


Layout: Vide planilha “Layout Conferência dos Cadastros”, aba “S1070-Processos”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:




Linhas de detalhe “Informações de Identificação do Processo”:




Linhas de detalhe “Informações de Suspensão de Exigibilidade de Tributos”:

As informações sobre suspensão de exigibilidades de tributos poderão ser várias para um único processo.

Assim, para cada registro infoSusp existente no evento, será impressa uma linha destas informações.




= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS16581 | Criação do Relatório de Conferência da Geração dos Cadastros | Criação do relatório de conferência da geração dos cadastros. | 07/02/2018 |
| MFS18065 | Atualização do eSocial p/ vrs 2.4.02 | Relatório do evento S-1005: inclusão de nova opção na lista de valores do campo ”Tipo de Processo” para o Processo FAP; Relatório do evento S-1070: inclusão de nova opção na lista de valores do campo ”Tipo de Processo”, e inclusão do campo “Observação”; | 06/06/2018 |
| MFS-88128 | Elisabete Costa | Alterações para versão S1.0 Evento S-1005. | 15/06/2022 |
| MFS-88129 | Elisabete Costa | Alterações para versão S1.0 Evento S-1010. | 21/06/2022 |
| MFS-88130 | Elisabete Costa | Alterações para versão S1.0 Evento S-1020. | 22/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| ABRE | Ao clicar nesta opção, será aberta a janela dos parâmetros para emissão do relatório. |
| --- | --- |
| IMPRIME | Opção para imprimir o relatório. |
| SETAS | As setas são utilizadas para a paginação do relatório emitido. |
| FECHA | Fecha a tela da conferência. |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período Inicial | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano inicial para a emissão do relatório.  Deve ser um mês válido. |  |
| Período Final | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano final para a emissão do relatório.  Deve ser um mês válido e >= ao mês/ano inicial. |  |
| Versão  (campo retirado da tela na MFS18065) | Alfanumérico | S | N | Listbox | Este campo é uma lista, que a princípio terá apenas uma opção: [2.4.01]   MFS18065: Este campo foi retirado da tela, para que o usuário possa consultar eventos gerados em qualquer versão. |  |
| Eventos | Alfanumérico | S | N | Listbox | Este campo é uma lista onde são exibidas as opções de relatório para seleção do usuário:  S-1005 - Estabelecimentos S-1010 - Rubricas S-1020 - Lotações  S-1070 - Processos Administrativos / Judiciais  Obs: Observar que na tela da geração dos dados é possível selecionar e gerar vários eventos simultaneamente. Mas para emitir o relatório, o usuário deve selecionar um evento por vez. Por isso nesta tela o campo é uma lista. |  |
| Estabelecimentos Centralizadores | Alfanumérico | S | N | Checkbox | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão disponibilizados para seleção apenas os estabelecimentos da Empresa cadastrados na parametrização dos dados iniciais do eSocial (menu “Parâmetros > Dados Iniciais”).  (lembrando que esta parametrização só trabalha com os estabelecimentos centralizadores das obrigações federais) |  |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimento”. |  |


| Evento S-1005 | Ver item “5-Relatório do Evento S-1005” |
| --- | --- |
| Evento S-1010 | Ver item “6-Relatório do Evento S-1010” |
| Evento S-1020 | Ver item “7-Relatório do Evento S-1020” |
| Evento S-1070 | Ver item “8-Relatório do Evento S-1070” |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1005 – Estabelecimentos”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Período informado em tela para emissão do relatório (mês/ano do período inicial e final); |


| Identificador do Evento | Conteúdo do campo id do registro evtTabEstab |
| --- | --- |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| Tipo de Inscrição | Campo de preenchimento fixo = “1-CNPJ” |
| --- | --- |
| Número de Inscrição | Conteúdo do campo nrInsc do registro ideEstab |
| Validade Inicial | Mês a ano do campo iniValid do registro ideEstab, no formato MM/AAAA |
| Validade Final | Mês a ano do campo fimValid do registro ideEstab, no formato MM/AAAA |
| CNAE | Conteúdo do campo cnaePrep do registro dadosEstab |
| Alíquota RAT | Conteúdo do campo aliqRat do registro aliqGilrat, considerando apenas a posição inteira  Obs: No layout do eSocial esta alíquota é um campo numérico de apenas 1 posição. Mas nas tabelas do eSocial o campo foi criado com 4 casas decimais apenas por precaução, caso no futuro as alíquotas passem a utilizar decimais. |
| FAP | Conteúdo do campo fap do registro aliqGilrat, no formato 9,9999 |
| Alíquota após ajuste | Conteúdo do campo aliqRatAjust do registro aliqGilrat, no formato 9,9999  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| Processo RAT | Os campos do relatório referentes ao processo RAT serão preenchidos apenas quando existir o registro procAdmJudRat no evento. Caso contrário, ficarão em branco.   Tipo: Este campo é preenchido dependendo do conteúdo do campo tpProc do registro procAdmJudRat:           Se campo tpProc = 1                O campo será preenchido com “1-Administrativo”          Senão                O campo será preenchido com “2-Judicial”  Número: Conteúdo do campo nrProc do registro procAdmJudRat;  Código Indicativo da Suspensão: Conteúdo do campo codSusp do registro procAdmJudRat; |
| Regime de Ponto | Este campo é preenchido dependendo do conteúdo do campo regPt do registro infoTrab:  Se campo regPt = 0      O campo será preenchido com “0-Não utiliza”; Se campo regPt = 1      O campo será preenchido com “1-Manual”; Se campo regPt = 2      O campo será preenchido com “2-Mecânico”; Se campo regPt = 3      O campo será preenchido com “3-Eletrônico (Port. MTE 1.510/2009)”; Se campo regPt = 4      O campo será preenchido com “4-Não eletrônico alternativo (art. 1 Port. MTE 373/2011)”; Se campo regPt = 5      O campo será preenchido com “5-Eletrônico alternativo (art. 2 Port. MTE 373/2011)”; Se campo regPt = 6      O campo será preenchido com “6-Eletrônico – outros”;           Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| Processo FAP: | Os campos do relatório referentes ao processo FAP serão preenchidos apenas quando existir o registro procAdmJudFap no evento. Caso contrário, ficarão em branco.   Tipo: Este campo é preenchido dependendo do conteúdo do campo tpProc do registro procAdmJudFap:           Se campo tpProc = 1 O campo será preenchido com “1-Administrativo”           Se campo tpProc = 2  O campo será preenchido com “2-Judicial”           Se campo tpProc = 4  O campo será preenchido com “4-Processo FAP”  Número: Conteúdo do campo nrProc do registro procAdmJudFap;  Código Indicativo da Suspensão: Conteúdo do campo codSusp do registro procAdmJudFap; |
| Contratação Aprendiz | Este campo é preenchido dependendo do conteúdo do campo contApr do registro infoApr:  Se campo contApr = 0      O campo será preenchido com “0-Dispensado de acordo com a lei”; Se campo contApr = 1      O campo será preenchido com                              “1-Dispensado, mesmo que parcialmente, em virtude de processo judicial”; Se campo contApr = 2      O campo será preenchido com “Obrigado”;  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| Número Processo | Conteúdo do campo nrProcJud do registro infoApr. Caso o campo não tenha sido gerado no evento, o campo do relatório ficará em branco. |
| Entidade Educativa | Conteúdo do campo contEntEd do registro infoApr. Caso o campo não tenha sido gerado no evento, o campo do relatório ficará em branco.  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| Número Inscrição | Conteúdo do campo nrInsc do registro infoEntEduc. Caso o campo não tenha sido gerado no evento, o campo do relatório ficará em branco. |
| Contratação PCD | Conteúdo do campo contPCD do registro infoPCD. Este campo do relatório será preenchido apenas quando existir o registro infoPCD no evento. Caso contrário, ficará em branco.  Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| Número Processo | Conteúdo do campo nrProcJud do registro infoPCD. Este campo do relatório será preenchido apenas quando existir o registro infoPCD no evento, e o campo nrProcJud tiver sido gerado. Caso contrário, ficará em branco. |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1010 – Rubricas”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Período informado em tela para emissão do relatório (mês/ano do período inicial e final); |


| Identificador do Evento | Conteúdo do campo id do registro evtTabRubrica |
| --- | --- |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| Código da Rubrica | Conteúdo do campo codRubr do registro ideRubrica |
| --- | --- |
| Identificador da Tabela | Conteúdo do campo ideTabRubr do registro ideRubrica |
| Validade Inicial | Mês a ano do campo iniValid do registro ideRubrica, no formato MM/AAAA |
| Validade Final | Mês a ano do campo fimValid do registro ideRubrica, no formato MM/AAAA |
| Descrição | Conteúdo do campo dscRubr do registro dadosRubrica |
| Tipo | Este campo é preenchido dependendo do conteúdo do campo tpRubr do registro dadosRubrica:  Se campo tpRubr = 1      O campo será preenchido com “1-Vencimento” Se campo tpRubr = 2      O campo será preenchido com “2-Desconto” Se campo tpRubr = 3      O campo será preenchido com “3-Informativa” Se campo tpRubr = 4      O campo será preenchido com “4-Informativa dedutora” |
| Natureza | Este campo é preenchido com o conteúdo do campo natRubr do registro dadosRubrica, e da descrição da natureza da rubrica, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXXXXXXX).  A descrição da natureza da rubrica é recuperada da tabela “Tabela de Natureza das Rubricas da Folha de Pagamento – eSocial” (TACES64). |
| Cód.Incidência CP | Este campo é preenchido com o conteúdo do campo codIncCP do registro dadosRubrica, e da descrição do código de incidência, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXXXXXXX).  A descrição do código de incidência é recuperada da tabela “Tabela de Códigos de Incidência Tributária das Rubricas - eSocial” (TACES62).   Para recuperar o código de incidência na TACES62, considerar:  - Tipo = “1” - Código de Incidência Tributária = conteúdo do campo codIncCP |
| Cód.Incidência FGTS | Este campo é preenchido com o conteúdo do campo codIncFGTS do registro dadosRubrica, e da descrição do código de incidência, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXX).  A descrição deste código de incidência não consta na TACES62, pois este campo é gerado sempre fixo com o conteúdo “00”. Desta forma, será utilizada sempre a descrição abaixo, referente ao código “00”:                                            “00-Não é base de cálculo do FGTS” |
| Cód.Incidência IRRF | Este campo é preenchido com o conteúdo do campo codIncIRRF do registro dadosRubrica, e da descrição do código de incidência, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXX).  A descrição do código de incidência é recuperada da tabela “Tabela de Códigos de Incidência Tributária das Rubricas - eSocial” (TACES62).   Para recuperar o código de incidência na TACES62, considerar:  - Tipo = “2” - Código de Incidência Tributária = conteúdo do campo codIncIRRF |
| Cód.Incidência SIND | Este campo é preenchido com o conteúdo do campo codIncSIND do registro dadosRubrica, e da descrição do código de incidência, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXX).  A descrição deste código de incidência não consta na TACES62, pois este campo é gerado sempre fixo com o conteúdo “00”. Desta forma, será utilizada sempre a descrição abaixo, referente ao código “00”:                                              “00-Não é base de cálculo” Este campo só deve ser gerado até a versão 2.5, a partir da versão S1.0 ele não deve ser gerado. |
| Cód.Incidência CPRP | A partir da versão S1.0 foi criado o campo codIncCPRP. O mesmo não deve ser gerado, pois se trata de contribuições de regime militar Este campo é preenchido com o conteúdo do campo codIncCPRP do registro dadosRubrica, e da descrição do código de incidência, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXX).  Para recuperar o código de incidência na TACES62, considerar:  - Tipo = “1” - Código de Incidência Tributária = conteúdo do campo codIncIRRF |
| Teto Remunatório | A partir da versão S1.0 foi criado o campo tetoRemun. O mesmo não deve ser gerado, pois é obrigatório se a natureza jurídica do declarante for Administração Pública (grupo [1])  Este campo é preenchido com o conteúdo do campo tetoRemun do registro dadosRubrica. |
| Observação | Conteúdo do campo observação do registro dadosRubrica |


| Processo CP | Esta linha será impressa apenas quando existir no evento o registro ideProcessoCP.  Tipo: Este campo é preenchido dependendo do conteúdo do campo tpProc do registro ideProcessoCP:       Se campo tpProc = 1            O campo será preenchido com “1-Administrativo”      Senão            O campo será preenchido com “2-Judicial”  Número: Conteúdo do campo nrProc do registro ideProcessoCP;  Extensão da Decisão: Este campo é preenchido dependendo do conteúdo do campo extDecisao do                                       registro ideProcessoCP:     Se campo extDecisao = 1       O campo será preenchido com “1-Contribuição Previdenciária Patronal”    Senão       O campo será preenchido com “2-Contribuição Previdenciária Patronal + Descontada dos Segurados”   Cód. do Indicativo de Suspensão: Conteúdo do campo codSusp do registro ideProcessoCP; |
| --- | --- |
| Processo IRRF | Esta linha será impressa apenas quando existir no evento o registro ideProcessoIRRF.  Número: Conteúdo do campo nrProc do registro ideProcessoIRRF;  Cód. do Indicativo de Suspensão: Conteúdo do campo codSusp do registro ideProcessoIRRF; |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1020 – Lotações”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Período informado em tela para emissão do relatório (mês/ano do período inicial e final); |


| Identificador do Evento | Conteúdo do campo id do registro evtTabLotacao |
| --- | --- |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| Código da Lotação | Conteúdo do campo codLotacao do registro ideLotacao |
| --- | --- |
| Validade Inicial | Mês a ano do campo iniValid do registro ideLotacao, no formato MM/AAAA |
| Validade Final | Mês a ano do campo fimValid do registro ideLotacao, no formato MM/AAAA |
| Tipo de Lotação | Este campo é preenchido com o conteúdo do campo tpLotacao do registro dadosLotacao, e da descrição do tipo de lotação, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXXXXXXX).  As descrições do tipo de lotação são as seguintes (a lista apresenta as 14 opções da “Tabela 10 - Tipos de Lotação Tributária” do eSocial):  (quando não existir a informação do campo  tpLotacao, o campo do relatório ficará em branco)   01-Classificação da atividade econômica exercida pela PJ p/ fins de atribuição de código FPAS 02-Obra de Construção Civil - Empreitada Parcial ou Sub-empreitada 03-PF tomadora de serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa 04-PJ tomadora de serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa 05-PJ tomadora de serviços prestados por cooperados por intermédio de cooperativa de trabalho 06-Entidade benefic./isenta tomadora de serviços prestados p/cooperados p/intermédio de coop. de trabalho 07- PF tomadora de serviços prestados por cooperados por intermédio de cooperativa de trabalho 08-Operador Portuário tomador de serviços de trabalhadores avulsos 09-Contratante de trabalhadores avulsos não portuários por intermédio de Sindicato 10-Embarcação inscrita no Registro Especial Brasileiro - REB  21-Classificação da atividade econômica ou obra própria de construção civil da PF 24-Empregador Doméstico  90-Atividades desenvolvidas no exterior por trabalhador vinculado ao Reg Geral de Previd Social (expatriados) 91-Atividades desenvolvidas por trabalhador estrangeiro vinculado a Reg de Previd. Social Estrangeiro |
| Tipo de Inscrição | Este campo é preenchido dependendo do conteúdo do campo tpInsc do registro dadosLotacao:  Se campo tpInsc = “1”      O campo será preenchido com “1-CNPJ”; Se campo tpInsc = “2”      O campo será preenchido com “2-CPF”; Se campo tpInsc = “4”      O campo será preenchido com “4-CNO”;  Caso a informação deste campo não exista no evento, o campo do relatório ficará em branco. |
| Número de Inscrição | Conteúdo do campo nrInsc do registro dadosLotacao. |
| Cód. FPAS | Conteúdo do campo fpas do registro fpasLotacao. |
| Cód. Terceiros | Conteúdo do campo codTercs do registro fpasLotacao. |
| Cód. Combinado de Terceiros (Recolhimento Suspenso) | Conteúdo do campo codTercsSusp do registro fpasLotacao. |


| Código Terceiro | Conteúdo do campo codTerc do registro procJudTerceiro |
| --- | --- |
| Número | Conteúdo do campo nrProcJud do registro procJudTerceiro |
| Cód. do Indicativo de Suspensão | Conteúdo do campo codSusp do registro procJudTerceiro |


| Alíquota RAT | Conteúdo do campo aliqRat do registro dadosOpPort |
| --- | --- |
| Fator Acidentário de Prevenção | Conteúdo do campo fap do registro dadosOpPort |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1070 – Processos”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Período informado em tela para emissão do relatório (mês/ano do período inicial e final); |


| Identificador do Evento | Conteúdo do campo id do registro evtTabProcesso |
| --- | --- |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| Tipo | Este campo é preenchido dependendo do conteúdo do campo tpProc do registro ideProcesso:           Se campo tpProc = 1 O campo será preenchido com “1-Administrativo”           Se campo tpProc = 2  O campo será preenchido com “2-Judicial”           Se campo tpProc = 4  O campo será preenchido com “4-Processo FAP” |
| --- | --- |
| Número | Conteúdo do campo nrProc do registro ideProcesso |
| Validade Inicial | Mês a ano do campo iniValid do registro ideProcesso, no formato MM/AAAA |
| Validade Final | Mês a ano do campo fimValid do registro ideProcesso, no formato MM/AAAA |
| Autoria | Este campo é preenchido dependendo do conteúdo do campo indAutoria do registro dadosProc:  Se campo indAutoria = 1      O campo será preenchido com “1-Próprio Contribuinte” Senão      O campo será preenchido com “2-Outra Entidade, Empresa ou Empregado”  Caso a informação deste campo não exista no evento, o campo do relatório ficará em branco. |
| Matéria do Processo | Este campo é preenchido com o conteúdo do campo indMatProc do registro dadosProc, e da descrição do indicativo da matéria, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXXXXXXX).  As descrições do indicativo da matéria são as seguintes (conforme vrs 2.4.01 do eSocial):  (quando não existir a informação do campo  indMatProc, o campo do relatório ficará em branco)  01 - Tributária  02 - Autorização de trabalho de menor 03 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD)  04 - Dispensa, ainda que parcial, de contratação de aprendiz  05 - Segurança e Saúde do Trabalho  06 - Conversão de Licença Saúde em Acidente de Trabalho  07 - FGTS  08 - Contribuição sindical  99 - Outros assuntos |
| UF Vara | Conteúdo do campo UfVara do registro dadosProcJud |
| Município | Conteúdo do campo codMunic do registro dadosProcJud |
| Código de Identificação da Vara | Conteúdo do campo idVara do registro dadosProcJud |
| Observação | Conteúdo do campo observacao do registro dadosProc |


| Código do Indicativo da Suspensão | Conteúdo do campo codSusp do registro infoSusp |
| --- | --- |
| Indicativo de Suspensão | Este campo é preenchido com o conteúdo do campo indSusp do registro infoSusp, e da descrição do indicativo de suspensão, conforme formato do layout (9999-XXXXXXXXXXXXXXXXXXXXXXXXXXX).  As descrições do indicativo de suspensão são as seguintes (conforme vrs 2.4.01 do eSocial):  (quando não existir a informação do campo  indSusp, o campo do relatório ficará em branco)  01 - Liminar em Mandado de Segurança 02 - Depósito Judicial do Montante Integral 03 - Depósito Administrativo do Montante Integral 04 - Antecipação de Tutela 05 - Liminar em Medida Cautelar 08 - Sentença em Mandado de Segurança Favorável ao Contribuinte 09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF 10 - Acórdão do TRF Favorável ao Contribuinte 11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte 12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte 13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo 14 - Contestação Administrativa FAP  90 - Decisão Definitiva a favor do contribuinte 92 - Sem suspensão da exigibilidade |
| Data da Decisão | Data do campo dtDecisão do registro infoSusp, no formato DD/MM/AAAA |
| Indicativo de Depósito | Conteúdo do campo indDeposito do registro infoSusp |
