# MTZ_REINF_Relatorio-R9005-Bases-e-tributos-retencoes-na-fonte

> Fonte: MTZ_REINF_Relatorio-R9005-Bases-e-tributos-retencoes-na-fonte.docx


TETHOMSON REUTERS

Módulo REINF

Relatório de Conferência do Evento R-9005 (Bases e Tributos - Retenções na Fonte)


Localização: Menu SPED, módulo EFD – Reinf, menu Relatórios   Conferência dos Eventos   R-9005 (Bases e Tributos – Retenções na Fonte)





DOCUMENTO DE REQUISITO








Sumário

1.	Regras Gerais	3
2.	Layout da Tela	4
3.	Regras de Funcionamento dos Campos	5
4.	Regras da Recuperação dos Dados	6
5.	Layout e Preenchimento dos Campos no Relatório	7




















## Regras Gerais


Relatório criado com objetivo de possibilitar a consulta dos valores calculados pelo Fisco retorno do evento R-9005. Este relatório apresenta as informações da geração a partir da versão 2.1.1 do REINF.















## Layout da Tela










## Regras de Funcionamento dos Campos





## Regras da Recuperação dos Dados



A origem dos dados para emissão do relatório tem como base os eventos R-4010, R-4020, R-4040, R-4080 e R-9005:

Para cada evento da família 4000 listado acima recuperado conforme regra acima (***), será listado no relatório as informações do evento R-9005 correspondente.




Para cada R-9005:

Será gerado um relatório conforme o layout anexo (“Layout_Relatorio_Conferencia_R-9005.xlsx”).

O numero de páginas será variável, pois dependerá da quantidade de código de receita e natureza de rendimento.


No cabeçalho será demonstrado a empresa e o estabelecimento referentes ao evento R-9005 em questão.


Ordenação dos dados para apresentação no relatório:

O relatório será ordenado pelas informações de empresa e estabelecimento e evento que aparecem no relatório:

- Razão Social da Empresa (o cabeçalho mostra apenas a razão social da empresa);
- Código do Estabelecimento;
- Evento


## Layout e Preenchimento dos Campos no Relatório



Abas geradas: Parâmetros, Processos, Arquivos, Relatório (conforme padrão do produto)
Layout do relatório exibido em tela (Relatório): Vide planilha “Layout_Relatorio_Conferencia_R-9005.xlsx”, considerando o layout, formato e label indicado na planilha ’Conferência R-9005 – TELA’.
Formato do arquivo (gerado na aba Arquivos): .CSV. Apresentar as colunas considerando o layout, formato e label indicado na planilha ’Conferência R-9005 – CSV’, do arquivo “Layout_Relatorio_Conferencia_R-9005.xlsx”



A seguir será descrito o preenchimento dos campos e suas respectivas regras do relatório (apresentado em tela), a partir do evento R-9005

Linhas do cabeçalho:

Como o relatório é por evento-9005, no cabeçalho sempre aparecerá a empresa e estabelecimento referentes aos eventos em questão.
Haverá um salto de página a cada R-9005 (demonstrando as informações de um dos eventos da família 40: R-4010, R-4020, R-4040, R-4080).



Linhas de detalhe de identificação do evento R-9005:



Não deverá ser apresentado as informações dos períodos das apurações não existentes no R-9005


Linhas de detalhe dos totais das retenções de apuração com período mensal:

(“Totalizador da base de cálculo, apuração e retenção dos tributos com período de apuração mensal:”)

Nesta linha são demonstrados os totais das retenções de período de apuração mensal na tag totApurMen.


Para cada código de receita e natureza de rendimento serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurMen.



Colunas das Informações da apuração e retenção dos tributos com período de apuração mensal:

Nestas colunas são demonstrados as Informações da apuração e retenção dos tributos com período de apuração mensal existentes na tag totApurTribMen.

Na mesma linha de detalhe dos totais das retenções de apuração com período mensal, serão demonstradas as informações dos tributos de período de apuração mensal existentes na tag totApurTribMen.


Linhas de detalhe dos totais das retenções de apuração com período quinzenal:

(“Totalizador da base de cálculo, apuração e retenção dos tributos com período de apuração quinzenal:”)

