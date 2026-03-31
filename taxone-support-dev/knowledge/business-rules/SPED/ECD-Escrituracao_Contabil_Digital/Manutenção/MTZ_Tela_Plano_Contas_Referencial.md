# MTZ_Tela_Plano_Contas_Referencial

- **Fonte:** MTZ_Tela_Plano_Contas_Referencial.docx
- **Modificado:** 2026-03-05
- **Tamanho:** 123 KB

---

THOMSON REUTERS

Matriz da tela de Plano de Contas Referencial 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4745

Marcos G\. de Paula

Atualização das opções disponíveis no campo Entidade Responsável\.

MFS8620

Lara Aline

Atualização das opções disponíveis no campo Entidade Responsável\.

MFS17883

João Henrique

Inclusão da opção 10 \- Financeiras – Lucro Presumido\.

MFS17892

João Henrique

Atualização da versão do plano de contas referencial para 4\.00

MFS23870

João Henrique

Atualização da versão do plano de contas referencial para 5\.00

[MFS\-60592](https://jira.thomsonreuters.com/browse/MFS-60592)

Alessandra Cristina Navatta

Atualizada a especificação, considerando a versão 6\.00 do plano de contas \(apesar de não ser escopo da demanda\) 

Atualização da versão do plano de contas referencial para 7\.00

MFS\-81170

Alessandra Cristina Navatta

Atualização da versão do plano de contas referencial\. Inclusão da versão 8\.00

MFS\-511450

Elisabete Costa

Atualização da versão do plano de contas referencial\. Inclusão da versão 9\.00

MFS\-599648

Rosemeire Santos

Atualização da versão do plano de contas referencial\. Inclusão da versão 10\.00

__MFS\-749696__

Rosemeire Santos

Atualização da versão do plano de contas referencial\. Inclusão da versão 11\.00

__MFS__[__977310__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/977310)

Rogério Ohashi

O objetivo dessa demanda é incluir as colunas de Data Inicial e Data Final, conforme informação da TFIX64, Somente para o código “00\-SUSEP”

__MFS\-1035615__

Rosemeire Santos

Atualização da versão do plano de contas referencial\. Inclusão da versão 12\.00

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc376448359)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc376448360)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc376448361)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc376448362)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	4](#_Toc376448363)

[2\.	Regras dos Campos	4](#_Toc376448364)

# <a id="_Toc376448359"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc376448360"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc376448361"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

Usuário do Sistema\.

__Pré\- Condições__

Estar logado no produto MasterSAF DW\.

__Pós\-Condições__

Não se aplica\.

<a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a>

### <a id="_Toc376448362"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc376448363"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc376448364"></a>Regras dos Campos 

__Localização da tela:__ 

Módulo: SPED >> ECD\-Escrituração Contábil Digital

Menu: Manutenção

__Título da tela: __Plano de Contas Referencial

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Entidade Responsável

Alfa

S

S

Formato: Dropdown

Considerar a seguinte formatação para exibição:

- 00 \- SUSEP
- 10 \- Secretaria da Receita Federal
- 20 \- Banco Central do Brasil \(Cosif\)
- 1 \- PJ em Geral
- 2 \- PJ em Geral \- Lucro Presumido
- 3 \- Financeiras
- 4 \- Seguradoras
- 5 \- Imunes e Isentas em Geral
- 6 \- Financeiras \- Imunes e Isentas
- 7 \- Seguradoras \- Imunes e Isentas
- 8 \- Entidades Fechadas de Previdência Complementar
- 9 \- Partidos Políticos
- 10 \- Financeiras – Lucro Presumido/Secretaria da Receita Federal

Excluir a opção 10 \- Secretaria da Receita Federal da lista, pois a mesma será atendida juntamente com a opção 10 \- Financeiras – Lucro Presumido/Secretaria da Receita Federal\.

Com base no conteúdo indicado neste campo, serão demonstradas as contas contábeis da TFIX64 na lista abaixo\. Esta demonstração deve respeitar o que foi indicado no campo Versão, ou seja, para demonstração da listagem teremos uma combinação de Versão \+ Entidade Responsável indicada pelo usuário\.

Ex\.: Se o usuário seleciona Versão “1\.00” e Entidade Responsável “00 – SUSEP”, na listagem abaixo serão demonstradas apenas as contas da Versão “1\.00” e Entidade “00 – SUSEP”\.

\[__ALTERAÇÃO\-MFS__[__977310__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/977310)\] AlteraçãoTela Plano de Conta Referencial “00\-SUSEP”

Conforme solicitação do cliente IRB, foram incluídas as colunas de Data Inicial e Data Final, conforme inforação da TFIX64\. \(somente para SUSEP\)\.

OS4745

MFS8620

MFS17883

Versão

N

S

S

DropDownList

Nesse campo serão exibidas as versões do plano de contas referencial\.

1\.00

2\.00

3\.00

4\.00

5\.00

6\.00

7\.00 

8\.00 

9\.00

10\.00

11\.00

12\.00

Opção Default: Exibir a versão mais atual

MFS[17892](http://ent.jira.int.thomsonreuters.com/browse/MFS-17892)

MFS23870

MFS\-60592

MFS\-81170

MFS\-511450

MFS\-599648

__MFS\-749696__

__MFS\-1035615__

*\* Descrição não disponível em tela*

