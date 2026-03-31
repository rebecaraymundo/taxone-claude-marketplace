# MTZ-REINF-Relatorio-R9011-Consolidacao-bases-tributos-Contribuicao-previdenciaria

> Fonte: MTZ-REINF-Relatorio-R9011-Consolidacao-bases-tributos-Contribuicao-previdenciaria.docx






THOMSON REUTERS

Módulo REINF

Relatório de Conferência do Evento R-9011 (Consolidação de Bases e Tributos - Contribuição Previdenciária)


Localização: Menu SPED, módulo EFD – Reinf, menu Relatórios à  Conferência dos Eventos  à R-9011 (Consolidação de Bases e Tributos - Contribuição previdenciária)




DOCUMENTO DE REQUISITO



Sumário

1.	Regras Gerais	3
2.	Layout da Tela	4
3.	Regras de Funcionamento dos Campos	5
4.	Regras da Recuperação dos Dados	6
5.	Layout e Preenchimento dos Campos no Relatório	7
6.	Layout e Preenchimento dos Campos (Arquivo TXT)	12


















## Regras Gerais


Relatório criado com objetivo de possibilitar a consulta dos valores calculados pelo Fisco retorno do evento R-9011. Este relatório apresenta as informações da geração a partir da versão 2.1.1 do REINF.















## Layout da Tela








## Regras de Funcionamento dos Campos





## Regras da Recuperação dos Dados


A origem dos dados para emissão do relatório tem como base os eventos R-2099 e R-9011:

Para cada evento R-2099 recuperado conforme regra acima (***), será listado no relatório as informações do evento R-9011 correspondente.




Para cada R-2099:

Para cada R-2099 será gerado um relatório conforme o layout anexo (“Layout_Relatorio_Conferencia_R-9011.xlsx”).

O número de páginas é variável, pois dependerá da quantidade de prestadores, tomadores, etc...

No cabeçalho será demonstrado a empresa e o estabelecimento referentes ao evento R-2099 em questão.

A cada novo R-2099, haverá quebra de página.


Ordenação dos dados para apresentação no relatório:

O relatório será ordenado pelas informações de empresa e estabelecimento que aparecem no relatório:

- Razão Social da Empresa (o cabeçalho mostra apenas a razão social da empresa);
- Código do Estabelecimento;


## Layout e Preenchimento dos Campos no Relatório


Abas geradas: Parâmetros, Processos, Arquivos, Relatório (conforme padrão do produto)
Layout do relatório exibido em tela (aba Relatório): Vide planilha “Layout_Relatorio_Conferencia_R-9011.xlsx”.
Formato do arquivo (gerado na aba Arquivos): .CSV. Apresentar todas as colunas que estão sendo apresentadas no relatório de tela.




A seguir será descrito o preenchimento dos campos e suas respectivas regras do relatório (apresentado em tela), a partir do evento R-9011 referente ao R-2099 em questão:


Linhas do cabeçalho:

Como o relatório é por evento R-2099, no cabeçalho sempre aparecerá a empresa e estabelecimento referentes ao R-2099 em questão.
Na quebra de R-2099, haverá salto de página e na próxima página se inicia um novo evento R-2099.







Linhas de detalhe de identificação do evento R-9011:



Não deverá ser apresentado as informações dos eventos não existentes no R-9011

Linhas de detalhe dos totais de CP sobre serviços tomados:

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços tomados (R-2010)”)

Nesta linha são demonstrados os totais de todos os prestadores de serviço existentes na tag RTom.

Para cada prestador será apresentado o CNPJ e o valor total da base de cálculo, e a seguir, os valores calculados por código de receita existentes na tag infoCRTom.






Linhas de detalhe dos totais de CP sobre serviços prestados:  R-2020

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados (R-2020)”)

Nesta linha são demonstrados os totais de todos os tomadores de serviço existentes na tag RPrest.





Linhas de detalhe dos totais de CP sobre recursos repassados a associações desportivas:

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associação Desportiva (R-2040)”)

