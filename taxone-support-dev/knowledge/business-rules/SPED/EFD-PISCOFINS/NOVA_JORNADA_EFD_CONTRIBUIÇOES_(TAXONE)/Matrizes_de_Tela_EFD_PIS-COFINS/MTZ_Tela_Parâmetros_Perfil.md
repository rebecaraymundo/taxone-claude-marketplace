# MTZ_Tela_Parâmetros_Perfil

- **Fonte:** MTZ_Tela_Parâmetros_Perfil.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 47 KB

---

    

# EFD \- PIS/PASEP \- COFINS \- Tela Perfil 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-GE

Criação do documento

Tela \- Perfil

14/03/2012

OS3169\-GE25

Alteração do Documento

Adequação da tela para atendimento ao Lucro Presumido

14/03/2012

OS3584\-DW1

Alteração do Documento

Adequação da tela para atendimento ao Bloco P

OS3169\-25CDW

Alteração do Documento

Alteração do nome da tela de Perfil

OS3845

Inclusão de novo registro

Incluído o registro 0120 – Identificação dos meses de dispensa

11/12/2012

OS4762

Exclusão de registros e alteração de descrição

Exclusão dos Registros C800, C810 e C820 e alteração de descrição nos registros C400 e C490\.

27/03/2015

MFS\-20225

Inclusão de Leiaute

Essa MFS tem como objetivo incluir nova versão de leiaute em atendimento a Nota de Documentação Evolutiva da EFD\-Contribuições – 001/2018\.

10/12/2018

MFS29843

Inclusão de Leiaute

Essa MFS tem como objetivo incluir nova versão de leiaute em atendimento ao Guia Prático da EFD\-Contribuições versão 1\.32\.

24/01/2020

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN01__

Campo “__Leiaute”__ 🡪 O objetivo deste campo é informar o leiaute a ser considerado para a criação do perfil possibilitando ao usuário criar um Perfil específico para geração do “EFD – Escrituração Fiscal Digital \- PIS/PASEP\-COFINS”\.

__\[ALTERADA – MFS\-20225\]__

__Conteúdo do campo:__

- Escrituração Fiscal Digital da Contribuição para o PIS/Pasep e da Cofins – Versão 1\.0\.0
- EFD – Escrituração Fiscal Digital das Contribuições – Até Versão 1\.27
- EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1\.28
- EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1\.32

A partir da __MFS\-20225__ foi necessário separar os layouts por conta da alteração que os registros M210 e M610 tiveram, pois foram acrescentados campos nesses registros que valerão a partir de 2019, porém, como a entrega da EFD precisará ocorrer ainda em novembro e dezembro de 2018, a sua estrutura deverá ser sem o acréscimo desses campos\.

Campo “__Perfil__” 🡪 Neste campo o usuário deverá digitar o código e uma descrição livres, para a criação de um novo perfil\. 

OS3169\-GE

MFS\-20225

MFS29843

__RN02__

Quadro “__Definição__ __dos Blocos__” 🡪 Neste quadro aparecerão os blocos referentes ao leiaute informado\.  Ao clicar num determinado bloco, os registros correspondentes aparecerão no quadro “Definição dos Registros”\. 

OS3169\-GE

__RN03__

No Perfil para atendimento do “EFD – Escrituração Fiscal Digital \- PIS/PASEP\-COFINS” serão considerados os seguintes blocos:

Bloco

Descrição

0

 Abertura, Identificação e Referências

A

 Documentos Fiscais \- Serviços \(ISS\)

C

 Documentos Fiscais I – Mercadorias \(ICMS/IPI\)

D

 Documentos Fiscais II – Serviços \(ICMS\)

F

 Demais Documentos e Operações

M

 Apuração da Contribuição e Crédito de PIS/PASEP e da COFINS

1

 Complemento da Escrituração – Controle de Saldos de Créditos e de Retenções, Operações Extemporâneas e Outras Informações

9

 Controle e Encerramento do Arquivo Digital

OS3169\-GE

__RN04__

Quadro “__Definição dos Registros__” 🡪 Neste quadro aparecerão os registros correspondentes ao Bloco escolhido\. A informação dos registros deverá ser recuperada das TFIX 67,68,69,70, considerando o layout escolhido\. Inicialmente só existe uma opção de layout \(“EFD100”\), mas deve ser disponibilizado um novo ato legal com novo layout\.

