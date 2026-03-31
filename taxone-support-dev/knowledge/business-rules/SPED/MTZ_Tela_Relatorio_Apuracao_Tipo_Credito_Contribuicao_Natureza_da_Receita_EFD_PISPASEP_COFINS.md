# MTZ_Tela_Relatorio_Apuracao_Tipo_Credito_Contribuicao_Natureza da Receita_EFD_PISPASEP_COFINS

> Fonte: MTZ_Tela_Relatorio_Apuracao_Tipo_Credito_Contribuicao_Natureza da Receita_EFD_PISPASEP_COFINS.docx






THOMSON REUTERS

Matriz da Tela/Relatório Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita) –
EFD PIS/PASEP-COFINS


Localização:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu:      Relatórios          >> Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	12
3.	Relatório	13


## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Relatórios          >> Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)


## Sugestão de Layout



## Relatório


Ver documento matriz MTZ_Relatorio_Apuração_Tipo_Crédito_Contribuição_Natureza da Receita_EFD_PISPASEP_COFINS.doc





| OS/CH | Nome | Descrição |
| --- | --- | --- |
|  |  |  |
| MFS-61786 | Elisabete Costa | Criação das telas de Emissão do Relatório Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita) |
|  |  |  |
|  |  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo | Texto | S | S | MM/YYYY | Período: |  |
| Tipo | Texto | S | S | Formato:  Radio Button Group  Default:  Habilitado Sintético e Analítico | Deve ser informado o tipo de relatório que é emitido.  Conteúdo:  Tipo do Demonstrativo: Analítico  Sintético |  |
| Tipo | Texto | S | S | Chek BOX | DEMONSTRATIVO DE APURAÇÃO POR TIPO DE CRÉDITO |  |
|  |  |  |  |  |  |  |
| Tipo | Texto | S | S | Formato:  Radio Button Group  Default:  Habilitado Sintético e Analítico | Considerações:  Se o usuário optar em emitir o Relatório Analítico, após a emissão é apresentado cada documento fiscal gerado no registro A100/A170, C100/C170, C190/C195, C395/C396, C500/C505, D100/D105, D500/D505, F100, F120, F130, F150, F205, F210 e F800 vinculado a composição no detalhamento do tipo de crédito.  Se o usuário optar em emitir o Relatório Sintético, após emissão é apresentado à totalização dos valores de cada registro vinculado a composição do tipo de contribuição.  No DW e no TAX ONE as duas opções Sintético e Analítico permanecem habilitadas. |  |
| Cód.Tipo Crédito | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Neste campo deverá apresentada uma lista recuperada da TFIX93.  Além de apresentar as opções da TFIX93, deve apresentar a opção branca  Conteúdo: <*Todas* > 	        Opção   101-Credito vinculado a receita tributada no mercado interno - Aliquota Basica                                          102-Credito vinculado a receita tributada no mercado interno - Aliquotas Diferenciadas                                  103-Credito vinculado a receita tributada no mercado interno - Aliquota por Unidade de Produto                          104-Credito vinculado a receita tributada no mercado interno - Estoque de Abertura                                      105-Credito vinculado a receita tributada no mercado interno - Aquisicao Embalagens para revenda                        106-Credito vinculado a receita tributada no mercado interno - Presumido da Agroindustria                               107-Credito vinculado a receita tributada no mercado interno - Outros Creditos Presumidos                               108-Credito vinculado a receita tributada no mercado interno - Importacao                                               109-Credito vinculado a receita tributada no mercado interno - Atividade Imobiliaria                                    199-Credito vinculado a receita tributada no mercado interno - Outros                                                   201-Credito vinculado a receita nao tributada no mercado interno - Aliquota Basica                                      202-Credito vinculado a receita nao tributada no mercado interno - Aliquotas Diferenciadas                              203-Credito vinculado a receita nao tributada no mercado interno - Aliquota por Unidade de Produto                      204-Credito vinculado a receita nao tributada no mercado interno - Estoque de Abertura                                  205-Credito vinculado a receita nao tributada no mercado interno - Aquisicao Embalagens para revenda                    206-Credito vinculado a receita nao tributada no mercado interno - Presumido da Agroindustria                           207-Credito vinculado a receita nao tributada no mercado interno - Outros Creditos Presumidos                           208-Credito vinculado a receita nao tributada no mercado interno - Importacao                                           299-Credito vinculado a receita nao tributada no mercado interno - Outros                                               301-Credito vinculado a receita de exportacao - Aliquota Basica                                                         302-Credito vinculado a receita de exportacao - Aliquotas Diferenciadas                                                 303-Credito vinculado a receita de exportacao - Aliquota por Unidade de Produto                                         304-Credito vinculado a receita de exportacao - Estoque de Abertura                                                     305-Credito vinculado a receita de exportacao - Aquisicao Embalagens para revenda                                       306-Credito vinculado a receita de exportacao - Presumido da Agroindustria                                              307-Credito vinculado a receita de exportacao - Outros Creditos Presumidos                                              308-Credito vinculado a receita de exportacao - Importacao                                                              399-Credito vinculado a receita de exportacao - Outros |  |
| Nat. Base de Crédito | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Esse campo deve possuir as opções abaixo.  Esse campo não é de preenchimento Obrigatório.  Conteúdo: <*Todas* > (opção)  Aquisição de bens para revenda Aquisição de bens utilizados como insumo Aquisição de serviços utilizados como insumo Energia elétrica e térmica, inclusive sob a forma de vapor  Aluguéis de prédios Aluguéis de máquinas e equipamentos Armazenagem de mercadoria e frete na operação de venda Contraprestações de arrendamento mercantil Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito sobre encargos de depreciação). Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito com base no valor de aquisição). Amortização e Depreciação de edificações e benfeitorias em imóveis Devolução de Vendas Sujeitas à Incidência Não-Cumulativa Outras Operações com Direito a Crédito Atividade de Transporte de Cargas – Subcontratação Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária Atividade Imobiliária – Custo Orçado de unidade não concluída Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale-transporte, vale-refeição ou vale-alimentação, fardamento ou uniforme Estoque de abertura de bens |  |
| Registro | Texto | S | S | Formato:  Check Box  Default:  Habilitado e Todos Marcados | Esse campo deve possuir as opções abaixo. O campo é de preenchimento obrigatório. Além disso, por default  todas as opções: M100, M105,  M500, M505 devem ficar marcados. M100 – Crédito de PIS/PASEP Relativo ao Período M105 – Detalhamento da Base de Calculo do Crédito Apurado no Período – PIS/PASEP M500 – Crédito da COFINS Relativo ao Período M505 – Detalhamento da Base de Calculo do Crédito Apurado no Período – COFINS |  |
| Tipo | Texto | S | S | Formato:  Radio Button Group  Default:  Habilitado Sintético | Deve ser informado o tipo de relatório que é emitido.  Conteúdo: Analítico  Sintético  Considerações:  Se o usuário optar em emitir o Relatório Analítico, após a emissão é apresentado cada documento fiscal gerado no registro A100/A170, C100/C170 e C180/C181/C185 vinculado a composição no detalhamento do tipo de contribuição. Para os registros C381, C385, C481, C485, C491, C495, C601, C605, D201, D205, D300, D350, D601, D605, F100 e F200 são apresentadas cada linha de registro vinculado à composição no detalhamento do tipo de contribuição. Se o usuário optar em emitir o Relatório Sintético, após emissão é apresentado à totalização dos valores de cada registro vinculado a composição do tipo de contribuição. |  |
| Tipo | Texto | S | S | Chek BOX | DEMONSTRATIVO DE APURAÇÃO POR TIPO DE CONTRIBUIÇÃO |  |
| Tipo Contribuição | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Esse campo é utilizado para filtrar o código da natureza da base de crédito gerado nos registros M210 e M610 que deve ser apresentado no relatório.    Conteúdo: <*Todas* > (opção)  01 - Contribuição não-cumulativa apurada a alíquota básica  02 - Contribuição não-cumulativa apurada a alíquotas diferenciadas 03 - Contribuição não-cumulativa apurada a alíquota por unidade de medida de produto 04 - Contribuição não-cumulativa apurada a alíquota básica – Atividade Imobiliária 31 - Contribuição apurada por substituição tributária 32 - Contribuição apurada por substituição tributária – Vendas à Zona Franca de Manaus 51 - Contribuição cumulativa apurada a alíquota básica 52 - Contribuição cumulativa apurada a alíquotas diferenciadas 53 - Contribuição cumulativa apurada a alíquota por unidade de medida de produto 54 - Contribuição cumulativa apurada a alíquota básica – Atividade Imobiliária |  |
| Cód. Sit. Tributária | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Esse campo é utilizado para filtrar o código da situação tributária referente ao PIS/COFINS gerado nos registros M210 e M610 que deve ser apresentado no relatório.   Conteúdo: <*Todas* > (opção)  01 - Operação Tributável com Alíquota Básica 02 - Operação Tributável com Alíquota Diferenciada 03 - Operação Tributável com Alíquota por Unidade de Medida de Produto 04 - Operação Tributável Monofásica - Revenda a Alíquota Zero 05 - Operação Tributável por Substituição Tributária 06 - Operação Tributável a Alíquota Zero 07 - Operação Isenta da Contribuição 08 - Operação sem Incidência da Contribuição 09 - Operação com Suspensão da Contribuição 49 - Outras Operações de Saída |  |
| Cód. Registro Utilizado para Detalhar a Apuração | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Esse campo é utilizado para filtrar o código de registro utilizado para detalhar a apuração.  Conteúdo: <*Todas* > (opção)  A100/A170 – Nota Fiscal de Serviço C100/C170 – Nota Fiscal (Código 01, 1B, 04) e NF-e (Código 55) C180/C181/C185 – Consolidação de Notas Fiscais Eletrônicas Emitidas pela Pessoa Jurídica (Código 55) – Operações de Vendas C380/C381/C385 – Nota Fiscal de Venda a Consumidor (Código 02) – Consolidação de Documentos Emitidos C405/C481/C485 – Redução Z (Códigos 02 e 2D) C490/C491/C495 – Consolidação de Documentos Emitidos por ECF (Códigos 02, 2D) C600/C601/C605 – Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d’água C800 – Cupom Fiscal Eletrônico (Código 59) D200/D201/D205 – Resumo da Escrituração Diária – Prestação de Serviços de Transportes (Códigos 07, 08, 8B, 09, 10, 11, 26, 27 e 57) D300 – Resumo da Escrituração Diária (Código 13, 14, 15, 16 e 18) D350 – Resumo Diário de Cupom Fiscal Emitido por ECF (Códigos 2E, 13, 14, 15 e 16) D600/D601/D605 – Consolidação da Prestação de Serviço de Comunicação (Código 21) e de Serviço de Telecomunicação (Código 22) F100 – Demais Documentos e Operações Geradoras de Contribuição e Créditos F200 – Operações da Atividade Imobiliária – Unidade Imobiliária Vendida |  |
| Registros | Texto | S | S | Formato:  Check Box  Default:  Habilitado e Todos Marcados | Deve informar qual o registro da apuração da contribuição abaixo que deve ser apresentado no relatório. Para identificar os registros vinculados a composição do detalhamento do Tipo de Contribuição é necessário marcar as opções: "M210 e M610’’:  M200 - Consolidação da Contribuição para o PIS/PASEP do Período M210 - Detalhamento da Contribuição para o PIS/PASEP do Período M600 - Consolidação da Contribuição para a Segur.Social - COFINS do Período  M610 - Detalhamento da Contribuição para a Segur.Social - COFINS do Período |  |
| Tipo | Texto | S | S | Chek BOX | DEMONSTRATIVO DA APURAÇÃO POR TIPO DE NATUREZA DA RECEITA |  |
| Cód. Sit. Tributária Específica | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | O campo Cód. Sit. Tributária Específica deve possuir as opções abaixo.    Conteúdo: <*Todas* > (opção)  04  -  Operação Tributável Monofásica - Revenda a Alíquota Zero 05  -  Operação Tributável por Substituição Tributária 06 - Operação Tributável a Alíquota Zero 07 - Operação Isenta da Contribuição 08 - Operação sem Incidência da Contribuição 09 - Operação com Suspensão da Contribuição |  |
| Registro | Texto | S | S | Formato:  Check Box  Default:  Habilitado e Todos Marcados | Esse campo deve possuir as opções abaixo. O campo é de preenchimento obrigatório. Além disso, por default  todas as opções devem ficar marcados.  M400 - Rec.Isentas,Não Incid.Contrib.,Sujeitas a Alíq 0 ou Suspensão-PIS M410 – Det.Rec.Isentas,Não Incid.Contrib.,Sujeitas a Alíq 0 ou Suspensão-PIS M800 – Rec.Isentas,Não Incid.Contrib.,Sujeitas a Alíq. 0 ou Suspensão-COFINS M810 – Det.Rec..Isentas,Não Incid.Contrib.,Sujeitas a Alíq. 0 ou Suspensão-COFINS |  |
| Registro | Texto | S | S | Formato:  Multi select  Default:  Habilitado | Apurações |  |
