# MTZ-eSocial-Relatorio-Conferencia-dos-Movimentos

> Fonte: MTZ-eSocial-Relatorio-Conferencia-dos-Movimentos.docx



THOMSON REUTERS

Módulo eSocial

Relatório de Conferência da Geração dos Movimentos


Localização: Menu SPED, módulo Informações p/o eSocial, menu Relatórios  Conferência da Geração dos Movimentos


DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	3
4.	Emissão do Relatório	5
5.	Relatório do Evento S-1200 (Remuneração de Trabalhador)	6
6.	Relatório do Evento S-1210 (Pagamentos de Rendimentos do Trabalho)	12
7.	Relatório do Evento S-1300 (Contribuição Sindical Patronal)	18
8.	Relatório do Evento S-1250 (Aquisição de Produção Rural)	20



Devido ao end-of-support da mensageria OS E-Social, e a não utilização de clientes no Tax One integrados, o módulo Informações para o E-Social será retirado do TAX ONE e deverá permanecer no DW.












## Regras Gerais


O relatório de conferência dos movimentos é gerado a partir das tabelas auxiliares alimentadas na geração dos dados (menu Geração > Geração dos Movimentos). O objetivo é que o usuário possa conferir exatamente as informações que serão utilizadas para gerar os arquivos XML.


## Layout da Tela


[MFS26046] – Inclusão da opção Situação que irá filtrar as possibilidades do status da ocorrência. Se for pesquisada apenas uma situação irá mostrar a data de ocorrência maior dessa situação. Caso seja pesquisada mais de uma será apresentada a maior dessas escolhidas





Botões da barra de menu:




## Regras de Funcionamento dos Campos







## Emissão do Relatório


Será gerado um relatório para cada um dos estabelecimentos selecionados no campo “Estabelecimentos Centralizadores”.

O relatório a ser gerado será a opção escolhida pelo usuário no campo “Evento”, observando que o campo só permite a emissão de um modelo de relatório por vez.

[MFS20751]
[MFS-87292]

A partir da versão S-1.0 não devem ser exibidos os eventos S-1250 e S-1300

## Relatório do Evento S-1200 (Remuneração de Trabalhador)


Origem dos dados: Tabelas auxiliares geradas no menu “Geração dos Movimentos”.


Recuperação dos dados: Para o relatório de cada estabelecimento, os eventos serão recuperados da seguinte forma:

[MFS26046]
- Considera  o último evento S-1200 que tenha sido gerado previamente (no menu “Geração dos Movimentos”) para o estabelecimento centralizador em questão, com a situação escolhida pelo usuário, caso mais de uma situação seja escolhida irá mostrar a mais atual.

- O mês/ano do campo perApur (registro ideEvento) do evento deve ser = mês/ano do Período informado em tela;


Layout: Vide planilha “Layout Conferência dos Movimentos”, aba “S1200-Remuneracao Trabalhador”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:




Linha de detalhe “Informações de Identificação do Trabalhador”:




Linhas de detalhe “Remuneração Outras Empresas”:

A linha com o título “Remuneração Outras Empresas” será impressa apenas quando existir pelo menos um registro remunOutrEmpr no evento.

No evento S-1200 pode existir nenhuma, ou várias ocorrências do registro remunOutrEmpr.

Assim, para cada registro remunOutrEmpr existente, será impressa uma linha destas informações.





Linhas de detalhe “Informações Complementares do Trabalhador / Informações Complementares Contratuais ”:

MTZ18065: Como na versão 2.4.02 os campos do registro “infoComplem” (nome, data nascimento, cód. CBO e Natureza da Atividade) foram subdivididos em dois registros diferentes (infoComplem e infoComplCont), o relatório será alterado apenas para mudar o título da linha fazendo referência aos dois registros;



Linhas de detalhe “Informações de Processos”:

A linha com o título “Informações de Processos” será impressa apenas quando existir pelo menos um registro procJudTrab no evento.

No evento S-1200 pode existir nenhuma, ou várias ocorrências do registro procJudTrab.

