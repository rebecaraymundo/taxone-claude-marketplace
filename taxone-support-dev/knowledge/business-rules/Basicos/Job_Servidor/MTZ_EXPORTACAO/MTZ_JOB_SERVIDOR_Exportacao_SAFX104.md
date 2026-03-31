# MTZ_JOB_SERVIDOR_Exportacao_SAFX104

- **Fonte:** MTZ_JOB_SERVIDOR_Exportacao_SAFX104.docx
- **Modificado:** 2021-05-20
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Regras de Exportação SAF104

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS2732\-A

Juliana Garcia

O objetivo desta OS é incluir o campo Data Final de Vigência para manter um histórico da parametrização com as gerações\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de Exportação do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX104 \- Parâmetros de Produto por UF \(Ressarcimento e Complemento de ICMS\-ST\), que deve ser exportada com a seguinte estrutura:

__\[ALTERADA – OS2732\-A\]__

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Tipo de Registro

A

001

SIM

SIM

UF

A

002

SIM

SIM

Indicador de Produto

A

001

SIM

SIM

Código do Produto

A

035

SIM

SIM

Início de Vigência

N

008

SIM

SIM

Alíquota Interna

N

003V004

SIM

Indicador de Produtos Associados

A

001

Código de Produto Associados

A

035

Modelo do Livro

N

001

Validade Final

N

008

 

OS2732\-A

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

