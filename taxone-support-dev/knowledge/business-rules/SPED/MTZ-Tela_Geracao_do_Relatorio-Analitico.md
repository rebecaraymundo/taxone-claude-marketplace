# MTZ-Tela_Geracao_do_Relatorio-Analitico

> Fonte: MTZ-Tela_Geracao_do_Relatorio-Analitico.docx



## Tela Geração do Relatório Sintético/Analítico



Menu: SPED
Módulo: ECD
Menu: Relatórios > Geração do Relatório Sintético/Analítico.




DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO






| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS4067 | Tarso Lima | O objetivo do campo será buscar as informações do plano de conta, uniformizando as demostrações contabeis da empresa.    Como escopo da atualização, teremos:  Criação do campo “Versão do Plano Referencial” na tela Geração do Relatório Sintético/Analítico  . | 10/09/2013 |
| OS3960 | Relatório Analítico por Beneficiário – Valor das deduções | Conforme Chamado nº 2607/2013, o cliente solicitou que no Relatório de Demonstração Sintético por Código de Retenção seja exibida a soma das Deduções (Previdência Oficial, Previdência Privada, Pensão Alimentícia e Dependentes). | 02/03/2015 |


| Cód. |  | DR |
| --- | --- | --- |
| RN01 | Campo Versão  Incluir na tela Geração do Relatório Sintético/Analítico o Campo “Versão do Plano Referencial”.  Deverá ser um campo do tipo lista, e servirá para selecionar a “Versão do Plano Referencial” do Plano Contabil.  Deverá conter a opções “1.00 e 3.00” em sua lista, e ao abrir a tela o mesmo deverá estar selecionado 1.0 por Default. | OS4067 |
| RN02 | Relatório: Módulo: Federal > Obrigações de Tributos Federais Menu: DIRF > Demonstrativo > Demonstrativo Analítico por Beneficiário Este relatório no campo Deduções: deverá ser informado o somatório de todo o valor dos campos Valor INSS Retido – Terceiros, Valor Dependentes – Terceiros, Valor Previdência Privada e Valor Pensão Alimentícia da tela de Controle de Tributos (campos 29 – VLR_PREV_PRIVADA, 30 – VLR_PENS_ALIMENT, 41 – VLR_DED_INSS_TERC e 42 – VLR_DED_DEP_TERC da SAFX53 ou X530_RETIFICACAO_IRRF mais recente) para o mês em questão. | OS3960 |
