# MTZ_ISS_FORMATO_ESPECIFICO_EMISSAO_LIVRO_ISSQN

- **Fonte:** MTZ_ISS_FORMATO_ESPECIFICO_EMISSAO_LIVRO_ISSQN.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 61 KB

---

THOMSON REUTERS

Municipal \- ISS

ISSQN Normal – Obrigações\-Formato Específico – Emissão do Livro ISSQN

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

CH12930\_2014

Julyana Perrucini

Este documento tem como objetivo alterar a geração do Imposto a Recolher da totalização do Demonstrativo de Débito/Crédito\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

*\(reservado para regra geral do livro\)\.*

<OS>\.

__Demonstrativo Débito/Crédito: __Imposto a Recolher

RN01

Preencher com a soma do valor Total da Apuração do ISS e os lançamentos que houver para Crédito do Imposto calculando a diferença da soma desses valores aos lançamentos de Débito do Imposto, ou seja, \(\(vlr\_iss for all\)  \+ total\_credito\) \- total\_debito\.

__*Atenção: *__A regra mencionada se aplica para todos os formatos específicos, sem exceção\.

__*Observação:*__ Todos os livros específicos geram esse campo com a condição mencionada acima, porém inverteram a regra através do chamado 33863/2006 para o município de Porto Alegre, mas já haviam passado a orientação ao usuário para solução do problema e mesmo assim foi implementada a solução indevidamente acarretando falhas\.

CH12930\_2014

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

