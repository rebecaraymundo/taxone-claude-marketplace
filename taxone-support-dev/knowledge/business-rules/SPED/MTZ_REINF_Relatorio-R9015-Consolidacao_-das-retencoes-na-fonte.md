# MTZ_REINF_Relatorio-R9015-Consolidacao -das-retencoes-na-fonte

> Fonte: MTZ_REINF_Relatorio-R9015-Consolidacao -das-retencoes-na-fonte.docx


THOMSON REUTERS

Módulo REINF

Relatório de Conferência do Evento R-9015 (Consolidação das Retenções na Fonte)


Localização: Menu SPED, módulo EFD – Reinf, menu Relatórios à  Conferência dos Eventos  à R-9015 (Consolidação das Retenções na Fonte)





DOCUMENTO DE REQUISITO








Sumário

1.	Regras Gerais	3
2.	Layout da Tela	4
3.	Regras de Funcionamento dos Campos	5
4.	Regras da Recuperação dos Dados	6
5.	Layout e Preenchimento dos Campos no Relatório	7




















## Regras Gerais


Relatório criado com objetivo de possibilitar a consulta dos valores calculados pelo Fisco retorno do evento R-9015. Este relatório apresenta as informações da geração a partir da versão 2.1.1 do REINF.















## Layout da Tela










## Regras de Funcionamento dos Campos





## Regras da Recuperação dos Dados



A origem dos dados para emissão do relatório tem como base os eventos R-4099:

Para cada evento R-4099 recuperado conforme regra acima (***), será listado no relatório as informações do evento R-9015 correspondente.




Para cada R-9015:

Será gerado um relatório conforme o layout anexo (“Layout_Relatorio_Conferencia_R-9015.xlsx”).


No cabeçalho será demonstrado a empresa e o estabelecimento referentes ao evento R-9015 em questão.


Ordenação dos dados para apresentação no relatório:

O relatório será ordenado pelas informações de empresa e estabelecimento e evento que aparecem no relatório:

- Razão Social da Empresa (o cabeçalho mostra apenas a razão social da empresa);
- Código do Estabelecimento;
- Evento


## Layout e Preenchimento dos Campos no Relatório



Abas geradas: Parâmetros, Processos, Arquivos, Relatório (conforme padrão do produto)
Layout do relatório exibido em tela (Relatório): Vide planilha “Layout_Relatorio_Conferencia_R-9015.xlsx”, considerando o layout, formato e label indicado na planilha ’Conferência R-9015 – TELA’.
Formato do arquivo (gerado na aba Arquivos): .CSV. Apresentar as colunas considerando o layout, formato e label indicado na planilha ’Conferência R-9015 – CSV’, do arquivo “Layout_Relatorio_Conferencia_R-9015.xlsx”




A seguir será descrito o preenchimento dos campos e suas respectivas do relatório (apresentado em tela), a partir do evento R-9015

Linhas do cabeçalho:

Como o relatório é por evento-9015, no cabeçalho sempre aparecerá a empresa e estabelecimento referentes aos eventos em questão.





Linhas de detalhe de identificação do evento R-9015:




Não deverá ser apresentado as informações dos períodos de apuração não existentes no R-9015


Linhas de detalhe dos totais das retenções de apuração com período mensal:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração mensal:”)


Nesta linha são demonstrados os totais das retenções de período de apuração mensal na tag totApurMen.


Para cada código de receita e natureza de rendimento serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurMen.




Linhas de detalhe dos totais das retenções de apuração com período quinzenal:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração quinzenal.:”)

Nesta linha são demonstrados os totais das retenções de período de apuração quinzenal na tag totApurQui.

Para cada período de apuração, código de receita e natureza de rendimento, serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurQui.


Linhas de detalhe dos totais das retenções de apuração com período decendial:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração decendial:”)

Nesta linha são demonstrados os totais das retenções de período de apuração decendial na tag totApurDec.

Para cada período de apuração e código de receita serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurDec.



Linhas de detalhe dos totais das retenções de apuração com período semanal:

(“Totalizador das bases de cálculo e das retenções dos tributos com apuração semanal.:”)

Nesta linha são demonstrados os totais das retenções de período de apuração semanal na tag totApurSem.

Para cada período de apuração, código de receita e natureza de rendimento serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurSem.


Linhas de detalhe dos totais das retenções de apuração com período de apuração diária:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração diária:”)

Nesta linha são demonstrados os totais das retenções de período de apuração diária na tag totApurDia.

Para cada período de apuração, código de receita e natureza de rendimento, serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurDia.





