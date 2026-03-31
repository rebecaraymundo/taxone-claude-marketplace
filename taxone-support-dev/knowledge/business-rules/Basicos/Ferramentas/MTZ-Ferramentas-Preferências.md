# MTZ-Ferramentas-Preferências

- **Fonte:** MTZ-Ferramentas-Preferências.docx
- **Modificado:** 2023-03-22
- **Tamanho:** 99 KB

---

THOMSON REUTERS

Módulo Ferramentas – Preferências

__Localização__: Menu Básicos, Módulo Ferramentas, item Parâmetros do Sistema à Preferências

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS\-60622

Rogério Ohashi

Inclusão de Parâmetro “DATA MART – Utilizar Versão para geração Expressa\.

14/04/2021

MFS\-87722

Alessandra Cristina Navatta

Exclusão do Parâmetro “DATA MART – Utilizar Versão para geração Expressa \(Grandes Volumes\)”\. A funcionalidade será executada sempre e de forma transparente ao usuário\.

17/06/2022

MFS\-81646

Andréa Rocha

Inclusão do parâmetro para fazer o controle do número de processos programados que podem ser executados em paralelo, que vai ser utilizado pelas telas de geração de framework\.  O Parâmetro somente estará disponível no DW\.

23/06/2022

MFS\-92054

Alessandra Cristina Navatta

Inclusão de parâmetro na tabela __Prt\_Par\_Msaf, __Este parâmetro não será exibido em tela\.

Este parâmetro terá um tratamento apenas no produto TAXONE\. O tratamento será específico para o cliente PROFARMA\. \(detalhes na tela Importação / execução, MTZ\-Job\_Servidor\-Importacao\-execucao\.doc\)

23/08/2022

MFS432792

Rogério Ohashi

Inclusão de Parâmetro “Usuário Banco de Dados” para permitir que o usuário informado na interface é diferente do Owner do Banco de Dados diferente do owner do Banco de Dados\.

17/01/2023

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

__\[ALTERAÇÃO MFS\-87722\] Exclusão do Parâmetro “DATA MART – Utilizar Versão para geração Expressa \(Grandes Volumes\)”\. __

A funcionalidade será executada sempre e de forma transparente ao usuário\.

__\[MFS\-60622\] Parâmetro: DATA MART – Utilizar Versão para geração Expressa \(Grandes Volumes\)__

O parâmetro será responsável em manter Marcado ou Desmarcado a opção de geração da “Versão para geração Expressa” na tela de Equalização/Limpeza – DATA MART, com o objetivo de evitar problemas de Performance \(para clientes com baixa volumetria de Notas Fiscais\), objetivando que somente os clientes com grande volumetria de Notas Fiscais utilizem a “Versão para geração Expressa”\.

Obs\* A recomendação é utilizar o parâmetro com volumetria superior a 1 milhão de notas fiscais por estabelecimento por período\.

__RN01__

__                                                        Parâmetros de Tela__

__\[ALTERAÇÃO MFS\-87722\] Exclusão do Parâmetro “DATA MART – Utilizar Versão para geração Expressa \(Grandes Volumes\)”\. __

A funcionalidade será executada sempre e de forma transparente ao usuário\.

__\[MFS\-60622\]__

\- Incluir abaixo do parâmetro: “Importação das SAFX01, 07, 08 e 09 p/ processo em threads\.

Este parâmetro será responsável em “Marcar” ou “Desmarcar”, \(default\) no parâmetro “Versão para geração Expressa” na tela de “Equalização/Limpeza – DATA MART\.

Incluir o Checkbox:  

      DATA MART – Utilizar Versão para geração Expressa \(Grandes Volumes\)   \[  \] <a id="_Hlk63326405"></a>

Default = desmarcado

__\[MFS81646\]  __Inclusão do parâmetro para fazer o controle do número de processos programados que podem ser executados em paralelo

\- Incluir o novo parâmetro abaixo do parâmetro “Número de Threads”:

       Parâmetro: “Qt máxima de Processos Programados em Paralelo”

       Campo do tipo numérico de 3 posições\.  Campo não obrigatório\.

       __Obs__\.:  Quando a quantidade não for informada ou for igual a zeros, os processos serão executados conforme o funcionamento já existente\.   Quando a quantidade for informada, essa quantidade será o número de processos em paralelo que poderão ser executados ao mesmo tempo, quando forem selecionados vários estabelecimentos para serem gerados\.  Esse parâmetro vai ser utilizado pelas telas de geração que utilizam o framework e tem a de opção executar processos programados, como por exemplo, as telas de geração de meio magnético\.  __O Parâmetro somente estará disponível no DW\.__

  

__\[ALTERAÇÃO MFS\-92054\]__ Criação de parâmetro na tabela

Criar um parâmetro na tabela PRT\_PAR\_MSAF:

Tamanho: 1 posição

Tipo: Varchar

Lista de Valores:

- S
- N

Default: N

Sugestão de nome: IND\_VALID\_IMPORT__’__

Este parâmetro não será exibido em tela

__Este parâmetro terá um tratamento apenas no produto TAXONE\. O tratamento será específico para o cliente PROFARMA\. \(detalhes na tela Importação / execução, MTZ\-Job\_Servidor\-Importacao\-execucao\.doc\)__

__\[ALTERAÇÃO \- MFS432792\]__ Criação de parâmetro na tabela PRT\_PAR\_MSAF:

Criar um parâmetro na tabela “Usuário DB – Alternativo”:

Tamanho: 100 posições

Tipo: Varchar2

Sugestão de nome: DB\_OWNER

# Este parâmetro foi incluído para os clientes que possuem particularidades no processo de DBLINK onde o objeto de importação SAF\_IMPORTA\_BAT está definido um usuário diferente do owner do Banco de Dados, com esse parâmetro o usuário poderá informar o Usuário Owner alternativo possibilitando a importação da tabela em questão\.

__Obs¹:__ Atualmente o sistema só permite a importação se o owner for igual ao usuário \(owner\) de Banco de Dados\.

__Obs²:__ Esse parâmetro deverá ser implementado __somente no MastersafDW\.__