Assim, para cada registro procJudTrab existente, será impressa uma linha destas informações.




Linhas de detalhe “Demonstrativos de Pagamento do Período”:

Sob este título serão exibidos todos os demonstrativos de pagamento existentes no evento em questão.

Poderão existir ‘n’ demonstrativos (‘n’ registros dmDev) num único evento.

Para cada demonstrativo, será impresso:

- Uma linha com o código identificador do demonstrativo, a categoria do trabalhador e a lotação;
- A seguir, as rubricas referentes ao demonstrativo em questão (registro itensRemun);





## Relatório do Evento S-1210 (Pagamentos de Rendimentos do Trabalho)



Origem dos dados: Tabelas auxiliares geradas no menu “Geração dos Movimentos”.


Recuperação dos dados: Para o relatório de cada estabelecimento, os eventos serão recuperados da seguinte forma:

[MFS26046]
- Considerar  o último evento S-1210 que tenha sido gerado previamente (no menu “Geração dos Movimentos”) para o
estabelecimento centralizador em questão, com a situação escolhida pelo usuário, caso mais de uma situação seja escolhida irá mostrar a mais atual.



- O mês/ano do campo perApur (registro ideEvento) do evento deve ser = mês/ano do Período informado em tela;


Layout: Vide planilha “Layout Conferência dos Movimentos”, aba “S1210-Pagamentos do Período”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:




Linha de detalhe “Beneficiário do Pagamento”:






Nas linhas seguintes serão demonstrados todos os pagamentos existentes no evento (registro infoPgto), agrupados pela data de pagamento e tipo do pagamento.

Para cada data e tipo de pagamento existente no evento (ou seja, para cada registro infoPgto), será impressa uma linha com os campos “Data de Pagamento”, “Tipo” e “Residente no Brasil”.

Linha da data e tipo de pagamento:



Linha dos dados de identificação do demonstrativo:

A seguir serão demonstrados todos os demonstrativos para os quais houve pagamento, e para cada demonstrativo, as retenções efetuadas no ato do pagamento, conforme layout do relatório.
[MFS-87306]


Linha dos valores das retenções efetuadas no ato de pagamento:
[MFS-87306]
Esta linha e seus campos só devem ser gerados até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado.

Estes dados aparecem sob o título

“Retenções efetuadas no ato do pagamento pelo valor XXXXX (XXXXXXXXXXX)”

Onde “XXXXX (XXXXXXXXXXX)” é um conteúdo variável, dependendo do tipo de pagamento (campo “Tipo” da linha que mostra a data do pagamento), da seguinte forma:

- Para pagamento total, o título será = “Retenções efetuadas no ato do pagamento pelo valor total (registro retPgtoTot)”

- Para pagamento parcial, o título será = “Retenções efetuadas no ato do pagamento pelo valor parcial (registro infoPgtoParc)”

As informações das retenções ficam em registros diferentes no evento S-1210, o que depende, também, do tipo de pagamento (campo “Tipo” da linha que mostra a data do pagamento), da seguinte forma:

- Para pagamento total, as linhas das retenções efetuadas serão preenchidas a partir do registro retPgtoTot;

- Para pagamento parcial, as linhas das retenções efetuadas serão preenchidas a partir do registro infoPgtoParc;


Linha de detalhe “Informações complementares de pagamentos a beneficiários do exterior”
[MFS-87306]
Esta linha e seus campos só devem ser gerados até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado.

As linhas referentes às informações de pagamentos efetuados a beneficiário do exterior, serão impressas no relatório apenas quando existir no evento o registro idePais. Caso contrário, estas linhas não aparecerão, inclusive a linha do título (“Informações complementares de pagamentos a beneficiários do exterior”) também não será gerada.




## Relatório do Evento S-1300 (Contribuição Sindical Patronal)



Origem dos dados: Tabelas auxiliares geradas no menu “Geração dos Movimentos”.


Recuperação dos dados: Para o relatório de cada estabelecimento, os eventos serão recuperados da seguinte forma:

