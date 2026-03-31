# MTZ_REINF_Relatorio-R9001-Bases-e-tributos-contribuicao-previdenciaria

> Fonte: MTZ_REINF_Relatorio-R9001-Bases-e-tributos-contribuicao-previdenciaria.docx


THOMSON REUTERS

Módulo REINF

Relatório de Conferência do Evento R-9001 (Bases e Tributos - Contribuição Previdenciária)


Localização: Menu SPED, módulo EFD – Reinf, menu Relatórios à Conferência dos Eventos à R-9001 (Bases e Tributos - Contribuição Previdenciária)





DOCUMENTO DE REQUISITO







Sumário

1.	Regras Gerais	3
2.	Layout da Tela	4
3.	Regras de Funcionamento dos Campos	4
4.	Regras da Recuperação dos Dados	6
5.	Layout e Preenchimento dos Campos no Relatório	7




















## Regras Gerais


Relatório criado com objetivo de possibilitar a consulta dos valores calculados pelo Fisco retorno do evento R-9001. Este relatório apresenta as informações da geração a partir da versão 2.1.1 do REINF.















## Layout da Tela






## Regras de Funcionamento dos Campos





## Regras da Recuperação dos Dados



A origem dos dados para emissão do relatório tem como base os eventos R-2010, R-2020, R-2040, R-2050, R-2055, R-2060 e R-9001:

Para cada evento da família 2000 listado acima recuperado conforme regra acima (***), será listado no relatório as informações do evento R-9001 correspondente.




Para cada R-9001:

Será gerado um relatório conforme o layout anexo (“Layout_Relatorio_Conferencia_R-9001.xlsx”).

O número de páginas é variável, pois dependerá da quantidade de prestadores, tomadores, produtores rurais, etc.

No cabeçalho será demonstrado a empresa e o estabelecimento referentes ao evento R-9001 em questão.


Ordenação dos dados para apresentação no relatório:

O relatório será ordenado pelas informações de empresa e estabelecimento e evento que aparecem no relatório:

- Razão Social da Empresa (o cabeçalho mostra apenas a razão social da empresa);
- Código do Estabelecimento;
- Evento


## Layout e Preenchimento dos Campos no Relatório


Abas geradas: Parâmetros, Processos, Arquivos, Relatório (conforme padrão do produto)
Layout do relatório exibido em tela (Relatório): Vide planilha “Layout_Relatorio_Conferencia_R-9001.xlsx”, considerando o layout, formato e label indicado na planilha ’Conferência R-9001 – TELA’,.
Formato do arquivo (gerado na aba Arquivos): .CSV. Apresentar as colunas considerando o layout, formato e label indicado na planilha ’Conferência R-9001 – CSV’, do arquivo “Layout_Relatorio_Conferencia_R-9001.xlsx”



A seguir será descrito o preenchimento dos campos e suas respectivas regras do relatório (apresentado em tela),  a partir do evento R-9001


Linhas do cabeçalho:

Como o relatório é por eventos R-9001, no cabeçalho sempre aparecerá a empresa e estabelecimento referentes aos eventos em questão.
Haverá um salto de página a cada R-9001 (demonstrando as informações de um dos eventos da família 20: R-2010, R-2020, R-2040, R-2050, R-2055, R-2060).









Linhas de detalhe de identificação do evento R-9001:



Não deverá ser apresentado as informações dos eventos não existentes no R-9001


Linhas de detalhe dos totais de CP sobre serviços tomados:

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços tomados (R-2010):”)

Nesta linha são demonstrados os totais de todos os tomadores de serviço existentes na tag RTom.

Para cada tomador será apresentado o CNPJ e o valor total da base de cálculo, e a seguir, os valores calculados por código de receita existentes na tag infoCRTom.





Linhas de detalhe dos totais de CP sobre serviços prestados:

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados (R-2020):”)

Nesta linha são demonstrados os totais de todos os prestadores de serviço existentes na tag RPrest.

Para cada prestador será apresentado a Inscrição do Tomador e o valor total da base de cálculo, e a seguir, os valores calculados por código de receita existentes na tag Rprest.



