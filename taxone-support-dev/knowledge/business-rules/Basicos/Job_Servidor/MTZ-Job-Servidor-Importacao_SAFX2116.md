# MTZ-Job-Servidor-Importacao_SAFX2116

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX2116.docx
- **Modificado:** 2020-03-13
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2116

Tabela de Parametrização do Plano de Contas da Empresa x Códigos de Tributação DESIF 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS32572

Liliane Assaf

Criação da SAFX2116 para atendimento a DES\-IF 

04/03/2020

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Tabela de Parametrização do Plano de Contas da Empresa x Códigos de Tributação DESIF \(SAFX2116\)__

__Estrutura da tabela SAFX2116__ 🡪 vide manual de layout

A SAFX2116 tem como objetivo permitir a parametrização da conta contábil relacionada a um Código de Tributação DES\-IF\.

O Código de Tributação DES\-IF é oriundo da Tabela de Códigos de Tributação DESIF \- Anexo 6, carregada via importação da TACES102\.

A conta contábil é oriunda do Plano de Contas \(SAFX2002\)\.

A parametrização só permite que a conta contábil seja associada a um Código de Tributação DES\-IF, numa determinada vigência estabelecida pelas datas início e fim de validade\.

O sistema fará um controle para NÃO permita gravação de intervalos intercalados para uma conta contábil

__Campos que compõe a chave da tabela definitiva \(X2116\_CONTA\_TRIB\_DESIF\):__

 Grupo da Conta Contábil \(GRUPO\_CONTA\),

 Código da Conta Contábil \(COD\_CONTA\),

 Data de Vigência Inicial \(VALID\_INI\)

A manutenção da tabela está disponível no módulo Municipal >> Parâmetros para Município, menu: Parâmetros 🡪 Serviços Bancários 🡪 DES\-IF 🡪 Plano de Contas da Empresa x Códigos de Tributação DESIF\.

__Base Legal:__

Secretaria Municipal de Fazenda da Prefeitura de São Paulo:

Instrução Normativa SF/SUREM Nº 17, DE 26 DE SETEMBRO DE 2017

Portaria SF/SUREM nº 57, de 4 de outubro de 2017

 

MFS32572

__RN01__

__Campo Conta Contábil__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*90011\-* *Conta Contabil deve ser preenchida*\.”\)\.

O código informado deve existir na Tabela do Plano de Contas \(SAFX2002\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que a conta contábil não existe na tabela \(mensagem: “*93330 \- Conta Contabil nao cadastrada ou data de validade posterior a data de vigência inicial*”\)\.

MFS32572

__RN02__

__Campo Data de Vigência Inicial__

Campo de preenchimento __*obrigatório*__\.

Deve ser uma data válida\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                  “900025 \- O parametro data de vigencia inicial nao pode ser nulo e deve ser uma data valida\.”*

MFS32572

__RN03__

__Campo Data de Vigência Final__

Deve ser uma data válida\.

Quando não for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                  “900026\- O parametro data de vigencia final deve ser uma data valida\.”*

Se o usuário preencher a data final de vigência menor que a data inicial de vigência, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                  “93333 \- O parametro data de vigencia final não pode ser menor que data de vigencia inicial\.”*

Se já existir registro na base para a Conta Contábil \(grupo e código da conta\), então verificar se período formado pelas datas de vigência Inicial e Final do registro que está sendo importado, não se intercala com o período de algum registro existente na Tabela de Parametrização do Plano de Contas da Empresa x Códigos de Tributação DESIF\.

Para isso executar o seguinte procedimento:

1\) Recuperar o registro imediatamente anterior ao que está sendo importado:

Recuperar o registro da “Tabela de Parametrização do Plano de Contas da Empresa x Códigos de Tributação DESIF” de acordo com os seguintes critérios:

- Grupo e Código da Conta Contábil igual ao do registro ser importado;
- Data de Vigência Inicial menor que a Data de Vigência Inicial do registro a ser importado\.

Recuperar o registro de máxima Data de Vigência Inicial que atenda aos critérios acima\.

Caso seja encontrado registro, então comparar a Data de Vigência Final do registro recuperado com a Data de Vigência Inicial do registro a ser importado\.

Se Data de Vigência Final do registro recuperado for nulo,

ou 

Se Data de Vigência Final do registro recuperado >= Data de Vigência Inicial do registro a ser importado, então:

O registro não será importado e será gravada a seguinte mensagem de erro:

* “93334\-* *Existe parametrizacao para Conta Contabil com Vigencia Inicial anterior a que esta sendo importada e com Data de Vigencia Final nao preenchida ou maior que a Data de Vigencia Inicial importada” *

2\) Recuperar o registro imediatamente posterior ao que está sendo importado:

Recuperar o registro da “Tabela de Parametrização do Plano de Contas da Empresa x Códigos de Tributação DESIF” de com os seguintes critérios:

- Grupo e Código da Conta Contábil igual ao do registro ser importado;
- Data de Vigência Inicial maior que a Data de Vigência Inicial do registro a ser importado\.

Recuperar o registro de menor Data de Vigência Inicial que atenda aos critérios acima\.

Caso seja encontrado registro, então comparar a Data de Vigência Inicial do registro recuperado com a Data de Vigência Final do registro a ser importado\.

Se Data de Vigência Final do registro a ser importado for nulo,

Ou

Se Data de Vigência Final do registro a ser importado for >= Data de Vigência Inicial do registro recuperado, o registro não será importado e será gravada a seguinte mensagem de erro:

*“93335 \- Existe parametrizacao para Conta Contabil com Vigencia Inicial posterior a que esta sendo importada e a Data de Vigencia Final importada nao e menor que Data de Vigencia Inicial existente\.” *

MFS32572

__RN04__

__Campo Código de Tributação DESIF __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada uma mensagem informando que o campo não foi preenchido \(mensagem “*93336 \-  Codigo de Tributacao DESIF obrigatorio e nao informado*”\)\.

O código informado deve existir na Tabela de Códigos de Tributação DESIF \- Anexo 6 \(TACES102 \- CAD\_TRIB\_DESIF\)\. Quando não encontrado, o registro não será importado, e no log de erros será gravada uma mensagem informando que o código não existe na tabela \(mensagem: “*93337 \-* *Código de Tributação DESIF inválido, pois não pertence a Tabela de Códigos de Tributação DESIF – Anexo 6\.*”

            Solução Erro:  “*Certifique\-se que a Tabela de Códigos de Tributação DESIF – Anexo 6 foi atualizada pela importação da TACES102”*\)\.

MFS32572

__RN05__

__Campo Indicador de Retenção na Fonte pelo Tomador do Serviço __

Campo não obrigatório\.

Valores aceitos são:

S – sim

N \- não

Quando preenchido e o valor for diferente de S e N, o registro não será importado e no log de erros será gravada a seguinte mensagem:

*93338 \- Indicador de Retencao na Fonte pelo Tomador invalido\. Os valores aceitos sao: <@>, <S> ou <N>\.*

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

