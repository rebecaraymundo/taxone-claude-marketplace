# MTZ_Tela_Manutenção_Bloco F_Demais_Receitas_Lucro_Presumido

> Fonte: MTZ_Tela_Manutenção_Bloco F_Demais_Receitas_Lucro_Presumido.docx



## EFD - PIS/PASEP - COFINS – Tela - Demais Receitas – Lucro Presumido (F500/F510/F550/F560) (SAFX183)


Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Registro do Bloco F >> Demais Receitas - Lucro Presumido (F500/F510/F550/F560)

DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO

















Telas

Com o campo Valor Base preenchido:

Na aba de Demais Receitas, preenchimento da Valor Base PIS/PASEP e COFINS:


Com o campo Quantidade Base preenchida:


Na aba de Demais Receitas, preenchimento da Quantidade Base PIS/PASEP e COFINS:






| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3169-GE25 | Criação do Documento | Criação da tela Demais Receitas- Lucro Presumido (F500/F510/F550/F560) | 27/04/2012 |
| OS3169-25CDW | Alteração do Documento | A tela será dividida em duas Abas:  Demais Receitas e Valores Recebidos | 25/05/2012 |
| OS3932 | Alteração do Documento | Inclusão do campo | 22/02/2013 |
| OS4316 | Inclusão de campo | Incluir o campo Código e Descrição da SCP |  |
| OS4579 | Alteração de Campo | Alteração do campo Número do Lançamento |  |
| MFS747447 | Andréa Rocha | Alteração da regra de preenchimento dos campos Alíquota do PIS e Alíquota do COFINS, de acordo com a definição dos códigos de CST PIS/COFINS. | 17/01/2024 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Criação da Tela ‘Demais Receitas – Lucro Presumido (F500/F510/F550/F560)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital -  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F. | OS3169-GE25 |
| RN01 | Campos Chaves: “Empresa”, “Estabelecimento’’, “Regime”,”Ind. da composição da Receita”, “Informação Complementar da Composição da Receita”, “Nº do Documento/Operação”, “Série”, “Sub-série”, “Nº do Lançamento”, “Data Operação”,“Código Modelo”, “CFOP”,  “Indicador da Pessoa Fís/Jur”, “Codigo /Destinatario/Emitente/Remetente”, “Indicador do Produto”, “Produto”, “Conta”, “Informação Complementar”,” Cód. Sit. Trib. PIS/PASEP”, “Alíquota PIS/PASEP (em %)”, “Alíquota PIS/PASEP (em Reais)”, “Cód. Sit. Trib. COFINS”, “Alíquota COFINS (em %)”, “Alíquota COFINS  (em Reais)”. | OS3169-GE25 |
| RN02 | Campos Obrigatórios: “Empresa”, “Estabelecimento’’, ’’ Tipo de Regime’’, ‘’Data Operação”, “Valor Total da Receita”, “ Cód. Sit. Trib. PIS/PASEP” , “Cód. Sit. Trib. COFINS”. | OS3169-GE25 |
| RN03 | Se o campo Ind. da Composição da Receita estiver preenchido com ‘99’, o campo “informação Complementar da Composição da Receita” é de preenchimento obrigatório. | OS3169-GE25 |
| RN04 | Esta nova tela deverá conter os botões (Novo, Abre, Exclui, Confirme, F509/519/F559/F569, Relatório, Fecha.) | OS3169-GE25 |
| RN05 | Alteração da Tela ‘Demais Receitas – Lucro Presumido (F500/F510/F550/F560)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital -  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F. A tela será dividida em duas Abas:  Demais Receitas e Valores Recebidos | OS3169-25CDW |
| RN06 | Na Aba Demais Receitas, deverá ser incluído os campos Situação do Documento e Tipo de Faturamento.  Valores Válidos para os campos:  Situação do Documento: 1 - Documento Regular 2-   Documento Cancelado  3 -  Outros  Tipo de Faturamento:  1 - A Vista 2 - A Prazo 3 - Sem pagamento | OS3169-25CDW |
| RN07 | Aba Valores Recebidos  Serão exibidos os campos Quantidade Base PIS, se o registro PAI possuir preenchido os campos “Alíquota do PIS em Reais” e “Quantidade Base PIS”, caso contrario, exibir o campo Valor Base PIS/PASEP.  Serão exibidos os campos Quantidade Base COFINS, se o registro PAI possuir preenchido os campos “Alíquota do COFINS em Reais” e “Quantidade Base COFINS” , caso contrario, exibir o campo Valor Base COFINS. | OS3169-25CDW |
| RN08 | Se os campos obrigatórios não forem preenchidos, exibir a seguinte msg: ” Campo XXX de preenchimento obrigatório!” | OS3169-25CDW |
| RN09 | O campo competência deve ser igual ou maior que o mês/ano informado no campo Data da Operação da SAFX183. Caso contrário, exibir a seguinte msg de erro ao usuário: ‘A competência do valor recebido, deve ser igual ou maior que a data da operação da Receita.’ | OS3169-25CDW |
| RN10 | No relatório da tela, deve ser apresentado às informações das receitas e logo em seguida as informações da SAFX187 (quando existir informações), usando o subtítulo Valores Recebidos. | OS3169-25CDW |
| RN11 | Incluir o campo Código da Natureza da Receita, que deve estar previamente cadastrado na TACES72 (DWT_NAT_REC). Campo Não Obrigatório. | OS3932 |
| RN12 | Deverá ser criado o campo Código da SCP, acompanhado da pasta de seleção da informação e o campo de texto para demonstração da descrição vinculada ao código.  Quando acionada a pasta, serão demonstrados os registros da tabela SAFX2057 – Cadastro da SCP. Para o código selecionado, será demonstrada também a descrição da SCP.  Nome do campo em tela: “Código da SCP:”  Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”. | OS4316 |
| RN13 | Campo Número do Lançamento  Deverá ser alterado para suportar até 40 caracteres. | OS4579 |
| RN14 | Campo Alíquota do PIS  Tipo: N Tamanho: 008V004 Não obrigatório  Validação: Quando o campo Código Situação Tributária do PIS for diferente de “6” e o campo Valor da Base de cálculo do PIS estiver preenchido, o campo Alíquota do PIS deve ser preenchido. Caso contrário exibir, a seguinte mensagem de erro ao usuário:            “Se Valor Base PIS  e informado, devera ser preenchido o campo Aliquota em Percentuais.” | MFS747447 |
| RN15 | Campo Alíquota da COFINS  Tipo: N Tamanho: 008V004 Não obrigatório  Validação: Quando o campo Código Situação Tributária da COFINS for diferente de “6” e o campo Valor da Base de cálculo da COFINS estiver preenchido, o campo Alíquota da COFINS deve ser preenchido. Caso contrário exibir, a seguinte mensagem de erro ao usuário:            “Se Valor Base COFINS  e informado, devera ser preenchido o campo Aliquota em Percentuais.” | MFS747447 |
