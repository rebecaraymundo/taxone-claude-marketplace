# MTZ-Tela_Geracao_do_Relatorio-Analitico

- **Fonte:** MTZ-Tela_Geracao_do_Relatorio-Analitico.docx
- **Modificado:** 2022-02-28
- **Tamanho:** 30 KB

---

    

# Tela Geração do Relatório Sintético/Analítico

Menu: SPED

Módulo: ECD

Menu: Relatórios > Geração do Relatório Sintético/Analítico\.

* *

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS4067

Tarso Lima

O objetivo do campo será buscar as informações do plano de conta, uniformizando as demostrações contabeis da empresa\.  

Como escopo da atualização, teremos:

Criação do campo “Versão do Plano Referencial” na tela Geração do Relatório Sintético/Analítico  \.

10/09/2013

OS3960

Relatório Analítico por Beneficiário – Valor das deduções

Conforme Chamado nº 2607/2013, o cliente solicitou que no Relatório de Demonstração Sintético por Código de Retenção seja exibida a soma das Deduções \(Previdência Oficial, Previdência Privada, Pensão Alimentícia e Dependentes\)\.

02/03/2015

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN01__

Campo Versão

Incluir na tela Geração do Relatório Sintético/Analítico o Campo “Versão do Plano Referencial”\.

Deverá ser um campo do tipo lista, e servirá para selecionar a “Versão do Plano Referencial” do Plano Contabil\.

Deverá conter a opções “1\.00 e 3\.00” em sua lista, e ao abrir a tela o mesmo deverá estar selecionado 1\.0 por Default\.

__OS4067__

__RN02__

 __Relatório:__

Módulo: Federal > Obrigações de Tributos Federais

Menu: DIRF > Demonstrativo > Demonstrativo Analítico por Beneficiário

Este relatório no campo __Deduções:__ deverá ser informado o somatório de todo o valor dos campos Valor INSS Retido – Terceiros, Valor Dependentes – Terceiros, Valor Previdência Privada e Valor Pensão Alimentícia da tela de Controle de Tributos \(campos 29 – VLR\_PREV\_PRIVADA, 30 – VLR\_PENS\_ALIMENT, 41 – VLR\_DED\_INSS\_TERC e 42 – VLR\_DED\_DEP\_TERC da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\) para o mês em questão\.

 

__OS3960__

