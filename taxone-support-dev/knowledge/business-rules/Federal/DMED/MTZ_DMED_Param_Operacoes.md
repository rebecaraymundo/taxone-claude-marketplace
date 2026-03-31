# MTZ_DMED_Param_Operacoes

- **Fonte:** MTZ_DMED_Param_Operacoes.docx
- **Modificado:** 2022-02-15
- **Tamanho:** 67 KB

---

THOMSON REUTERS

__                                    Módulo DMED – Parametrização das Operações__

__Localização__: Menu Federal,  Módulo: DMED, item de menu Parâmetros 🡪 Operações

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS3814

Criação do Módulo da DMED 

Criação do Módulo da DMED

13/11/2014

\(criação do docto\)

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Manutenção criada na OS3814 para a parametrização das operações \(SAFX2001\) a serem consideradas na geração do meio magnético da DMED\.

Apesar da DMED ser uma obrigação federal a ser gerada por empresa, a parametrização é por estabelecimento\. 

A geração da obrigação trabalha com a centralização de estabelecimentos do módulo parâmetros \(menu “Centralização da Escrituração de Obrigações Federais”\), o mesmo procedimento utilizado pelas obrigações federais do Sped\.

Desta forma, basta que o usuário parametrize os dados em nome do estabelecimento centralizador da geração\. 

__Opções da barra de menu:__

__SELECIONAR GRUPO__ – Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento\. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento\. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo Operação”\.

Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais o estabelecimento esteja associado\. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login\. 

__CONFIRMA__ – Salva os dados incluídos ou alterados;

__RELATÓRIO__ – Para emitir o relatório o usuário poderá selecionar um estabelecimento \(e também uma categoria específica, se desejar\), e serão listados todos os dados parametrizados para os critérios selecionados;

__FECHA__ – Fecha a janela da parametrização;

__RN01__

__                                                        Estabelecimento __

Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo\.

__RN02__

__                                                           Grupo Operação __

Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Selecionar Grupo” da barra de menu\. 

__RN03__

__                                                           Categoria __

Este campo é uma lista com as seguintes opções:

Operadora – Pagamentos de planos de saúde

Operadora – Valores de reembolso aos clientes do plano de saúde

Prestador – Pagamentos de serviços médicos prestados

Após a exibição do Estabelecimento e Grupo selecionados na opção “Selecionar Grupo” \(conforme RN01 e RN02\), o sistema exibira neste campo a primeira opção de categoria, conforme a lista acima, e no quadro das operações, aparecerá a lista dos códigos de operação da SAFX2001, \(conforme RN04\) onde aparecerão marcadas as operações já selecionadas para esta categoria\.

O usuário poderá então selecionar a categoria desejada, e a cada escolha de uma nova categoria, o quadro das operações será atualizado\.

Para cada categoria, o usuário poderá escolher as operações a serem consideradas \(no quadro “Operações”\)\.

__RN04__

__                                                         Operações__

No campo “Operações” será exibida a lista dos códigos de operação da SAFX2001 para que o usuário selecione os códigos a serem associados à categoria informada no campo “Categoria”\.

Serão disponibilizadas para seleção apenas as operações do grupo selecionado \(campo “Grupo Operação”\)\.

Sempre que no cadastro da SAFX2001 existir o mesmo código de operação em linhas repetidas, com datas de validade diferentes, será exibido na lista apenas uma ocorrência do código \(que será o de maior data de validade\)\. 

= = = = = 

