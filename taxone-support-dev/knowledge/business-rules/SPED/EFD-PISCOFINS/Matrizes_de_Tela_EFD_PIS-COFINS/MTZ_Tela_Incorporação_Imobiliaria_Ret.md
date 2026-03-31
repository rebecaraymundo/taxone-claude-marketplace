# MTZ_Tela_Incorporação_Imobiliaria_Ret

- **Fonte:** MTZ_Tela_Incorporação_Imobiliaria_Ret.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 100 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4316\-B

Marcos G\. de Paula

Criação do campo Código da SCP\.

CH14608\_2015

Lara Aline

Alteração na nomenclatura do campo Insc\. Imobiliária para Incorporação Imobiliária\.

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

Menu: Manutenção >> Incorporação Imobiliária – Ret \(1800\)

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

S

Incluir na tela o campo Código da SCP no formato padrão do Mastersaf DW com pasta de seleção e campo de texto para digitação do código\. Deverá acessar as informações da tabela SAFX2057\.

Este campo deverá ser chave, mas não obrigatório\.

OS4316\-B

Inc\. Imobiliária

Alfanumérico

S

S

Altera a nomenclatura do campo Insc\. Imobiliária para Inc\. Imobiliária\.

Alterar também a mensagem de erro 92242 da TFIX22 de *“Inscricao Imobiliaria não informada e invalida” *para* “Incorporação Imobiliária não informada e inválida”\.*

CH14608\_2015

*\* Descrição não disponível em tela*

