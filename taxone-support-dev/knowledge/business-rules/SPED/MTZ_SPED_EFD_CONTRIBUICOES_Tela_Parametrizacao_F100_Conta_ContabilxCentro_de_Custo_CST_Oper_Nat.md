# MTZ_SPED_EFD_CONTRIBUICOES_Tela_Parametrizacao_F100_Conta_ContabilxCentro_de_Custo_CST_Oper_Nat

> Fonte: MTZ_SPED_EFD_CONTRIBUICOES_Tela_Parametrizacao_F100_Conta_ContabilxCentro_de_Custo_CST_Oper_Nat.docx






THOMSON REUTERS

Parametrização – Registro F100 – Conta Contábil x Centro de Custo/ CST/ Operação/ Nat. Base de Crédito
EFD-Contribuições



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	4
2.	Regras dos Campos	5

## Regras dos Campos


Localização da tela: SPED\ EFD – Escrituração Fiscal Digital das Contribuições\ Parâmetros\ Registro F100\ Conta Contábil x Centro de Custo/ CST/ Operação/ Nat. Base de Crédito

Título da tela: Parametrização da Conta Contábil x Centro de Custo/ CST/ Operação/ Nat. Base de Crédito

[ALTERADA - CH15489_2017 / MFS12992 / MFS509499]

Considerações:

Nessa tela deve ser permitida a combinação de Empresa, Estabelecimento, Data de Início Validade, Conta Contábil, Centro de Custos (se houver), Tipo de Operação para CST, Alíquotas diferentes. Exemplo:

Estabelecimento: F100
Data de Início Validade: 01/01/2017
Conta Contábil: 001.1
Centro de Custos: em branco
Produto: em branco
Tipo de Operação: 0
CST PIS e COFINS: 56
Nat. da Base do Crédito: 01
Alíquota PIS: 1,5
Alíquota COFINS: 7,6

Estabelecimento: F100
Data de Início Validade: 01/01/2017
Conta Contábil: 001.1
Centro de Custos: em branco
Produto: 000123456
Tipo de Operação: 0
CST PIS e COFINS: 66
Nat. da Base do Crédito: 01
Alíquota PIS: 2,5
Alíquota COFINS: 12,6

Não permitir alíquotas iguais para os mesmos CST.







