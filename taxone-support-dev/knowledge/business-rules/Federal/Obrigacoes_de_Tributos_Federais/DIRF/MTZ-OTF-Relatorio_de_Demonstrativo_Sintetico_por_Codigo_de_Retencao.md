# MTZ-OTF-Relatorio_de_Demonstrativo_Sintetico_por_Codigo_de_Retencao

- **Fonte:** MTZ-OTF-Relatorio_de_Demonstrativo_Sintetico_por_Codigo_de_Retencao.docx
- **Modificado:** 2022-05-02
- **Tamanho:** 33 KB

---

    

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Relatório de Demonstrativo Sintético por Código de Retenção

Menu: Federal

Módulo: Obrigações de Tributos Federais

Menu: Federal >> Obrigações de Tributos Federais >> DIRF >> Demonstrativo >> Demonstrativo Sintético por Código de Retenção\.

* *

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3967

Tarso Lima

Conforme Chamado nº 5124/2013, o cliente solicitou que no Relatório de Demonstrativo Sintético por Código de Retenção tenha o campo “Código de Tributo” para facilitar a conferência das informações que serão confrontadas com a DIRF\.

16/09/2013

OS3960

Elenilson Coutinho

Conforme Chamado nº 2607/2013, o cliente solicitou que no Relatório de Demonstração Sintético por Código de Retenção seja exibida a soma das Deduções \(Previdência Oficial, Previdência Privada, Pensão Alimentícia e Dependentes\)\.

19/03/2015

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN01__

Criar o campo “ Código de Tributo” no Relatório de Demonstrativo Sintético por Código de Retenção\.

O novo campo trará as informações do “Código do Tributo” da DIRF\.

O novo campo que contemplará o“Código de Tributo” no “Relatório de Demonstrativo Sintético por Código de Retenção” deverá vir do campo “Tributos” da tela “Controle de Tributos”\.

__OS3967__

__RN02__

A somatoria do “Código de Tributo” dos campos: “Rendimento”, “Deduções” e “Imposto de Renda” devem sair dos seguintes campos:

\- Valor Bruto \(Rendimento\)

\- Valor Previdencia Privada \(Deduções\)

  Valor INSS

  Pensão Alimenicia

  Valor Dependentes

__OBS:__ A composição das deduções conforme acima, será válida somente para pessoas físicas\. Para pessoas jurídicas, não existem as deduções legais, conforme testes no PGD da DIRF 2014\.

\-Valor IR Retido \(Imposto Retido\)

__OS3967__

__RN03__

A somatoria do “Código de Retenção” será a soma dos “Códigos Tributos” \(Rendimento, Deduções e Imposto de Retido\)

__OS3967__

__RN04__

As informações serão recuperadas da tabela de Controle de Tributos – X53\_RETENCAO\_IRRF\. Caso exista registro na tabela X530\_RETIFICACAO\_IRRF esse registro deve ser recuperado ao invés do registro da tabela X53\_RETENCAO\_IRRF\.

Caso existam mais de um registro na tabela X530\_RETIFICACAO\_IRRF, deve ser recuperado o registro com a Data de Retificação mais recente\.

__OBS:__ vale salientar que o cliente deve ter gerado a DIRF previamente para poder gerar o relatório, pois o relatório está atrelado ao número de processo sistêmico gerado pela DIRF\. 

__OS3967__

__RN05__

O Código de Retenção não sofre nenhuma transformação na geração das obrigações acessórias e/ou relatórios de apoio\. O Código de Retenção que será considerado no relatório é também recuperado da X53\_RETENCAO\_IRRF/ X530\_RETIFICACAO\_IRRF\.

__OS3967__

__RN03__

Módulo: Federal 🡪 Obrigações de Tributos Federais

Menu: DIRF🡪 Demonstrativo 🡪 Demonstrativo Sintético por Código de Retenção

__Deduções:__ deverá ser informado o valor do campo \(VLR\_VERBA\) da SAFX21, conforme parametrização referente a deduções na tela Parâmetros/Verba \(Módulo >> Federal >> Obrigações de Tributos Federais –Menu >> Parâmetros\)\. 

__OS3960__

