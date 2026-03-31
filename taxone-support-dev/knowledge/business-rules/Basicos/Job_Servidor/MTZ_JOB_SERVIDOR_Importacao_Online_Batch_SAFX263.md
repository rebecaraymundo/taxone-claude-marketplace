# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX263

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX263.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS16848

Lara Aline

Definição das regras de importação, Online e Batch, da SAFX263\.

MFS18237

Lara Aline

Inclusão de 3 campos para atendimento do evento R\-2020 do EFD\-Reinf

MFS22920

Lara Aline

Inclusão de 1 campo para atendimento do evento S\-1250 do eSocial\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX263 \- Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Data da Escrita Fiscal

N

008

SIM

SIM

Movimento Entrada/Saída

A

001

SIM

SIM

Normal ou Devolução

A

001

SIM

SIM

Tipo do Documento

A

005

SIM

SIM

Indicador Pessoa Física/Jurídica

A

001

SIM

SIM

Código/Destinatário/Emitente/ Remetente

A

014

SIM

SIM

Número do Documento Fiscal/ Número do Mapa Resumo de Caixa

A

012

SIM

SIM

Série do Documento Fiscal

A

003

NÃO

SIM

Subsérie do Documento Fiscal

A

002

NÃO

SIM

Tipo do Processo

A

001

SIM

SIM

Número do Processo

A

021

SIM

SIM

Código do Indicativo da Suspensão de Exigibilidade de Tributos

A

014

NÃO

NÃO

Valor da Contribuição Previdenciária com exigibilidade suspensa

N

015V002

NÃO

NÃO

Valor da contribuição para Gilrat com exigibilidade suspensa

N

015V002

NÃO

NÃO

Valor da contribuição para o Senar com exigibilidade suspensa

N

015V002

NÃO

NÃO

Indicador do Evento

A

001

SIM

SIM

Indicador do Processo

A

001

NÃO

NÃO

Valor Retenção não Efetuada

N

015V002

NÃO

NÃO

Indicador do Tipo do Processo Judicial

A

001

NÃO

NÃO

 

MFS16848

MFS18237

MFS22920

RN02

__Campo Código da Empresa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS16848

RN03

__Campo Código do Estabelecimento__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido\.

MFS16848

RN04

__Campo Data da Escrita Fiscal__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Data da Escrita Fiscal não informado”\. 

MFS16848

RN05

__Campo Movimento Entrada/Saída__

Movimento Entrada/Saída, de acordo com:

1 \- Documento de Entrada, Documento de Terceiros;

2 \- Documento de Entrada emitida pelo Estabelecimento, acolhendo Notas de Produtores Agropecuários;

3 \- Documento de Entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário;                                                                                                                                        

4 \- Documento de Entrada emitida pelo Estabelecimento, outros motivos legais;

5 \- Documento de Entrada emitida pelo Estabelecimento, globalizando Conhecimento de Frete ou Material Uso/Consumo;

9 \- Documento de Saída\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Movimento Entrada/Saída não informado”\. 

MFS16848

RN06

__Campo Normal ou Devolução__

Motivo da Entrada / Saída, de acordo com:

1 \- Normal;

2 \- Devolução \(Quando se tratar de Devolução de Mercadorias\- Produtos, Insumos, Materiais Uso/Consumo, Ativo, etc\., previstos em legislação\)\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Normal ou Devolução não informado”\. 

MFS16848

RN07

__Campo Tipo do Documento__

Tipo de Documento de acordo com a Tabela de Tipo de Documentos  \(SAFX2005\) \-  \(Duplicata,  Fatura,  Nota  Fiscal  Fatura,  Recibo  e  etc\. \.\.\. \)\. 

Quando se trata de Documentos Fiscais Modelos 2B, 2C ou 2D informar “MRC”\. 

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Tipo do Documento não informado”\. 

MFS16848

RN08

__Campo Indicador Pessoa Física/Jurídica__

Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), conforme segue:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador Pessoa Física/Jurídica não informado”\. 

MFS16848

RN09

__Campo Código/Destinatário/Emitente/ Remetente__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Código/Destinatário/Emitente/Remetente não informado”\. 

MFS16848

RN10

__Campo Número do Documento Fiscal/ Número do Mapa Resumo de Caixa__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Número do Documento Fiscal/ Número do Mapa Resumo de Caixa não informado”\. 

MFS16848

RN11

__Campo Série do Documento Fiscal__

Como o campo é chave, porém não é obrigatório o preenchimento, se não preenchido gravar branco \(" "\)\.

MFS16848

RN12

__Campo Subsérie do Documento Fiscal__

Como o campo é chave, porém não é obrigatório o preenchimento, se não preenchido gravar branco \(" "\)\.

MFS16848

RN13

__Campo Tipo do Processo__

Tipo do Processo, sendo:

1 \- Administrativo;

2 – Judicial\.

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Tipo do Processo não informado”\. 

O cadastro do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS16848

RN14

__Campo Número do Processo__

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Número do Processo não informado”\. 

