# MTZ_Tela_Lancamentos_Ajustes_Positivos_Negativos

> Fonte: MTZ_Tela_Lancamentos_Ajustes_Positivos_Negativos.docx






THOMSON REUTERS

Matriz da tela Lançamentos de Ajuste Positivo/Negativo



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	4
1.1.1.1.2.	Fluxo Alternativo 1 – Novo Registro	4
2.	Regras dos Campos	4

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
Módulo: MasterSAF DW >> SPED >> EFD-Contribuições Financeira/Assemelhada
Menu: Manutenção >> Registro do Bloco I

Título da tela: Lançamentos de Ajuste Positivo/Negativo



* Descrição não disponível em tela



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS3810-G | Marcos G. de Paula | Definição das regras da tela de Lançamentos de Ajuste Positivo/Negativo |
| MFS61556 | Andréa Rocha | Inclusão de novos códigos (02 a 05) para os campos de Código de Situação Tributária do PIS e Código de Situação Tributária do COFINS, de acordo com os códigos disponibilizados no Guia Prático. |


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
| Estabelecimento | Dropdown | S | S |  | Campo do tipo lista que demonstra a relação de estabelecimentos vinculados à empresa que acessou o módulo. |  |
| Data da Operação | Editbox | S | S | Formato: DD/MM/AAAA |  |  |
| Cód. Situação Tributária PIS | Editbox | S | S |  | Campo do tipo texto, acompanhado da pasta de seleção do Código de Situação Tributária. Teremos: pasta de seleção, caixa de texto com a data de atualização, código CST e descrição do CST.  [MFS61556] Inclusão dos códigos 02, 03, 04 e 05, conforme a lista de códigos disponibilizada pelo Guia Prático  Só serão permitidos os seguintes códigos da Situação Tributária PIS:  1 – Operação Tributável com Alíquota Básica 2 – Operação Tributável com Alíquota Diferenciada 3 – Operação Tributável com Alíquota por Unidade de Medida de Produto 4 – Operação Tributável Monofásica - Revenda a Alíquota Zero 5 – Operação Tributável por Substituição Tributária 6 – Operação Tributável a Alíquota Zero 7 – Operação Isenta da Contribuição 8 – Operação sem Incidência da Contribuição 9 – Operação com Suspensão da Contribuição 49 – Outras Operações de Saída 99 – Outras Operações  Caso o usuário informe um código diferente dos previstos ou não informe nenhum, o sistema deve exibir a seguinte mensagem de erro “O Código de PIS/COFINS deve ser preenchido com :  <1>, <6>, <7>, <8>, <9>, <49> ou <99>”. | OS3810-G MFS61556 |
| Alíquota PIS | Editbox | N | S | Formato: ,0000 | O valor informado neste campo deve ser nulo ou maior ou igual a zero. Se for informado valor menor que zero, retornar mensagem de erro: “Valor Alíquota PIS deve ser maior que 0”. | OS3810-G |
| Cód. Situação Tributária COFINS | Editbox | S | S |  | Campo do tipo texto, acompanhado da pasta de seleção do Código de Situação Tributária. Teremos: pasta de seleção, caixa de texto com a data de atualização, código CST e descrição do CST.  [MFS61556] Inclusão dos códigos 02, 03, 04 e 05, conforme a lista de códigos disponibilizada pelo Guia Prático  Só serão permitidos os seguintes códigos da Situação Tributária COFINS:  1 – Operação Tributável com Alíquota Básica 2 – Operação Tributável com Alíquota Diferenciada 3 – Operação Tributável com Alíquota por Unidade de Medida de Produto 4 – Operação Tributável Monofásica - Revenda a Alíquota Zero 5 – Operação Tributável por Substituição Tributária 6 – Operação Tributável a Alíquota Zero 7 – Operação Isenta da Contribuição 8 – Operação sem Incidência da Contribuição 9 – Operação com Suspensão da Contribuição 49 – Outras Operações de Saída 99 – Outras Operações  Caso o usuário informe um código diferente dos previstos ou não informe nenhum, o sistema deve exibir a seguinte mensagem de erro “O Código de PIS/COFINS deve ser preenchido com :  <1>, <6>, <7>, <8>, <9>, <49> ou <99>”. | OS3810-G MFS61556 |
| Alíquota COFINS | Editbox | N | S | Formato: ,0000 | O valor informado neste campo deve ser nulo ou maior ou igual a zero. Se for informado valor menor que zero, retornar mensagem de erro: “Valor Alíquota COFINS deve ser maior que 0”. | OS3810-G |
| Cód. Receita/Dedução/ Exclusão (Atributo) | Editbox | S | S |  | Campo do tipo texto, acompanhado da pasta de seleção da informação da TACES82. Teremos: pasta de seleção, caixa de texto com o Cód. Receita/Dedução/ Exclusão, Atributo e descrição do Cód. Receita/Dedução/ Exclusão (Atributo).  Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido: “O Cód. Receita/Dedução/Exclusão deve ser preenchido”.  Caso o código indicado pelo usuário não esteja na TACES82, retornar mensagem de erro: “Cód. Receita/Dedução/Exclusão inválido”. | OS3810-G |
| Cód. Compl. da Receita/ Dedução/ Exclusão | Editbox | S | S |  | Campo do tipo texto, acompanhado da pasta de seleção da informação da TACES83. Teremos: pasta de seleção, caixa de texto com o Cód. Compl. da Receita/ Dedução/ Exclusão e a descrição do Cód. Compl. da Receita/ Dedução/ Exclusão.  Como o campo é obrigatório de preenchimento, deve ser exibida mensagem de erro padrão caso esse campo não esteja preenchido: “O Cód. Complemento Receita/Dedução/Exclusão deve ser preenchido”.  Caso o código indicado pelo usuário não esteja na TACES83, retornar mensagem de erro: “Cód. Complemento Receita/ Dedução/ Exclusão inválido”. | OS3810-G |
| Cód. Natureza Receita | Editbox | N | S |  | Campo do tipo texto, acompanhado da pasta de seleção da informação da TACES72. Teremos: pasta de seleção, caixa de texto com o Cód. Natureza Receita e a descrição do Cód. Natureza Receita.  Como o campo é obrigatório de preenchimento quando o CST do PIS ou da COFINS seja igual a 6, 7, 8 ou 9 e deve ser exibida mensagem de erro caso esse campo não esteja preenchido: “Não existe Natureza Receita para o Código de Situação Tributária PIS/COFINS. Favor preencher o Cód. Natureza”. | OS3810-G |
| Conta Contábil | Editbox | N | S |  | Campo do tipo texto, acompanhado da pasta de seleção da informação da SAFX2002. Teremos: pasta de seleção, caixa de texto com o Cód. da Conta Contábil e a descrição da Conta Contábil.  Caso não exista conta contábil cadastrada, retornar mensagem de erro: “Conta Contábil não cadastrada”. | OS3810-G |
| Valor do Ajuste | Editbox | N | S | Formato: ,00 |  | OS3810-G |
| Tipo de Ajuste | Radio Button | N | S | Default: Positivo | Campo do tipo radio Button com as opções: Positivo Negativo | OS3810-G |