Nesta linha são demonstrados os totais repassados a todas as associações desportivas existentes na tag RRecRepAD.



Linhas de detalhe dos totais das contribuições sobre a comercialização de produção por produtor rural:

(“Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria (R-2050)”)

Nesta linha são demonstrados os totais das contribuições sobre comercialização de produção de produtor rural, calculados por código de receita. São demonstrados todos os códigos de receita existentes na tag RComl.






Linhas de detalhe dos totais das contribuições sobre a Aquisição de produção rural:

(“Totalizador das contribuições sociais incidentes sobre aquisição de produção- RAquis (R-2055)”)

Nesta linha são demonstrados os totais das contribuições sociais incidentes sobre aquisição de produção rural, calculados por código de receita. São demonstrados todos os códigos de receita existentes na tag RAquis.





Linhas de detalhe dos totais de CP sobre a receita bruta:

(“Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB (R-2060)”)

Nesta linha são demonstrados os totais das contribuições sobre a receita bruta, calculados por código de receita. São demonstrados todos os códigos de receita existentes na tag RCPRB.





= = = = = =



| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79968 | Alessandra Cristina Navatta | Criação do relatório de conferência do evento R-9011 (Consolidação de Bases e Tributos - Contribuição Previdenciária) | 29/12/2022 |


| Sobre o evento R-9011:  Estes valores estarão no evento R-9011, evento gerado pelo Fisco, e enviado aos contribuintes após o recebimento do evento R-2099 (junto com a mensagem de retorno).  O Fisco envia o R-9011 sempre que um evento R-2099 é recepcionado com sucesso (status de retorno do Onesource = “Evento recebido pelo Fisco com sucesso” ou “Evento recebido pelo Fisco com advertência”). O Onesource processa estes dados e retorna para o MSAF um XML (através da STG_EVENTOS_REINF_IN), que contém entre outras informações, estes valores gerados pelo Fisco.  No módulo REINF (DW) estes dados são recuperados para emissão do relatório.  Cada evento R-9011 é vinculado a um evento R-2099 (através da tabela de ocorrências). |
| --- |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano do período para emissão do relatório.  Deve ser um mês válido. |
| Multiempresas | Alfanumérico | N | S | Default:  Desmarcado | Na abertura da tela esta opção aparecerá sempre desmarcada. |
| Empresa / Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos para seleção do usuário.  A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   Será feita a pesquisa de todos os eventos R-2099 existentes para o período informado, cujo status indique que o evento já foi recebido pelo Fisco com sucesso/advertência.  (A pesquisa é baseada na tabela “OC” do R-2099,  e a partir dela, se obtém a empresa, estab. e período na PGER_APUR)   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos R-2099 encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; |
| Selecionar todos / Desmarcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados. |


| (***) Regra de montagem da lista dos estabelecimentos, descrita no item 3, campo “Empresa/Estabelecimento”. Lembrando que, pela regra, são demonstrados apenas os estabelecimentos com R-2099 já entregue ao Fisco com sucesso, e neste caso, todos terão o seu R-9011 especifico; |
| --- |


| Primeira linha | Razão social da empresa referente ao R-2099 em questão; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Informações do estabelecimento referente ao R-2099 em questão; -Código e razão social -Inscrição estadual -CNPJ |
| Terceira e quarta linha | Título do relatório (“Relatório de Conferência do R-9011 - Consolidação de Bases e Tributos - Contribuição Previdenciária”); Período – Mês /Ano informados na tela da geração |