A partir da versão S-1.0 este registro não será mais gerado, portanto não haverá dados para geração do relatório.
[MFS-87306]


[MFS26046]
- Considerar o último evento S-1300 que tenha sido gerado previamente (no menu “Geração dos Movimentos”) para o estabelecimento centralizador em questão, com a situação escolhida pelo usuário, caso mais de uma situação seja escolhida irá mostrar a mais atual.

- O mês/ano do campo perApur (registro ideEvento) do evento deve ser = mês/ano do Período informado em tela;


Layout: Vide planilha “Layout Conferência dos Movimentos”, aba “S1300-Contribuicoes Sindicais”.


Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:




Linha de detalhe “Informações da Contribuição Sindical”:

Será impressa uma linha desse tipo para cada contribuição sindical existente no evento (registro contribSind).


[MFS20751]
[MFS-87292]

## Relatório do Evento S-1250 (Aquisição de Produção Rural)


Origem dos dados: Tabelas auxiliares geradas no menu “Geração do Evento S-1250”.

A partir da versão S-1.0 este registro não será mais gerado, portanto não haverá dados para geração do relatório.

Recuperação dos dados: Para o relatório de cada estabelecimento, os eventos serão recuperados da seguinte forma:

[MFS26046]
- Considerar  o último evento S-1250 que tenha sido gerado previamente (no menu “Geração do Evento S-1250”) para o estabelecimento em questão, com a situação escolhida pelo usuário, caso mais de uma situação seja escolhida irá mostrar a mais atual.


- O mês/ano do campo perApur (registro ideEvento) do evento deve ser = mês/ano do Período informado em tela;

Layout: Vide planilha “Layout Conferência dos Movimentos”, aba “S1250-Aquisicao de Prod Rural”.

Preenchimento dos campos do relatório:


Linhas do cabeçalho:



Linhas de detalhe “Informações de Identificação do Evento e do Empregador”:




Linha de detalhe “Identificação do estabelecimento adquirente da produção”:




Linha de detalhe “Aquisição de Produção Rural”:

Será impressa uma linha desse tipo para cada tipo de aquisição existente no evento (registro tpAquis).




Linhas de detalhe “Identificação dos produtores rurais dos quais foi efetuada aquisição da produção pelo contribuinte declarante”:

A linha com o título “Identificação dos produtores rurais dos quais foi efetuada aquisição da produção pelo contribuinte declarante” será impressa de acordo com o registro tpAquis do evento.

Poderão existir uma ou várias ocorrências do registro ideProdutor para cada registro tpAquis.

Assim, para cada registro ideProdutor existente, será impressa uma linha destas informações.



Linhas de detalhe “Detalhamento das notas fiscais relativas a aquisição de produção do produtor rural”:

A linha com o título “Detalhamento das notas fiscais relativas a aquisição de produção do produtor rural” será impressa apenas quando existir pelo menos um registro nfs no evento.

No evento S-1250 pode existir nenhuma, ou várias ocorrências do registro nfs.

Assim, para cada registro nfs existente, será impressa uma linha destas informações.




Linhas de detalhe “Processo judicial com decisão/sentença determinado a não retenção, pelo adquirente, das contribuições incidentes sobre a aquisição de produção”:

A linha com o título “Processo judicial com decisão/sentença determinado a não retenção, pelo adquirente, das contribuições incidentes sobre a aquisição de produção” será impressa apenas quando existir pelo menos um registro infoProcJud no evento.

No evento S-1250 pode existir nenhuma, ou até 10 ocorrências do registro infoProcJud.

Assim, para cada registro infoProcJud existente, será impressa uma linha destas informações.





= = = = = =



| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS16742 | Criação do Relatório de Conferência da Geração dos Movimentos | Criação do relatório de conferência da geração dos movimentos. | 20/02/2018 |
| MFS18065 | Atualização do eSocial para versão 2.4.02. | Atualizações da versão 2.4.02. | 07/06/2018 |
| MFS20751 | Lara Aline | Inclusão geração do evento S-1250. | 29/08/2018 |
| MFS26046 | Cibele Siqueira Eduardo Cruz | Atualização para a geração do relatório apenas do último evento válido da situação da ocorrência escolhida | 10/04/2019 25/04/2019 |
| MFS-87292 | Elisabete Costa | Alterações para a Versão S-1.0 Evento S-1200 e Exclusão dos eventos S-1250 e S-1300 para a versão S-1.0 | 06/06/2022 |
| MFS-87306 | Elisabete Costa | Alterações para a Versão S-1.0 Evento S-1210 e Exclusão dos eventos S-1250 e S-1300 para a versão S-1.0 | 06/06/2022 |
| MFS-96008 | Elisabete Costa | Retirada do Módulo: Informações para o E-Social do T1 | 04/11/2022 |


| ABRE | Ao clicar nesta opção, será aberta a janela dos parâmetros para emissão do relatório. |
| --- | --- |
| IMPRIME | Opção para imprimir o relatório. |
| SETAS | As setas são utilizadas para a paginação do relatório emitido. |
| FECHA | Fecha a tela da conferência. |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Neste campo será informado o período (mês e ano) para a emissão do relatório.  Deve ser um mês válido. |  |
| Versão  (campo retirado da tela na MFS18065) | Alfanumérico | S | N | Listbox | Este campo é uma lista, que a princípio terá apenas uma opção: [2.4.01]   MFS18065: Este campo foi retirado da tela, para que o usuário possa consultar eventos gerados em qualquer versão. |  |
| Evento | Alfanumérico | S | N | Listbox | [MFS-87292] Este campo é uma lista onde são exibidas as opções de relatório para seleção do usuário:  S-1200 – Remuneração de Trabalhador  vinculado ao                   Regime Geral de Previd. Social S-1210 – Pagamentos de Rendimentos do Trabalho S-1250 – Aquisição de Produção Rural S-1300 – Contribuição Sindical Patronal A partir da versão S-1.0 não devem ser exibidos os eventos S-1250 e S-1300 Obs: Observar que na tela da geração dos dados é possível selecionar e gerar vários eventos simultaneamente. Mas para emitir o relatório, o usuário deve selecionar um evento por vez. Por isso nesta tela o campo é uma lista. | MFS20751 |
| Estabelecimentos Centralizadores | Alfanumérico | S | N | Checkbox | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão disponibilizados para seleção apenas os estabelecimentos da Empresa cadastrados na parametrização dos dados iniciais do eSocial (menu “Parâmetros > Dados Iniciais”).  (lembrando que esta parametrização só trabalha com os estabelecimentos centralizadores das obrigações federais)  [MFS20750] [MFS-87292] Caso no campo Evento for selecionado o evento S-1250 - Aquisição de Produção Rural: A partir da versão S-1.0 não devem ser exibidos os eventos S-1250  Serão disponibilizados para seleção todos os estabelecimentos da Empresa, que possuam vinculo de centralização com os estabelecimentos centralizadores cadastrados na parametrização dos dados iniciais do eSocial (menu “Parâmetros > Dados Iniciais”).   (Nesse caso está parametrização trabalhará com os estabelecimentos centralizadores e os estabelecimentos centralizados nesses centralizadores nas obrigações federais.) |  |
| Marcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimento”. |  |


| Evento S-1200 | Ver item “5-Relatório do Evento S-1200” |
| --- | --- |
| Evento S-1210 | Ver item “6-Relatório do Evento S-1210” |
| Evento S-1250 | Ver item “8-Relatório do Evento S-1250” |
| Evento S-1300 | Ver item “7-Relatório do Evento S-1300” |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1200”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Descrição do evento (“Remuneração do Trabalhador”) + período informado em tela para emissão do relatório (mês/ano); |