Obs\.: As TFIX’s  serão alterada para conter os dados do novo layout\. 

OS3169\-GE

__RN05__

Para cada registro são demonstradas as seguintes informações:

 

- __Reg\.:__           Número do registro                   \(campo “Registro” da TFIX\)
- __Nível:__         Nível do registro na hierarquia  \(campo “Nivel” da TFIX\)
- __Descrição:__ Nome do registro                      \(campo “Descrição” da TFIX\)

                          \(usar endentação de acordo com o nível do registro\)

- __Obrigatoriedade: __Obrigatoriedade de geração dos registros\. Nesta coluna aparecerá a informação se o registro é obrigatório ou não\. *Esta coluna é apenas informativa\.* Para os registros de movimento \(campo “Registro de Movimento” da TFIX = “S”\) será exibido o formato “X/X”, mostrando a obrigatoriedade dos movimentos na entrada e na saída, separadamente\. Para os registros normais \(campo “Registro de Movimento” da TFIX = “N”\), aparecerá apenas o formato  “X”\. 

Ao recuperar a obrigatoriedade da TFIX, deve\-se considerar o perfil informado pelo usuário \(no campo “Perfil de Apresentação”\), já que há variações na obrigatoriedade de apresentação dos registros entre os dois perfis\.

- __Contribuição Social:__ Indicador S/N para a incidência da contribuição \(campo “Contribuição Social” da TFIX\)
- __Crédito:__ Indicador S/N para a incidência da contribuição \(campo “Contribuição Social” da TFIX\)

OS3169\-GE

__RN06__

__Funcionamento da tela:__

__Inclusão de um novo perfil:__

Para criar um perfil, o usuário deve informar o layout, o perfil de apresentação e o código/descrição do perfil a ser criado\. Após a informação destes dados, o procedimento será:

- Mostrar os blocos no quadro “Definição dos Blocos” conforme a relação dos blocos já descrita acima\. O primeiro bloco da lista deve aparecer em foco \(Bloco 0\);
- O quadro “Definição dos Registros” deve apresentar os registros do Bloco escolhido, que serão recuperados da TFIX\. Como o Bloco 0 aparecerá sempre selecionado por default, este quadro também mostrará inicialmente os registros do Bloco 0;
- Sempre que o usuário selecionar outro bloco no quadro “Definição dos Blocos”, o quadro “Definição dos Registros” deve ser exibido com os registros referentes ao bloco escolhido\. 
- Na criação de um novo perfil, no quadro dos registros deverão aparecer “marcados” __*APENAS*__ os registros obrigatórios\.

OS3169\-GE

__RN07__

        __Entende\-se por registro obrigatório:__

    

        Registros comuns com obrigatoriedade = O

        Registros de movimento com obrigatoriedade = O para as entradas  __OU  __para as saídas 

       \(ou seja, sempre que existir uma opção “O”, seja ela referente à operação de entrada ou de saída\)

        Exemplo:

                              =  O/O \(obrigatório para as entradas e para as saídas\)

                              =  O/N \(obrigatório p/as entradas e não gerar p/as saídas\) 

                              =  N/O \(obrigatório p/as saídas e não gerar p/as entradas\)

Os registros que *não devem ser gerados*, que são os registros com obrigatoriedade = “N”, *não deverão ser habilitados* para alteração do usuário, e permanecerão sempre desmarcados\.

O perfil de apresentação *não poderá ser alterado* \(mesmo que internamente esta informação não faça parte da chave da tabela\)\. Este procedimento evitará problemas na inicialização dos registros\. Caso o usuário precise alterar o perfil de apresentação, ele deverá criar um novo perfil\.

OS3169\-GE

__RN08__

        __Entende\-se por registro que NÃO deve ser gerado:__

    

        Registros comuns com obrigatoriedade  =  N

        Registros de movimento com obrigatoriedade  = N para as entradas  __E  __para as saídas 

- O usuário poderá efetuar alterações marcando / desmarcando o campo de seleção de cada registro\. A alteração na seleção dos registros deve obedecer  as seguintes regras gerais:

OS3169\-GE

__RN09__

__Regras Gerais:__

