# Roteiro_Testes_BETHA

- **Fonte:** Roteiro_Testes_BETHA.docx
- **Modificado:** 2023-08-09
- **Tamanho:** 77 KB

---

### Validador \- BETHA 

### Roteiro de Testes

__OS/CH/MFS__

__Nome__

__Descrição__

Rosemeire Santos

Este documento tem como objetivo auxiliar na criação de massa de dados e na validação dos municípios que utilizam o validador BETHA\.

### REGRAS DE NEGÓCIO 

__Regra__

__DESCRIÇÃO__

__MFS__

__RN01__

__Estrutura de menus do módulo BETHA:__

- Arquivo
- Manutenção
	- Materiais
- Obrigações
	- Meio Magnético
	- Meio Magnético – Bancos
	- Geração – Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)

__RN02__

Arquivo no formato TXT\.

__RN03__

O Modulo deve estar licenciado\.

__RN04__

__Constar nos Parâmetros para Municípios:__

- Parâmetros – Tipo Docto Msaf x Tipo Docto

- Parâmetros – Classificação de Serviços

- Parâmetros – Serviços Bancários

- 
	- 
		- Plano de Conta Referencial

- 
	- 
		- Plano de Contas x Códigos de Serviços

__RN05__

__Espécie de Documentos aceitas \- Regra RN27\. __

- C\-Cupom Fiscal           

- J\-Nota Fiscal Conjugada  

- N\-Nota Fiscal            

- O\-Outros                 

- R\-Recibo                 

__RN06__

__Situação do documento aceitas \- Regra RN28\. __

- N\-Normal 

- C\-Cancelada 

- A\- Anulada 

- I\- Isenta

- R\- Retida

- S\- Substituta 

- T\- Não tributável 

- E\- Regime especial

__RN07__

__Natureza da operação \- Regra RN34\. __

- Parâmetros – Classificação de Serviços

- 
	- 
		- 
			- 1 \- Tributação no município 

- 
	- 
		- 
			- 2 \- Tributação fora do município 

- 
	- 
		- 
			- 3 \- Isenção 

- 
	- 
		- 
			- 4 \- Imune 

- 
	- 
		- 
			- 5 \- Exigibilidade suspensa por decisão judicial 

- 
	- 
		- 
			- 6 \- Exigibilidade suspensa por procedimento administrativo 

- 
	- 
		- 
			- 7 \- Não incidência 

__RN08__

__Tipos de Serviços __\- __Regras TMZ RN06, RN07 e \(RN07\.a Específicas\)\.__

O arquivo gera dados de serviços prestados e tomados\.

__RN09__

__Deduções de Materiais \- __O tipo de registro 5 será utilizado somente por prestadores enquadrados como construtoras, possibilitando 

a declaração dos materiais\.

Tem aba Manutenção para inclusão dos Parâmetros \- __Regras MTZ RN52 e RN53\.__

__RN10__

__Meio Magnético Serviços Bancários \- __O tipo de registro 4 serão utilizados somente por prestadores enquadrados como declarantes

 por planos de contas\.

Tem uma regra especifica no __MTZ RN45\.__

__RN11__

Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

