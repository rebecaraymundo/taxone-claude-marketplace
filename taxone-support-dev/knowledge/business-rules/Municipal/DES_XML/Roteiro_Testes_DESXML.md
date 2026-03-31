# Roteiro_Testes_DESXML

- **Fonte:** Roteiro_Testes_DESXML.docx
- **Modificado:** 2025-11-25
- **Tamanho:** 75 KB

---

### Validador \- DESXML

### Roteiro de Testes

__OS/CH/MFS__

__Nome__

__Descrição__

Rosemeire Santos

Este documento tem como objetivo auxiliar na criação de massa de dados e na validação dos municípios que utilizam o validador DESXML\.

### REGRAS DE NEGÓCIO 

__Regra__

__DESCRIÇÃO__

__MFS__

__RN01__

__Estrutura de menus do módulo DESXML:__

Deverão ser criado o seguinte menu e sub\-menus no módulo DES XML:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
- Janela
- Ajuda

__RN02__

Arquivo no formato XML\.

__RN03__

Módulo deve estar licenciado, estabelecimento cadastrado com município e inscrição municipal\.

__RN04__

__Constar nos Parâmetros para Municípios:__

- Parâmetros – Tipo Docto Msaf x Tipo Docto

- Parâmetros – Classificação de Serviços

__RN05__

__Tipos de Serviços\.__

O arquivo gera apenas serviços tomados\.

O sistema tem a funcionalidade para dar aceite nas notas que são do mesmo município\.

__Regra RN05 \- Específica __> Desconsiderar as Notas Fiscais de Prestadores de Serviços quando forem do Município de Mococa/SP

__RN06__

__Tipos de documentos aceitos \- Regra RN25: 			__

- CUPOM FISC \- Cupom Fiscal                                          	
- EXTRATO \- Extrato                                                  	
- FATURA \- Fatura                                                    	
- MISTA \- Nota Fiscal Conjugada Estadual/Municipal                   	
- NADA \- Nao houve emissao de documento                              	
- NFFS \- Nota Fiscal Fatura de Servicos                              	
- NFS \- Nota Fiscal de Servicos                                     	
- NFSS \- Nota Fiscal Simplificada de Servico                         	
- RECIBO \- Recibo                                                    	
- RPA \- Recibo de Profissional Autonomo                             	
- NFSEO \- Nota Fiscal de Servicos Eletronica de Outros Municipios    	
- OUTROS \- Outros Tipos de Nota          

                            	

__RN07__

__Situação dos documentos aceitos \- Regra RN28:			__

- 1 \- Nota Normal:			
- 2 \- Nota Cancelada:			
- 3 \- Nota Extraviada:			
- 4 \- Nota de Devolução:			
- 5 \- Nota Não Tributada: Parâmetros – Classificação de Serviços

__RN08__

__Operações de Notas \- Regra RN21:			__

 “I” – Inclusão: Quando o campo Tipo da Operação da tela de geração, estiver selecionado com a opção “Inclusão”\.	 “A” – Alteração: Quando o campo Tipo da Operação da tela de geração, estiver selecionado com a opção “Alteração”

 “E” – Exclusão:  Quando o campo Tipo da Operação da tela de geração, estiver selecionado com a opção “Exclusão”\.

__RN09__

__Tipo de Pessoa \- Regra RN33:	__

 F – Pessoa Física 		

 J – Pessoa Jurídica 		

 E – Pessoa do Exterior		

__RN10__

__Serviços \- Regras RN48, RN49, RN50, RN51, RN52, RN53, RN54, RN60, RN61 e RN62:__

	

<CodigoServico>			

 ✔ Campo obrigatório\.			

 ✔ Deve fazer parte do cadastro de serviços\.			

			

<ValorNota>			

 ✔ Campo obrigatório se nota é normal ou não tributada\. Nas demais situações \(cancelada,	

devolvida ou extravida\), o valor da nota pode não ser informado\.			

 ✔ Os demais campos de valores da nota, seguem a mesma regra referente á situação da		

nota\.			

			

<ValorDeducao>			

 ✔ Campo não obrigatório\.			

 ✔ Se informado não pode ser Maior ou igual ao valor da nota\.			

			

<BaseCalculo>			

 ✔ Campo obrigatório\.			

 ✔ Deve ser sempre igual ao valor da nota menos dedução\.			

			

<AliqISS>			

✔ Campo não obrigatório\.			

✔ Não pode ser um valor negativo ou >= a 100\.			

			

<ISSDevido>			

 ✔ Campo não obrigatório\.			

 ✔ Não pode ser um valor negativo ou >= à base de cálculo da nota			

			

<ISSRetido>			

 ✔ Campo não obrigatório\.			

 ✔ Não pode ser um valor negativo ou >= à base de cálculo da nota\.			

			

 ✔ Se ISSDevido foi informado, então ISS Retido deve ser igual a zero\.			

 ✔ Se ISSRetido foi informado, então ISS Devido deve ser igual a zero			

 ✔ Se ISSDevido igual a zero e ISSRetido igual a zero, a situação da nota deve ser		

 obrigatoriamente não tributada\.			

			

<Observacao>			

 ✔ Campo não obrigatório\.			

 ✔ Observação sobre o item de serviço\.			

			

<QtdfNfeIncluidas>			

 ✔ Informar a quantidade total de notas cujo campo OperacaoNota = I			

<QtdfNfeAlteradas>			

 ✔ Informar a quantidade total de notas cujo campo OperacaoNota = A			

<QtdfNfeExcluidas>			

 ✔ Informar a quantidade total de notas cujo campo OperacaoNota = E			

__CONSIDERAÇÕES DESTE MODELO:__

1. __Quando uma Regra de Negócio for EXCLUÍDA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[EXCLUÍDA – __Descrição da Regra de Negócio 01\]

MFS\-XXXX

1. __Quando uma Regra de Negócio for ALTERADA, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrita abaixo:__

__RN01__

__\[ALTERADA – MFS\-XXXX\]__ Descrição da Regra de Negócio 01

MFS\-XXXX