- Os registros obrigatórios não serão habilitados para alteração \(seguindo o mesmo conceito de registro obrigatório descrito acima\);                
- Ao desmarcar um registro PAI, deve\-se automaticamente desmarcar *todos *os FILHOS, e demais registros dos níveis inferiores associados a ele;;
- Ao marcar um registro FILHO cujo PAI esteja desmarcado, deve\-se marcar automaticamente o PAI, e demais registros dos níveis anteriores a ele;
- A relação de dependência entre os registros deve ser observada através da informação do nível \(consultar documento Hierarquia\.doc”\);  

OS3169\-GE

__RN10__

__Alterações de perfis já existentes:__

Através do botão ABRE o usuário poderá selecionar o perfil desejado\. Na janela de seleção do botão ABRE, deverão aparecer *somente* os perfis criados para geração do Sped Fiscal\. Não deverão aparecer perfis de geração de outros meios magnéticos \(outros módulos\)\.

No caso da consulta / alteração de um perfil *já existente*, os registros devem ser exibidos conforme tenham sido atualizados anteriormente, com a seleção feita pelo usuário\.

OS3169\-GE

__RN11__

Incluir no bloco F, na definição dos Registros, logo abaixo do registro F211, as seguintes informações:

F500 \(\*\)

3

Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido  – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa

OE

F509 \(\*\)

4

Processo Referenciado

OE

F510 \(\*\)

3

Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido  – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa \(Apuração da Contribuição por Unidade de Medida de Produto\)

OE

F519 \(\*\)

4

Processo Referenciado

OE

F525 \(\*\)

3

Composição da Receita Escriturada no Período – Detalhamento da Receita Recebida pelo Regime de Caixa

OE

F550 \(\*\)

3

Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido  – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência

OE

F559 \(\*\)

4

Processo Referenciado

OE

F560 \(\*\)

3

Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido  – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência \(Apuração da Contribuição por Unidade de Medida de Produto\)

OE

F569 \(\*\)

4

Processo Referenciado

OE

__ATENÇÃO: Os registros F500/F509/510/F519/F525 devem ficar desabilitados até a implementação da OS 3169\-GE25C que trata a geração do Lucro Presumido – Regime Caixa\.__

OS3169\-GE25

__RN12__

Incluir no bloco 1 , na definição dos Registros, logo abaixo do registro 1809, a seguinte informação:

1900

2

Consolidação dos Documentos Emitidos por Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Regime de Caixa ou de Competência

OE

Se o usuário marcar um dos registros F500/F510/F550/F560 o registro 1900 deve ser marcado automaticamente \(sem ser possível desabilitar a geração do registro\)\.

Se o usuário marcar um dos registros F500/F510 ele não pode marcar os registros /F550/F560 e vice\-versa\.

OS3169\-GE25

__RN13__

Incluir na definição dos blocos a linha do bloco P e  na definição dos Registros, as seguintes informações:

Bloco P:

P001

1

Abertura do Bloco P

OE

P010

2

Identificacao do Estabelecimento

OE

P100

3

Contribuicao Previdenciaria sobre a Receita Bruta

OE

P110

4

Complemento da Escrituracao – Detalhamento da Apuracao da Contribuicao

OE

P199

4

Processo Referenciado

OE

P200

2

Consolidacao da Contribuicao Previdenciaria sobre a Receita Bruta

OE

P210

3

Ajuste da Contribuicao Previdenciaria Apurada sobre a Receita Bruta

OE

P999

1

Encerramento do Bloco P

OE

IMPORTANTE: Não será tratado o registro P110 nesta OS\.

OS3584\-DW1

__RN14__

Incluir no bloco 0 , na definição dos Registros, logo abaixo do registro 0140, a seguinte informação:

Bloco 0:

0145

3

Regime de Apuracao da Contr\. Previdenciaria sobre a Receita Bruta

OE

OS3584\-DW1

__RN15__

Alteração do nome da tela de Perfil\. Localização Parâmetros

Dê: Perfil de Geração – EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS \(Inclusão de um novo perfil\)	

Para: Perfil de Geração – <a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>EFD – Escrituração Fiscal Digital das Contribuições \(Inclusão de um novo perfil\)		

OS3169\-25CDW

__RN16__

