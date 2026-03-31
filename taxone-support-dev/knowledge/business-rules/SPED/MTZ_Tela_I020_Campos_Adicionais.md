# MTZ_Tela_I020_Campos_Adicionais

> Fonte: MTZ_Tela_I020_Campos_Adicionais.docx






THOMSON REUTERS

Matriz da tela Registro I020 - Campos Adicionais



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
Módulo: SPED >> ECD-Escrituração Contábil Digital
Menu: Parâmetros

Título da tela: Registro I020 – Campos Adicionais

Funcionamento da tela: Nesta tela serão parametrizados os dados necessários para geração do registro I020 – Campos Adicionais da ECD. Esta parametrização terá um reflexo na geração de outros registros, pois o conteúdo aqui informado será um campo adicional na estrutura do registro indicado no campo Código do Registro.

Devem ser considerados como campos-chave para esta tela os campos “Código do Registro” e “Sequencial do campo adicional”.



* Descrição não disponível em tela


## Layout da Tela no DW




## Layout da Tela no TaxOne - MFS-628959





| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4123 | Marcos G. de Paula | Definição das regras para a tela Registro I020 – Campos Adicionais. |
| OS4544 | Elenilson Coutinho | Alteração da Tela Registro I020 – Campos Adicionais. |
| OS4745 | Marcos G. de Paula | Alteração da tela para atender à versão 3.00 do Layout da ECD. |
| MFS-628959 | Rosemeire Santos | Modificação da tela Registro I020 – Campos Adicionais para T1 |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do Sistema. |
| Pré- Condições | Estar logado no produto MasterSAF DW/T1. |
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
| Tipo de Livro | Dropdown | S | S |  | Exibir os Tipos de Livro cujo conteúdo do registro I020 no Perfil seja igual a "F".  Considerar a seguinte formatação para exibição:  G - Livro Diário (Completa sem Escrituração Auxiliar) R - Livro Diário com Escrituração Resumida (com Escrituração Auxiliar) B - Livro Balancetes Diários e Balanços (Matriz) S - Escrituração SCP Mantida pelo Sócio Ostensivo  Por ser campo obrigatório, se não for informado, retornar a mensagem: “Informe Tipo de Livro”. | OS4123 OS4745 MFS-628959 |
| Perfil | Dropdown | S | S |  | Exibir os Perfis cadastrados para o Tipo de Livro informado.  Por ser campo obrigatório, se não for informado, retornar a mensagem: “Informe Perfil”. | OS4123     MFS-628959 |
| Códigos do Registro | Dropdown | S | S |  | Exibir as seguintes informações:  Registro I050 – Plano de Contas Registro I200 – Lançamentos Contábeis Registro I250 – Partidas do Lançamento Contábil  Se o conteúdo do campo “Tipo de Livro = B - Livro Balancetes Diários e Balanços (Matriz)”, NÂO exibir Registro I200 – Lançamentos Contábeis e Registro I250 – Partidas do Lançamento  Obs: Por ser campo obrigatório, se não for informado, retornar a mensagem: “Campo obrigatório não informado” e posicionar o cursor sobre o campo. | OS4123 OS4544 MFS-628959 |
| Sequencial do campo adicional | Editbox | S | S | Formato: Numérico, sem decimais. | Deve aceitar até 3 dígitos (número máximo: 999).  Por ser campo obrigatório, se não for informado, retornar a mensagem: “Campo obrigatório não informado” e posicionar o cursor sobre o campo. | OS4123 MFS-628959 |
| Nome do campo Adicional | Editbox | S | S |  | Deve aceitar até 255 caracteres.  Por ser campo obrigatório, se não for informado, retornar a mensagem: “Campo obrigatório não informado” e posicionar o cursor sobre o campo. | OS4123 MFS-628959 |
| Descrição do campo adicional | Editbox | N | S |  | Deve aceitar até 255 caracteres. | OS4123 MFS-628959 |
| Origem do campo adicional | Dropdown | S | S |  | O conteúdo deste campo será exibido conforme registro selecionado no campo “Código do Registro”, considerando as seguintes regras.  Se for selecionado o “Registro I050 – Plano de Contas”, demonstrar as seguintes opções:  Código Reduzido da Conta Indicador de Lançamentos Globais Código de Conta Analítica Totalizadora Código de Conta Padrão Código do Centro de Custo Indicador de Situação da Conta  Se for selecionado o “Registro I200 – Lançamentos Contábeis” ou o “Registro I250 – Partidas do Lançamento Contábil”, demonstrar as seguintes opções:  Conta Contra Partida Código da Operação Código do Índice de Conversão Valor do Lançamento Convertido Código do Serviço Reservado 1 Reservado 2 Reservado 3 Reservado 4 Reservado 5 Reservado 6 Reservado 7 Reservado 8  Estes campos estão disponíveis nas tabelas SAFX2002 e SAFX01, tabelas estas utilizadas para gerar os registros I050, I200 e I250. São os campos que não são gerados no layout padrão dos registros e serão disponibilizados para geração como campo adicional.  Por ser campo obrigatório, se não for informado, retornar a mensagem: “Campo obrigatório não informado” e posicionar o cursor sobre o campo. | OS4123 MFS-628959 |
| Formato do conteúdo do campo adicional | Editbox | S | N |  | Este campo deve ser preenchido considerando o tipo especificado para o campo selecionado no campo “Origem do campo adicional”, informado no manual de layout do Mastersaf DW.  Se o tipo for “A”, demonstrar neste campo a expressão: “C – Caractere”.  Se o tipo for “N”, demonstrar neste campo a expressão: “N – Numérico”. | OS4123 MFS-628959 |
