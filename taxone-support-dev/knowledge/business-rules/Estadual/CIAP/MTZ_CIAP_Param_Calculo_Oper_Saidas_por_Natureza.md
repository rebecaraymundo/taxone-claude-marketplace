# MTZ_CIAP_Param_Calculo_Oper_Saidas_por_Natureza

- **Fonte:** MTZ_CIAP_Param_Calculo_Oper_Saidas_por_Natureza.docx
- **Modificado:** 2021-08-27
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Módulo Ativo Permanente 

__Tela de Parâmetro p/ Cálculo do Total das Operações de Saídas/Devoluções \(Por CFOP / Natureza de Operação\)__

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

__Data__

MFS15006

Criação do documento

Inclusão do campo Valores para Totalização

27/08/2021

Sumário

[1\.	Layout da Tela	3](#_Toc515030687)

[2\.	Regras dos Campos	3](#_Toc515030688)

# <a id="_Toc350763252"></a><a id="_Toc515030687"></a><a id="OLE_LINK6"></a>Layout da Tela 

Estabelecimento \[xxxxxx – xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\]

Grupo Natureza \[xx\]

CFOP’s:                                                                                                                                      Valores para Totalização:

\[ \] xxxx – sss \- aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                      \[ \] Valor Contábil   \[ \] Valor Contábil \- Valor do ICMS\-ST   \[  \] Base Tributada   \[  \] Isenta   \[ \] Outras    \[ \]Redução

\[ \] yyyy – sss \- bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                      \[ \] Valor Contábil   \[ \] Valor Contábil \- Valor do ICMS\-ST   \[  \] Base Tributada   \[  \] Isenta   \[ \] Outras    \[ \]Redução

\[ \] zzzz – sss \- ccccccccccccccccccccccccccccccccccc                       \[ \] Valor Contábil   \[ \] Valor Contábil \- Valor do ICMS\-ST   \[  \] Base Tributada   \[  \] Isenta   \[ \] Outras    \[ \]Redução

\[Selecionar Todos\]    \[Desmarcar Todos\]    \[Marcar Entradas\]    \[Desmarcar Entradas\]    \[Marcar Saídas\]    \[Desmarcar Saídas\]

\[ \] Replicar para os Estabelecimento

UF: \[ RJ \\/\]

Estabelecimento

\[ \] xxxxxx – aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

\[ \] yyyyyy – aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

\[ \] zzzzzz – aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# <a id="_Toc515030688"></a>Regras dos Campos 

__Localização da tela:__ Menu Estadual,  Módulo: Ativo Permanente, item de menu Cadastros 🡪 Parâmetros p/ Cálculo do Total das Operações de Saídas/Devoluções 🡪 Por Extensão de CFOP

__Título da tela: __Extensão de CFOP p/ Cálculo do Total das Operações de Saídas/Devoluções

__Considerações Gerais: __

- Poderão ser parametrizado “N” \(vários\) códigos nessa parametrização\.
- Para cada Estabelecimento selecionado na tela serão carregados todos os CFOP´s cadastrados\.
- Na abertura da tela será exibida uma janela para seleção do Estabelecimento/Grupo/Validade de Relacionamento \(Estabelecimentos x Tabelas\) que será utilizado para obtenção das Naturezas de Operação\.

__Opções da barra de menu:__

- 
	- 
		- __GRUPO – __Ao clicar nesta opção, abrirá uma janela para seleção do Estabelecimento/Grupo/Validade de Relacionamento \(Estabelecimentos x Tabelas\), e o usuário deverá selecionar o grupo e estabelecimento\. 
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

Default: Desabilitado

Estabelecimento previamente selecionado na janela de seleção Estabelecimento/Grupo/Validade\.

Campo desabilitado\.

Grupo Natureza

Alfanumérico

S

N

Default: Desabilitado

Nesse campo será exibido o Grupo de Natureza de Operação escolhido na abertura da tela\.

CFOP´s / Naturezas de Operação

Caixa de seleção de CFOP´s/Natureza de Operação

S

S

Default: não selecionado

Nesse quadro dos CFOP’s e Naturezas será exibida a lista das combinações de CFOP \+ Natureza \(SAFX2081\), considerando apenas as operações de entradas e saídas \(códigos iniciados por 1, 2, 3, 5, 6 ou 7\) da SAFX2012\.

Valores para Totalização:

\(criado na MFS15006\)

Na criação do campo, os CFOP’s já parametrizados foram inicializados com a opção “Valor Contábil”, pois este era o valor utilizado originalmente\.

Alfanumérico

S

N

Default:

Valor Contábil

Neste campo o usuário indicará os valores a serem considerados na totalização das notas do CFOP e Natureza selecionado\. As opções serão habilitadas apenas para os CFOP’s/Natureza selecionados\.

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

Caso o CFOP/Natureza seja marcado e posteriormente desmarcado, as opções de valor que se encontrem marcadas, serão desmarcadas\.

Crítica ao salvar a operação:

Ao clicar no botão <Confirma> será verificado se existe alguma CFOP/Nat selecionado que esteja com todas as opções de valor desmarcadas\. Caso sim, será exibida a mensagem abaixo e a operação *não* será salva:

*“Favor informar os valores a serem utilizados para cada CFOP/Natureza selecionado”*

MFS18604

Selecionar Todos

Botão

N

S

Default: desabilitado

Quando acionado, muda o status dos CFOP´s que não estão selecionados para selecionado\.

MFS4302

Desmarcar Todos

Botão

N

S

Default: desabilitado

Quando acionado, muda o status dos CFOP´s que estão selecionados para não selecionado\.

MFS4302