Nesta linha são demonstrados os totais das retenções de período de apuração quinzenal na tag totApurQui.

Para cada período de apuração, código de receita  e natureza de rendimento, serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurQui.


Linhas das Informações da apuração e retenção dos tributos com período de apuração quinzenal:

Nesta linha são demonstrados as Informações da apuração e retenção dos tributos com período de apuração quinzenal existentes na tag totApurTribQui.

Na mesma linha de detalhe dos totais das retenções de apuração com período quinzenal, serão demonstradas as informações dos tributos de período de apuração quinzenal existentes na tag totApurTribQui.


Linhas de detalhe dos totais das retenções de apuração com período decendial:

(“Totalizador da base de cálculo, apuração e retenção dos tributos com período de apuração decendial:”)

Nesta linha são demonstrados os totais das retenções de período de apuração decendial na tag totApurDec.

Para cada período de apuração e código de receita serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurDec.


Linhas das Informações da apuração e retenção dos tributos com período de apuração decendial:

Nesta linha são demonstrados as Informações da apuração e retenção dos tributos com período de apuração decendial existentes na tag totApurTribDec.

Na mesma linha de detalhe dos totais das retenções de apuração com período decendial, serão demonstradas as informações dos tributos de período de apuração decendial existentes na tag totApurTribDec.


Linhas de detalhe dos totais das retenções de apuração com período semanal:

(“Totalizador da base de cálculo, apuração e retenção dos tributos com período de apuração semanal:”)

Nesta linha são demonstrados os totais das retenções de período de apuração semanal na tag totApurSem.

Para cada período de apuração, código de receita e natureza de rendimento serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurSem.


Linhas das Informações da apuração e retenção dos tributos com período de apuração semanal:

Nesta linha são demonstrados as Informações da apuração e retenção dos tributos com período de apuração semanal existentes na tag totApurTribSem.

Na mesma linha de detalhe dos totais das retenções de apuração com período semanal, serão demonstradas as informações dos tributos de período de apuração semanal existentes na tag totApurTribSem.


Linhas de detalhe dos totais das retenções de apuração com período de apuração diária:

(“Totalizador da base de cálculo, apuração e retenção dos tributos com período de apuração diária:”)

Nesta linha são demonstrados os totais das retenções de período de apuração diária na tag totApurDia.

Para cada período de apuração, código de receita e natureza de rendimento, serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurDia.


Linhas das Informações da apuração e retenção dos tributos com período de apuração diária:

Nesta linha são demonstrados as Informações da apuração e retenção dos tributos com período de apuração diária existentes na tag totApurTribDia.

Na mesma linha de detalhe dos totais das retenções de apuração com período diária, serão demonstradas as informações dos tributos de período de apuração diária existentes na tag totApurTribDia.



| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79965 | Alessandra Cristina Navatta | Criação do relatório de conferência do evento R-9005 (Bases e Tributos – Retenções na Fonte) | 03/01/2023 |
| MFS-79962 | Alessandra Cristina Navatta | Inclusão do layout em formato CSV | 27/02/2023 |
| MFS-569146 | Alessandra Cristina Navatta | Ajustada a referência dos campos, já que houve inclusão do campo 22-tpEV (tag infoRecEv) no layout, mas, não há impacto nas regras.  Não houve impacto na implementação do relatório | 21/09/2023 |


| Sobre o evento R-9005:  Estes valores estarão no evento R-9005, evento gerado pelo Fisco, e enviado aos contribuintes após o recebimento dos eventos R-4010, R-4020, R-4040, R-4080, recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  O Fisco envia o R-9005 sempre que um evento da família 4000 listados acima for recepcionado com sucesso (status de retorno do Onesource = “Evento recebido pelo Fisco com sucesso” ou “Evento recebido pelo Fisco com advertência”). O Onesource processa estes dados e retorna para o MSAF um XML (através da STG_EVENTOS_REINF_IN), que contém entre outras informações, estes valores gerados pelo Fisco.  No módulo REINF (DW) estes dados são recuperados para emissão do relatório. |
| --- |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano do período para emissão do relatório.  Deve ser um mês válido. |
| Multiempresas | Alfanumérico | N | S | Default:  Desmarcado | Na abertura da tela esta opção aparecerá sempre desmarcada. |
| Empresa / Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos para seleção do usuário.  A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   A pesquisa é baseada no campo de indicação existe na PGER_APUR referente aos eventos R-4010, R-4020, R-4040, R-4080 existentes para o período informado e a partir dela, se obtém a empresa, estab. e período. Caso não seja encontrado, para o período em questão, geração de pelo menos um dos eventos indicados acima, não será recuperado nenhum estabelecimento.   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos R-4010, R-4020, R-4040, R-4080 encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; |
| Selecionar todos / Desmarcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados. |


