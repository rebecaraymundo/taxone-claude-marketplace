# MTZ-Job-Servidor-Importacao-SAFX295

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX295.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX295

Tabela de Detalhamento das Contribuições com Exigibilidade Suspensa

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS29842

Andréa Rocha

Criação da tabela SAFX295 para geração do registro 1011, da nova versão do Sped Contribuiçõesl \(vigência Jan/2020\)\. 

19/11/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX295__ 🡪 vide manual de layout

A SAFX295 é uma tabela que referencia a tabela DWT\_PROC\_REF \(Processo Referenciado\)\.

__Campos que compõe a chave da tabela:__

                      \[Código da empresa \+ Código do estabelecimento \+ Data da geração \+ Número do processo \+ Sequencial\]

A manutenção da tabela é feita nos módulos EFD\-Contribuições e EFD\- Contribuições Financeira\.

MFS29842

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

MFS29842

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

MFS29842

__RN03__

__Campo Data Geração__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchida, ou data inválida, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*Data de Geração não preenchida ou inválida”*\)\.

MFS29842

__RN04__

__Campo Número do Processo__

Campo de preenchimento __*obrigatório*__\.

Será validada a existência do número do processo na tabela de Cadastro de Processos Referenciados \(DWT\_PROC\_REF\)\.  Se o número do processo for válido, verificar se o tipo de processo é igual a “A” \(Ação judicial\) e a natureza da ação for um código de 12 a 19\.  Somente serão aceitos os números de processo que forem do tipo “Ação judicial” e “Natureza de Ação” for do tipo “Exigibilidade suspensa”\.

Quando não preenchido, ou o número de processo inválido, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*Número do Processo não preenchido ou inválido”*\)\.

MFS29842

__RN05__

__Campo Sequencial__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“O Sequencial deve ser preenchido”\.*

MFS29842

__RN06__

__Campo Registro de Referência__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN07__

__Campo Chave de Acesso da NF\-Eletrônica__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN08__

__Campo Indicador da Pessoa Física/Jurídica __

Campo de preenchimento __*não*__ obrigatório\.

Valores válidos: '1', '2', ‘3’, ‘4’, ‘5’\.

Quando for um indicador inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo está com conteúdo inválido \(mensagem padrão\)\.

MFS29842

__RN09__

__Campo Código da Pessoa Física/Jurídica \(Destinatário/Emitente\) __

Campo de preenchimento __*não*__ obrigatório\.

A partir do conteúdo dos campos 08 e 09 \(indicador e código da pessoa fis/jur\) será verificada a existência da pessoa informada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Quando não encontrada, o registro não será importado, e no log de erros será gravada uma mensagem informando que a pessoa não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN10__

__Campo Indicador do Produto __

Campo de preenchimento __*não*__ obrigatório\.

Valores válidos, de acordo com os indicadores da Tabela de Produtos \(SAFX2013\): 1, 2, 3, 4, 5, 6, 7 e 8\.

Quando for um indicador inválido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo está com conteúdo inválido \(mensagem padrão\)\.

MFS29842

__RN11__

__Campo Produto __

Campo de preenchimento __*não*__ obrigatório\.

Será validada a existência do produto informado \(Indicador e Código\) na Tabela de Produtos \(SAFX2013\)\. 

Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN12__

__Campo Data da Operação__

Campo de preenchimento __*não*__ obrigatório\.

Deve ser uma data válida\.

Quando for uma data inválida, o registro não será importado, e no log de erros será gravada uma mensagem de erro \(“*Data de Operação inválida”*\)\.

MFS29842

__RN13__

__Campo Valor da Operação/Item__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN14__

__Campo Código Situação Tributária PIS__

Campo de preenchimento __*não*__ obrigatório\.

Será validada a existência do código informado na Tabela de Situação Tributária \(Y2027\)\. 

Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN15__

__Campo Base de Cálculo PIS__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN16__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Alíquota do PIS__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN17__

__Campo Valor Tributo PIS__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN18__

__Campo Código Situação Tributária COFINS__

Campo de preenchimento não obrigatório\.

Será validada a existência do código informado na Tabela de Situação Tributária \(Y2027\)\. 

Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN19__

__Campo Base de Cálculo COFINS__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN20__

__Campo Alíquota do COFINS__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN21__

__Campo Valor Tributo COFINS__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN22__

__Campo Código Situação Tributária PIS Suspensa__

Campo de preenchimento __*não*__ obrigatório\.

Será validada a existência do código informado na Tabela de Situação Tributária \(Y2027\)\. 

Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN23__

__Campo Base de Cálculo PIS Suspensa__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN24__

__Campo Alíquota do PIS Suspensa__

Campo de preenchimento não obrigatório\.

MFS29842

__RN25__

__Campo Valor Tributo PIS Suspensa__

Campo de preenchimento não obrigatório\.

MFS29842

__RN26__

__Campo Código Situação Tributária COFINS Suspensa__

Campo de preenchimento __*não*__ obrigatório\.

Será validada a existência do código informado na Tabela de Situação Tributária \(Y2027\)\. 

Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN27__

__Campo Base de Cálculo COFINS Suspensa__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN28__

__Campo Alíquota do COFINS Suspensa__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN29__

__Campo Valor Tributo COFINS Suspensa__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

__RN30__

__Campo Código da Conta __

Campo de preenchimento __*não*__ obrigatório\.

Será validada a existência da conta informada na Tabela de Contas \(SAFX2002\)\. 

Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN31__

__Campo Código do Centro de Custos__

Campo de preenchimento __*não*__ obrigatório\.

Será validada a existência da conta informada na Tabela de Centro de Custos \(SAFX2003\)\. 

Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o produto não existe na tabela \(mensagem padrão\)\.

MFS29842

__RN32__

__Campo Descrição do Documento__

Campo de preenchimento __*não*__ obrigatório\.

MFS29842

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

