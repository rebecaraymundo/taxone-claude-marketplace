# MTZ-Tela_1101_1501_doc_extemporaneos

- **Fonte:** MTZ-Tela_1101_1501_doc_extemporaneos.docx
- **Modificado:** 2022-03-31
- **Tamanho:** 38 KB

---

__    __

# Matriz Tela \- Documentos e Operações de Períodos Anteriores – \(1101/1501\)

# \(EFD\-PIS/PASEP – COFINS\) \- \(SAFX168\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-GE24

Criação da tela Documentos e operações anteriores \(1101/1501\)

Será criada uma tela para atendimento do Bloco 1 registros 1101 e 1501, da EFD – PIS/PASEP COFINS, estes registros são para informação de créditos de documentos/operação extemporâneo

08/08/2011

OS3903

Alteração campo 17

Retiradas as críticas de obrigatoriedade do campo 17\-Código Fiscal \(ver __RN05__\)

12/06/2014

MFS\-65742

Validação mensagem 92292

Documentar a mensagem 92292 e ajustá\-la inserindo um exemplo de preenchimento

29/03/2022

## REGRAS TELA

#### Cód\.

### DR

__RN00__

__Regras gerais__

__Campos Chaves:__ Empresa, Estabelecimento, Data Operação, Número, Série, Subsérie, Pessoa Física/Jurídica, Produto, Serviço, Número do Item, Número do Documento

- __Campos Obrigatórios:__ Empresa, estabelecimento, data da operação, valor da operação, CFOP, código da natureza da base de crédito, indicador da origem do crédito, Código de Situação \(CST\) do PIS, Valor do PIS, Código de Situação \(CST\) do COFINS, Valor da COFINS

__Campos obrigatórios de forma condicional:__

Os campos de PIS e da COFINS devem ser obrigatórios conforme o preenchimento dos dados da tabela, ou seja:

PIS

- Base de Cálculo do PIS ou Quantidade Base do PIS;
- Alíquota do PIS \(em %\) ou Alíquota do PIS \(em reais\);

Caso algum dos campos seja preenchido, então devemos considerá\-los como obrigatórios, levando em consideração que os pares de campos de base e alíquota deverão obedecer às condição a seguir: 

- Os pares que devem ser obrigatórios são: \(Base PIS e Alíquota PIS \(em %\) ou \(Quantidade Base PIS e Alíquota PIS \(em reais\);
- Estes pares de campos devem ser exclusivos, ou seja, apenas um dos pares deve ser preenchido\.

__\[ALTERAÇÃO MFS\-65742\]__ Caso, a regra acima não seja verdadeira, exibir a mensagem: “Preenchidos campos de base/quantidade e/ou aliquota\(%\)/aliquota\(reais\) simultaneamente\. Ex\. de preenchimentos aceitos: Base PIS e Aliquota PIS\(em %\) ou Quantidade Base PIS e Aliquota PIS\(em reais\)”

As mesmas regras acima devem ser seguidas para a COFINS\.

OS3169\-GE24

MFS\-65742

__RN01__

__Campo 01 – Pessoa Fis/Jur__

 

Recuperar X04

OS3169\-GE24

__RN02__

__Campo 02 – Modelo Documento__

Recuperar X2024

OS3169\-GE24

__RN03__

__Campo 03 – Produto \(Gr\. Ind\. Cod/Val\)__

Recuperar X2013

OS3169\-GE24

__RN04__

__Campo 04 \- Serviço \(Gr\. Ind\. Cod/Val\)__

Recuperar X2018

OS3169\-GE24

__RN05__

__Campo 05 – CFOP__

Recuperar X2012

__Alteração da OS3903 __– O campo não será mais obrigatório, desta forma, *não* será mais exibida  mensagem de erro quando o campo *não* for preenchido, e o registro poderá ser salvo normalmente\. Se digitado \(ao invés de recuperado na janela de seleção\),  permanece a crítica original  que  verifica a existência do código informado  na Tabelas dos Códigos Fiscais \(SAFX2012\)\.  

OS3169\-GE24

__RN06__

__Campo 06 – Cód\. Base de calculo de credito__

__06__ – Deve conter lista:

01

Aquisição de bens para revenda

02

Aquisição de bens utilizados como insumo

03

Aquisição de serviços utilizados como insumo

04

Energia elétrica e térmica, inclusive sob a forma de vapor

05

Aluguéis de prédios

06

Aluguéis de máquinas e equipamentos

07

Armazenagem de mercadoria e frete na operação de venda

08

Contraprestações de arrendamento mercantil

09

Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito sobre encargos de depreciação\)\.

10

Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito com base no valor de aquisição\)\.

11

Amortização e Depreciação de edificações e benfeitorias em imóveis

12

Devolução de Vendas Sujeitas à Incidência Não\-Cumulativa

13

Outras Operações com Direito a Crédito

14

Atividade de Transporte de Cargas – Subcontratação

15

Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária

16

Atividade Imobiliária – Custo Orçado de unidade não concluída

17

Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale\-transporte, vale\-refeição ou vale\-alimentação, fardamento ou uniforme\.

18

Estoque de abertura de bens

OS3169\-GE24

__RN07__

__Campo 07 – Origem do Credito \(ind\)__

__07__ \-  Deve conter lista:

0

Operação no mercado Interno

1

Operação de Importação

OS3169\-GE24

__RN08__

__Campo 08 \- Conta \(Gr\. Ind\. Cod/Val\)__

Recuperar X2002

OS3169\-GE24

__RN09__

__Campo 09\- Custo \(Gr\. Ind\. Cod/Val\)__

Recuperar X2003

OS3169\-GE24

__RN10__

__Campo 10 – Cod Sit trib PIS/PASEP__

Recuperar Taces 65

OS3169\-GE24

__RN11__

__Campo 11– Cod Sit trib COFINS__

Recuperar Taces 65

OS3169\-GE24