| (***) Regra de montagem da lista dos estabelecimentos, descrita no item 3, campo “Empresa/Estabelecimento”. Lembrando que, pela regra, são demonstrados apenas os estabelecimentos com R-4010, R-4020, R-4040, R-4080 já entregues ao Fisco com sucesso e ou advertência, e neste caso, terão um evento R-9005 específico; |
| --- |


| Primeira linha | Razão social da empresa referente ao evento R-9005 em questão; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Informações do estabelecimento referente aos eventos R-4010, R-4020, R-4040, R-4080; -Código e razão social -Inscrição estadual -CNPJ |
| Terceira e quarta linha | Título do relatório (“Relatório de Conferência do R-9005 - Bases e Tributos – Retenções na Fonte”); Período – Mês /Ano informados na tela da geração |


| Número Inscrição Contribuinte | Conteúdo do campo 08-nrInsc (tag ideContri); |
| --- | --- |
| Tipo | Se campo 07-tpInsc = 1 (tag ideContri), preencher com “CNPJ”; Se campo 07-tpInsc = 2 (tag ideContri), preencher com “CPF”; |
| ID Evento R-9005 | Conteúdo do campo 03-Id (tag evtRet) |
| ID Evento R-XXXX*, Onde R-XXXX* é o número do evento existente no R-9005 | Conteúdo do campo 23-idEv (tag infoRecEv) |
| Protocolo da Entrega do Lote | Conteúdo do campo 19-nrProtLote (tag infoRecEv) |
| N. Recibo Arquivo | Conteúdo do campo 25-nrRecArqBase (tag infoTotal) |


| Cód. Receita | Conteúdo do campo 33-CRMen da tag totApurMen, formato válido 999999; |
| --- | --- |
| Valor Base Trib. Apur. Mensal | Conteúdo do campo 34- vlrBaseCRMen da tag totApurMen; |
| Valor Base Trib. – Exig. Suspensa | Conteúdo do campo 35- vlrBaseCRMenSusp da tag totApurMen; |
| Natureza de Rendimento | Conteúdo do campo 36- natRend da tag totApurMen; |


| Valor Trib. Ret. Inf. Contrib. | Conteúdo do campo 38-vlrCRMenInf (tag totApurTribMen) |
| --- | --- |
| Valor Trib. Ret. Calc. RFB | Conteúdo do campo 39-vlrCRMenCalc (tag totApurTribMen) |
| Valor Trib. Não Efetuado Inf. Contrib. | Conteúdo do campo 40-vlrCRMenSuspInf (tag totApurTribMen) |
| Valor Trib. Não Efetuado Calc. RFB | Conteúdo do campo 41-vlrCRMenSuspCalc (tag totApurTribMen) |


| Per. Apur. Quinzenal | Conteúdo do campo 43- perApurQui da tag totApurQui; |
| --- | --- |
| Cód. Receita | Conteúdo do campo 44-CRQui da tag totApurQui, formato válido 999999; |
| Valor Base Trib.  Apur. Quinzenal | Conteúdo do campo 44- vlrBaseCRQui da tag totApurQui; |
| Valor Base Trib. – Exig. Suspensa | Conteúdo do campo 46- vlrBaseCRQuiSusp da tag totApurQui; |
| Natureza de Rendimento | Conteúdo do campo 47- natRend da tag totApurQui; |


