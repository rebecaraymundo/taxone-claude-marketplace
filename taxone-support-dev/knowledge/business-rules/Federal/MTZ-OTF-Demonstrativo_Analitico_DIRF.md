# MTZ-OTF-Demonstrativo_Analítico_DIRF

> Fonte: MTZ-OTF-Demonstrativo_Analítico_DIRF.docx


## Obrigações de Tributos Federais - Demonstrativo Analítico por Beneficiário





DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO





Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:


Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:





| DR | Nome | Descrição |
| --- | --- | --- |
| OS3171-A2 | Obrigações de Tributos Federais - Demonstrativo Analítico por Beneficiário | O relatório Demonstrativo na visão Analítica da DIRF não foi preparado para ler o Nùmero do Processo quando o Ano Base da declaração for a partir de 2010. |
| OS3961 | Obrigações de Tributos Federais – Gerar valores de Rendimentos, Deduções e Imposto Retido. | O objetivo deste documento de requisito é permitir que o cliente ao gerar o relatório “Demonstrativo Analítico por Beneficiário” do módulo “Obrigações de Tributos Federais”, os valores de Rendimentos, Deduções e Imposto Retido sejam gerados normalmente. Exemplo código 0473. |


| Cód. | Descrição | DR |
| --- | --- | --- |
| RN01 | O campo “Número do Processo” da tela de Demonstrativo Analítico deverá recuperar todos os Processos gerados da DIRF, independente do Ano Base (Ano Calendário). | OS3171-A2 |
| RN02 | Ao gerar o relatório “Demonstrativo Sintético por Beneficiário” do módulo Obrigações de Tributos Federais, o sistema deverá gerar as colunas “Rendimentos”, “Deduções” e “Imposto Retido” a partir da Folha de Pagamento da seguinte forma:  Rendimentos: deverá ser informado o somatório de todo o valor do campo “Valor da Verba” da tela de Ficha Financeira (campo 09 – VLR_VERBA da SAFX21) para o mês em questão, desde que a Verba mencionada esteja parametrizada na tela de Parâmetros por Verba como “Rendimentos Tributáveis” no campo “Parâmetros para DIRF”. Deduções: deverá ser informado o somatório de todo o valor do campo “Valor Verba” da tela de Ficha Financeira (campos 09 – VLR_VERBA da SAFX21) para o mês em questão, desde que a Verba mencionada esteja parametrizada na tela de Parâmetros por Verba como “Deduções (Previdência Oficial)”, “Deduções (Dependentes)”, “Deduções (Pensão Alimentícia)” ou “Deduções (Previdência Privada/FAPI)” no campo “Parâmetros para DIRF”. Imposto Retido: deverá ser informado o somatório de todo o valor do campo “Valor da Verba” da tela de Ficha Financeira (campo 09 – VLR_VERBA da SAFX21) para o mês em questão, desde que a Verba mencionada esteja parametrizada na tela de Parâmetros por Verba como “Imposto de Renda Retido” no campo “Parâmetros para DIRF”. | CH2607_2013 |
| RN03 | Caminho: Módulo Federal  Obrigações de Tributos Federais Menu: DIRF  Demonstrativo Analítico por Beneficiário  Inclusão das Informações referente a Quantidade e valores de “Rendimentos”, “Deduções” e “Retido” para Beneficiários Residentes no Exterior PF/PJ.  o sistema deverá gerar as colunas “Rendimentos”, “Deduções” e “Imposto Retido” considerando a seguinte regra:  Rendimentos: deverá ser informado o somatório de todo o valor do campo Valor Bruto da tela de Controle de Tributos (campo 14 – VLR_BRUTO da SAFX53 ou X530_RETIFICACAO_IRRF mais recente) para o mês em questão. Deduções: deverá ser informado o somatório de todo o valor dos campos Valor INSS Retido – Terceiros, Valor Dependentes – Terceiros, Valor Previdência Privada e Valor Pensão Alimentícia da tela de Controle de Tributos (campos 29 – VLR_PREV_PRIVADA, 30 – VLR_PENS_ALIMENT, 41 – VLR_DED_INSS_TERC e 42 – VLR_DED_DEP_TERC da SAFX53 ou X530_RETIFICACAO_IRRF mais recente) para o mês em questão. Só será gerado está informação para beneficiário PF residente no Brasil. Imposto Retido: deverá ser informado o somatório de todo o valor do campo Valor Tributo da tela de Controle de Tributos (campo 15 – VLR_IR_RETIDO da SAFX53 ou X530_RETIFICACAO_IRRF mais recente) para o mês em questão.   Residentes no exterior pessoa Física e Jurídica (UF=EX)  O campo CPF/CNPJ(SAFX04) não deverá ser preenchido, para estes casos utiliza-se a informação do ID Fiscal que quando preenchido considera-se o beneficiário como pessoa física, quando não preenchido pessoa jurídica. | OS3961 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |


| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
