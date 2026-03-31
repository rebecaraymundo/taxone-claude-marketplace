# MTZ_Tela_Retencoes_Disponiveis_PIS_PASEP_COFINS_SCP

- **Fonte:** MTZ_Tela_Retencoes_Disponiveis_PIS_PASEP_COFINS_SCP.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Matriz da tela Retenções Disponíveis \- PIS/PASEP e COFINS \- menu SCP

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4316\-B

Marcos G\. de Paula

Duplicação da tela com inclusão do campo Código da SCP\.

OS4649

Elenilson Coutinho

Inclusão de indicadores de Natureza da Retenção 

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

	Menu: Obrigação SCP >> Manutenção >> Controle das Retenções na Fonte – PIS/PASEP

e

Menu: Obrigação SCP >> Manutenção >> Controle das Retenções na Fonte –COFINS

	Esta tela deverá ser uma replica da tela de Retenções Disponíveis disponível no menu Obrigação >> Manutenção >> Controle das Retenções na Fonte – PIS/PASEP e Obrigação >> Manutenção >> Controle das Retenções na Fonte – COFINS, contemplando a inclusão do campo Código da SCP que servirá para detalhar a qual SCP se refere a apuração\.

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

‘

Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código\. Deverá acessar as informações da tabela SAFX2057\.

Este campo servirá com base para pesquisa das retenções geradas a partir do processamento realizado pelo menu Obrigações SCP, sendo que, se não for informado na pesquisa nenhum código da SCP para pesquisa, devem ser considerados os registros de crédito gerados para o Sócio Ostensivo, que não tem nenhum código de SCP vinculado\.

OS4316\-B

Natureza da Retenção na Fonte

DropDown

S

S

Deverá incluir na lista os indicadores:

51 – Retenção por Órgãos, Autarquias e Fundações Federais

52 – Retenção por outras Entidades da Administração Pública Federal	

53 – Retenção por Pessoa Jurídicas de Direito Privado

54 – Recolhimento por Sociedade Cooperativa

55 – Retenção por Fabricante de Máquinas e Veículos 

59 – Outras Retenções – Rendimentos sujeitos à regra específica de incidência cumulativa \(art\. 8° da Lei n° 10\.637/2002 e art\. 10 da Lei n° 10\.833/2003\)\.

OS4

649

*\* Descrição não disponível em tela*

