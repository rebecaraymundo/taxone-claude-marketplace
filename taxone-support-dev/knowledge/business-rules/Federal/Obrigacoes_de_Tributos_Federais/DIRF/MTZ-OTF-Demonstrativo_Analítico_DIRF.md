# MTZ-OTF-Demonstrativo_Analítico_DIRF

- **Fonte:** MTZ-OTF-Demonstrativo_Analítico_DIRF.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 30 KB

---

# Obrigações de Tributos Federais \- Demonstrativo Analítico por Beneficiário

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3171\-A2

Obrigações de Tributos Federais \- Demonstrativo Analítico por Beneficiário

O relatório Demonstrativo na visão Analítica da DIRF não foi preparado para ler o Nùmero do Processo quando o Ano Base da declaração for a partir de 2010\.

OS3961

Obrigações de Tributos Federais – Gerar valores de Rendimentos, Deduções e Imposto Retido\.

O objetivo deste documento de requisito é permitir que o cliente ao gerar o relatório “Demonstrativo Analítico por Beneficiário” do módulo “Obrigações de Tributos Federais”, os valores de Rendimentos, Deduções e Imposto Retido sejam gerados normalmente\. Exemplo código 0473\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

O campo “Número do Processo” da tela de Demonstrativo Analítico deverá recuperar todos os Processos gerados da DIRF, independente do Ano Base \(Ano Calendário\)\.

OS3171\-A2

__RN02__

Ao gerar o relatório “Demonstrativo Sintético por Beneficiário” do módulo Obrigações de Tributos Federais, o sistema deverá gerar as colunas “Rendimentos”, “Deduções” e “Imposto Retido” a partir da Folha de Pagamento da seguinte forma:

- __Rendimentos:__ deverá ser informado o somatório de todo o valor do campo “Valor da Verba” da tela de Ficha Financeira \(campo 09 – VLR\_VERBA da SAFX21\) para o mês em questão, desde que a Verba mencionada esteja parametrizada na tela de Parâmetros por Verba como “Rendimentos Tributáveis” no campo “Parâmetros para DIRF”\.
- __Deduções:__ deverá ser informado o somatório de todo o valor do campo “Valor Verba” da tela de Ficha Financeira \(campos 09 – VLR\_VERBA da SAFX21\) para o mês em questão, desde que a Verba mencionada esteja parametrizada na tela de Parâmetros por Verba como “Deduções \(Previdência Oficial\)”, “Deduções \(Dependentes\)”, “Deduções \(Pensão Alimentícia\)” ou “Deduções \(Previdência Privada/FAPI\)” no campo “Parâmetros para DIRF”\.
- __Imposto Retido:__ deverá ser informado o somatório de todo o valor do campo “Valor da Verba” da tela de Ficha Financeira \(campo 09 – VLR\_VERBA da SAFX21\) para o mês em questão, desde que a Verba mencionada esteja parametrizada na tela de Parâmetros por Verba como “Imposto de Renda Retido” no campo “Parâmetros para DIRF”\.

CH2607\_2013

__RN03__

Caminho: Módulo Federal 🡪 Obrigações de Tributos Federais Menu: DIRF 🡪 Demonstrativo Analítico por Beneficiário

Inclusão das Informações referente a Quantidade e valores de “Rendimentos”, “Deduções” e “Retido” para Beneficiários Residentes no Exterior PF/PJ\.

o sistema deverá gerar as colunas “Rendimentos”, “Deduções” e “Imposto Retido” considerando a seguinte regra:

- __Rendimentos:__ deverá ser informado o somatório de todo o valor do campo Valor Bruto da tela de Controle de Tributos \(campo 14 – VLR\_BRUTO da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\) para o mês em questão\.
- __Deduções:__ deverá ser informado o somatório de todo o valor dos campos Valor INSS Retido – Terceiros, Valor Dependentes – Terceiros, Valor Previdência Privada e Valor Pensão Alimentícia da tela de Controle de Tributos \(campos 29 – VLR\_PREV\_PRIVADA, 30 – VLR\_PENS\_ALIMENT, 41 – VLR\_DED\_INSS\_TERC e 42 – VLR\_DED\_DEP\_TERC da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\) para o mês em questão\. Só será gerado está informação para beneficiário PF residente no Brasil\.
- __Imposto Retido:__ deverá ser informado o somatório de todo o valor do campo Valor Tributo da tela de Controle de Tributos \(campo 15 – VLR\_IR\_RETIDO da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\) para o mês em questão\.

Residentes no exterior pessoa Física e Jurídica \(UF=EX\)

O campo CPF/CNPJ\(SAFX04\) não deverá ser preenchido, para estes casos utiliza\-se a informação do ID Fiscal que quando preenchido considera\-se o beneficiário como pessoa física, quando não preenchido pessoa jurídica\.

OS3961

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

