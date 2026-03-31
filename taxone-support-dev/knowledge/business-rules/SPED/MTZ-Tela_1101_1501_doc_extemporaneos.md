# MTZ-Tela_1101_1501_doc_extemporaneos

> Fonte: MTZ-Tela_1101_1501_doc_extemporaneos.docx



## Matriz Tela - Documentos e Operações de Períodos Anteriores – (1101/1501)

## (EFD-PIS/PASEP – COFINS) - (SAFX168)



DOCUMENTO DE REQUISITO


### REGRAS TELA






| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3169-GE24 | Criação da tela Documentos e operações anteriores (1101/1501) | Será criada uma tela para atendimento do Bloco 1 registros 1101 e 1501, da EFD – PIS/PASEP COFINS, estes registros são para informação de créditos de documentos/operação extemporâneo | 08/08/2011 |
| OS3903 | Alteração campo 17 | Retiradas as críticas de obrigatoriedade do campo 17-Código Fiscal (ver RN05) | 12/06/2014 |
| MFS-65742 | Validação mensagem 92292 | Documentar a mensagem 92292 e ajustá-la inserindo um exemplo de preenchimento | 29/03/2022 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Regras gerais  Campos Chaves: Empresa, Estabelecimento, Data Operação, Número, Série, Subsérie, Pessoa Física/Jurídica, Produto, Serviço, Número do Item, Número do Documento  Campos Obrigatórios: Empresa, estabelecimento, data da operação, valor da operação, CFOP, código da natureza da base de crédito, indicador da origem do crédito, Código de Situação (CST) do PIS, Valor do PIS, Código de Situação (CST) do COFINS, Valor da COFINS   Campos obrigatórios de forma condicional:  Os campos de PIS e da COFINS devem ser obrigatórios conforme o preenchimento dos dados da tabela, ou seja: PIS Base de Cálculo do PIS ou Quantidade Base do PIS; Alíquota do PIS (em %) ou Alíquota do PIS (em reais);  Caso algum dos campos seja preenchido, então devemos considerá-los como obrigatórios, levando em consideração que os pares de campos de base e alíquota deverão obedecer às condição a seguir:  Os pares que devem ser obrigatórios são: (Base PIS e Alíquota PIS (em %) ou (Quantidade Base PIS e Alíquota PIS (em reais); Estes pares de campos devem ser exclusivos, ou seja, apenas um dos pares deve ser preenchido. [ALTERAÇÃO MFS-65742] Caso, a regra acima não seja verdadeira, exibir a mensagem: “Preenchidos campos de base/quantidade e/ou aliquota(%)/aliquota(reais) simultaneamente. Ex. de preenchimentos aceitos: Base PIS e Aliquota PIS(em %) ou Quantidade Base PIS e Aliquota PIS(em reais)” As mesmas regras acima devem ser seguidas para a COFINS. | OS3169-GE24 MFS-65742 |
| RN01 | Campo 01 – Pessoa Fis/Jur   Recuperar X04 | OS3169-GE24 |
| RN02 | Campo 02 – Modelo Documento  Recuperar X2024 | OS3169-GE24 |
| RN03 | Campo 03 – Produto (Gr. Ind. Cod/Val)  Recuperar X2013 | OS3169-GE24 |
| RN04 | Campo 04 - Serviço (Gr. Ind. Cod/Val)  Recuperar X2018 | OS3169-GE24 |
| RN05 | Campo 05 – CFOP  Recuperar X2012  Alteração da OS3903 – O campo não será mais obrigatório, desta forma, não será mais exibida  mensagem de erro quando o campo não for preenchido, e o registro poderá ser salvo normalmente. Se digitado (ao invés de recuperado na janela de seleção),  permanece a crítica original  que  verifica a existência do código informado  na Tabelas dos Códigos Fiscais (SAFX2012). | OS3169-GE24 |
| RN06 | Campo 06 – Cód. Base de calculo de credito  06 – Deve conter lista: | OS3169-GE24 |
| RN07 | Campo 07 – Origem do Credito (ind)  07 -  Deve conter lista: | OS3169-GE24 |
| RN08 | Campo 08 - Conta (Gr. Ind. Cod/Val)  Recuperar X2002 | OS3169-GE24 |
| RN09 | Campo 09- Custo (Gr. Ind. Cod/Val)  Recuperar X2003 | OS3169-GE24 |
| RN10 | Campo 10 – Cod Sit trib PIS/PASEP  Recuperar Taces 65 | OS3169-GE24 |
| RN11 | Campo 11– Cod Sit trib COFINS  Recuperar Taces 65 | OS3169-GE24 |
