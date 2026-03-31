# MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Credito

> Fonte: MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Credito.docx






THOMSON REUTERS

Matriz da tela/relatório Demonstrativo da Apuração por Tipo de Crédito


Localização:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu:      Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito
Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito


DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	1
1.1.	Diagrama de Casos de Uso	1
1.1.1.	UC001 – Manutenção da Estrutura Padrão	1
1.1.1.1.1.	Fluxo Principal	1
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	1
2.	Regras dos Campos	1
3.	Sugestão de Layout	1
4.	Relatório	1

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso




### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]



#### Fluxo Principal



#### Fluxo Alternativo 1 – Novo Registro




## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito
Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito

As informações que serão demonstradas na tela são baseadas no apurado no processo de geração dos registros.
No acesso à tela deve ser demonstrada a tela padrão de seleção dos registros gerados, considerando as seguintes informações: Estabelecimento, Código da SCP*, Tipo do Livro, Data da Apuração Inicial, Data da Apuração Final, Indicador de Situação da Apuração, Indicador de Validade da Apuração, Data da Realização da Apuração, Descrição da Obs, Id Reg e Código do Layout.

*Caso seja gerado por SCP.





## Sugestão de Layout


## Relatório


Ver documento matriz MTZ_Relatorio_de_Demonstrativo_da_Apuracao_EFD_PISPASEP-COFINS.doc


| OS/CH | Nome | Descrição |
| --- | --- | --- |
|  |  |  |
| OS3169-GE13D | Telas de Emissão do Relatório Demonstrativo da Apuração e alteração da tela Geração dos Registros | Criação das telas de Emissão do Relatório Demonstrativo da Apuração “Por Tipo de Crédito’’ e ‘’Por Tipo de Contribuição’’. Também na tela de Geração dos Registros a inclusão do parâmetro ‘’Gerar Relatórios Demonstrativos da Apuração no Período Informado’’ |
| OS3583 | Alteração – Tela de Emissão do Relatório Demonstrativo da Apuração | Criação da tela de Emissão do Relatório Demonstrativo da Apuração “Por Tipo de Natureza de Crédito’’ |
| OS3631 | Telas de Emissão do Relatório Demonstrativo da Apuração | Alteração da tela de Emissão do Relatório Demonstrativo da Apuração ‘’Por Tipo de Contribuição’’ – inclusão dos filtros Cód. Situação Tributária e Cód. Registro. |
| OS4316-B | Marcos G. de Paula | Duplicação da tela e relatório com seleção da apuração por SCP. |
| MFS37761 | Liliane V. Assaf | Para o TAX ONE habilitar apenas a opção sintético, pois o relatório analítico passa a ser disponibilizado na opção de menu “Relatórios  Demonstrativo da Apuração (Crédito / Contribuição / Natureza da Receita)” |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW. |
| Pós-Condições | Não se aplica. |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  | Fim do fluxo Alternativo |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo | Texto | S | S | Formato:  Radio Button Group  Default:  Habilitado Sintético | Deve ser informado o tipo de relatório que é emitido.  Conteúdo: Analítico  Sintético  Considerações:  Se o usuário optar em emitir o Relatório Analítico, após a emissão é apresentado cada documento fiscal gerado no registro A100/A170, C100/C170, C190/C195, C395/C396, C500/C505, D100/D105, D500/D505, F100, F120, F130, F150, F205, F210 e F800 vinculado a composição no detalhamento do tipo de crédito.  Se o usuário optar em emitir o Relatório Sintético, após emissão é apresentado à totalização dos valores de cada registro vinculado a composição do tipo de contribuição. [MFS37761]: No TAX ONE o relatório Analítico passou a ser gerado através da opção de menu “Relatórios >> Demonstrativo de Apuração (Crédito/Contribuição/Natureza da Receita)”. Desta forma, apenas a opção Sintético fica habilitada para utilização. No DW as duas opções Sintético e Analítico permanecem habilitadas. | OS3169-GE13D MFS37761 |
| Tipo Crédito | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Neste campo deverá apresentada uma lista recuperada da TFIX98.  Além de apresentar as opções da TFIX98, deve apresentar a opção branca | OS3169-GE13D |
| Nat. Base de Crédito | Texto | N | S | Formato:  Combo Box  Default:  Habilitado e Desmarcado | Esse campo deve possuir as opções abaixo.  Esse campo não é de preenchimento Obrigatório.       < > (opção Branco) Aquisição de bens para revenda Aquisição de bens utilizados como insumo Aquisição de serviços utilizados como insumo Energia elétrica e térmica, inclusive sob a forma de vapor  Aluguéis de prédios Aluguéis de máquinas e equipamentos Armazenagem de mercadoria e frete na operação de venda Contraprestações de arrendamento mercantil Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito sobre encargos de depreciação). Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado (crédito com base no valor de aquisição). Amortização e Depreciação de edificações e benfeitorias em imóveis Devolução de Vendas Sujeitas à Incidência Não-Cumulativa Outras Operações com Direito a Crédito Atividade de Transporte de Cargas – Subcontratação Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária Atividade Imobiliária – Custo Orçado de unidade não concluída Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale-transporte, vale-refeição ou vale-alimentação, fardamento ou uniforme Estoque de abertura de bens | OS3169-GE13D |
| Registro | Texto | S | S | Formato:  Check Box  Default:  Habilitado e Todos Marcados | Esse campo deve possuir as opções abaixo. O campo é de preenchimento obrigatório. Além disso, por default  todas as opções: M100, M105,  M500, M505 devem ficar marcados. M100 – Crédito de PIS/PASEP Relativo ao Período M105 – Detalhamento da Base de Calculo do Crédito Apurado no Período – PIS/PASEP M500 – Crédito da COFINS Relativo ao Período M505 – Detalhamento da Base de Calculo do Crédito Apurado no Período – COFINS | OS3169-GE13D |
|  |  |  |  |  |  |  |
