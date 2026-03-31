# MTZ-Job-Servidor-Importacao_SAFX307

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX307.docx
- **Modificado:** 2020-09-15
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX307

Tabela de Parametrização por NCM – Registro C176 do Sped Fiscal 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS36503

Andréa Rocha

Criação de nova tabela SAFX para carga da parametrização por NCM do Registro C176 do SPED\-EFD, também usada no módulo do Ressarcimento de ICMS\-ST – PR\.

MFS43978

Andréa Rocha

Inclusão do campo % de Redução de BC\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX307 🡪 vide manual de layout

Campos que compõe a chave da tabela:

__   Código da Empresa \+ Código do Estabelecimento \+ NCM \+ Alíquota Interna \+ Inicio Validade__

A manutenção desta tabela é feita no Módulo EFD – Escrituração Fiscal Digital, menu Parâmetros 🡪 Registro C176 🡪 NCM’s\.

Ou no módulo Estadual \- Ressarcimento de ICMS\-ST – PR, menu Parâmetros 🡪 Registro C176 🡪 NCM’s\.

Tabela de Destino:

A SAFX307 alimenta a tabela definitiva EFD\_PAR\_NBM\_C176\.

Sobre as mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS36503

__RN01__

__Campo 01 \-  Código da Empresa__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS36503

__RN02__

__Campo 02 \- Código do Estabelecimento__

Campo de preenchimento __*obrigatório*__\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS36503

__RN03__

__Campo 03 \- Código do NBM__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O codigo do NCM e de preenchimento obrigatorio e nao foi informado”*

Crítica da existência do NBM na SAFX2043:

O NBM informado será validado na Tabela de NBMs\. Caso o NBM não exista na tabela, o registro não será importado e no log de erros será gravada a seguinte mensagem: 

* “O codigo do NCM invalido ou nao preenchido”*

MFS36503

__RN04__

__Campo 04 – Alíquota Interna do Produto__

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, ou quando for um valor inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“Alíquota Interna do Produto invalida ou nao preenchida”*

MFS36503

__RN05__

__Campo 05 \- Início Validade __

Campo de preenchimento __*obrigatório*__\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Início Validade é de preenchimento obrigatório e não foi informado”*

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Início Validade é invalido”*

MFS36503

__RN06__

__Campo 06 \- Fim Validade __

Campo de preenchimento não obrigatório\.

Caso o campo esteja preenchido, se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O campo Data Fim Validade é invalido”*

Caso o campo esteja preenchido, se for uma data menor que a Data Início Validade, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O campo Data Fim Validade, quando preenchido, deve ser maior ou igual a Data Início Validade”*

__Tratamento para não permitir Intervalos Intercalados de Datas__:

Vamos adotar tratamentos para evitar que um NCM para uma determinada empresa e estabelecimento tenha parametrizações com intervalos de datas inicial e final que se intercalem\. Ou seja, não podemos permitir que uma parametrização do NCM tenha Data Início ou Fim de Validade entre as datas Início e Fim Validade da parametrização já existente na base\.

__Exemplo1: NCM sem Data Fim de Validade__

Dado o NCM “AAAA” da Empresa ‘076’ e Estabelecimento ‘001’\.

Parametrização já existente na base registrado com Início Validade 01/01/2018 e Fim Validade nulo

Registros a serem importados via SAFX307:

__Início Validade__

__Fim Validade__

__Resultado da Importação__

01/01/2017

31/12/2017

Ok importado com sucesso

01/01/2017

01/01/2018

Erro na importação\. Data Fim intercala o registro já existe na base\. Registro não importado

01/01/2017

Erro na importação\. Data Fim nula, intercalando com o registro já existe na base\. Registro não importado

02/01/2018

Erro na importação, Data Fim do registro existente na base é nula\. Registro não importado

__Exemplo2: NCM com Data Fim de Validade__

Dado o NCM AAAA da Empresa ‘076’ e Estabelecimento ‘001’\.

Parametrização já existente na base registrado com Início Validade 01/01/2018 e Fim Validade 31/01/2018

Registros a serem importados via SAFX307:

__Início Validade__

__Fim Validade__

__Resultado da Importação__

01/01/2017

31/12/2017

Ok importado com sucesso

01/01/2017

01/01/2018

Erro na importação\. Data Fim intercala com o registro já existe na base\. Registro não importado

01/01/2017

Erro na importação\. Data Fim nula, intercalando com o registro já existe na base\. Registro não importado

02/01/2018

Erro na importação\. Data Início intercala com o registro já existe na base\.

01/02/2018

Ok importado com sucesso

<a id="_Hlk2188990"></a>

__Situações tratadas na importação__:

1. Dada a Empresa, Estabelecimento, NCM e Alíquota Interna da parametrização que está sendo importada, buscar na base a parametrização de mesma Empresa, Estabelecimento, NCM e Alíquota Interna com Data Início Validade imediatamente posterior à Data Início Validade do registro que está sendo importado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro que está sendo importado com a Data Início Validade do registro encontrado\.

Se Data Fim de Validade do registro que está sendo importado >= Data Início Validade do registro encontrado ou

     Data Fim de Validade do registro que está sendo importado for nula então:

O registro não será importado e no log de erros será gravada a seguinte mensagem:

*Já existe parametrização por NCM vigente nas datas Início e/ou Fim de Validade informada\.*

1. Dada a Empresa, Estabelecimento, NCM e Alíquota Interna da parametrização que está sendo importada, buscar na base a parametrização de mesma Empresa, Estabelecimento, NCM e Alíquota Interna com Data Início Validade imediatamente anterior à Data Início Validade do registro que está sendo importado\.

Caso o registro seja encontrado, comparar a Data Fim de Validade do registro encontrado com a Data Início Validade do registro que está sendo importado\.

Se Data Fim de Validade do registro encontrado >= Data Início Validade do registro que está sendo importado ou

     Data Fim de Validade do registro encontrado for nula então:

O registro não será importado e no log de erros será gravada a seguinte mensagem:

*Já existe parametrização por NCM vigente nas datas Início e/ou Fim de Validade informada\.*

MFS36503

__RN07__

__Campo 07 \- Sujeito ao FCP__

Campo de preenchimento não obrigatório\.

Quando preenchido, o registro deve ser preenchido com “S” ou “N”\. Caso não esteja não preenchido com “S” ou “N”, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O campo Sujeito ao FCP deve ser preenchido com “S” ou “N”\.”*

MFS36503

__RN08__

__Campo 08 – Alíquota FCP__

Campo de preenchimento não obrigatório\.

Este campo só deve ser preenchido se o campo 07 \- Sujeito ao FCP estiver preenchido com “S”\.  Caso não esteja preenchido com “S” e o campo Alíquota estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*“O campo Alíquota FCP somente deve ser preenchido quando o campo Sujeito ao FCP estiver preenchido com “S”\.”*

MFS36503

__RN09__

__Campo 09 – % de Redução de BC__

Campo de preenchimento não obrigatório\.

MFS43978

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