Linhas de informações consolidadas relativas aos tributos de apuração com período mensal:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração mensal:”)

Nesta linha são demonstrados os totais dos tributos de período de apuração mensal na tag totApurMen.

Para cada código de receita serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurMen.






Linhas de informações consolidadas relativas aos tributos de apuração com período quinzenal:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração quinzenal.:”)

Nesta linha são demonstrados os totais dos tributos de período de apuração quinzenal na tag totApurQui.

Para cada período de apuração e código de receita, serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurQui.


Linhas de informações consolidadas relativas aos tributos de apuração com período decendial:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração decendial:”)

Nesta linha são demonstrados os totais dos tributos de período de apuração decendial na tag totApurDec.

Para cada período de apuração e código de receita serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurDec.



Linhas de informações consolidadas relativas aos tributos de apuração com período semanal:

(“Totalizador das bases de cálculo e das retenções dos tributos com apuração semanal:”)

Nesta linha são demonstrados os totais dos tributos de período de apuração semanal na tag totApurSem.

Para cada período de apuração e código de receita que serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurSem.


Linhas de informações consolidadas relativas aos tributos de apuração com período diária:

(“Totalizador das bases de cálculo e das retenções dos tributos com período de apuração diária:”)

Nesta linha são demonstrados os totais dos tributos de período de apuração diária na tag totApurDia.

Para cada período de apuração e código de receita, serão demonstrados o valor total da base de cálculo, e a seguir, os valores calculados existentes na tag totApurDia.



| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-79971 | Alessandra Cristina Navatta | Criação do relatório de conferência do evento R-9015 (Consolidação das Retenções na Fonte) | 06/01/2023 |
| MFS-79971 | Alessandra Cristina Navatta | Inclusão do layout em formato CSV | 06/03/2023 |
| MFS-569151 | Alessandra Cristina Navatta | Ajustada a referência dos campos, já que houve inclusão do campo 22-tpEV (tag infoRecEv) no layout, mas, não há impacto nas regras.  Não houve impacto na implementação do relatório | 21/09/2023 |


| Sobre o evento R-9015:  Estes valores estarão no evento R-9015, evento gerado pelo Fisco, e enviado aos contribuintes após o recebimento do evento R-4099 (junto com a mensagem de retorno).e são obtidas no XML de retorno enviado pelo integrador do Onesource.  O Fisco envia o R-9015 sempre que um evento R-4099 é recepcionado com sucesso (status de retorno do Onesource = “Evento recebido pelo Fisco com sucesso” ou “Evento recebido pelo Fisco com advertência”). O Onesource processa estes dados e retorna para o MSAF um XML (através da STG_EVENTOS_REINF_IN), que contém entre outras informações, estes valores gerados pelo Fisco.  No módulo REINF (DW) estes dados são recuperados para emissão do relatório. |
| --- |


| Campo | Tipo | Obrig | Ed | Formato / Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Período | Data (mês e ano) | S | S | (MM/AAAA) | Mês e ano do período para emissão do relatório.  Deve ser um mês válido. |
| Multiempresas | Alfanumérico | N | S | Default:  Desmarcado | Na abertura da tela esta opção aparecerá sempre desmarcada. |
| Empresa / Estabelecimento | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos para seleção do usuário.  A lista dos estabelecimentos depende do período e da opção “Multiempresas”. Por isso, será montada somente após o usuário informar o período.  Obs.: Sempre que o período ou a opção de multiempresa forem alterados, esta lista será refeita automaticamente.   Regra dos estabelecimentos a serem exibidos:   Será feita a pesquisa de todos os eventos R-4099 existentes para o período informado, cujo status indique que o evento já foi recebido pelo Fisco com sucesso/advertência.  (A pesquisa é baseada na tabela “OC” do R-4099,  e a partir dela, se obtém a empresa, estab. e período na PGER_APUR)   Serão disponibilizados para seleção apenas os estabelecimentos dos eventos R-4099 encontrados conforme a condição acima.  Além das condições acima, deve-se observar também a opção de multiempresas:  Se opção “Multiempresas” desmarcada:      Considera apenas os estabelecimentos da empresa do login; Senão      Considera os estabelecimentos de todas as empresas;  Para cada estabelecimento a ser exibido, será mostrado:  - Código da empresa; - Código do estabelecimento; - Razão Social do estabelecimento; |
| Selecionar todos / Desmarcar todos | Alfanumérico | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados. |


| (***) Regra de montagem da lista dos estabelecimentos, descrita no item 3, campo “Empresa/Estabelecimento”. Lembrando que, pela regra, são demonstrados apenas os estabelecimentos com R-4099 já entregues ao Fisco com sucesso e ou advertência, e neste caso, terão um evento R-9015 específico; |
| --- |


