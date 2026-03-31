# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2059

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2059.docx
- **Modificado:** 2022-06-06
- **Tamanho:** 72 KB

---

THOMSON REUTERS

__Informação de Suspensão de Exigibilidade de Tributos__

__Localização__

__Módulo:__ Básicos🡪 MasterSAF DW

__Menu:__ 	Manutenção 🡪 Códigos 🡪 Cadastro Processo Administrativo/Judicial \(REINF\) >> Aba Informações de Suspensão de Exigibilidade de Tributos

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-9755

Elenilson Coutinho

Definição das regras de importação, Online e Batch, da SAFX2059\.

MFS\-13810

Lara Aline

Inclusão de 2 novos indicadores de suspensão e ajuste no campo indicador de depósito\.

MFS15147

Alteração do campo “Indicador da Suspensão de Exigibilidade de Tributos”\.

Inclusão de uma nova opção na lista de valores do campo “Indicador da Suspensão de Exigibilidade de Tributos”\.

MFS18065

Atualização do eSocial p/ vrs 2\.4\.02

Inclusão de nova opção na lista de valores do campo Tipo de Processo

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

A rotina de importação online e batch do módulo JOB Servidor deverão ser ajustadas para que contemple as informações da tabela SAFX2059 – Informação de Suspensão de Exigibilidade de Tributos, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Indicador do Tipo de Processo

A

001

SIM

SIM

Número do Processo

A

021

SIM

SIM

Data Início/Inclusão/Alteração da Validade

N

008

NÃO

NAO

Código do Indicativo da Suspensão de Exigibilidade de Tributos

A

014

NÃO

NÃO

Indicador da Suspensão de Exigibilidade de Tributos

A

002

SIM

NÃO

Data da Decisão

N

008

SIM

NÃO

Indicador de Depósito

A

001

SIM

NÃO

 

MFS\-9755

RN01

__Regra Geral__

Caso não encontrado informações do processo para referência \(Tipo de Processo, Número do Processo, Início Validade\) na tabela pai \(SAFX2058\) exibir a seguinte mensagem:

“Nao existe Processo Administrativo Judicial para o registro de Informacao de Suspensao de Exibilidade de Tributos\.”

RN02

__Indicador do Tipo de Processo__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Indicador do Tipo de Processo Não Preenchido”\.

__MFS18065__: Inclusão do tipo de processo = 4 \(Processo FAP\)

 

Crítica: Valor esperado 1, 2 ou 4, caso contrário exibir a seguinte mensagem: *“Indicador do Tipo de Processo deve ser <1>, <2> ou <4>”*\.

O tipo 4 \(Processo FAP\) só pode ser utilizado para o eSocial, pois foi incluído na versão 2\.4\.02 do layout, e não consta no REINF\. Assim será feita a seguinte crítica:

Se “Tipo de Processo” = 4 e “Indicador de Incidência REINF” = “S”:

      O registro não será importado e será gerada a seguinte mensagem de erro *“O Tipo de Processo = 4 não deve ser utilizado*

*      quando o indicador de incidência REINF  = S”*

MFS\-9755

MFS18065

RN03

__Número do Processo__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Número do Processo deve ser preenchido”\.

MFS\-9755

RN04

__Data Início/Inclusão/Alteração da Validade__

Crítica: Caso não for uma data válida exibir a seguinte mensagem: Campo Data Início/Inclusão/Alteração da Validade com formato inválido\.

Caso não preenchido, deverá ser informado o primeiro dia do mês\.

MFS\-9755

RN05

__Código do Indicativo da Suspensão de Exigibilidade de Tributos__

MFS\-9755

RN06

__Indicador de Suspensão de Exigibilidade de Tributos__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Indicador de Suspensão de Exigibilidade de Tributos não preenchido”\.

__\[Alterado MFS13810\]__ – Inclusão dos valores 02 e 03;

__\[Alterado MFS15147\]__ – Inclusão do valor 14;

Crítica: Valor esperado 01, 02, 03, 04, 05, 08, 09, 10, 11, 12, 13, 14, 90 e 92 caso contrário exibir a seguinte mensagem: “Indicador de Suspensão de Exigibilidade de Tributos deve ser <01>, <02>, <03>, <04>, <05>, <08>, <09>, <10>, <11>, <12>, <13>, <14>, <90> e <92>”\.

MFS\-9755

MFS\-13810

MFS15147

RN07

__Data da Decisão__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Data Decisão não preenchido”\.

Crítica: Caso não for uma data válida exibir a seguinte mensagem: Campo Data da Decisão com formato inválido\.

MFS\-9755

RN08

__Indicador de Depósito__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Indicador de Depósito não preenchido”\.

Crítica: Valor esperado S e N, caso contrário exibir a seguinte mensagem: “Indicador de Depósito deve ser <S> ou <N>”\.

Verificar se no campo Indicador de Suspensão de Exigibilidade de Tributos foi preenchido com o código = “90”, nesse caso o valor informado nesse campo deverá ser igual a ‘Não’, caso contrário exibir a seguinte mensagem: “Se Indicador de Suspensão de Exigibilidade de Tributos igual a ‘90’, o campo Indicador de Depósito deverá ser preenchido obrigatoriamente com ‘N’\.”\.

Verificar se no campo Indicador de Suspensão de Exigibilidade de Tributos foi preenchido com o código = “02 OU 03”, nesse caso o valor informado nesse campo deverá ser igual a ‘Sim’, caso contrário exibir a seguinte mensagem: “Se Indicador de Suspensão de Exigibilidade de Tributos igual a ’02 ou 03’, o campo Indicador de Depósito deverá ser preenchido obrigatoriamente com ‘S’\.”\.

MFS\-9755

MFS13810

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

