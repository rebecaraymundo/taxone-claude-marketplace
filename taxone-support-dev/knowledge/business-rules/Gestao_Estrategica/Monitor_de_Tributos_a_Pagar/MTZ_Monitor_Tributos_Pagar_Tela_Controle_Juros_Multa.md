# MTZ_Monitor_Tributos_Pagar_Tela_Controle_Juros_Multa

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Tela_Controle_Juros_Multa.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Controle de Juros e Multa

Tax Monitor

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-5050

Controle  de Juros e Multa 

Criação da tela de controle de juros e multas

MFS\-6310

Geração do Arquivo de Impostos Apurados

Retirar os impostos ICMS e ICMS\-ST 

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc355275051)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc355275052)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc355275053)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc355275054)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc355275055)

[2\.	Regras dos Campos	5](#_Toc355275056)

# <a id="_Toc355275051"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc355275052"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc355275053"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

\[Quem executará o evento\. Ex\.: Usuário do sistema\]\.

__Pré\- Condições__

\[Condições necessárias para execução\. Ex\.: Estabelecimento cadastrado\]

__Pós\-Condições__

\[Resultado após executar caso de uso\. Ex\.: Informação armazenada no banco de dados\]

### <a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a><a id="_Toc355275054"></a>Fluxo Principal 

\[Descrever a ação principal que será realizada na tela especificada\.

 Ex\.: O usuário deseja realizar o cadastro de uma estrutura padrão\.

__Ações do Ator__

__Ações do Sistema__

\[Descrever a interação do ator com o sistema\. 

Ex\.: O usuário acessa a tela de estrutura padrão\]\.

\[Descrever a ação esperada do sistema

Ex\.:O sistema apresenta a tela, conforme as regras definidas no tópico “Regras dos Campos”\.\]

\[Ex\.:O usuário preenche os campos da Manutenção de Estrutura do Produto\.

__<<Fluxo Alternativo 1>>__

\[Ex\.:O sistema apresenta os campos preenchidos\.\]

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

### <a id="_Toc355275055"></a>Fluxo Alternativo 1 – Localizar registros \(Exemplo\)

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Localizar”\.

O sistema apresenta os registros cadastrados, de acordo com os parâmetros informados\.

__Fim do fluxo Alternativo__

# <a id="_Toc350763252"></a><a id="_Toc355275056"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Solução Complementar >> Tax Monitor

                           Menu: Painel 

__Título da tela: __Controle de Juros e Multas

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Dropdown

N

S

Defaut: Não preenchido

Deverá exibir a lista dos estabelecimentos pertencentes à empresa logada e permissão de acesso pelo usuário, juntamente com a opção “Todos”\.

Obs: Quando selecionado a opção “todos”, o campo “conta” deverá ser bloqueado\.

MFS\-5050

Data Inicial

Text 

S

S

Formato: DD/MM/AAAA

Caso o campo não esteja preenchido deve ser exibida a seguinte mensagem de erro: “Informe Data Inicial”\.

MFS\-5050

Data Final

Text 

S

S

Formato: DD/MM/AAAA

A Data Final informada deve ser maior ou igual a Data Inicial\. Caso seja informada uma data menor, retornar a mensagem: “Data Final deve ser maior ou igual a Data Inicial”\.

Caso o campo não esteja preenchido deve ser exibida a seguinte mensagem de erro: “Informe Data Final”\.

Obs: A data deverá ser sempre o último dia do mês, caso contrário exibir a seguinte mensagem: “Informe o último dia do mês”\.

MFS\-5050

Grupo Tributo

Dropdown 

S

S

Defaut: Não preenchido

Preencher conforme abaixo:

     Todos

1 – Federal

2 – Estadual 

3 – Municipal 

4 – Previdenciário

Caso o campo não esteja preenchido, deve ser exibida a seguinte mensagem de erro: “Informe Grupo Tributo”\.

Não serão apresentados os respectivos “números” dos tributos, apenas a descrição\. Estes números serão a referencia para o campo “grupo\_tributo” da TFIX140\.

Obs: Quando selecionado a opção “todos”, o campo “conta” deverá ser bloqueado\.

MFS\-5050

Tributo

Dropdown

S

S

Será habilitado quando for informado o Grupo Tributo, demonstrando apenas os Tributos relacionados ao Grupo indicado, conforme regras abaixo:

Para o Grupo Federal, demonstrar as opções:

- TODOS
- IRPJ
- IRRF
- CSLL
- PIS/PASEP
- COFINS 
- IPI
- PIS/PASEP \(PRÓPRIO\)
- COFINS \(PRÓPRIO\)

MFS\-6310

Para o Grupo Municipal, demonstrar as opções:

- ISS

Para o Grupo Previdenciário, demonstrar as opções:

- INSS

Caso o campo não esteja preenchido, deve ser exibida a mensagem de erro: “Informe Tributo”\.

Obs: Caso a opção “Todos” esteja preenchido no campo “Grupo tributo” este campo receberá o valor “Todos” automaticamente\.

MFS\-5050

MFS\-6310

Conta \(Gr\./Cód\./Data Val\.\):

Pasta

N

S

Defaut: Não preenchido

Deverão ser listadas somente as contas cadastradas na tela de Conta Contábil x Tributo, ou seja, serão apresentadas conforme filtro por grupo e tributo\.

MFS\-5050

Consultar

Botão

N

N

Quando acionado irá consultar as informações conforme parâmetros de seleção\.

MFS\-5050

 Estabelecimento

Text 

N

N

Serão listados o\(s\) estabelecimento\(s\) conforme consulta\.

MFS\-5050

Código da Conta

Text

N

N

Serão listadas a\(s\) conta\(s\) conforme consulta\.

MFS\-5050

Data Apuração

Text 

N

N

Serão listadas a\(s\) data\(s\) conforme consulta\.

MFS\-5050

Grupo Tributo

Text

N

N

Serão listados o\(s\) grupo\(s\) conforme consulta\.

MFS\-5050

Tributo

Text

N

N

Serão listados o\(s\) tributo\(s\) conforme consulta\.

MFS\-5050

Data de Pagamento

Text

N

N

 Serão listadas a\(s\) Data\(s\) conforme consulta\.

MFS\-5050

Valor Principal

Text

N

N

Serão listados o\(s\) valore\(s\) conforme consulta\.

MFS\-5050

Juros

Text

N

N

Serão listados o\(s\) valore\(s\) conforme consulta\.

MFS\-5050

Multa

Text

N

N

Serão listados o\(s\) valore\(s\) conforme consulta\.

MFS\-5050

Valor Total

Text

N

N

Serão listados o\(s\) valore\(s\) conforme consulta\.

MFS\-5050

Total

Text 

N

N

Deverá totalizar os campos Valor Principal, Juros, Multa e Valor Total\.

MFS\-5050