| Número Inscrição Contribuinte | Conteúdo do campo 08-nrInsc (tag ideContri); |
| --- | --- |
| Tipo | Se campo 07-tpInsc = 1 (tag ideContri), preencher com “CNPJ”; Se campo 07-tpInsc = 2 (tag ideContri), preencher com “CPF”; |
| ID Evento R-9011 | Conteúdo do campo 03-Id (tag evtTotalContrib) |
| ID Evento R-2099 | Conteúdo do campo 22-idEv (tag infoRecEv) |
| N. Recibo Arquivo Base (R-2099) | Conteúdo do campo 25-nrRecArqBase (tag infoTotalContrib) |
| Protocolo do Fechamento | Conteúdo do campo 19-nrProtEntr (tag infoRecEv) |
| Indicativo de Movimento | Se campo 26-indExistInfo (tag infoTotalContrib) = 1       Preencher com “1-Há informações de bases e/ou de tributos”;  Se campo 26-indExistInfo (tag infoTotalContrib) = 2       Preencher com “2 - Há movimento, porém não há informações de bases ou de tributos”;  Se campo 26-indExistInfo (tag infoTotalContrib) = 3       Preencher com “3 - Não há movimento na competência”; |
| Identificador da Escrituração DCTFWeb | Conteúdo do campo 27- infoTotalContrib (tag infoTotalContrib) |


| CNPJ Prestador | Conteúdo do campo 29-cnpjPrestador (tag RTom), formatado como CNPJ ( 99.999.999/9999-99) |
| --- | --- |
| CNO | Conteúdo do campo 30-cno (tag RTom) |
| Total Base de Cálculo | Conteúdo do campo 31-vlrTotalBaseRet (tag RTom) |
|  | Nestes campos serão demonstrados os valores por código de receita que existirem na tag infoCRTom: |
| Cód. Receita | Cód.Receita – Conteúdo do campo 33-CRTom, formato válido 999999; |
| Valor Contrib.Prev. | Valor Contrib Prev - Conteúdo do campo 34-vlrCRTom; |
| Valor Contrib.Prev.-Exigibilidade Suspensa | Valor Contrib Prev Exig Susp - Conteúdo do campo 35-vlrCRTomSusp; |


| Tomador | Conteúdo do campo 38-nrInscTomador (tag RPrest);  Ao lado do número será mostrado o tipo de inscrição, se CNPJ ou CNO:  Se campo 37-tpInscTomador 1, trata-se de CNPJ; Se campo 37-tpInscTomador 4, trata-se de CNO;  Ex: Tomador: 99999999999999 (CNPJ)       Tomador: 99999999999999 (CNO) |
| --- | --- |
| Total BC Retenção | Conteúdo do campo 39-vlrTotalBaseRet; |
| Total Valor Retenção | Conteúdo do campo 40-vlrTotalRetPrinc; |
| Total Valor Ret Adic | Conteúdo do campo 41-vlrTotalRetAdic; |
| Total Valor Ret não Efetuada | Conteúdo do campo 42-vlrTotalNRetPrinc; |
| Total Valor Ret Adic não Efetuada | Conteúdo do campo43-vlrTotalNRetAdic; |


| Cód. Receita | Conteúdo do campo 45-CRRecRepAD, formato válido 999999; |
| --- | --- |
| Valor Contrib.Prev. | Conteúdo do campo 46-vlrCRRecRepAD; |
| Valor Contrib.Prev. não Efetuada | Conteúdo do campo 47-vlrCRRecRepADSusp; |


| Cód. Receita | Conteúdo do campo 49-CRCompl, formato válido 999999; |
| --- | --- |
| Valor Contrib. Previdenciária | Conteúdo do campo 50-vlrCRCompl; |
| Valor Contrib. Previdenciária – Exigibilidade Suspensa | Conteúdo do campo 51-vlrCRComplSusp; |


| Cód. Receita | Conteúdo do campo 53- CRAquis, no formato 999999; |
| --- | --- |
| Valor Contrib. Previdenciária | Conteúdo do campo 54- vlrCRAquis; |
| Valor Contrib. Previdenciária - Exigibilidade Suspensa | Conteúdo do campo 55- vlrCRAquisSusp; |


| Cód. Receita | Conteúdo do campo 57-CRCPRB, no formato 999999; |
| --- | --- |
| Valor Contrib. Previdenciária | Conteúdo do campo 58-vlrCRCPRB; |
| Valor Contrib. Previdenciária – Exigibilidade Suspensa | Conteúdo do campo 59-vlrCRCPRBSusp; |
