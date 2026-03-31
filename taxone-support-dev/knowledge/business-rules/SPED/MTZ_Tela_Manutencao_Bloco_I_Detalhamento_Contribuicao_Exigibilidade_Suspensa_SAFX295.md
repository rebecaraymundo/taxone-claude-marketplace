# MTZ_Tela_Manutenção_Bloco I_Detalhamento_Contribuicao_Exigibilidade_Suspensa_SAFX295

> Fonte: MTZ_Tela_Manutenção_Bloco I_Detalhamento_Contribuicao_Exigibilidade_Suspensa_SAFX295.docx






THOMSON REUTERS

Módulo EFD-Contribuições – Manutenção da Tabela SAFX295

SAFX295 - Tabela de Detalhamento das Contribuições com Exigibilidade Suspensa


Localização: Menu SPED, Módulo: EFD – Escrituração Fiscal Digital das Contribuições, item Manutenção  Registro do bloco I  Detalhamento das Contribuições com Exigibilidade Suspensa

Localização: Menu SPED, Módulo: EFD – Contribuições Financeira/Assemelhada, item Manutenção  Registro do bloco 1  Detalhamento das Contribuições com Exigibilidade Suspensa




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	3
3.	Regras de Funcionamento dos Campos	4
























## Regras Gerais


A SAFX295 (“Detalhamento das Contribuições com Exigibilidade Suspensa”) é uma tabela que referencia a tabela DWT_PROC_REF (Cadastro do Processo Referenciado).


Esta tabela será usada para gerar o registro 1011 do EFD-Contribuições, que é filho do registro 1010.  O registro 1010 é gerado baseado no cadastro do processo referenciado.

Estrutura das tabelas  vide manual de layout

Campos que compõe a chave das tabelas:

[Código da empresa + Código do estabelecimento + Data da geração + Número do processo + Sequencial]



## Layout da Tela




Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS29842 | Andréa Rocha | Criação da tabela SAFX295 para geração do registro 1011, da nova versão do SPED - EFD- Contribuições SPED - EFD- Contribuições Financeira (vigência Jan/2020). | 22/11/2019 |
|  |  |  |  |
|  |  |  |  |


| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro. |
| --- | --- |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão do registro. |
| CONFIRMA | Opção para salvar as informações do registro incluído ou alterado. |
| RELATÓRIO | Esta opção permite imprimir os dados da tabela. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S | Listbox | Neste campo será exibida a lista dos estabelecimentos da empresa para seleção do usuário.  Caso tenha sido informado um estabelecimento no login, este campo exibirá fixo o estabelecimento informado, e o usuário não poderá alterá-lo. | MFS29842 |
| Data Geração | Data | S | S | (DD/MM/AAAA) | Neste campo será informada uma data válida. | MFS29842 |
| Número do Processo | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da Tabela de Cadastro de Processo Referenciado (DWT_PROC_REF).  Serão disponibilizadas para seleção apenas os processos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os processos com data de validade <= a data da geração.  - Apenas os processos com o tipo de processo igual a “A” (Ação judicial).    - Apenas os processos em que a natureza da ação for um código de 12 a 19 (Exigibilidade suspensa).    Em caso de processos de mesmo código e validades diferentes, será exibida apenas a linha mais atual, considerando a data da geração (a de maior validade que seja <= a data do documento fiscal).  Quando o Número do Processo for digitado, será validado a sua existência na tabela, considerando as regras acima sobre Grupo e data de validade. Caso não exista, será exibida a mensagem “Número do Processo não cadastrado ou inválido”. | MFS29842 |
| Sequencial | Alfanumérico | S | S |  | Neste campo será informado o sequencial. | MFS29842 |
| Registro de Referência | Alfanumérico | N | S |  | Neste campo será informado o Código do registro de referência. | MFS29842 |
| Chave de Acesso da NF-Eletrônica | Alfanumérico | N | S |  | Neste campo será informada Chave de Acesso da NF-Eletrônica | MFS29842 |
| Pessoa Física/Jurídica | Alfanumérico | N | S | Formato: Text Input/ Pasta de Seleção SAFX04 | Este campo trabalha com janela de seleção da Tabela da Pessoa Física/Jurídica (SAFX04).  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código da pessoa fis/jur for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Pessoa Física/Jurídica não cadastrada”. | MFS29842 |
| Produto | Alfanumérico | N | S | Formato: Text Input/ Pasta de Seleção SAFX2013 | Este campo trabalha com janela de seleção da Tabela da Produto (SAFX2013).  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código do produto for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Produto não cadastrado”. | MFS29842 |
| Data da Operação | Data | N | S | (DD/MM/AAAA) | Neste campo será informada uma data válida. | MFS29842 |
| Valor da Operação/Item | Numérico | N | S |  | Neste campo será informado o valor da operação. | MFS29842 |
| Código Situação Tributária PIS | Numérico | N | S | Formato: Text Input/ Pasta de Seleção TACES65 | Este campo trabalha com janela de seleção da Tabela de situação tributária do PIS/PASEP (TACES65).  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código da situação for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Código não cadastrado”. | MFS29842 |
| Base de Cálculo PIS | Numérico | N | S |  | Neste campo será informado a base de cálculo do PIS. | MFS29842 |
| Alíquota do PIS | Numérico | N | S |  | Neste campo será informado a alíquota do PIS. | MFS29842 |
| Valor PIS | Numérico | N | S |  | Neste campo será informado o valor do PIS. | MFS29842 |
| Código Situação Tributária COFINS | Numérico | N | S | Formato: Text Input/ Pasta de Seleção TACES65 | Este campo trabalha com janela de seleção da Tabela de situação tributária do PIS/PASEP (TACES65).  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código da situação for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Código não cadastrado”. | MFS29842 |
| Base de Cálculo COFINS | Numérico | N | S |  | Neste campo será informado a base de cálculo do COFINS. | MFS29842 |
| Alíquota do COFINS | Numérico | N | S |  | Neste campo será informado a alíquota do COFINS. | MFS29842 |
| Valor COFINS | Numérico | N | S |  | Neste campo será informado o valor do COFINS. | MFS29842 |
| Código Situação Tributária PIS Suspensa | Numérico | N | S | Formato: Text Input/ Pasta de Seleção TACES65 | Este campo trabalha com janela de seleção da Tabela de situação tributária do PIS/PASEP (TACES65).  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código da situação for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Código não cadastrado”. | MFS29842 |
| Base de Cálculo PIS Suspensa | Numérico | N | S |  | Neste campo será informado a base de cálculo do PIS Suspensa. | MFS29842 |
| Alíquota do PIS Suspensa | Numérico | N | S |  | Neste campo será informado a alíquota do PIS Suspensa. | MFS29842 |
| Valor PIS Suspensa | Numérico | N | S |  | Neste campo será informado o valor do PIS Suspensa. | MFS29842 |
| Código Situação Tributária COFINS Suspensa | Numérico | N | S | Formato: Text Input/ Pasta de Seleção TACES65 | Este campo trabalha com janela de seleção da Tabela de situação tributária do PIS/PASEP (TACES65).  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código da situação for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Código não cadastrado”. | MFS29842 |
| Base de Cálculo COFINS Suspensa | Numérico | N | S |  | Neste campo será informado a base de cálculo do COFINS Suspensa. | MFS29842 |
| Alíquota do COFINS Suspensa | Numérico | N | S |  | Neste campo será informado a alíquota do COFINS Suspensa. | MFS29842 |
| Valor COFINS Suspensa | Numérico | N | S |  | Neste campo será informado o valor do COFINS Suspensa. | MFS29842 |
| Conta Contábil | Alfanumérico | N | S | Formato: Text Input/ Pasta de Seleção SAFX2002 | Este campo trabalha com janela de seleção da Tabela de Plano de Contas.  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código da pessoa fis/jur for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Conta Contábil não cadastrada”. | MFS29842 |
| Centro de Custo | Alfanumérico | N | S | Formato: Text Input/ Pasta de Seleção SAFX2003 | Este campo trabalha com janela de seleção da Tabela de Centro de Custo (SAFX2003).  Serão disponibilizadas para seleção apenas os códigos que atendam as seguintes condições:  - Apenas do Grupo (Relacionamento Tabelas x Grupo) válido para o estabelecimento e a data da geração em questão;  - Apenas os códigos com data de validade <= a data da geração.  Quando o código da pessoa fis/jur for digitado, será validada a sua existência na tabela. Caso não exista, será exibida a mensagem “Centro de Custo não cadastrado”. | MFS29842 |
| Descrição do Documento | Alfanumérico | N | S |  | Neste campo será informada a descrição do documento. | MFS29842 |