| MFS/CH | Nome | Descrição | Descrição |
| --- | --- | --- | --- |
| CH15489_2017 (MFS12992) | Julyana Perrucini | Este documento tem como objetivo reestruturar a tabela do parâmetro do Registro F100 por Conta Contábil para aceitar a mesma operação com CST e alíquotas diferentes. |
| MFS509499 | Rogério Ohashi | Este documento tem como objetivo incluir o Campo de Código de Produto na tela/tabela do parâmetro do Registro F100 para aceitar Natureza de Base de Crédito diferentes. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato: Combo Box  Default: Estab. informado na tela | Informar o Estabelecimento que corresponde a parametrização (aparecerá automaticamente quando informado no login).  Tratamento: Campo desabilitado quando informado estabelecimento na tela inicial; Se o estabelecimento não for informado na tela inicial, será demonstrado o combo box em branco; Se não for selecionado um estabelecimento, ao salvar o registro emitir a mensagem na tela: “Selecionar o Estabelecimento”. | CH15489_2017 (MFS-12992) |
| Data de Início Validade | Data | S | N | Formato: Text Input DD/MM/AAAA  Default: Habilitado | Deverá ser informada a Data de Validade de início da parametrização.  Tratamento: Após salvar o registro não permitir a edição; Se o campo não for preenchido, ao salvar o registro emitir a mensagem na tela: “A Data de Início Validade deve ser preenchida”. | CH15489_2017 (MFS-12992) |
| Conta | Numérico | S | N | Formato: Seleção SAFX2002  Default: Habilitado | Deverá ser informada a conta contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela de Plano de Contas (SAFX2002).  Tratamento: Após salvar o registro não permitir a edição; Se o campo não for preenchido, ao salvar o registro emitir a mensagem na tela: “A Conta Contábil deve ser informada”. | CH15489_2017 (MFS-12992) |
| Centro de Custo | Numérico | N | N | Formato: Seleção SAFX2003  Default: Habilitado | Deverá ser informado o centro de custo referente ao Imposto, de acordo com a Tabela de Centro de Custos (SAFX2003).  Tratamento: Após salvar o registro não permitir a edição. | CH15489_2017 (MFS-12992) |
| Produto (Gr./Ind./Cód./Desc.) | Numérico | N | N | Formato: Pasta de Seleção SAFX2013  Default: Habilitado | Este campo deve possibilitar o usuário buscar o produto na SAFX2013, ou digitar o indicador do produto e código manualmente na tela, carregando a descrição.  Serão listadas as seguintes opções para o “Indicador do Produto”:  1 - Produto Acabado  2 - Insumo 3 - Embalagem 4 - Consumo  5 - Outros  6 - Em Elaboração 7 - Intermediário  8 – Miscelânias  Tratamento: Após salvar o registro não permitir a edição. | MFS509499 |
| Tipo de Operação | Texto | S | S | Formato: Combo Box  Default: Habilitado | Informar de acordo com:  0 – Operação Representativa de Aquisição, Custos, Despesa ou Encargos, Sujeita à Incidência de Crédito de PIS/PASEP ou COFINS 1 – Operação Representativa de Receita Auferida Sujeita ao Pagamento da Contribuição para o PIS/PASEP e da COFINS 2 – Operação Representativa de Receita Auferida Não Sujeita ao Pagamento da Contribuição para o PIS/PASEP e da COFINS  Observação: Esse campo é obrigatório para selecionar o CST. | CH15489_2017 (MFS-12992) |
| Cód. Sit.Trib. PIS | Texto | S | S | Formato: Seleção TACES65  Default: Habilitado | Informar de acordo com a Tabela de CST (TACES65), seguindo a regra:  Quando Tipo de Operação = “0”, informar o conteúdo de acordo com os códigos 50 a 66. Quando Tipo de Operação = “1”, informar o conteúdo de acordo com os códigos 01, 02, 03 ou 05. Quando Tipo de Operação = “2”, informar o conteúdo de acordo com os códigos 04, 06, 07, 08, 09, 49 ou 99.  Tratamento: Se o campo não for preenchido, ao salvar o registro emitir a mensagem na tela: “O Cód. Sit.Trib. PIS deve ser informado”. | CH15489_2017 (MFS-12992) |
| Cód. Sit.Trib. COFINS | Texto | S | S | Formato: Seleção TACES65  Default: Habilitado | Informar de acordo com a Tabela de CST, seguindo a regra:  Quando Tipo de Operação = “0”, informar o conteúdo de acordo com os códigos 50 a 66. Quando Tipo de Operação = “1”, informar o conteúdo de acordo com os códigos 01, 02, 03 ou 05. Quando Tipo de Operação = “2”, informar o conteúdo de acordo com os códigos 04, 06, 07, 08, 09, 49 ou 99.  Tratamento: Se o campo não for preenchido, ao salvar o registro emitir a mensagem na tela: “O Cód. Sit.Trib. COFINS deve ser informado”. | CH15489_2017 (MFS-12992) |
| Nat. da Base do Crédito | Texto | S | S | Formato: Combo Box  Default: Habilitado | Informar de acordo com:  1 – Aquisição de bens para revenda 2 – Aquisição de bens utilizados como insumo 3 – Aquisição de serviços utilizados como insumo 4 – Energia elétrica e térmica, inclusive sob a forma de vapor 5 – Aluguéis de prédios 6 – Aluguéis de máquinas e equipamentos 7 – Armazenagem de mercadoria e frete na operação de venda 8 – Contraprestações de arrendamento mercantil 9 – Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito sobre encargos de depreciação) 10 – Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito com base no valor de aquisição) 11 – Amortização e Depreciação de edificações e benfeitorias em imóveis 12 – Devolução de Vendas Sujeitas à Incidência Não-Cumulativa 13 – Outras Operações com Direito a Crédito 14 – Atividade de Transporte de Cargas – Subcontratação 17 – Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale-transporte, vale-refeição ou vale-alimentação, fardamento ou uniforme  Tratamento: Se o campo não for preenchido, ao salvar o registro emitir a mensagem na tela: “A Nat. da Base do Crédito deve ser informada”. | CH15489_2017 (MFS-12992) |
| Alíquota PIS | Numérico | N | S | Formato: Text Input 0,0000  Default: Habilitado | Deverá ser informada a alíquota do PIS preenchida no documento ou na operação, se na importação do registro na SAFX147 esse campo não for informado. | CH15489_2017 (MFS-12992) |
| Alíquota COFINS | Numérico | N | S | Formato: Text Input 0,0000  Default: Habilitado | Deverá ser informada a alíquota da COFINS preenchida no documento ou na operação, se na importação do registro na SAFX147 esse campo não for informado. | CH15489_2017 (MFS-12992) |
