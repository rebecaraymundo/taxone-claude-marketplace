# MTZ-OTF-Parametros_por_Codigo_de_Receita_IN_698-2006

- **Fonte:** MTZ-OTF-Parametros_por_Codigo_de_Receita_IN_698-2006.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 47 KB

---

# Obrigações de Tributos Federais \- Parâmetros por Código de Receita – IN 698/2006

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3752

Obrigações de Tributos Federais \- Nomenclatura IN 698/2006

Trata\-se da criação do Informe de Rendimentos Financeiros, de acordo com a IN 698/2006\.

#### Cód\.

### Descrição

###     DR

# RN01

Deverá ser criada no módulo Obrigações de Tributos Federais, a tela “<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a>Parâmetros por Código de Receita – IN 698/2006”\. Essa tela irá permitir que o usuário vincule os Códigos de Receita \(Código DARF\) com as classes \(quadros\), linhas e descrições do Informe de Rendimentos Financeiros cadastradas na tela de “Nomenclatura – IN 698/2006”\.

Essa tela será disponibilizada abaixo do menu: Parâmetros >> Parâmetros por Código de Receita – IN 698/2006\. Esse menu deverá ser disponibilizado abaixo do menu Parâmetros >> Parâmetros p/ Verba \(Folha de Pagamento\)\.

OS3752

# RN02

Ao selecionar o menu para abrir a tela, o sistema deverá permitir que o usuário selecione o Grupo referente ao Estabelecimento logado no Manager\.

Isso é necessário devido à vinculação com o Código de Receita \(SAFX2019\) que possui grupo vinculado\.

OS3752

# RN03

A tela “Parâmetros por Código de Receita – IN 698/2006” deverá permitir as operações de inclusão, consulta, alteração e exclusão dos registros\.

O sistema só deverá permitir a associação do Código de Receita com a Nomenclatura UMA ÚNICA VEZ\. Isso ocorre porque um Código de Receita só pode ser utilizado para ser exibido em uma única linha do Informe de Rendimentos\. 

*OBS: essa regra já é utilizada hoje no Parâmetros por Verba para o Informe de Rendimentos de Funcionários\.*

OS3752

# RN04

Deverá ser previsto para essa tela um relatório de conferência\.

OS3752

# RN05

Nessa tela deverão ser exibidos os seguintes campos:

- __Estabelecimento:__ nesse campo deverá ser exibido o Estabelecimento selecionado no Manager\. O estabelecimento não poderá ser alterado e o mesmo será exibido no formato “Código Estabelecimento” \+ “Descrição Estabelecimento”, separados por hífen \(\-\)\. *Exemplo: 001 – Estabelecimento 001*\. 
- __Grupo:__ nesse campo deverá ser exibido o Grupo, conforme o grupo selecionado na abertura da tela\.
- __Código Receita \(DARF\):__ nesse campo o usuário poderá selecionar o Código DARF\. O sistema irá recuperar todos os Códigos DARF cadastrados no módulo DW, menu: Manutenção >> Códigos >> Código do DARF, cujo campo DIRF esteja selecionado\. Vale salientar que embora para uma mesma Empresa, Estabelecimento e Grupo existam mais de um Código Receita \(DARF\) com datas de validade distintas, o sistema só irá exibir o Código Receita \(DARF\) mais atual\. Essa regra é válida para que o usuário não precise cadastrar o mesmo código diversas vezes\. Caso por ventura o cliente possua retenções “apontadas” para um mesmo código com datas de validade distintas, todas serão recuperadas para composição do Informe de Rendimentos\. Campo obrigatório de preenchimento\.
- __Parâmetros para Informe de Rendimentos__
	- __Classe para Rendimento: __nesse campo o usuário poderá selecionar a Nomenclatura cadastrada no módulo Obrigações de Tributos Federais, menu: Parâmetros >> Nomenclatura – IN 698/2006\. O sistema irá exibir as informações da Nomenclatura cadastrada, da seguinte maneira:
		- Descrição da Classe: nesse campo será exibida a Descrição da Classe, conforme campo “Classe”\.
		- Descrição da Linha: nesse campo será exibida a Descrição da Nomenclatura, conforme campo “Descrição”\.
		- Número: nesse campo será exibida a Linha da Nomenclatura, conforme campo “Número”\.

Campo obrigatório de preenchimento\.

OS3752

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