| Identificador do Evento | Conteúdo do campo id do registro evtRemun |
| --- | --- |
| Ind.Retificação | Este campo é preenchido dependendo do conteúdo do campo indRetif do registro ideEvento:  Se campo indRetif = “1”      O campo será preenchido com “1-Arquivo Original” Senão      O campo será preenchido com “2-Arquivo de Retificação” |
| N.Recibo (Arq.Retificado) | Conteúdo do campo nrRecibo do registro ideEvento |
| Período | Campo de preenchimento fixo = “1-Mensal” |
| Mês/Ano | Mês e ano do campo perApur do registro ideEvento (no formato MM/AAAA) |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| CPF | Conteúdo do campo cpfTrab do registro ideTrabalhador |
| --- | --- |
| NIS | Conteúdo do campo nisTrab do registro ideTrabalhador Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. |
| Indicador de desconto da contribuição previdenciária | Este campo é preenchido dependendo do conteúdo do campo indMV do registro infoMV:  Se campo indMV = 1      O campo será preenchido com “1-Contribuição descontada pelo primeiro empregador” Se campo indMV = 2      O campo será preenchido com “2-Contribuição descontada por outra(s) empresa(s) sobre valor inferior      ao limite máximo do salário de contribuição” Se campo indMV = 3      O campo será preenchido com “3-Contribuição sobre o limite máximo de salário de contribuição já       descontada em outra(s) empresa(s)” |


| Tipo | Este campo é preenchido dependendo do conteúdo do campo tpInsc do registro remunOutrEmpr:  Se campo tpInsc = “1”      O campo será preenchido com “1-CNPJ” Senão      O campo será preenchido com “2-CPF” |
| --- | --- |
| Número | Conteúdo do campo nrInsc do registro remunOutrEmpr |
| Cód.Categoria do Trabalhador | Conteúdo do campo codCateg do registro remunOutrEmpr |
| Remuneração | Conteúdo do campo vlrRemunOE do registro remunOutrEmpr |


| Nome | Conteúdo do campo nmTrab do registro infoComplem |
| --- | --- |
| Nascimento | Conteúdo do campo dtNascto do registro infoComplem |
| Cód.CBO | Conteúdo do campo codCBO do registro infoComplem |
| Natureza  Atividade | Este campo é preenchido dependendo do conteúdo do campo natAtividade do registro infoComplem:  Se campo natAtividade = “1”      O campo será preenchido com “1-Trabalho Urbano” Senão      O campo será preenchido com “2-Trabalho Rural” |


| Abrangência | Este campo é preenchido dependendo do conteúdo do campo tpTrib do registro procJudTrab:  Se campo tpTrib = “1”      O campo será preenchido com “1-IRRF” Se campo tpTrib = “2”      O campo será preenchido com “2- Contribuições sociais do trabalhador” Se campo tpTrib = “3”      O campo será preenchido com “3-FGTS” Se campo tpTrib = “4”      O campo será preenchido com “4- Contribuição sindical”  [MFS-87292] Obs: Se o campo tpTrib na tabela auxiliar estiver nulo, o campo no relatório ficará em branco. |
| --- | --- |
| Número | Conteúdo do campo nrProcJud do registro procJudTerceiro |
| Cód. do Indicativo de Suspensão | Conteúdo do campo codSusp do registro procJudTerceiro |


| Ident.Demonstrativo | Conteúdo do campo idDmDev do registro dmDev |
| --- | --- |
| Cód. Categoria do Trabalhador | Conteúdo do campo codCateg do registro dmDev |
| Cód. Lotação | Conteúdo do campo codLotacao do registro ideEstabLot |
| Tipo Inscrição | Este campo é preenchido dependendo do conteúdo do campo tpInsc do registro ideEstabLot:  Se campo tpInsc = “1”      O campo será preenchido com “1-CNPJ” Se campo tpInsc = “2”      O campo será preenchido com “2-CPF” Se campo tpInsc = “3”      O campo será preenchido com “3-CAEPF” Se campo tpInsc = “4”      O campo será preenchido com “4-CNO” [MFS-87292] |
| N. Inscrição | Conteúdo do campo nrInsc do registro ideEstabLot |
| Rubricas | Para cada rubrica do demonstrativo, será impressa uma linha com os seguintes dados:   - Código: conteúdo do campo codRubr do registro itensRemun; - Tabela: conteúdo do campo ideTabRubr do registro itensRemun; - Qtd.Refer.: conteúdo do campo qtdRubr do registro itensRemun; - Fator: conteúdo do campo fatorRubr do registro itensRemun; - Valor Unitário: conteúdo do campo vrUnit do registro itensRemun; (Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado.) - Tipo de apuração de IR: conteúdo do campo indApurIR do registro itensRemun; (Este campo só deve ser gerado a partir da versão S-1.0.) - Valor Total: conteúdo do campo vrRubr do registro itensRemun; [MFS-87306] |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1210”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Descrição do evento (“Pagamentos de Rendimentos do Trabalho”) + período informado em tela para emissão do relatório (mês/ano); |


