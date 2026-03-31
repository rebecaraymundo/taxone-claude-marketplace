# MTZ_Tela_Numero_Ordem

- **Fonte:** MTZ_Tela_Numero_Ordem.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 96 KB

---

THOMSON REUTERS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4745

Marcos G\. de Paula

Atualização das opções disponíveis no campo Tipo de Livro

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

Menu: Parâmetros

__Título da tela: __Número de Ordem

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Tipo Livro

Alfa

S

S

Formato: Dropdown

Default: não preenchido

Considerar a seguinte formatação para exibição:

- Z – Razão Auxiliar \(Livro Contábil Auxiliar conforme Leiaute definido nos Registros I500\)
- A – Livro Diário Auxiliar com Escrituração Resumida
- G – Livro Diário \(Completa sem Escrituração Auxiliar\)
- R – Livro Diário com Escrituração Resumida \(com Escrituração Auxiliar\)
- B – Livro Balancetes Diários e Balanços \(Matriz\)
- S – Escrituração SCP Mantida pelo Sócio Ostensivo

Por ser campo obrigatório, se não for informado, retornar a mensagem: “Informar o Livro”\.

OS4745

Livro Auxiliar ao Diário

Alfa

N

S

Formato: Dropdown

Default: não preenchido

Exibe a relação de Livros Auxiliares ao Diário\. Fica habilitado apenas quando o campo Tipo Livro é igual a “Z – Razão Auxiliar \(Livro Contábil Auxiliar conforme Leiaute definido nos Registros I500\)” ou “A – Livro Diário Auxiliar com Escrituração Resumida”

*\* Descrição não disponível em tela*

