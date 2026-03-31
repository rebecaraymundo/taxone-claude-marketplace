# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2101

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2101.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Regras de Importação Online e Batch SAFX2101 – Contas Referenciais x Plano de Contas

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-28929

Alessandra Cristina Navatta

Incluir validação para aceitar associação apenas em contas referenciais e contas contábeis do tipo analítica\.

Atenção: Não foi feita a engenharia reversa da importação da SAFX2101, caso necessário, esta atividade será realizada em demanda futura\.

MFS30566

Liliane Videira Assaf

Alteração nas regras RN01, RN02, RN03, para permitir associação de contas referenciais e contábeis do tipo Sintética, para o Plano Referencial COSIF\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN01

__Campo 01 \- Código Conta Contábil__

__Tabela de cadastro correspondente: __Tabela do Plano de Contas \- \(SAFX2002\)

__Tratamentos:__

Caso o campo 05 – Entidade Responsável seja __diferente__ de __20__ \- Banco Central do Brasil \(COSIF\), então:

           Somente é aceita Conta Contábil \(SAFX2002\) com Indicador = “A” \(conta analítica\)\. 

\- Se a conta informada não estiver cadastrada com campo ‘IND\_CONTA’ = ‘A’ – Analítica, exibir a mensagem: 

“Conta Contábil informada não é do tipo analítica\. Somente são aceitas Contas Contábeis Analíticas para esta Associação\.”

Caso o campo 05 – Entidade Responsável seja __igual__ a __20__ \- Banco Central do Brasil \(COSIF\), então:

           São aceitas Contas Contábeis \(SAFX2002\) com Indicador = “A” \(conta analítica\) e 

                                                                                                            “S” \(conta sintética\)\.

MFS\-28929

MFS\-30566

RN02

__Campo 02 \- Indicador da Conta__

Caso o campo 05 – Entidade Responsável seja __diferente__ de __20__ \- Banco Central do Brasil \(COSIF\), então:

           Somente é aceito o Indicador da Conta = “A” \(conta analítica\)\. 

Caso o campo 05 – Entidade Responsável seja __igual__ a __20__ \- Banco Central do Brasil \(COSIF\), então:

           São aceitos os Indicadores da Conta = “A” \(conta analítica\) e 

                                                                          “S” \(conta sintética\)\.

MFS\-30566

RN03

__Campo 03 \- Código Conta Referencial__

__Tabela de cadastro correspondente: __Plano de Contas Referencial \(SPED Contábil\) \- \(TFIX64\)\.

Tratamentos 

Caso o campo 05 – Entidade Responsável seja __diferente__ de __20__ \- Banco Central do Brasil \(COSIF\), então:

           Somente é aceita Conta Referencial \(TFIX64\) com Indicador = “A” \(conta analítica\)\. 

\- Se a conta informada não estiver cadastrada com campo ‘IND\_CONTA’ = ‘A’ – Analítica, exibir a mensagem: “Conta Referencial informada não é do tipo analítica\. Somente são aceitas Contas Referenciais Analíticas para esta Associação\.“

Caso o campo 05 – Entidade Responsável seja __igual__ a __20__ \- Banco Central do Brasil \(COSIF\), então:

           São aceitas Contas Referenciais \(TFIX64\) com Indicador = “A” \(conta analítica\) e 

                                                                                                          “S” \(conta sintética\)\.

MFS\-28929

MFS\-30566

RN04

__Campo 04 \- Versão da Conta Referencial__

__Tabela de cadastro correspondente__: Plano de Contas Referencial \(SPED Contábil\) \- \(TFIX64\)\.

Valores aceitos: 1\.00, 3\.00\.

MFS\-30566

RN02

__Campo 05 \- Código da Entidade Responsável__

Tabela de cadastro correspondente: Plano de Contas Referencial \(SPED Contábil\) \- \(TFIX64\)\.

Tratamentos 

Caso o campo 04 \- Versão da Conta Referencial seja 1\.00 então

Código da Entidade Responsável válidos são: 00, 10, 20\.

Caso o campo 04 \- Versão da Conta Referencial seja 3\.00 então

Código da Entidade Responsável válidos são: 00, 10, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9\.

MFS\-30566

RN02

__Campo 06 \- Código do Centro de Custo__

Tabela de cadastro correspondente: Tabela de Centro de Custo  \- \(SAFX2003\)\.

MFS\-30566

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