| Identificador do Evento | Conteúdo do campo id do registro evtPgtos |
| --- | --- |
| Ind.Retificação | Este campo é preenchido dependendo do conteúdo do campo indRetif do registro ideEvento:  Se campo indRetif = “1”      O campo será preenchido com “1-Arquivo Original” Senão      O campo será preenchido com “2-Arquivo de Retificação” |
| N.Recibo (Arq.Retificado) | Conteúdo do campo nrRecibo do registro ideEvento |
| Período | Campo de preenchimento fixo = “1-Mensal” |
| Mês/Ano | Mês e ano do campo perApur do registro ideEvento (no formato MM/AAAA) |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| CPF | Conteúdo do campo cpfBenef do registro ideBenef |
| --- | --- |
| Valor da dedução da base de cálculo do IRRF relativo aos dependentes | Conteúdo do campo vrDedDep do registro deps Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. |


| Data do Pagamento | Conteúdo do campo dtPgto do registro infoPgto |
| --- | --- |
| Tipo | Este campo é preenchido dependendo do conteúdo do campo tpPgto do registro infoPgto:  Se campo tpPgto = 1      O campo será preenchido com “1-Pagamento de remuneração, conforme apurado em {dmDev} do S-1200”; Se campo tpPgto = 2      O campo será preenchido com “2-Pagamento de verbas rescisórias conforme apurado em {dmDev} do S-2299”; Se campo tpPgto = 3      O campo será preenchido com “3-Pagamento de verbas rescisórias conforme apurado em {dmDev} do S-2399”; Se campo tpPgto = 5      O campo será preenchido com “5-Pagamento de remuneração conforme apurado em {dmDev} do S-1202”; Se campo tpPgto = 6      O campo será preenchido com “6-Pagamento de Benefícios Previdenciários, conforme apurado em {dmDev} do       S-1207”; Se campo tpPgto = 7      O campo será preenchido com “7-Recibo de férias”; Se campo tpPgto = 9      O campo será preenchido com “9-Pagamento relativo a competências anteriores ao início de obrigatoriedade dos       eventos periódicos para o contribuinte”; |
| Residente no Brasil | Conteúdo do campo indResBr do registro infoPgto Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. [MFS-87306] |


| Competência | Mês e ano do campo perRef do registro detPgtoFl(para versão até 2.5) ou infoPgto (a partir da versão S-1.0) (no formato MM/AAAA) |
| --- | --- |
| Identificador do Demonstrativo | Conteúdo do campo ideDmDev do registro detPgtoFl(para versão até 2.5) ou infoPgto (a partir da versão S-1.0) |
| Pagamento Total | Conteúdo do campo indPgtoTt do registro detPgtoFl Este campo só deve ser gerado até a versão 2.5, a partir da versão S-1.0 ele não deve ser gerado. |
| Valor Líquido | Conteúdo do campo vrLiq do registro detPgtoFl(para versão até 2.5) ou infoPgto (a partir da versão S-1.0) |