Linhas de detalhe dos totais de CP sobre recursos repassados a associações desportivas:

(“Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associação Desportiva (R-2040):.”)

Nesta linha são demonstrados os totais de cada associação desportiva existentes na tag RRecRepAD.

Para cada prestador será apresentado o CNPJ da associação desportiva e o valor total da base do repasse, e a seguir, os valores calculados por código de receita existentes na tag RRecRepAD.



Linhas de detalhe dos totais de CS incidentes sobre a comercialização de produtor rural pessoa jurídica e agroindústria:

(“Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria (R-2050):”)


Nesta linha são demonstrados os totais de cada produtor rural existente na tag RComl.

Serão exibidos os valores calculados por código de receita existente na tag RComl.



Linhas de detalhe dos totais de CS incidentes sobre a aquisição de produção:

(“Totalizador das contribuições sociais incidentes sobre aquisição de produção- RAquis (R-2055):”)

Nesta linha são demonstrados os totais de cada aquisição existente na tag CRAquis.

Serão exibidos os valores calculados por código de receita existente na tag CRAquis.




Linhas de detalhe dos totais de CP sobre a receita bruta - CPRB:

(“Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB (R-2060):”)

Nesta linha são demonstrados os totais da CP sobre a receita bruta existente na tag RCPRB.

Serão exibidos os valores calculados por código de receita existente na tag RCPRB.




| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79962 | Alessandra Cristina Navatta | Criação do relatório de conferência do evento R-9001 (Bases e Tributos - Contribuição Previdenciária) | 30/12/2022 |
| MFS-79962 | Alessandra Cristina Navatta | Inclusão do layout em formato CSV | 24/02/2023 |


| Sobre o evento R-9001:  Estes valores estarão no evento R-9001, evento gerado pelo Fisco, e enviado aos contribuintes após o recebimento dos eventos R-2010, R-2020, R-2040, R-2050, R-2055 e R-2060, recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  O Fisco envia o R-9001 sempre que um evento da família 2000 listados acima for recepcionado com sucesso (status de retorno do Onesource = “Evento recebido pelo Fisco com sucesso” ou “Evento recebido pelo Fisco com advertência”). O Onesource processa estes dados e retorna para o MSAF um XML (através da STG_EVENTOS_REINF_IN), que contém entre outras informações, estes valores gerados pelo Fisco.  No módulo REINF (DW) estes dados são recuperados para emissão do relatório. |
| --- |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano do período para emissão do relatório.  Deve ser um mês válido. |
| Multiempresas | Alfanumérico | N | S | Default:  Desmarcado | Na abertura da tela esta opção aparecerá sempre desmarcada. |
| Empresa / Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos para seleção do usuário.  A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   A pesquisa é baseada no campo de indicação existe na PGER_APUR referente aos eventos R-2010, R-2020, R-2040, R-2050, R-2055 e ou R-2060 existentes para o período informado e a partir dela, se obtém a empresa, estab. e período. Caso não seja encontrado, para o período em questão, geração de pelo menos um dos eventos indicados acima, não será recuperado nenhum estabelecimento.   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos R-2010, R-2020, R-2040, R-2050, R-2055 e ou R-2060 encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; |
| Selecionar todos / Desmarcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados. |


| (***) Regra de montagem da lista dos estabelecimentos, descrita no item 3, campo “Empresa/Estabelecimento”. Lembrando que, pela regra, são demonstrados apenas os estabelecimentos com R-2010, R-2020, R-2040, R-2050, R-2055, R-2060 já entregues ao Fisco com sucesso e ou advertência, e neste caso, terão um evento R-9001 específico; |
| --- |


| Primeira linha | Razão social da empresa referente ao evento (R-9001) em questão; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Informações do estabelecimento referente aos eventos R-2010, R-2020, R-2040, R-2050, R-2055, R-2060; -Código e razão social -Inscrição estadual -CNPJ |
| Terceira e quarta linha | Título do relatório (“Relatório de Conferência do R-9001 - Bases e Tributos - Contribuição Previdenciária”); Período – Mês /Ano informados na tela da geração |


