# MTZ_Tela_Creditos_Disponiveis_PIS_PASEP_COFINS_SCP

- **Fonte:** MTZ_Tela_Creditos_Disponiveis_PIS_PASEP_COFINS_SCP.docx
- **Modificado:** 2023-07-18
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Matriz da tela Créditos Disponíveis \- PIS/PASEP e COFINS \- menu SCP

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4316\-B

Marcos G\. de Paula

Duplicação da tela com inclusão do campo Código da SCP\.

MFS28515

Andréa Rocha

Incluir uma nova opção para o campo Status\.

18/10/2019

MFS34355

Liliane Assaf

Alteração no tratamento dos créditos prescritos com mais de 5 anos\.

Desfazendo a alteração feita pela MFS28515

28/06/2020

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc378091802)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc378091803)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc378091804)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc378091805)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	4](#_Toc378091806)

[2\.	Regras dos Campos	4](#_Toc378091807)

# <a id="_Toc378091802"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc378091803"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc378091804"></a>UC001 – Manutenção da Estrutura Padrão

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

### <a id="_Toc378091805"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc378091806"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc378091807"></a>Regras dos Campos 

__Localização da tela:__ 

	Módulo: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

	Menu: Obrigação SCP >> Manutenção >> Controle dos Créditos Fiscais – PIS/PASEP

e

Menu: Obrigação SCP >> Manutenção >> Controle dos Créditos Fiscais – COFINS

	Esta tela deverá ser uma replica da tela de Créditos Disponíveis disponível no menu Obrigação >> Manutenção >> Controle dos Créditos Fiscais – PIS/PASEP e Obrigação >> Manutenção >> Controle dos Créditos Fiscais – COFINS, contemplando a inclusão do campo Código da SCP que servirá para detalhar a qual SCP se refere a apuração\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Código da SCP

Editbox

N

N

Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código\. Deverá acessar as informações da tabela SAFX2057\.

Este campo servirá com base para pesquisa dos créditos gerados a partir do processamento realizado pelo menu Obrigações SCP, sendo que, se não for informado na pesquisa nenhum código da SCP para pesquisa, devem ser considerados os registros de crédito gerados para o Sócio Ostensivo, que não tem nenhum código de SCP vinculado\.

OS4316\-B

Status

Listbox

N

S

Campo somente para consulta\. 

Valores que compõe esse campo:

\- Disponível

\- Fechado

O campo vai ser habilitado para alteração, com as seguintes opções:

\- Disponível

\- Cancelado por Prazo de Prescrição

Obs\.:  Quando o Status for igual a “Fechado”, não ficará habilitado para alteração\.

MFS28515

MFS34355

*\* Descrição não disponível em tela*

