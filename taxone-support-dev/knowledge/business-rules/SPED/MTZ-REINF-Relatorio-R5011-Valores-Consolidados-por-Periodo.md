# MTZ-REINF-Relatorio-R5011-Valores-Consolidados-por-Periodo

> Fonte: MTZ-REINF-Relatorio-R5011-Valores-Consolidados-por-Periodo.docx






THOMSON REUTERS

Módulo REINF

Relatório de Conferência do Evento R-5011 (Valores Consolidados por Período)


Localização: Menu SPED, módulo EFD – Reinf, menu Relatórios   Conferência dos Eventos   R-5011 (Valores Consolidados por Período)




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	3
3.	Regras de Funcionamento dos Campos	4
4.	Regras da Recuperação dos Dados	5
5.	Layout e Preenchimento dos Campos no Relatório	6






















## Regras Gerais


Relatório criado na MFS17628, com objetivo de possibilitar a consulta dos valores calculados pelo Fisco no fechamento do período.













## Layout da Tela






## Regras de Funcionamento dos Campos





## Regras da Recuperação dos Dados


A origem dos dados para emissão do relatório tem como base os eventos R-2099 e R-5011:

Para cada evento R-2099 recuperado conforme regra acima (***), será listado no relatório as informações do evento R-5011 correspondente.




Para cada R-2099:

Para cada R-2099 será gerado um relatório conforme o layout anexo (“Layout Relatório Conferencia R-5011”).

O número de páginas é variável, pois dependerá da quantidade de prestadores, tomadores, etc...

No cabeçalho será demonstrado a empresa e o estabelecimento referentes ao evento R-2099 em questão.

A cada novo R-2099, haverá quebra de página.


Ordenação dos dados para apresentação no relatório:

O relatório será ordenado pelas informações de empresa e estabelecimento que aparecem no relatório:

- Razão Social da Empresa (o cabeçalho mostra apenas a razão social da empresa);
- Código do Estabelecimento;


## Layout e Preenchimento dos Campos no Relatório


Layout: Vide planilha “Layout Relatório Conferencia R-5011”.


A seguir será descrito o preenchimento dos campos do relatório, a partir do evento R-5011 referente ao R-2099 em questão:


Linhas do cabeçalho:

Como o relatório é por evento R-2099, no cabeçalho sempre aparecerá a empresa e estabelecimento referentes ao R-2099 em questão.
Na quebra de R-2099, haverá salto de página e na próxima página se inicia um novo evento R-2099.







Linhas de detalhe de identificação do evento R-5011:




Linhas de detalhe dos totais de CP sobre serviços tomados:

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços tomados (R-2010)”)

Nesta linha são demonstrados os totais de todos os prestadores de serviço existentes na tag RTom.

Para cada prestador será apresentado o CNPJ e o valor total da base de cálculo, e a seguir, os valores calculados por código de receita existentes na tag infoCRTom.


[MFS20930] – [MFS36441] Alteração formato do campo Cód. Receita.



Linhas de detalhe dos totais de CP sobre serviços prestados:  R-2020

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados )”)

Nesta linha são demonstrados os totais de todos os tomadores de serviço existentes na tag RPrest.





Linhas de detalhe dos totais de CP sobre recursos repassados a associações desportivas:

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associação Desportiva (R-2040)”)

Nesta linha são demonstrados os totais repassados a todas as associações desportivas existentes na tag RRecRepAD.

[MFS20930] – [MFS36441] Alteração formato do campo Cód. Receita.


Linhas de detalhe dos totais das contribuições sobre a comercialização de produção por produtor rural:

(“Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria (R-2050)”)

Nesta linha são demonstrados os totais das contribuições sobre comercialização de produção de produtor rural, calculados por código de receita. São demonstrados todos os códigos de receita existentes na tag RComl.


[MFS36441] Alteração formato do campo Cód. Receita.


[MFS36441] Inclusão das linhas RAquis - Contribuições sobre a Aquisição de produção rural, referente ao evento (R-2055)


Linhas de detalhe dos totais das contribuições sobre a Aquisição de produção rural:

(“Totalizador das contribuições sociais incidentes sobre aquisição de produção- RAquis (R-2055)”)

Nesta linha são demonstrados os totais das contribuições sociais incidentes sobre aquisição de produção rural, calculados por código de receita. São demonstrados todos os códigos de receita existentes na tag RAquis.





Linhas de detalhe dos totais de CP sobre a receita bruta:

(“Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB (R-2060)”)

