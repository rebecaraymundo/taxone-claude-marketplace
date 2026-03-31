# MTZ_DMED_Param_Dados_Iniciais

- **Fonte:** MTZ_DMED_Param_Dados_Iniciais.docx
- **Modificado:** 2023-08-21
- **Tamanho:** 113 KB

---

THOMSON REUTERS

__Módulo DMED – Parametrização dos Dados Iniciais__

__Localização__: Menu Federal,  Módulo: DMED, item de menu Parâmetros 🡪 Dados Iniciais

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

Manutenção criada na OS3814 para a parametrização das informações básicas que serão utilizadas na geração do meio magnético da DMED\.

Apesar da DMED ser uma obrigação federal a ser gerada por empresa, a parametrização é por estabelecimento\. 

A geração da obrigação trabalha com a centralização de estabelecimentos do módulo parâmetros \(menu “Centralização da Escrituração de Obrigações Federais”\), o mesmo procedimento utilizado pelas obrigações federais do Sped\.

Desta forma, basta que o usuário parametrize os dados em nome do estabelecimento centralizador da geração\. 

__Opções da barra de menu:__

__NOVO__ – Limpa todos os campos da tela, com exceção do estabelecimento, permitindo a inclusão de um novo registro; 

__ABRE__ – Ao clicar nesta opção, serão exibidos para seleção do usuário todos os dados já parametrizados\. O usuário poderá selecionar um registro, e seus dados serão exibidos em tela para consulta / alteração / exclusão;

__EXCLUI__ – permite a exclusão dos dados;

__CONFIRMA__ – Salva os dados incluídos ou alterados;

__RELATÓRIO__ – para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado;

__FECHA__ – fecha a janela da parametrização;

__RN01__

__                                                       Estabelecimento__

Este campo exibe a lista dos estabelecimentos para escolha do usuário, e exibirá como default o estabelecimento informado no login\.

São considerados apenas os estabelecimentos da empresa do login\.

__RN02__

__                                          Responsável  pela  Declaração__

Este campo é de preenchimento *obrigatório* e trabalha com janela de seleção da tabela dos responsáveis legais \(módulo Parâmetros, item “Requisitos Legais 🡪 Responsável por Informações”\)\.

Se o código do responsável for digitado, será validada a sua existência no cadastro\. Caso não exista, será exibida a mensagem de erro abaixo e a operação não será salva:

*                     “Responsável pela declaração inválido\. Informar um código existente na tabela dos responsáveis legais \(Módulo Parâmetros\)”*

Também será verificado se o responsável informado é uma pessoa física:

Se a categoria do responsável for = “Empresa” \(campo “Categoria”\), será exibida a mensagem de erro abaixo e a operação não será salva:

* “Responsável pela declaração inválido\. Informar um código da tabela dos responsáveis legais \(Módulo Parâmetros\) cuja categoria não seja = Empresa”*

*\(a versão atual da DMED \(2014/2015\) exige um responsável pessoa física, pois no registro “RESPO”, o campo “02\-CPF” é de preenchimento obrigatório, com tamanho fixo de 11 posições\)*

__RN03__

__                                          Responsável  pela  Empresa__

Este campo é de preenchimento *obrigatório* e trabalha com janela de seleção da tabela dos responsáveis legais \(módulo Parâmetros, item “Requisitos Legais 🡪 Responsável por Informações”\)\.

Se o código do responsável for digitado, será validada a sua existência no cadastro\. Caso não exista, será exibida a mensagem de erro abaixo e a operação não será salva:

*                    “Responsável pela empresa inválido\. Informar um código existente na tabela dos responsáveis legais \(Módulo Parâmetros\)”*

Também será verificado se o responsável informado é uma pessoa física:

Se a categoria do responsável for = “Empresa” \(campo “Categoria”\), será exibida a mensagem de erro abaixo e a operação não será salva:

* “Responsável pela empresa inválido\. Informar um código da tabela dos responsáveis legais \(Módulo Parâmetros\) cuja categoria não seja = Empresa”*

__RN04__

__                                                         Tipo do Declarante__

Campo de preenchimento *obrigatório*\.

Tipo: N

Tamanho: 001

Opção default: nenhuma

Este campo é uma lista com as seguintes opções:

1 \- Prestador de serviço de saúde

2 \- Operadora de plano privado de assistência à saúde

3 \- Prestador de serviço de saúde e Operadora de plano privado de assistência à saúde

Quando não informado, será exibida a mensagem abaixo e a operação não será salva:

*                                                                   “O tipo do declarante deve ser informado”*

__RN05__

__                                                            Registro ANS__

Tipo: N

Tamanho: 006

Este campo é de preenchimento *obrigatório* apenas quando o campo “Tipo do Declarante” for = 2 ou 3\.

Ao salvar a operação será validada esta condição, e caso o tipo do declarante seja 2 ou 3, e o campo não tenha sido preenchido, será exibida a mensagem abaixo e a operação não será salva:

*                                                         “O registro ANS deve ser informado quando o tipo de declarante for 2 ou 3”*

__RN06__

__                               Cadastro Nacional de Estabelecimento de Saúde \(CNES\)__

Tipo: N

Tamanho: 007

Campo *não obrigatório*\.

__RN07__

__                                                   Parâmetros para geração da DMED__

Este campo apresenta três opções para seleção do usuário:

                                                                                  \(  \) Operações 

                                                                                  \(  \) Contas Contábeis

                                                                                  \(  \) Operações \+ Contas Contábeis

Tipo: N

Tamanho: 001 \(será gravada 1, 2 ou 3, dependendo da opção selecionada\)

Opção default: nenhuma

As opções são alternativas, e o campo é de preenchimento obrigatório, ou seja, o usuário terá que escolher uma das opções\.

Se ao salvar a operação nenhuma das opções tenha sido selecionada, será exibida a mensagem abaixo e a operação não será salva:

*                                                 “É obrigatória a seleção de uma opção de parâmetros para geração da DMED”*

= = = = = 

