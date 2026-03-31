# MTZ-TELA_MANUTENCAO-SAFX195

- **Fonte:** MTZ-TELA_MANUTENCAO-SAFX195.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 32 KB

---

# TELA DE MANUTENÇÃO SAFX195

# Informações Complementares de Informe de Rendimentos Financeiros

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3752\-A

Criação do documento

Definição das regras para a tela de manutenção da tabela SAFX195\.

REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Deverá ser criada uma nova tela para manutenção das informações referentes à SAFX195 no seguinte caminho:

Módulo: Federal >> Obrigações de Tributos Federais

Caminho no menu: Rendimentos >> Rendimentos Financeiros

Nome da Tela: Informações Complementares de Informe de Rendimentos Financeiros

OS3752\-A

__RN02__

Nesta tela estarão disponíveis os campos:

- Estabelecimento *\(campo obrigatório\)*
- Ano Calendário *\(campo obrigatório\)*
- Pessoa Fís\./Jur\. *\(campo obrigatório\)*
- Código Pessoa Fís\./Jur\. *\(campo obrigatório\)*
- CPF do Beneficiário
- Frame Rendimentos Isentos com os campos:
	- Contas de Poupança e Letras Hipotecárias – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Contas de Poupança e Letras Hipotecárias – Coluna Saldos em 31/12 Ano\-Calendário
	- Contas de Poupança e Letras Hipotecárias – Coluna Rendimentos
	- Lucros e Dividendos apurados a partir de 1996 e distribuídos no ano\-calendário – Coluna Rendimentos
	- Demais Rendimentos Isentos – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Demais Rendimentos Isentos – Coluna Saldos em 31/12 Ano\-Calendário
	- Demais Rendimentos Isentos – Coluna Rendimentos
- Frame Rendimentos Sujeitos à Tributação Exclusiva com os campos:
	- Fundos de Investimento – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Fundos de Investimento – Coluna Saldos em 31/12 Ano\-Calendário
	- Fundos de Investimento – Coluna Rendimentos Líquidos
	- Aplicações de Renda Fixa – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Aplicações de Renda Fixa – Coluna Saldos em 31/12 Ano\-Calendário
	- Aplicações de Renda Fixa – Coluna Rendimentos
	- Títulos de Capitalização – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Títulos de Capitalização – Coluna Saldos em 31/12 Ano\-Calendário
	- Títulos de Capitalização – Coluna Rendimentos Líquidos
	- Juros sobre Capital Próprio – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Juros sobre Capital Próprio – Coluna Saldos em 31/12 Ano\-Calendário
	- Juros sobre Capital Próprio – Coluna Rendimentos Líquidos
	- Operações Swap – Coluna Rendimentos Líquidos
	- Previdência Complementar, Fapi, PGBL e VGBL – Coluna Rendimentos Líquidos
	- Demais Rendimentos Sujeitos à Tributação Exclusiva – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Demais Rendimentos Sujeitos à Tributação Exclusiva – Coluna Saldos em 31/12 Ano\-Calendário
	- Demais Rendimentos Sujeitos à Tributação Exclusiva – Coluna Rendimentos Líquidos
- Frame Saldos em Contas Correntes e em VGBL com os campos:
	- Depósito em Conta Corrente de Depósito à Vista ou de Investimento – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Depósito em Conta Corrente de Depósito à Vista ou de Investimento – Coluna Saldos em 31/12 Ano\-Calendário
	- Prêmios Acumulados em VGBL – Coluna Saldos em 31/12 Ano\-Calendário Anterior
	- Prêmios Acumulados em VGBL – Coluna Saldos em 31/12 Ano\-Calendário
- Frame Créditos em Trânsito com os campos:
	- Fundos e Clubes de Investimento – Coluna Valores em 31/12 Ano\-Calendário Anterior
	- Fundos e Clubes de Investimento – Coluna Valores em 31/12 Ano\-Calendário
	- Demais Créditos em Trânsito – Coluna Valores em 31/12 Ano\-Calendário Anterior
	- Demais Créditos em Trânsito – Coluna Valores em 31/12 Ano\-Calendário

OS3752\-A

__RN03__

Campo Estabelecimento

Ao acessar a tela deverá ser carregado automaticamente o estabelecimento parametrizado no manager antes do acesso ao módulo de Obrigações de Tributos Federais\.

OS3752\-A

__RN04__

Campo Pessoa Fís\./Jur\.

Será um campo do tipo lista que terá as opções:

Fornecedor

Cliente

Estabelecimento

Transportadora

Cliente/Fornecedor/Transportadora

Poderá ser parametrizado pelo usuário ou ter a sua informação preenchida automaticamente quando for indicado um registro na leitura da tabela SAFX04, como é padrão no DW\.

OS3752\-A

__RN05__

Campo Código Pessoa Fís\./Jur\.

Será um campo de texto e poderá ser parametrizado pelo usuário ou ter a sua informação preenchida automaticamente quando for indicado um registro na leitura da tabela SAFX04, como é padrão no DW\.

OS3752\-A

__RN06__

Campo CPF do Beneficiário

Será um campo de texto que não permitirá digitação\. Deve recuperar a informação do campo CGC\-CPF do Cadastro de Pessoa Física/Jurídica vinculado ao registro e demonstrá\-la como display\.

OS3752\-A

__RN07__

Campos de valor

Os campos de valor foram divididos em frames e estão estruturados em linhas e colunas\. Teremos então:

- Frame Rendimentos Isentos:
	- Colunas: Saldos em 31/12 Ano\-Calendário Anterior, Saldos em 31/12 Ano\-Calendário e Rendimentos;
	- Linhas: Contas de Poupança e Letras Hipotecárias, Lucros e Dividendos apurados a partir de 1996 e distribuídos no ano\-calendário e Demais Rendimentos Isentos;

Tratamento diferenciado: para este frame a linha “Lucros e Dividendos apurados a partir de 1996 e distribuídos no ano\-calendário” demonstrará informações apenas na coluna de “Rendimentos”\.

- Frame Rendimentos Sujeitos à Tributação Exclusiva:
	- Colunas: Saldos em 31/12 Ano\-Calendário Anterior, Saldos em 31/12 Ano\-Calendário e Rendimentos Líquidos;
	- Linhas: Fundos de Investimento, Aplicações de Renda Fixa, Títulos de Capitalização, Juros sobre Capital Próprio, Operações Swap, Previdência Complementar, Fapi, PGBL e VGBL, Demais Rendimentos Sujeitos à Tributação Exclusiva;

Tratamento diferenciado: para este frame as linhas “Operações Swap” e “Previdência Complementar, Fapi, PGBL e VGBL” demonstrarão informações apenas na coluna “Rendimentos Líquidos”\.

- Frame Saldos em Contas Correntes e em VGBL:
	- Colunas: Saldos em 31/12 Ano\-Calendário Anterior e Saldos em 31/12 Ano\-Calendário;
	- Linhas: Depósito em Conta Corrente de Depósito à Vista ou de Investimento, Prêmios Acumulados em VGBL;
- Frame Créditos em Trânsito:
	- Colunas: Valores em 31/12 Ano\-Calendário Anterior e Valores em 31/12 Ano\-Calendário
	- Linhas: Fundos e Clubes de Investimento e Demais Créditos em Trânsito

Deverá ser demonstrada a informação para estes campos no formato padrão do DW\.

OS3752\-A

__RN08__

Deverá ser criado um relatório para exibição dos registros lidos na tela como é padrão do DW\.

OS3752\-A

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

