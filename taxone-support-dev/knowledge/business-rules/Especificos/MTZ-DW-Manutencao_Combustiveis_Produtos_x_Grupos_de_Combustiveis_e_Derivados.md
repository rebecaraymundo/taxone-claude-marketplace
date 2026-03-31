# MTZ-DW-Manutencao_Combustiveis_Produtos x Grupos de Combustíveis e Derivados

> Fonte: MTZ-DW-Manutencao_Combustiveis_Produtos x Grupos de Combustíveis e Derivados.docx



## Módulo DW – Manutenção – Produtos x Grupos de Combustíveis e Derivados



Localização: Menu Básicos, Módulo: Data Warehouse
Menu Manutenção >> Combustíveis (Não Varejistas) >> Produtos x Grupos de Combustíveis e Derivados

Localização: Menu Específicos, Módulo: Combustíveis e Derivados de Petróleo
Menu Parâmetros >> Produtos x Grupos de Combustíveis e Derivados


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO













| MFS | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| MFS540746 | Liliane Assaf | Disponibiliza tela de manutenção no módulo Data Warehouse | 15/06/2023 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Regras gerais Tela de manutenção disponível em dois módulos Data Warehouse e Combustíveis e Derivados de Petróleo.  Nesta opção é possível fazer a associação dos produtos (safx2013) aos dos Grupos de combustíveis e derivados.  Tabela: X96_GRP_COMB_PROD  Para que os tratamentos relacionados ao regime de tributação monofásica do ICMS possam corretamente ser aplicados na geração do Sped Fiscal, Livros de Apuração do ICMS e ICMS-ST e SCANC, o produto movimentado na nota fiscal deve estar aqui parametrizado e o campo “Código do Produto Oficial” preenchido com o código do produto ANP de um combustível que pertença à Tabela Produtos Sujeitos à Tributação Monofásica ICMS.  Módulo: Combustíveis e Derivados de Petróleo, menu Parâmetros >> Produtos Sujeitos à Tributação Monofásica ICMS Módulo: Data Warehouse menu Manutenção >> Combustíveis (Não Varejistas) >> Produtos Sujeitos à Tributação Monofásica ICMS |  |
| RN01 | Campo  – Validade Grupo Combustível:  Campo obrigatório. Deve ser uma data válida. |  |
| RN02 | Campo – Produto:  Campo obrigatório. Pastinha + Indicador + Código do Produto + Descrição, referente ao Cadastro de Produtos (SAFX2013). |  |
| RN03 | Campo – Grupo Combustível Campo obrigatório Grupo de Combustível cadastrado previamente em: Módulo: Data Warehouse Menu Manutenção >> Combustíveis (Não Varejistas) >> Grupos de Combustíveis e Derivados ou Módulo: Combustíveis e Derivados de Petróleo Menu Parâmetros >> Grupos de Combustíveis e Derivados |  |
| RN04 | Campo – Medida: Código + Descrição referente ao Cadastro de Medidas (SAFX2007). |  |
| RN05 | Campo – Cód. Prod Oficial Informar o código oficial do produto a ser utilizado na geração do meio magnético.     Obs: Este código deve estar de acordo com os códigos de produtos relacionados nas tabelas 4.1 e 4.2 do manual de orientação do SCANC (Sistema de Captação e Auditoria dos Anexos de Combustíveis). Preencher esse campo com o código do produto ANP para os combustíveis que entraram no regime de tributação monofásica do ICMS. Ver a relação dos códigos desses combustíveis na tabela Produtos Sujeitos à Tributação Monofásica ICMS que pode ser consultada em: Módulo: Combustíveis e Derivados de Petróleo, menu Parâmetros >> Produtos Sujeitos à Tributação Monofásica ICMS Módulo: Data Warehouse menu Manutenção >> Combustíveis (Não Varejistas) >> Produtos Sujeitos à Tributação Monofásica ICMS |  |
| RN06 | Campo - Fator Conv. Gás. A:  Informar o fator de conversão para Gasolina A. Este fator indica a quantidade de gasolina A compõe o produto que está sendo parametrizado. |  |
| RN06 | Campo - Fator Divisão do Vlr. Unitário Gás. A:  Informar o fator utilizado para divisão do valor unitário (PMPF, MFA, ANP) do grupo Gasolina. Como o valor unitário definido para o grupo Gasolina é referente à Gasolina C, os produtos referentes à Gasolina A devem utilizar este fator para ajustar o valor unitário que é usando no cálculo da Base ICMS-ST dos Anexos I e II. Informação sobre o preenchimento do campo: - Para todos grupos combustíveis exceto Gasolina, preencher 1. - Para os produtos referentes à Gasolina A preencher com o fator que representa o percentual de Gasolina A na composição da Gasolina C. Exemplo: 0.75 (fator que vale até 31/01/2003) e 0.80 (fator que vale a partir de 01/02/2003).     Obs: A informação deste campo é referente ao campo 10 da SAFX96. |  |
| RN07 | Campo - Fator de Ganho:  Informar o fator que indicar o ganho estimado do produto que está sendo parametrizado. |  |
| RN08 | Campo - Fator de Perda:  Informar o fator que indicar a perda estimada do produto que está sendo parametrizado. |  |
