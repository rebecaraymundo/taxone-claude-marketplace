# MTZ_LAICMS_Calculo_Diferencial_Aliquota_Devolucao

- **Fonte:** MTZ_LAICMS_Calculo_Diferencial_Aliquota_Devolucao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Módulo: Lançamentos Automáticos ICMS

__Cálculo dos Lançamentos__

__Regras para Diferencial de Alíquota Devolução Ativo/Mat\. Consumo__

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

CH26630/2015

Criação do documento

Definição de regras para Cálculo dos Lançamentos de Diferencial de Alíquota \- Devolução

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

__Parametrização da Base de Cálculo__

A parametrização da Base de Cálculo para geração do Lançamento Automático do Diferencial de Alíquota deve ser realizada no seguinte caminho:

Módulo: Ferramentas

Menu: Parâmetros do Sistema > Parâmetros por Estabelecimento

Teremos as seguintes opções:

1 – \(Base Tributada\)

2 – \(Base Tributada \+ Base Outras\)

3 – \(Valor Contábil – ICMS\-S – Base Redução – Base Isenta\)

4 – Valor Informado \(Sem Base de Cálculo\)

Estas opções serão recuperadas da tabela SAFX08 quando a apuração for realizada através do menu “Apuração” no módulo “ICMS” ou das tabelas DWT, quando o processamento for a partir do menu “DATA MART”, considerando as seguintes origens:

__Campo__

__Origem SAFX08__

__Origem DWT__

Base Tributada

Campo “Base ICMS”

Campo “Base de ICMS 1”

Base Outras

Campo “Base Outras ICMS”

Campo “Base de ICMS 3”

Valor Contábil

Campo “Valor Contábil do Item”

Campo “Valor Total da NF”

ICMS\-S

Campo “Valor do ICMSS”

Campo “Valor do ICMSS”

Base Redução

Campo “B\. Redução ICMS”

Campo “Base de ICMS 4”

Base Isenta

Campo “Base Isenta ICMS”

Campo “Base de ICMS 2”

Valor Informado

Campo “Valor Diferença Alíquotas ICMS – Ativo / Material Consumo”

Campo “Valor de Outras 1”

Esta informação será considerada no momento na geração do Cálculo dos Lançamentos\. Módulo: Lançamentos Automáticos ICMS > Lançamentos > Cálculo dos Lançamentos\.

CH26630/2015

RN02

__Cálculo dos Lançamentos__

Disponível em:

Módulo: Lançamentos Automáticos ICMS

Menu: Lançamentos > Cálculo dos Lançamentos

Para geração do Cálculo dos Lançamentos será considerado as seguintes parametrizações:

- Parametrização da Base de Cálculo: Módulo de Ferramentas > Parâmetros do Sistema > Parâmetros por Estabelecimento
- Parâmetros Lançamentos Automáticos: Módulo Lançamentos Automáticos ICMS > Menu Parâmetros > Lançamentos Automáticos 
- Parâmetros para Cálculo e Relatórios: Módulo Lançamentos Automáticos ICMS > Menu Parâmetros > Parâmetros p/ Cálculo e Relatórios 

   \- Classes de Relatório: definição do tipo de movimentação e parâmetros de lançamento automático a ser gerado\.

   \- Parâmetros de Relatórios p/ \.\.\. > definição de com diversos opções de parametrizações \(CFOP/Produto/NBM/Extenção/UF/Pessoa Fisica\_Juridica\) que serão considerados na seleção de documentos fiscais por tipo de lançamento automático\.

- Parâmetros para Cálculo de Lançamentos: Módulo Lançamentos Automáticos ICMS > Menu Parâmetros > Parâmetros p/ Cálculo de Lançamentos 
- Cálculo dos Lançamentos: Módulo Lançamentos Automáticos ICMS > Menu Lançamentos > Cálculo dos Lançamentos\.
- Lançamento no Livro de Apuração: Módulo Lançamentos Automáticos ICMS > Menu Lançamentos > Lançamento no Livro de Apuração > Neste momento os valores serão apurados e os lançamentos serão criados nas tabelas de Ajustes dos Lançamentos Complementares\.

Exemplo de parametrização para Diferencial de Alíquota:

Parametrização da Base de Cálculo

Foi parametrizado no módulo de Ferramentas > Parâmetros do Sistema > Parâmetros por Estabelecimento a opção "1 – \(Base Tributada\)"

Parâmetros Lançamentos Automáticos 

Foi parametrizado no Módulo Lançamentos Automáticos ICMS > Menu Parâmetros > Lançamentos Automáticos  foi parametrizado o Lançamento à Débito e Lançamento a Crédito\.

Parâmetros para Cálculo e Relatórios

Foi parametrizado no Módulo Lançamentos Automáticos ICMS > Menu Parâmetros > Parâmetros p/ Cálculo e Relatórios > Classe de Relatório > Classe Relatório: DIF – Diferencial Alíquota, Mov\. Entrada/Saida: 9 – Saídas e Tipo de Movimentação = Devolução\.

Foi parametrizado no Módulo Lançamentos Automáticos ICMS > Menu Parâmetros > Parâmetros p/ Cálculo e Relatórios > Parâmetros de Relatórios p/ CFOP: O CFOP 6556 vinculado ao parâmetro de relatório DIF – Diferencial Alíquota\.

Parâmetros para Cálculo de Lançamentos 

Foi parametrizado no Módulo Lançamentos Automáticos ICMS > Menu Parâmetros > Parâmetros p/ Cálculo de Lançamentos 

UF o parâmetro Dif\. Alíq\. Dev\. Ativo/Mat\. Consumo foi marcado com a parametrização dos Lançamentos Automáticos e no Critério p/Dif\.Aliq\.Devolução Ativo/Mat\.Consumo foi parametrizado a Classe de Relatório = DIF – Diferencial Alíquota e a seleção = Aliquota do Diferencial\.

Foi executado o Cálculo dos Lançamentos e o Lançamento no Livro de Apuração\.

Foi processada a apuração com os seguintes critérios na base:

__Nº NF__

__CFOP__

__Aliq\. Destino__

__BC ICMS__

__Aliq\. ICMS__

__Diferença Alíquota__

__Lançamento a Débito__

__Lançamento a Crédito__

1234

6556

18,00

2\.614,00

12,00

6,00

156,84

156,84

De acordo com os critérios parametrizados, para esta base de exemplo, serão gerados dois lançamentos complementares totalizando os valores apurados para todo documento fiscal que se enquadra nos critérios de seleção\.

__Importante:__ Caso a opção de Base de Cálculo escolhida for 4 \- Valor Informado \(Sem Base de Cálculo\) deverá apenas recuperar o valor do diferencial de alíquota presente na nota sem efetuar cálculo \(considerando campo de origem definido na RN01\)\.

CH26630/2015

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