| Código | Conteúdo do campo codRubr do registro retPgtoTot ou infoPgtoParc (conforme regra acima) |
| --- | --- |
| Tabela | Conteúdo do campo ideTabRubr do registro retPgtoTot ou infoPgtoParc (conforme regra acima) |
| Qtd.Refer | Conteúdo do campo qtdRubr do registro retPgtoTot ou infoPgtoParc (conforme regra acima) |
| Fator | Conteúdo do campo fatorRubr do registro retPgtoTot ou infoPgtoParc (conforme regra acima) |
| Valor Unitário | Conteúdo do campo vrUnit do registro retPgtoTot ou infoPgtoParc (conforme regra acima) |
| Valor Total | Conteúdo do campo vrRubr do registro retPgtoTot ou infoPgtoParc (conforme regra acima) |


| País | Conteúdo do campo codPais do registro idePais, concatenado com a descrição do país (tabela dos países), no formato XXX-XXXXXXXXXXXXXXXXXXXX |
| --- | --- |
| Indicativo NIF | Este campo é preenchido dependendo do conteúdo do campo indNIF do registro idePais:  Se campo indNIF = 1      O campo será preenchido com “1-Beneficiário com NIF”; Se campo indNIF = 2      O campo será preenchido com “2-Beneficiário dispensado do NIF”; Se campo indNIF = 3      O campo será preenchido com “3-País não exige NIF”;  Obs: Se o campo indNIF na tabela auxiliar estiver nulo, o campo no relatório ficará em branco. |
| NIF | Conteúdo do campo nifBenef do registro idePais |
| Logradouro | Conteúdo do campo dscLograd do registro endExt |
| Número | Conteúdo do campo nrLograd do registro endExt |
| Complemento Logradouro | Conteúdo do campo complem do registro endExt |
| Bairro | Conteúdo do campo bairro do registro endExt |
| Cidade | Conteúdo do campo nmCid do registro endExt |
| CEP | Conteúdo do campo codPostal do registro endExt |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1300”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Descrição do evento (“Contribuição Sindical Patronal”) + período informado em tela para emissão do relatório (mês/ano); |


| Identificador do Evento | Conteúdo do campo id do registro evtRemun |
| --- | --- |
| Ind.Retificação | Este campo é preenchido dependendo do conteúdo do campo indRetif do registro ideEvento:  Se campo indRetif = “1”      O campo será preenchido com “1-Arquivo Original” Senão      O campo será preenchido com “2-Arquivo de Retificação” |
| N.Recibo (Arq.Retificado) | Conteúdo do campo nrRecibo do registro ideEvento |
| Período | Campo de preenchimento fixo = “1-Mensal” |
| Mês/Ano | Mês e ano do campo perApur do registro ideEvento (no formato MM/AAAA) |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| CNPJ da Entidade Sindical | Conteúdo do campo cnpjSindic do registro contribSind |
| --- | --- |
| Tipo de Contribuição | Este campo é preenchido dependendo do conteúdo do campo tpContribSind do registro contribSind:  Se campo tpContribSind = 1      O campo será preenchido com “1-Contribuição Sindical Compulsória” Se campo tpContribSind = 2      O campo será preenchido com “2-Contribuição Associativa” Se campo tpContribSind = 3      O campo será preenchido com “3-Contribuição Assistencial” Se campo tpContribSind = 4      O campo será preenchido com “4-Contribuição Confederativa” |
| Valor da Contribuição | Conteúdo do campo vlrContribSind do registro contribSind |


| Primeira linha | Razão social da empresa; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Código e razão social do estabelecimento centralizador em questão; Título do relatório (“Relatório de Conferência do Evento S-1250”); Inscrição estadual do estabelecimento centralizador em questão; CNPJ do estabelecimento centralizador em questão; |
| Terceira linha | Descrição do evento (“Aquisição de Produção Rural”) + período informado em tela para emissão do relatório (mês/ano); |