O número do processo deve existir na tabela de Processo Administrativo/Judicial \(SAFX2058\), caso contrário exibir msg ao usuário\.

MFS16848

RN15

__Campo Código do Indicativo da Suspensão de Exigibilidade de Tributos __

Campo de preenchimento não obrigatório\. 

Caso informado, o Código do Indicativo da Suspensão de Exigibilidade de Tributos deve existir na tabela de Informação de Suspensão de Exigibilidade de Tributos \(SAFX2059\), caso contrário exibir msg ao usuário\. 

MFS16848

RN16

__Campo Valor da Contribuição Previdenciária com exigibilidade suspensa__

Campo de preenchimento não obrigatório\. 

Caso informado, o valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo Valor da Contribuição Previdenciária com exigibilidade suspensa deve ser maior que zero\.”

Se Indicador do Evento estiver preenchido com valor <2> e Valor da Contribuição Previdenciária com exigibilidade suspensa estiver preenchido exibir a seguinte mensagem: “Valor da Contribuição Previdenciária com exigibilidade suspensa” deve ser preenchido apenas se “Indicador do Evento” for igual a 5 \- R\-2050\.

MFS16848

MFS18237

RN17

__Campo Valor da contribuição para Gilrat com exigibilidade suspensa__

Campo de preenchimento não obrigatório\. 

Caso informado, o valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo Valor da contribuição para Gilrat com exigibilidade suspensa deve ser maior que zero\.”

Se Indicador do Evento estiver preenchido com valor <2> e Valor da contribuição para o Gilrat com exigibilidade suspensa estiver preenchido exibir a seguinte mensagem: “Valor da contribuição para o Gilrat com exigibilidade suspensa” deve ser preenchido apenas se “Indicador do Evento” for igual a 5 \- R\-2050\.

MFS16848

MFS18237

RN18

__Campo Valor da contribuição para o Senar com exigibilidade suspensa__

Campo de preenchimento não obrigatório\. 

Caso informado, o valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo Valor da contribuição para o Senar com exigibilidade suspensa deve ser maior que zero\.”

Se Indicador do Evento estiver preenchido com valor <2> e Valor da contribuição para o Senar com exigibilidade suspensa estiver preenchido exibir a seguinte mensagem: “Valor da contribuição para o Senar com exigibilidade suspensa” deve ser preenchido apenas se “Indicador do Evento” for igual a 5 \- R\-2050\.

MFS16848

MFS18237

RN19

__Campo Indicador do Evento__

Indicador do Evento, informar de qual evento corresponde a informação, conforme segue:

2 – R\-2020;

5 – R\-2050;

A \- S\-1250\. 

Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro caso não esteja preenchido: “Indicador do evento não informado”\. 

Crítica: Valor esperado 2, 5 ou A, caso contrário exibir a seguinte mensagem: “Indicador do Evento deve ser <2> R\-2020 ou <5> R\-2050 ou <A> S\-1250”\. 

MFS18237

RN20

__Campo Indicador do Processo__

Indicador do Processo, se a informação corresponde a um processo principal ou adicional, conforme segue:

1 – Principal;

2 – Adicional\.

Crítica: Se preenchido o valor esperado é 1, 2 caso contrário exibir a seguinte mensagem: “Indicador do Evento deve ser <1> ou <2>”\. 

Se Indicador do Evento estiver preenchido com valor <2> e Indicador do Processo não estiver preenchido exibir a seguinte mensagem: “Indicador do Processo” deve ser preenchido se “Indicador do Evento” for igual a 2 \- R\-2020\.

MFS18237

RN21

__Campo Valor Retenção não Efetuada__

Caso informado, o valor informado neste campo deve ser maior que zero, senão exibir a seguinte msg ao usuário: “O valor informado no campo Valor Retenção não Efetuada deve ser maior que zero\.”

Se Indicador do Evento estiver preenchido com valor <2> e Valor Retenção não Efetuada não estiver preenchido exibir a seguinte mensagem: “Valor Retenção não Efetuada” deve ser preenchido se “Indicador do Evento” for igual a 2 \- R\-2020\.

MFS18237

RN22

__Campo Indicador do Tipo do Processo Judicial__

Indicador do Processo Judicial, se a informação corresponde a um processo judicial do produtor ou comum a todos os produtores \(Coletivo\), conforme segue:

1 – Processo Judicial do Produtor;

2 – Processo Judicial Coletivo\.

Se o campo ‘Indicador do Evento’ estiver preenchido com valor <A> e o campo ‘Tipo do Processo’ estiver preenchido com valor <2> esse campo será de preenchimento obrigatório e caso não estiver preenchido exibir a seguinte mensagem: “Indicador do Tipo do Processo Judicial” deve ser preenchido se “Indicador do Evento” for igual a A \- S\-1250 e “Tipo do Processo” for igual a 2 \- Judicial\.

Crítica: Se preenchido, o valor esperado é 1, 2 caso contrário exibir a seguinte mensagem: “Indicador do Tipo do Processo Judicial deve ser <1> ou <2>”\. 

MFS22920

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