| Primeira linha | Razão social da empresa referente ao evento R-9015 em questão; Data da emissão do relatório; Página; |
| --- | --- |
| Segunda linha | Informações do estabelecimento referente aos eventos R-4099; -Código e razão social -Inscrição estadual -CNPJ |
| Terceira e quarta linha | Título do relatório (“Relatório de Conferência do R-9015 – Consolidação das Retenções na Fonte”); Período – Mês /Ano informados na tela da geração |


| Número Inscrição Contribuinte | Conteúdo do campo 08-nrInsc (tag ideContri); |
| --- | --- |
| Tipo | Se campo 07-tpInsc = 1 (tag ideContri), preencher com “CNPJ”; Se campo 07-tpInsc = 2 (tag ideContri), preencher com “CPF”; |
| ID Evento R-9015 | Conteúdo do campo 03-Id (tag evtRet) |
| ID Evento R-4099 | Conteúdo do campo 23-idEv (tag infoRecEv) |
| Protocolo da Entrega do Lote | Conteúdo do campo 20-nrProtLote (tag infoRecEv) |
| N. Recibo Arquivo | Conteúdo do campo 19-nrRecArqBase (tag infoTotal) |


| Cód Rec | Conteúdo do campo 29-CRMen da tag totApurMen, formato válido 999999; |
| --- | --- |
| Valor Trib Ret Inf Contrib | Conteúdo do campo 30- vlrCRMenInf da tag totApurMen; |
| Valor Trib Ret Calc. | Conteúdo do campo 31- vlrCRMenCalc da tag totApurMen; |
| Valor Trib Ret DCTF | Conteúdo do campo 32- vlrCRMenDCTF da tag totApurMen; |
| Valor Trib não Efetuada Inf. ConTrib | Conteúdo do campo 33- vlrCRMenSuspInf da tag totApurMen; |
| Valor Trib não Efetuada Calc. | Conteúdo do campo 34- vlrCRMenSuspCalc da tag totApurMen; |
| Valor Trib não Efetuada DCTF | Conteúdo do campo 35- vlrCRMenSuspDCTF da tag totApurMen; |
| Nat Rend | Conteúdo do campo 36-natRend da tag totApurMen; |


| Per Apur | Conteúdo do campo 38- perApurQui da tag totApurQui; |
| --- | --- |
| Cód. Rec | Conteúdo do campo 39-CRQui da tag totApurQui, formato válido 999999; |
| Valor Trib Ret Inf ConTrib | Conteúdo do campo 40- vlrCRQuiInf da tag totApurQui; |
| Valor Trib Ret Calc. | Conteúdo do campo 41- vlrCRQuiCalc da tag totApurQui; |
| Valor Trib Ret DCTF | Conteúdo do campo 42- vlrCRQuiDCTF da tag totApurQui; |
| Valor Trib não Efetuada Inf. ConTrib | Conteúdo do campo 43- vlrCRQuiSuspInf da tag totApurQui; |
| Valor Trib não Efetuada Calc. | Conteúdo do campo 44- vlrCRQuiSuspCalc da tag totApurQui; |
| Valor Trib não Efetuada DCTF | Conteúdo do campo 45- vlrCRQuiSuspDCTF da tag totApurQui; |
| Nat Rend | Conteúdo do campo 46- natRend da tag totApurQui; |


| Per Apur | Conteúdo do campo 48- perApurDec da tag totApurDec; |
| --- | --- |
| Cód. Rec | Conteúdo do campo 49-CRDec da tag totApurDec, formato válido 999999; |
| Valor Trib Ret Inf. ConTrib | Conteúdo do campo 50- vlrCRDecInf da tag totApurDec; |
| Valor Trib Ret Calc. | Conteúdo do campo 51- vlrCRDecCalc da tag totApurDec; |
| Valor Trib Ret DCTF | Conteúdo do campo 52- vlrCRDecDCTF da tag totApurDec; |
| Valor Trib Apur não Efetuada Inf. ConTrib | Conteúdo do campo 53- vlrCRDecSuspInf da tag totApurDec; |
| Valor Trib Apur não Efetuada Calc. | Conteúdo do campo 54- vlrCRDecSuspCalc da tag totApurDec; |
| Valor Trib Apur não Efetuada DCTF | Conteúdo do campo 55- vlrCRDeciSuspDCTF da tag totApurDec; |
| Nat Rend | Conteúdo do campo 56- natRend da tag totApurDec; |


