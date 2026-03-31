# MTZ_Ressarc_PR_Parametros_C176_Lancamentos

- **Fonte:** MTZ_Ressarc_PR_Parametros_C176_Lancamentos.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Módulo Ressarcimento de ICMS ST \- PR

Manutenção dos Parâmetros p/ a Geração dos Lançamentos referentes aos Valores do C176

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS ST, item Parâmetros 🡪 Registro C176 🡪 Parâmetros p/Geração dos Lançamentos 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS13569

Andréa Rocha

Criação da parametrização para geração dos lançamentos, referentes aos valores apurados para o registro C176\. 

08/09/2017

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Os dados parametrizados neste item são utilizados na rotina de geração da Utilização do Imposto no Período, realizada no menu “Geração 🡪 Utilização do Imposto no Período” do módulo de Ressarcimento\.

Estas informações servem para a geração dos lançamentos complementares da Apuração do ICMS, a partir dos valores apurados para o registro C176\. 

# <a id="_Toc451260496"></a>Layout da Tela

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção\. 	

EXCLUI

Esta opção permite a exclusão da parametrização do estabelecimento em questão\. 

CONFIRMA

Opção para salvar as informações incluídas ou alteradas\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

S

Este campo é uma lista dos estabelecimentos da empresa do login para seleção do usuário\. Somente devem ser mostrados os estabelecimentos cujo estado seja igual ao Paraná\.

Quando for informado um estabelecimento no login, o campo mostrará fixo este estabelecimento, e usuário não poderá alterá\-lo\.

MFS13569

Replicar para os Estabelecimentos

Alfanumérico

N

S

Ao clicar nesta opção, o usuário poderá selecionar os estabelecimentos desejados para realizar a replicação dos dados parametrizados\.

Serão demonstrados para replicação todos os estabelecimentos da mesma empresa e UF do estabelecimento parametrizado\.

MFS13569

__Parâmetros para geração dos lançamentos da Apuração do ICMS:__

– __Lançamento de Crédito: __

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Item da Apuração

Alfanumérico

__    S__

Neste campo será exibido fixo o item de crédito: “__006 – OUTROS CRÉDITOS \(DISCRIMINAR BAIXO\)__” da Tabela dos Itens da Apuração do ICMS\. 

MFS13569

Descrição do Lançamento

Alfanumérico

__    S__

Neste campo será informada a descrição do lançamento \(tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM\_APURAC\_DISCR\)\.

MFS13569

Classe de Lançamento

Alfanumérico

   N

Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF \(\*\), considerando apenas as classes da UF do estabelecimento em questão\.

\(\*\) Módulo Ferramentas, menu “Tabelas Internas 🡪 Manter 🡪Classes por UF”;

MFS13569

Amparo/Texto/Ocorrência

Alfanumérico 

   N

Este campo trabalha com janela de seleção da Tabela dos Códigos de Amparo Legal \(\*\), considerando apenas os códigos da UF do estabelecimento em questão\.

\(\*\) Módulo DW, menu “Cadastros 🡪 Código Amparo / Texto / Ocorrência”;

MFS13569

Subitem Amp\./Texto/Ocor\.

Alfanumérico

   N

Neste campo será exibido, quando for o caso, o código e a descrição do subitem do amparo legal informado, nos casos em que o usuário selecionar no campo anterior um amparo com subitem\. 

\(\*\) Módulo DW, menu “Cadastros 🡪 Código Subitem Amparo / Texto / Ocorrência”;

MFS13569

Cód\. Ajuste \(E111\) 

Alfanumérico

__    S__

S

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste de Sped Fiscal __\(\*\)__

Serão disponibilizados para seleção *apenas* os códigos com o terceiro caracter = “0” \(=Apuração Própria\) __e__ quarto caracter = “2” \(=Outros Créditos\), considerando apenas os códigos da UF do estabelecimento em questão\.

__\(\*\)__ Módulo ICMS, menu “Apuração > Apuração do ICMS > Lançamentos Complementares 🡪 Código de Ajuste Sped Fiscal”;

MFS13569

– __Lançamento de Estorno de Débito: __

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Item da Apuração

Alfanumérico

__    S__

Neste campo será exibido fixo o item de crédito: “__007 – ESTORNO DE DÉBITO \(DISCRIMINAR ABAIXO\)__” da Tabela dos Itens da Apuração do ICMS\. 

MFS13569

Descrição do Lançamento

Alfanumérico

__    S__

Neste campo será informada a descrição do lançamento \(tamanho: 150 caracteres, conforme tabela dos lançamentos complementares, ITEM\_APURAC\_DISCR\)\.

MFS13569

Classe de Lançamento

Alfanumérico

   N

Este campo trabalha com janela de seleção da Tabela de Classes de Lançamento por UF \(\*\), considerando apenas as classes da UF do estabelecimento em questão\.

\(\*\) Módulo Ferramentas, menu “Tabelas Internas 🡪 Manter 🡪Classes por UF”;

MFS13569

Amparo/Texto/Ocorrência

Alfanumérico 

   N

Este campo trabalha com janela de seleção da Tabela dos Códigos de Amparo Legal \(\*\), considerando apenas os códigos da UF do estabelecimento em questão\.

\(\*\) Módulo DW, menu “Cadastros 🡪 Código Amparo / Texto / Ocorrência”;

MFS13569

Subitem Amp\./Texto/Ocor\.

Alfanumérico

   N

Neste campo será exibido, quando for o caso, o código e a descrição do subitem do amparo legal informado, nos casos em que o usuário selecionar no campo anterior um amparo com subitem\. 

\(\*\) Módulo DW, menu “Cadastros 🡪 Código Subitem Amparo / Texto / Ocorrência”;

MFS13569

Cód\. Ajuste \(E111\) 

Alfanumérico

__    S__

S

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste de Sped Fiscal __\(\*\)__

Serão disponibilizados para seleção *apenas* os códigos com o terceiro caracter = “0” \(=Apuração Própria\) __e__ quarto caracter = “3” \(=Estorno de Débitos\), considerando apenas os códigos da UF do estabelecimento em questão\.

__\(\*\)__ Módulo ICMS, menu “Apuração > Apuração do ICMS > Lançamentos Complementares 🡪 Código de Ajuste Sped Fiscal”;

MFS13569

       = = = = = =

