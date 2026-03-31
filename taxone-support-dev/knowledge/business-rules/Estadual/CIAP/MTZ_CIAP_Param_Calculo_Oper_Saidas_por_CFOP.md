# MTZ_CIAP_Param_Calculo_Oper_Saidas_por_CFOP

- **Fonte:** MTZ_CIAP_Param_Calculo_Oper_Saidas_por_CFOP.docx
- **Modificado:** 2021-09-29
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Módulo Ativo Permanente 

__Tela de Parâmetro p/ Cálculo do Total das Operações de Saídas/Devoluções \(Por CFOP\)__

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data__

MFS15006

Criação do documento

Inclusão do campo Valores para Totalização

27/08/2021

<a id="_Hlk515030131"></a>

Sumário

[1\.	Layout da Tela	3](#_Toc515028106)

[2\.	Regras dos Campos	3](#_Toc515028107)

# <a id="_Toc515028106"></a><a id="_Toc350763252"></a><a id="OLE_LINK1"></a>Layout da Tela

Estabelecimento \[xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

CFOP’s:                                                                                                                                      Valores para Totalização:

\[ \] xxxx – aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                      \[ \] Valor Contábil   \[ \] Valor Contábil \- Valor do ICMS\-ST   \[  \] Base Tributada   \[  \] Isenta   \[ \] Outras    \[ \]Redução

\[ \] yyyy – bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                      \[ \] Valor Contábil   \[ \] Valor Contábil \- Valor do ICMS\-ST   \[  \] Base Tributada   \[  \] Isenta   \[ \] Outras    \[ \]Redução

\[ \] zzzz – ccccccccccccccccccccccccccccccccccc                       \[ \] Valor Contábil   \[ \] Valor Contábil \- Valor do ICMS\-ST   \[  \] Base Tributada   \[  \] Isenta   \[ \] Outras    \[ \]Redução

\[Selecionar Todos\]    \[Desmarcar Todos\]    \[Marcar Entradas\]    \[Desmarcar Entradas\]    \[Marcar Saídas\]    \[Desmarcar Saídas\]

\[ \] Replicar para os Estabelecimento

UF: \[ RJ \\/\]

Estabelecimento

\[ \] xxxxxx – aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

\[ \] yyyyyy – aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

\[ \] zzzzzz – aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# <a id="_Toc515028107"></a>Regras dos Campos 

__Localização da tela:__ Menu Estadual,  Módulo: Ativo Permanente, item de menu Cadastros 🡪 Parâmetros p/ Cálculo do Total das Operações de Saídas/Devoluções 🡪 Por CFOP

__Título da tela: __CFOP p/ Cálculo do Total das Operações de Saídas/Devoluções

__Considerações Gerais: __

- Poderão ser parametrizado “N” \(vários\) códigos nessa parametrização\.
- Para cada Estabelecimento selecionado na tela serão carregados todos os CFOP´s cadastrados\.

__Opções da barra de menu:__

- 
	- 
		- __CONFIRMA__ – Salva os dados incluídos ou alterados\.
		- __RELATÓRIO__ – Serão listados todos os dados parametrizados\.
		- __FECHA__ – Fecha a janela da parametrização\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Alfanumérico

S

N

Formato: 

Combo Box

Default: Habilitado

Este campo é de preenchimento obrigatório e será exibida a lista dos Estabelecimentos\.

Se o estabelecimento for informado no login do Manager, então este campo fica desabilitado informando o estabelecimento logado\. Senão o campo fica habilitado apresentando a lista de estabelecimentos da empresa de login

CFOP

Caixa de seleção de CFOP´s\.

S

S

Default: não selecionado

Neste quadro será exibida a lista dos CFOP’s de entradas \(códigos iniciados por 1, 2, ou 3\) e saídas \(códigos iniciados por 5 ou 6 ou 7\) da SAFX2012\. 

__Tratamento:__ Nos casos em que existir mais de um registro do mesmo CFOP, mas com diferentes datas de validade, será exibida apenas uma ocorrência do CFOP\.

<a id="_Hlk515030535"></a>

Valores para Totalização:

\(criado na MFS15006\)

Na criação do campo, os CFOP’s já parametrizados foram inicializados com a opção “Valor Contábil”, pois este era o valor utilizado originalmente\.

Alfanumérico

S

N

Default: 

Valor Contábil

Neste campo o usuário indicará os valores a serem considerados na totalização das notas do CFOP selecionado\. As opções serão habilitadas apenas para os CFOP’s selecionados\.

\- Valor Contábil

\- Valor Contábil \- Valor do ICMS\-ST   

\- Base Tributada

\- Isenta

\- Outras

\- Redução

Quando um CFOP for selecionado, a opção “Valor Contábil” será marcada automaticamente, pois este é o valor default\.

O usuário poderá escolher o Valor Contábil, __ou__, Valor Contábil \- Valor do ICMS\-ST __ou__ uma ou mais opções de base\.

Assim, q<a id="OLE_LINK2"></a>uando for marcada a opção “Valor Contábil”, as demais opções que possam estar marcadas, serão desmarcadas\.

Quando for marcada a opção “Valor Contábil \- Valor do ICMS\-ST”, as demais opções que possam estar marcadas, serão desmarcadas\.

E quando for marcada qualquer uma das opções de base \(Base Tributada, Isenta, Outras ou Redução\), as opções “Valor Contábil” e “Valor Contábil \- Valor do ICMS\-ST”, caso marcadas, serão desmarcadas\.

Caso o CFOP seja marcado e posteriormente desmarcado, as opções de valor que se encontrem marcadas, serão desmarcadas\.

Crítica ao salvar a operação:

Ao clicar no botão <Confirma> será verificado se existe algum CFOP selecionado que esteja com todas as opções de valor desmarcadas\. Caso sim, será exibida a mensagem abaixo e a operação *não* será salva:

*“Favor informar os valores a serem utilizados para cada CFOP selecionado”*

MFS15006

Selecionar Todos

Botão

N

S

Default: desabilitado

Quando acionado, muda o status dos CFOP´s que não estão selecionados para selecionado\.

Desmarcar Todos

Botão

N

S

Default: desabilitado

Quando acionado, muda o status dos CFOP´s que estão selecionados para não selecionado\.