| Per Apur | Conteúdo do campo 58- perApurSem da tag totApurSem; |
| --- | --- |
| Cód. Rec | Conteúdo do campo 59-CRSem da tag totApurSem, formato válido 999999; |
| Valor Trib Ret Inf ConTrib | Conteúdo do campo 60- vlrCRSemInf da tag totApurSem; |
| Valor Trib Ret Calc | Conteúdo do campo 61- vlrCRSemCalc da tag totApurSem; |
| Valor Trib Ret DCTF | Conteúdo do campo 62- vlrCRSemDCTF da tag totApurSem; |
| Valor Trib não Efetuada Inf ConTrib | Conteúdo do campo 63- vlrCRSemSuspInf da tag totApurSem; |
| Valor Trib não Efetuada Calc | Conteúdo do campo 64- vlrCRSemSuspCalc da tag totApurSem; |
| Valor Trib não Efetuada DCTF | Conteúdo do campo 65- vlrCRSemSuspDCTF da tag totApurSem; |
| Nat Rend | Conteúdo do campo 66- natRend da tag totApurSem; |


| Per Apur | Conteúdo do campo 68- perApurDia da tag totApurDia; |
| --- | --- |
| Cód Rec | Conteúdo do campo 69-CRDia da tag totApurDia, formato válido 999999; |
| Valor TribRet Inf ConTrib | Conteúdo do campo 70- vlrCRDiaInf da tag totApurDia; |
| Valor Trib Ret Calc | Conteúdo do campo 71- vlrCRDiaCalc da tag totApurDia; |
| Valor Trib Ret DCTF | Conteúdo do campo 72- vlrCRDiaDCTF da tag totApurDia; |
| Valor Trib não Efetuada Inf ConTrib | Conteúdo do campo 73- vlrCRDiaSuspInf da tag totApurDia; |
| Valor Trib não Efetuada Calc | Conteúdo do campo 74- vlrCRDiaSuspCalc da tag totApurDia; |
| Valor Trib não Efetuada DCTF | Conteúdo do campo 75- vlrCRDiaSuspDCTF da tag totApurDia; |
| Nat Rend | Conteúdo do campo 76- natRend da tag totApurDia; |


| Cód Rec - CR | Conteúdo do campo 79-CRMen da tag totApurMen, formato válido 999999; |
| --- | --- |
| Valor Trib Ret DCTF - CR | Conteúdo do campo 80- vlrCRMenDCTF da tag totApurMen; |
| Valor Trib não Efetuada DCTF - CR | Conteúdo do campo 81- vlrCRMenSuspDCTF da tag totApurMen; |


| Per Apur - CR | Conteúdo do campo 83- perApurQui da tag totApurQui; |
| --- | --- |
| Cód Rec - CR | Conteúdo do campo 84-CRQui da tag totApurQui, formato válido 999999; |
| Valor Trib Ret DCTF - CR | Conteúdo do campo 85- vlrCRQuiDCTF da tag totApurQui; |
| Valor Trib não Efetuada DCTF - CR | Conteúdo do campo 86- vlrCRQuiSuspDCTF da tag totApurQui; |


| Per Apur - CR | Conteúdo do campo 88- perApurDec da tag totApurDec; |
| --- | --- |
| Cód Rec - CR | Conteúdo do campo 89-CRDec da tag totApurDec, formato válido 999999; |
| Valor Trib Ret DCTF - CR | Conteúdo do campo 90- vlrCRDecDCTF da tag totApurDec; |
| Valor Trib não Efetuada DCTF - CR | Conteúdo do campo 91- vlrCRDeciSuspDCTF da tag totApurDec; |


| Per Apur - CR | Conteúdo do campo 93- perApurSem da tag totApurSem; |
| --- | --- |
| Cód Rec - CR | Conteúdo do campo 94-CRSem da tag totApurSem, formato válido 999999; |
| Valor Trib Ret DCTF - CR | Conteúdo do campo 95- vlrCRSemDCTF da tag totApurSem; |
| Valor Trib não Efetuada DCTF - CR | Conteúdo do campo 96- vlrCRSemSuspDCTF da tag totApurSem; |


| Per Apur - CR | Conteúdo do campo 98- perApurDia da tag totApurDia; |
| --- | --- |
| Cód Rec - CR | Conteúdo do campo 99-CRDia da tag totApurDia, formato válido 999999; |
| Valor Trib Ret DCTF - CR | Conteúdo do campo 100- vlrCRDiaDCTF da tag totApurDia; |
| Valor Trib não Efetuada DCTF - CR | Conteúdo do campo 101- vlrCRDiaSuspDCTF da tag totApurDia; |
