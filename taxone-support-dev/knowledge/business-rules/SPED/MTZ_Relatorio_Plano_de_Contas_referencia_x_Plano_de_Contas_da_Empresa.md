# MTZ_Relatorio_Plano_de_Contas_referencia_x_Plano_de_Contas_da_Empresa

> Fonte: MTZ_Relatorio_Plano_de_Contas_referencia_x_Plano_de_Contas_da_Empresa.docx






THOMSON REUTERS

Relatório de Plano de Contas Referencial x Plano de Contas de Empresa
Exportação do relatório em Excel



DOCUMENTO DE REQUISITO


Sumário

1.	TELA A SER DESENVOLVIDA	3
1.1.	Diagrama de Casos de Uso	3
1.1.1.	UC001 – Manutenção da Estrutura Padrão	3
1.1.1.1.1.	Fluxo Principal	3
1.1.1.1.2.	Fluxo Alternativo 1 – Localizar registros (Exemplo)	4
2.	REGRAS DOS CAMPOS	5
2.1.	Layout da Tela	5
3.	REGRAS DE GERAÇÃO DO RELATÓRIO	5
3.1.	Layout do Relatório	6

## TELA A SER DESENVOLVIDA


[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir]

### Diagrama de Casos de Uso





### UC001 – Manutenção da Estrutura Padrão


[Descrever a ação deste caso de uso.

Ex.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão.]


#### Fluxo Principal


[Descrever a ação principal que será realizada na tela especificada.

Ex.: O usuário deseja realizar o cadastro de uma estrutura padrão.



#### Fluxo Alternativo 1 – Localizar registros (Exemplo)




## REGRAS DOS CAMPOS


Localização da tela: Módulo: SPED à ECD – Escrituração Contábil Digital
Menu: Manutenção à Plano de Contas Referencial x Plano de Contas da Empresa

Título da tela: Plano de Contas Referencial x Plano de Contas de Empresa

[ALTERADA - CH22957_2015]
Regra Geral: A tabela de Contas Referenciais X Contas da Empresa deve permitir a inclusão de mesmas contas e centro de custo para entidade responsável diferente cadastrada em Dados Iniciais, pois se tratam de contas referenciais diferentes e de acordo com versões de layouts diferentes a ser entregues.


### Layout da Tela




## REGRAS DE GERAÇÃO DO RELATÓRIO


Origem das informações para geração: Obs: Existe a possibilidade de exportação deste relatório para o tipo Excel, através do menu Arquivo à Salvar Como, porém, a exportação será possível apenas após a geração do mesmo.

Regra de seleção:

Regra de agrupamento:

Ordenação:







### Layout do Relatório




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS1165 | Relatório de Plano de Contas Referencial x Plano de Contas da Empresa ECD – Escrituração Contábil Digital | Inclusão da coluna COD_CUSTO no relatório gerado exportado em Excel através da opção “Salvar Como”. |
| CH22957_2015 | Tratamento na inclusão de Contas Referenciais X Contas da Empresa X Centro de Custo para entidade responsável diferente | Este documento tem como objetivo tratar a inclusão de Contas Referenciais X Contas da Empresa X Centro de Custo para entidade responsável diferente de acordo com a versão da obrigação acessória. |
| MFS17892 | João Henrique | Atualização da versão do plano de contas referencial para 4.00 |
| MFS23780 | João Henrique | Atualização da versão do plano de contas referencial para 5.00 |
| MFS-60592 | Alessandra Cristina Navatta | Atualizada a especificação, considerando a versão 6.00 do plano de contas (apesar de não ser escopo da demanda)  Atualização da versão do plano de contas referencial para 7.00 |
| MFS-81170 | Alessandra Cristina Navatta | Atualização da versão do plano de contas referencial. Inclusão da versão 8.00. |
| MFS-511450 | Elisabete Costa | Atualização da versão do plano de contas referencial. Inclusão da versão 9.00. |
| MFS-599648 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão da versão 10.00. |
| MFS-749696 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão da versão 11.00. |
| MFS-1035615 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão da versão 12.00. |


| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal |  |
| Pré- Condições |  |
| Pós-Condições |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Ações do Ator | Ações do Sistema |
| --- | --- |
|  |  |
|  |  |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Centros de Custo | Texto | N | N | - | Se a Conta Referencial x Conta da Empresa não for suficiente para o relacionamento, o Usuário poderá complementá-lo com a seleção de Centros de Custo (previamente cadastrados em Básicos >> MasterSAF DW >> Manutenção >> Códigos >> Centro de Custo) através do botão de pesquisa (pasta amarela) no campo das contas da empresa para relacioná-las.  [ALTERADA – CH22957_2015] Tratamento: “O sistema irá, automaticamente, atribuir “;" (ponto e vírgula) para separar os códigos do Centro de Custo;  Não será possível excluir ou alterar nenhum código de Centro de Custo. Isso só será possível após a exclusão da Conta Referencial, adicionando a regra dos Centros de Custo novamente; Se o Centro de Custo selecionado já tiver sido atribuído para outro tipo de conta referencial e para uma mesma conta da empresa, ou seja, para outra entidade, emitir a mensagem na tela: “Centro de Custo selecionado já existe para esta Conta da Empresa e outra Conta Referência.”, após não permitir a gravação.  Observação: Estamos retirando o tratamento que existia para a parametrização do Centro de Custo, pois como as contas referenciais são diferentes por entidade, deve permitir que a mesma conta referenciada em outra entidade permita o relacionamento com o mesmo centro de custo. Isso ocorre por conta de mudanças de versão de layout. | CH22957_2015 |
| Versão | Numérico | S | N | DropDownList | Nesse campo é exibida a versão do plano de contas referencial.  1.00 2.00 3.00 4.00  5.00  6.00 7.00  8.00 9.00 10.00 11.00 12.00  Opção Default: Exibir a versão mais atual | MFS17892 MFS23780 MFS-60592 MFS-81170 MFS-511450 MFS-599648 MFS-749696 MFS-1035615 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- |
| Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho | Dados do Cabeçalho |
| [Campo/Coluna especificado no relatório] Ex.: Código do Material] | Tipo da informação Ex.: Texto, Numérico, Data] | Formato:  DD/MM/AA, 0,000,   Default: 0,000 | Definições do campo.   Ex.: Demonstrar o código do material | [MFS/CH] |
| Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório | Corpo do Relatório |


| COD_CUSTO | Texto |  | Incluir a coluna COD_CUSTO (SAFX2003) no relatório exportado para Excel. | MFS1165 |
| --- | --- | --- | --- | --- |
