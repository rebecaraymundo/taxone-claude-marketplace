# MTZ-Job-Servidor-Importacao_SAFX286

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX286.docx
- **Modificado:** 2022-12-21
- **Tamanho:** 107 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX286

__Ajuste/Outros Valores do Cupom Fiscal \- SAT__

__           __

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

	

\- Importação à Execução

\- Importação Batch à Programação à Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS93040

Aline Melo

Inclusão da nova SAFX286 no processo do Job Servidor\. 

26/08/2022

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX286__ à vide manual de layout

A manutenção desta tabela é feita na tela de Manutenção > Cupom Fiscal Eletrônico > Capa e Detalhe do Cupom Fiscal\-SAT, aba “Observações Cupom Fiscal – SAT”, no módulo DW: 

As informações importadas devem ser gravadas na tabela __*nova tabela\.*__

__Os campos que compõem a chave da tabela são:__

- COD\_EMPRESA \+ COD\_ESTAB \+ NUM\_EQUIP \+ NUM\_CUPOM \+ DATA\_EMISSAO \+ IDENT\_OBSERVACAO \+ COD\_AJUSTE\_SPED \+ NUM\_ITEM  	

__Processo de Importação Automática de SAFX__

Esse processo ocorre somente no TAX ONE e o mesmo já está habilitado para contemplar as novas SAFX’s\.

Para verificar as adequações necessárias, utilizar como exemplo, a SAFX04\.

MFS59797

__RN01__

__Campo Código da Empresa__

Campo COD\_EMPRESA

Campo de preenchimento __*obrigatório\.*__

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

MFS59797

__RN02__

__Campo Código do Estabelecimento__

Campo COD\_ESTAB

Campo de preenchimento __*obrigatório\.*__

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

MFS59797

__RN03__

__Número do Equipamento__

Campo NUM\_EQUIP

Campo de preenchimento __*obrigatório*__\.

MFS59797

__RN04__

__Número do Cupom Fiscal Eletrônico__

Campo NUM\_CUPOM

Campo de preenchimento __*obrigatório\.*__

MFS59797

__RN05__

__Campo Data de Emissão__

Campo DATA\_EMISSAO

Campo de preenchimento __*obrigatório\.*__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código *

MFS59797

__RN06__

__Campo Código da Observação__

Campo COD\_OBS\_LANCTO\_FISCAL

Campo de preenchimento __*obrigatório\.*__

MFS59797

__RN07__

__Campo Código do Ajuste__

Campo COD\_AJUSTE\_SPED

Campo de preenchimento __*obrigatório\.*__

__RN08__

__Campo Descrição Complementar do Ajuste__

Campo DSC\_COMPLEMENTAR

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN09__

__Campo Número do Item da Nota__

Campo NUM\_ITEM

Campo de preenchimento __*não obrigatório\.*__

__RN10__

__Campo Base de Cálculo do ICMS__

Campo VLR\_BASE\_ICMS

Campo de preenchimento __*não obrigatório\.*__

__RN11__

__Campo Alíquota do ICMS__

Campo ALIQUOTA\_ICMS

Campo de preenchimento __*não obrigatório\.*__

__RN12__

__Campo Valor do ICMS__

Campo VLR\_ICMS

Campo de preenchimento __*não obrigatório\.*__

__RN13__

__Campo Outros Valores__

Campo VLR\_OUTROS

Campo de preenchimento __*não obrigatório\.*__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

