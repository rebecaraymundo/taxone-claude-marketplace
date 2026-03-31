# MTZ_Tela_Parâmetros_Identificador_da_Nat_da_Base_de_Credito_por_Servico

- **Fonte:** MTZ_Tela_Parâmetros_Identificador_da_Nat_da_Base_de_Credito_por_Servico.docx
- **Modificado:** 2025-06-25
- **Tamanho:** 65 KB

---

THOMSON REUTERS

Identificador da Nat\. da Base de Crédito \(por Serviço\)

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS847777

Andréa Rocha

Inclusão do código 14 \(Transporte de Cargas\) no campo Nat\. da Base de Crédito\.

# <a id="_Toc350763252"></a><a id="_Toc393731778"></a>Regras dos Campos 

__Localização da tela:__ 

Módulo: SPED 🡪 EFD\-Escrituração Fiscal Digital das Contribuições

Menu:    Parâmetros 🡪 Identificador da Nat\. da Base de Crédito 🡪 Por Código de Serviço

__Título da tela: __Identificador da Nat\. da Base de Crédito \(por Serviço\)

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Editbox 

S

N

Irá apresentar a lista de Estabelecimentos disponíveis para a Empresa\.

Nat\. da Base de Crédito

Dropdown

S

S

Default: Não selecioando

Lista das naturezas da base de crédito, disponível na 

tabela 4\.3\.7 do layout de geração da EFD\-PIS/PASEP/COFINS, conforme tabela abaixo:

COD

DESC

3

Aquisição de serviços utilizados como insumo

4

Energia elétrica e térmica, inclusive sob a forma de vapor

5

Aluguéis de prédios

6

Aluguéis de máquinas e equipamentos

7

Armazenagem de mercadoria e frete na operação de venda

13

Outras Operações com Direito a Crédito

14

Transporte de Cargas – Contratação de prestador pessoa física ou PJ transportadora, optante pelo SIMPLES

15

Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária

17

Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale\-transporte, vale\-refeição ou vale\-alimentação, fardamento ou uniforme\.

MFS847777

Grupo

Dropdown

S

S

Default: Não selecionado

Irá apresentar a lista de grupos disponíveis para o estabelecimento selecionado\.

Seleção de Serviços

Checkbox

S

S

Default: Não selecionado

Deverão estar disponíveis para seleção todos os códigos de serviços cadastrados na tabela de Códigos de Serviços \(SAFX2018\)\.

Selecionar Todos

Botão

N

N

Irá selecionar todos os serviços listados em tela\.

Desmarcar Todos

Botão

N

N

Irá desmarcar todos os serviços listados em tela\.

Replicar para os estabelecimentos

Checkbox

N

S

Default: Não selecionado

Deverá listar todos os estabelecimentos da empresa de login do sistema\.

Selecionar Todos

Botão

N

N

Irá selecionar todos os serviços listados em tela\.

Obs: Este botão será habilitado somente quando o campo “Replicar para os estabelecimentos” for selecionado\.

Desmarcar Todos

Botão

N

N

Irá desmarcar todos os serviços listados em tela\.

Obs: Este botão será habilitado somente quando o campo “Replicar para os estabelecimentos” for selecionado\.

