# MTZ_TELA_Parâmetros_Autonomos_Multiplas_Rubricas

> Fonte: MTZ_TELA_Parâmetros_Autonomos_Multiplas_Rubricas.docx


## TELA DE PARAMETRIZAÇÃO

## Parâmetros p/ Autônomos – Múltiplas Rubricas








DOCUMENTO DE REQUISITO









REGRAS DE NEGÓCIO


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:


Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| DR | Nome | Descrição |
| --- | --- | --- |
| OS4010 | Criação do documento | Definição das regras para a tela de Parâmetros p/ Autônomos – Múltiplas Rubricas. |
|  |  |  |


| Cód. | Descrição | DR |
| --- | --- | --- |
| RN01 | Deverá ser criada uma nova tela para de parametrização no seguinte caminho:  Módulo: Federal >> Portaria 63 Caminho no menu: Parâmetros  Nome da Tela: Parâmetros p/ Autônomos – Múltiplas Rubricas | OS4010 |
| RN02 | Nesta tela estarão disponíveis os campos:  Data de Inclusão do Registro (campo obrigatório e chave)  Perfil (campo obrigatório e chave) Verba (campo obrigatório e chave) Campo a ser detalhado (campo obrigatório) Conta Contábil (campo obrigatório) Centro de Custo Ind. de BC do IRRF | OS4010 |
| RN03 | Campo Data de Inclusão do Registro  Campo do tipo data no formado DD/MM/AAAA. | OS4010 |
| RN04 | Campo Perfil  Campo do tipo lista. Deve mostrar o código do Perfil seguido da descrição, conforme cadastrado na tela de cadastro do Perfil. A demonstração deve ser semelhante à existente na tela de geração do meio magnético. | OS4010 |
| RN05 | Campo Verba  Campo com pasta de acesso + código + descrição. Deverá acessar a lista de informações da SAFX2023 para indicação de um código de verba, conforme padrão do DW. | OS4010 |
| RN06 | Campo Campo a ser detalhado  Campo do tipo lista. Deve mostrar os seguintes conteúdos:  22  Valor dos Produtos / Serviços 23  Valor Total do Documento Fiscal 44  Valor IR 59  Base IR Tributada 60  Base IR Isenta 68  Valor Total Serviços 85  Valor base INSS 87  Valor INSS Retido 151  Segunda Base de Cálculo para INSS 153  Segundo Valor de Tributo INSS 173  Juros INSS 174  Multa INSS 241  Base de Cálculo da Contribuição Previdenciária sobre Produção Rural Sub-rogação 243  Valor da Contribuição Previdenciária sobre Produção Rural Sub-rogação | OS4010 |
| RN07 | Campo Conta Contábil  Campo com pasta de acesso + código + descrição. Deverá acessar a lista de informações da SAFX2002 para indicação de um código da conta contábil, conforme padrão do DW. | OS4010 |
| RN08 | Campo Centro de Custo  Campo com pasta de acesso + código + descrição. Deverá acessar a lista de informações da SAFX2003 para indicação de um código do centro de custo, conforme padrão do DW. | OS4010 |
| RN09 | Campo Ind. De BC do IRRF  Campo do tipo lista. Deve mostrar os seguintes conteúdos:  1 – BC do Salário Mensal 2 – BC 13º Salário 3 – Não é BC 9 – Outras BC | OS4010 |
|  |  |  |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |


| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