Nesta linha são demonstrados os totais das contribuições sobre a receita bruta, calculados por código de receita. São demonstrados todos os códigos de receita existentes na tag RCPRB.



[MFS36441] Alteração formato do campo Cód. Receita. E alteração do número de campos do CRPRB, de 52, 53 e 54, passam a ser 56, 57 e 58, conforme nova versão 1.5.1.



= = = = = =

## Layout e Preenchimento dos Campos (Arquivo TXT)


O Relatório será gerado em arquivo texto, deverão ser gravadas todas as informações que são mostradas no Relatório de Conferência do Evento R-5011 (Valores Consolidados por Período), menu Relatórios  Conferência dos Eventos  R-5011 (Valores Consolidados por Período).

O arquivo texto deve ser gerado com o cabeçalho das colunas existentes no relatório e deve ser incluída uma coluna no início do arquivo, que irá identificar o evento, como por exemplo, R-2020.  Como existem vários layouts de relatório, um para cada evento, o cabeçalho de cada relatório deve ser gerado no arquivo, por este motivo a primeira coluna deve ser o identificador do evento.



| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS17628 | Relatório de Conferência do Evento R-5011 | Criação do relatório de conferência do evento R-5011 (Valores Consolidados por Período) | 17/05/2018 |
| MFS20930 | Lara Aline | Inclusão campo cno na tag Rtom, exclusão dos campos cnpjAssocDesp e vlrTotalRep da tag RRecRepADe ajuste na numeração dos campos de acordo com o novo Layout 1.4. | 17/09/2018 |
| MFS36441 | Alessandra Cristina Navatta | A inclusão do novo evento R-2055, impactou diretamente o evento R-5011.  Tivemos a inclusão das linhas RAquis e alteração do número dos campos RCPRB, alteração de formato de campo do Código da Receita. Além disso, a opção do relatório em formato TXT será gerada através desta tela (não será mais gerada em opção de Menu separada (SPED, módulo EFD – Reinf  Relatórios   Conferência dos Eventos   R-5011 (Valores Consolidados por Período)  Formato TXT). Devido este ajuste, o menu também será alterado. | 01/04/2021 |


| Sobre o evento R-5011:  Estes valores estarão no evento R-5011, evento gerado pelo Fisco, e enviado aos contribuintes após o recebimento do evento R-2099 (junto com a mensagem de retorno).  O Fisco envia o R-5011 sempre que um evento R-2099 é recepcionado com sucesso (status de retorno do Onesource = “Evento recebido pelo Fisco com sucesso” ou “Evento recebido pelo Fisco com advertência”). O Onesource processa estes dados e retorna para o MSAF um XML (através da STG_EVENTOS_REINF_IN), que contém entre outras informações, estes valores gerados pelo Fisco.  No módulo REINF (DW) estes dados são recuperados para emissão do relatório.  Cada evento R-5011 é vinculado a um evento R-2099 (através da tabela de ocorrências). |
| --- |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano do período para emissão do relatório.  Deve ser um mês válido. |
| Multiempresas | Alfanumérico | N | S | Default:  Desmarcado | Na abertura da tela esta opção aparecerá sempre desmarcada. |
| Empresa / Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos para seleção do usuário.  A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   Será feita a pesquisa de todos os eventos R-2099 existentes para o período informado, cujo status indique que o evento já foi recebido pelo Fisco com sucesso/advertência.  (A pesquisa é baseada na tabela “OC” do R-2099,  e a partir dela, se obtém a empresa, estab. e período na PGER_APUR)   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos R-2099 encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; |
| Selecionar todos / Desmarcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados. |


| (***) Regra de montagem da lista dos estabelecimentos, descrita no item 3, campo “Empresa/Estabelecimento”. Lembrando que, pela regra, são demonstrados apenas os estabelecimentos com R-2099 já entregue ao Fisco com sucesso, e neste caso, todos terão o seu R-5011 especifico; |
| --- |


| Primeira linha | Razão social da empresa referente ao R-2099 em questão; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Informações do estabelecimento referente ao R-2099 em questão; -Código e razão social -Inscrição estadual -CNPJ |
| Terceira e quarta linha | Título do relatório (“Relatório de Conferência do R-5011 - Valores Consolidados por Período”); Período – Mês a Ano informados na tela da geração |


| Número Inscrição Contribuinte | Conteúdo do campo 08-nrInsc (tag ideContri); |
| --- | --- |
| Tipo | Se campo 07-tpInsc = 1 (tag ideContri), preencher com “CNPJ”; Se campo 07-tpInsc = 2 (tag ideContri), preencher com “CPF”; |
| ID Evento R-5011 | Conteúdo do campo 03-Id (tag evtTotalContrib) |
| ID Evento R-2099 | Conteúdo do campo 22-idEv (tag infoRecEv) |
| N. Recibo Arquivo Base (R-2099) | Conteúdo do campo 25-nrRecArqBase (tag infoTotalContrib) |
| Protocolo do Fechamento | Conteúdo do campo 19-nrProtEntr (tag infoRecEv) |
| Indicativo de Movimento | Se campo 26-indExistInfo (tag infoTotalContrib) = 1       Preencher com “1-Há informações de bases e/ou de tributos”;  Se campo 26-indExistInfo (tag infoTotalContrib) = 2       Preencher com “2 - Há movimento, porém não há informações de bases ou de tributos”;  Se campo 26-indExistInfo (tag infoTotalContrib) = 3       Preencher com “3 - Não há movimento na competência”; |


| CNPJ Prestador | Conteúdo do campo 28-cnpjPrestador (tag RTom), formatado como CNPJ ( 99.999.999/9999-99) |
| --- | --- |
| CNO | Conteúdo do campo 29-cno (tag RTom) |
| Total Base de Cálculo | Conteúdo do campo 30-vlrTotalBaseRet (tag RTom) |
|  | Nestes campos serão demonstrados os valores por código de receita que existirem na tag infoCRTom: |
| Cód. Receita | Cód.Receita – Conteúdo do campo 32-CRTom, formato válido 999999; |
| Valor Contrib.Prev. | Valor Contrib Prev - Conteúdo do campo 33-vlrCRTom; |
| Valor Contrib.Prev.-Exigibilidade Suspensa | Valor Contrib Prev Exig Susp - Conteúdo do campo 34-vlrCRTomSusp; |


| Tomador | Conteúdo do campo 37-nrInscTomador (tag RPrest);  Ao lado do número será mostrado o tipo de inscrição, se CNPJ ou CNO:  Se campo 36-tpInscTomador 1, trata-se de CNPJ; Se campo 36-tpInscTomador 4, trata-se de CNO;  Ex: Tomador: 99999999999999 (CNPJ)       Tomador: 99999999999999 (CNO) |
| --- | --- |
| BC Ret. | Conteúdo do campo 38-vlrTotalBaseRet; |
| Vlr Ret | Conteúdo do campo 39-vlrTotalRetPrinc; |
| Vlr Ret Adic | Conteúdo do campo 40-vlrTotalRetAdic; |
| Vlr Ret não Efetuada | Conteúdo do campo 41-vlrTotalNRetPrinc; |
| Vlr Ret Adic não Efetuada | Conteúdo do campo42-vlrTotalNRetAdic; |


| CNPJ Assoc. Desportiva | Conteúdo do campo 43-cnpjAssocDesp (tag RRecRepAD), formatado como CNPJ ( 99.999.999/9999-99) |
| --- | --- |
| Valor Total do Repasse | Conteúdo do campo 44-vlrTotalRep |
| Cód. Receita | Conteúdo do campo 44-CRRecRepAD, formato válido 999999; |
| Valor Contrib.Prev. | Conteúdo do campo 45-vlrCRRecRepAD; |
| Valor Contrib.Prev. não Efetuada | Conteúdo do campo 46-vlrCRRecRepADSusp; |


| Código Receita | Conteúdo do campo 48-CRCompl, formato válido 999999; |
| --- | --- |
| Valor Contrib. Previdenciária | Conteúdo do campo 49-vlrCRCompl; |
| Valor Contrib. Previdenciária – Exigibilidade Suspensa | Conteúdo do campo 50-vlrCRComplSusp; |


| Código de Receita CR | Conteúdo do campo 52- CRAquis, no formato 999999; |
| --- | --- |
| Valor da contribuição previdenciária | Conteúdo do campo 53- vlrCRAquis; |
| Valor da contribuição previdenciária com exigibilidade suspensa | Conteúdo do campo 54- vlrCRAquisSusp; |


| Código Receita | Conteúdo do campo 56-CRCPRB, no formato 999999; |
| --- | --- |
| Valor Contrib. Previdenciária | Conteúdo do campo 57-vlrCRCPRB; |
| Valor Contrib. Previdenciária – Exigibilidade Suspensa | Conteúdo do campo 58-vlrCRCPRBSusp; |