| Valor Trib. Ret. Inf. Contrib. | Conteúdo do campo 49-vlrCRQuiInf (tag totApurTribQui) |
| --- | --- |
| Valor Trib. Ret. Calc. RFB | Conteúdo do campo 50-vlrCRQuiCalc (tag totApurTribQui) |
| Valor Trib. Não Efetuado Inf. Contrib. | Conteúdo do campo 51-vlrCRQuiSuspInf (tag totApurTribQui) |
| Valor Trib. Não Efetuado Calc. RFB | Conteúdo do campo 52-vlrCRQuiSuspCalc (tag totApurTribQui) |


| Per. Apur. Decendial | Conteúdo do campo 54- perApurDec da tag totApurDec; |
| --- | --- |
| Cód. Receita | Conteúdo do campo 55-CRDec da tag totApurDec, formato válido 999999; |
| Valor Base Trib. Apur. Decendial | Conteúdo do campo 56- vlrBaseCRDec da tag totApurDec; |
| Valor Base Trib. - Exig. Suspensa | Conteúdo do campo 57- vlrBaseCRDecSusp da tag totApurDec; |
| Natureza de Rendimento | Conteúdo do campo 58- natRend da tag totApurDec; |


| Valor Trib. Ret. Inf. Contrib. | Conteúdo do campo 60-vlrCRDecInf (tag totApurTribDec) |
| --- | --- |
| Valor Trib. Ret. Calc. RFB | Conteúdo do campo 61-vlrCRDecCalc (tag totApurTribDec) |
| Valor Trib. Não Efetuado Inf. Contrib. | Conteúdo do campo 62-vlrCRDecSuspInf (tag totApurTribDec) |
| Valor Trib. Não Efetuado Calc. RFB | Conteúdo do campo 63-vlrCRDecSuspCalc (tag totApurTribDec) |


| Per. Apur. Semanal | Conteúdo do campo 65- perApurSem da tag totApurSem; |
| --- | --- |
| Cód. Receita | Conteúdo do campo 66-CRSem da tag totApurSem, formato válido 999999; |
| Valor Base Trib. Apur. Semanal | Conteúdo do campo 67- vlrBaseCRSem da tag totApurSem; |
| Valor Base Trib. – Exig. Suspensa | Conteúdo do campo 68- vlrBaseCRSemSusp da tag totApurSem; |
| Natureza de Rendimento | Conteúdo do campo 69- natRend da tag totApurSem; |


| Valor Trib. Ret. Inf. Contrib. | Conteúdo do campo 71-vlrCRSemInf (tag totApurTribSem) |
| --- | --- |
| Valor Trib. Ret. Calc. RFB | Conteúdo do campo 72-vlrCRSemCalc (tag totApurTribSem) |
| Valor Trib. Não Efetuado Inf. Contrib. | Conteúdo do campo 73-vlrCRSemSuspInf (tag totApurTribSem) |
| Valor Trib. Não Efetuado Calc. RFB | Conteúdo do campo 74-vlrCRSemSuspCalc (tag totApurTribSem) |


| Per. Apur. Diária | Conteúdo do campo 76- perApurDia da tag totApurDia; |
| --- | --- |
| Cód. Receita | Conteúdo do campo 77-CRSem da tag totApurDia, formato válido 999999; |
| Valor Base Trib. Apur. Diária | Conteúdo do campo 78- vlrBaseCRDia da tag totApurDia; |
| Valor Base Trib. – Exig. Suspensa | Conteúdo do campo 79- vlrBaseCRDiaSusp da tag totApurDia; |
| Natureza de Rendimento | Conteúdo do campo 80- natRend da tag totApurDia; |


| Valor Trib. Ret. Inf. Contrib. | Conteúdo do campo 82-vlrCRDiaInf (tag totApurTribDia) |
| --- | --- |
| Valor Trib. Ret. Calc. RFB | Conteúdo do campo 83-vlrCRDiaCalc (tag totApurTribDia) |
| Valor Trib. Não Efetuado Inf. Contrib. | Conteúdo do campo 84-vlrCRDiaSuspInf (tag totApurTribDia) |
| Valor Trib. Não Efetuado Calc. RFB | Conteúdo do campo 85-vlrCRDiaSuspCalc (tag totApurTribDia) |