| Número Inscrição Contribuinte | Conteúdo do campo 08-nrInsc (tag ideContri); |
| --- | --- |
| Tipo | Se campo 07-tpInsc = 1 (tag ideContri), preencher com “CNPJ”; Se campo 07-tpInsc = 2 (tag ideContri), preencher com “CPF”; |
| ID Evento R-9001 | Conteúdo do campo 03-Id (tag evtTotal) |
| ID Evento R-XXXX*, Onde R-XXXX* é o número do evento existente no R-9001 | Conteúdo do campo 22-idEv (tag infoRecEv) |
| Protocolo da Entrega | Conteúdo do campo 19-nrProtEntr (tag infoRecEv) |
| Número Recibo Arquivo | Conteúdo do campo 25-nrRecArqBase (tag infoTotalContrib) |


| CNPJ Prestador | Conteúdo do campo 30-cnpjPrestador (tag RTom), formatado como CNPJ ( 99.999.999/9999-99) |
| --- | --- |
| CNO | Conteúdo do campo 31-cno (tag RTom) |
| Total Base de Cálculo | Conteúdo do campo 32-vlrTotalBaseRet (tag RTom) |
|  | Nestes campos serão demonstrados os valores por código de receita que existirem na tag infoCRTom: |
| Código Receita | Conteúdo do campo 34-CRTom, formato válido 999999; |
| Valor Contrib.Prev. | Conteúdo do campo 35-vlrCRTom; |
| Valor Contrib.Prev.-Exigibilidade Suspensa | Conteúdo do campo 36-vlrCRTomSusp; |


| Tomador | Conteúdo do campo 39-nrInscTomador (tagRPrest) |
| --- | --- |
| Total BC Retenção | Conteúdo do campo 40-vlrTotalBaseRet (tagRPrest) |
| Total Valor Retenção | Conteúdo do campo 41-vlrTotalRetPrinc (tagRPrest) |
| Total Valor Ret Adic | Conteúdo do campo 42-vlrTotalRetAdic (tagRPrest) |
| Total Valor Ret não Efetuada | Conteúdo do campo 43-vlrTotalNRetPrinc (tagRPrest) |
| Total Valor Ret Adic não Efetuada | Conteúdo do campo 44-vlrTotalNRetAdic (tagRPrest) |


| CNPJ Assoc. Desportiva | Conteúdo do campo 46- cnpjAssocDesp (tagRRecRepAD) |
| --- | --- |
| Valor Total do Repasse | Conteúdo do campo 47-vlrTotalRep (tagRRecRepAD) |
| Código Receita | Conteúdo do campo 48-CRRecRepAD (tagRRecRepAD), formato válido 999999 |
| Valor Contrib. Prev. | Conteúdo do campo 49-vlrCRRecRepAD (tagRRecRepAD) |
| Valor Contrib. Prev. não Efetuada | Conteúdo do campo 50-vlrCRRecRepADSusp (tagRRecRepAD) |


| Código Receita | Conteúdo do campo 52-CRComl (tagRComl), formato válido 999999 |
| --- | --- |
| Valor Contrib. Prev. | Conteúdo do campo 53-vlrCRComl (tagRComl) |
| Valor Contrib. Prev.- Exigibilidade Suspensa | Conteúdo do campo 54-vlrCRComlSusp (tagRComl) |


| Código Receita | Conteúdo do campo 56-CRAquis (tagRAquis), formato válido 999999 |
| --- | --- |
| Valor Contrib. Prev. | Conteúdo do campo 57-vlrCRAquis (tagRAquis) |
| Valor Contrib. Prev.- Exigibilidade Suspensa | Conteúdo do campo 58-vlrCRAquisSusp (tagRAquis) |


| Código Receita | Conteúdo do campo 60-CRAquis (tagRCPRB), formato válido 999999 |
| --- | --- |
| Valor Contrib. Prev. | Conteúdo do campo 61-vlrCRAquis (tagRCPRB) |
| Valor Contrib. Prev.- Exigibilidade Suspensa | Conteúdo do campo 62-vlrCRAquisSusp (tagRCPRB) |