| Identificador do Evento | Conteúdo do campo id do registro evtRemun |
| --- | --- |
| Ind.Retificação | Este campo é preenchido dependendo do conteúdo do campo indRetif do registro ideEvento:  Se campo indRetif = “1”      O campo será preenchido com “1-Arquivo Original” Senão      O campo será preenchido com “2-Arquivo de Retificação” |
| N.Recibo (Arq.Retificado) | Conteúdo do campo nrRecibo do registro ideEvento |
| Período | Campo de preenchimento fixo = “1-Mensal” |
| Mês/Ano | Mês e ano do campo perApur do registro ideEvento (no formato MM/AAAA) |
| Ambiente | Este campo é preenchido dependendo do conteúdo do campo tpAmb do registro ideEvento:  Se campo tpAmb = 1      O campo será preenchido com “1-Produção” Senão      O campo será preenchido com “2-Produção Restrita” |
| Processo de Emissão | Campo de preenchimento fixo = “1-Aplicativo do Empregador” |
| Versão | Conteúdo do campo verProc do registro ideEvento |
| Dados do Empregador | Tipo de Inscrição: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição: conteúdo do campo nrInsc do registro ideEmpregador; |


| Dados do Adquirente | Tipo de Inscrição do adquirente: campo de preenchimento fixo = “1-CNPJ”;  Número de Inscrição do adquirente: conteúdo do campo nrInscAdq do registro ideEstabAdquir; |
| --- | --- |


| Indicativo da Aquisição | Este campo é preenchido dependendo do conteúdo do campo indAquis do registro tpAquis:  Se campo indAquis = 1      O campo será preenchido com “1-Aquisição da produção de produtor rural pessoa física ou segurado especial em geral” Se campo indAquis = 2      O campo será preenchido com “2-Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA” Se campo indAquis = 3      O campo será preenchido com “3-Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA” Se campo indAquis = 4      O campo será preenchido com “4-Aquisição da produção de produtor rural pessoa física ou segurado especial em geral - Produção Isenta (Lei 13.606/2018)” Se campo indAquis = 5      O campo será preenchido com “5-Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA - Produção Isenta (Lei 13.606/2018)” Se campo indAquis = 6      O campo será preenchido com “6-Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA - Produção Isenta (Lei 13.606/2018)” |
| --- | --- |
| Valor Total da Aquisição | Conteúdo do campo vlrTotAquis do registro tpAquis |


| Tipo Insc. Produtor | Este campo é preenchido dependendo do conteúdo do campo tpInscProd do registro ideProdutor:  Se campo tpInscProd = “1”      O campo será preenchido com “1-CNPJ” Senão      O campo será preenchido com “2-CPF” |
| --- | --- |
| Número Insc. Produtor | Conteúdo do campo nrInscProd do registro tpInscProd |
| Valor Bruto | Conteúdo do campo vlrBruto do registro tpInscProd |
| Valor CP Desc. Produtor | Conteúdo do campo vrCPDescPR do registro tpInscProd |
| Valor Rat Desc. Produtor | Conteúdo do campo vrRatDescPR do registro tpInscProd |
| Valor Senar Desc. Produtor | Conteúdo do campo vrSenarDesc do registro tpInscProd |


| Série | Conteúdo do campo serie do registro nfs |
| --- | --- |
| Número da Nota Fiscal | Conteúdo do campo nrDocto do registro nfs |
| Data de Emissão da NF | Conteúdo do campo dtEmisNF do registro nfs |
| Valor Bruto | Conteúdo do campo vlrBruto do registro nfs |
| Valor CP Desc. Produtor | Conteúdo do campo vrCPDescPR do registro nfs |
| Valor Rat Desc. Produtor | Conteúdo do campo vrRatDescPR do registro nfs |
| Valor Senar Desc. Produtor | Conteúdo do campo vrSenarDesc do registro nfs |


| Número Processo Judicial | Conteúdo do campo nrProcJud do registro infoProcJud |
| --- | --- |
| Cód. do Indicativo de Suspensão | Conteúdo do campo codSusp do registro infoProcJud |
| Valor CP Não Retida | Conteúdo do campo vrCPNRet do registro infoProcJud |
| Valor Rat Não Retida | Conteúdo do campo vrRatNRet do registro infoProcJud |
| Valor Senar Não Retido | Conteúdo do campo vrSenarNRet do registro infoProcJud |