Habilitar os registros F500/F509/510/F519/F525 que tratam a geração do Lucro Presumido – Regime Caixa, conforme mencionado na RN11\. 

OS3169\-25C

__RN17__

Incluir no bloco 0 , a identificação do registro abaixo, posicionar logo abaixo do registro 0111 a partir do leiaute versão 2\.0\.1

Bloco 0:

0120

2

Identificação de períodos dispensados da Escrituração fiscal digital das contribuições – EFD\-contribuições\.

OE

OS3845

__RN18__

Excluir do bloco C , a identificação dos registros abaixo, a partir do leiaute versão 2\.0\.1

C800

3

Cupom Fiscal Eletronico – EFD\-contribuições\.

OE

C810

4

Detalhamento do Cupom Fiscal Eletrônico – EFD\-contribuições\.

OE

C820

4

Detalhamento do Cupom Fiscal Eletrônico – EFD\-contribuições\.

OE

OS4762

__RN19__

Alteração do bloco C, a descrição dos registros abaixo, a partir do leiaute versão 2\.0\.1

C400

3

Equipamento ECF \(Código 02, 2D, 59\) – EFD\-contribuições\.

OE/OE

C490

3

Equipamento ECF \(Código 02, 2D, 59 e 60\) – EFD\-contribuições\.

OE/OE

OS4762

__RN20__

Incluir os registros:

Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1\.28:

M215

4

Detalhamento dos Ajustes da Base de Cálculo Mensal de PIS/Pasep Apurada\.

O \(se M210, campos VL\_AJUS\_ACRES\_BC\_PIS > 0 ou VL\_AJUS\_REDUC\_BC\_PIS > 0\) N \(se M210, campos

VL\_AJUS\_ACRES\_BC\_PIS = 0 e VL\_AJUS\_REDUC\_BC\_PIS = 0\)

M615

4

Detalhamento dos Ajustes da Base de Cálculo Mensal da COFINS Apurada\.

O \(se M610, campos VL\_AJUS\_ACRES\_BC\_COFINS > 0 ou VL\_AJUS\_REDUC\_BC\_COFINS > 0\) N \(se M610, campos VL\_AJUS\_ACRES\_BC\_COFINS = 0 e VL\_AJUS\_REDUC\_BC\_COFINS = 0\)

1050

2

Detalhamento dos Ajustes da Base de Cálculo Mensal de PIS/Pasep e COFINS – Valores Extra Apuração

OC

MFS\-20225

__RN21__

Alterar o registro M210:

Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1\.28:

Considerar os campos:

VL\_AJUS\_ACRES

\_BC\_PIS 

Valor do total dos ajustes de acréscimo da base de cálculo da contribuição a que se refere o Campo 04

N

\-

02

S

VL\_AJUS\_REDU

C\_BC\_PIS

Valor do total dos ajustes de redução da base de cálculo da contribuição a que se refere o Campo 04

N

\-

02

S

VL\_BC\_CONT\_A

JUS

Valor da Base de Cálculo da Contribuição, após os ajustes\.

\(Campo 07 = Campo 04 \+ Campo 05 \- Campo 06\)

N

\-

02

S

Caso contrário, manter a estrutura antiga antes da versão 1\.28\.

MFS\-20225

__RN22__

Alterar o registro M610:

Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1\.28:

Considerar os campos:

VL\_AJUS\_ACRES

\_BC\_COFINS

Valor do total dos ajustes de acréscimo da base de cálculo da contribuição a que se refere o Campo 04

N

\-

02

S

VL\_AJUS\_REDU

C\_BC\_COFINS

Valor do total dos ajustes de redução da base de cálculo da contribuição a que se refere o Campo 04

N

\-

02

S

VL\_BC\_CONT\_A

JUS

Valor da Base de Cálculo da Contribuição, após os ajustes\.

\(Campo 07 = Campo 04 \+ Campo 05 \- Campo 06\)

N

\-

02

S

Caso contrário, manter a estrutura antiga antes da versão 1\.28\.

MFS\-20225

__RN23__

Incluir os registros:

Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1\.32:

0900

2

Composição das Receitas do Período – Receita Bruta e Demais Receitas

O \(se a escrituração for transmitida após o prazo regular de entrega\)

1011

3

Detalhamento das Contribuições com Exigibilidade Suspensa

OC

MFS\-29843

