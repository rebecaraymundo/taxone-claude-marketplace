# MTZ_Tela_Parâmetros_Registro 1900_Conta_Contabil

- **Fonte:** MTZ_Tela_Parâmetros_Registro 1900_Conta_Contabil.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 76 KB

---

THOMSON REUTERS

__Módulo EFD Contribuições – Parametrização das Contas Contábeis__

__Localização__: Menu SPED,  Módulo: Escrituração Fiscal Digital das Contribuições, item Parâmetros 🡪 Registro 1900 🡪 Conta Contábil

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS10591

Andréa Rocha

Criação da parametrização por conta contábil

23/08/2017

	

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Manutenção criada na MFS10591 para a parametrização das contas contábeis \(SAFX2002\) a serem consideradas na geração do registro 1900 do EFD Contribuições\.

__Opções da barra de menu:__

__SELECIONAR GRUPO__ – Ao clicar nesta opção, abrirá uma janela de seleção dos grupos de relacionamento das tabelas do Mastersaf, e o usuário deverá selecionar o grupo e estabelecimento\. Na abertura da tela esta janela será exibida automaticamente, obrigando o usuário a selecionar o Grupo e Estabelecimento\. O grupo e estabelecimento selecionados serão exibidos nos campos “Estabelecimento” e “Grupo Conta”\.

Caso tenha sido informado um estabelecimento no login, serão disponibilizados apenas os grupos aos quais o estabelecimento esteja associado\. Caso contrário, serão disponibilizados todos os grupos e estabelecimentos da Empresa do login\. 

__CONFIRMA__ – Salva os dados incluídos ou alterados;

__RELATÓRIO__ – Para emitir o relatório o usuário poderá selecionar um estabelecimento \(e também uma categoria específica, se desejar\), e serão listados todos os dados parametrizados para os critérios selecionados;

__FECHA__ – Fecha a janela da parametrização;

__RN01__

__                                                        Estabelecimento __

Neste campo será exibido o estabelecimento selecionado na janela de seleção do Grupo\.

__RN02__

__                                                           Grupo Conta __

Este campo exibe o grupo selecionado pelo usuário na abertura da tela, ou alterado pelo usuário na opção “Selecionar Grupo” da barra de menu\. 

__RN03__

__                                                        Pesquisar contas __

Este campo apresenta duas opções:

                                                                            \(  \) Pelas inicias do código 

                                                                            \(  \) Pelas iniciais da descrição 

Default: opção “Pelas iniciais do código”

__Utilização dos campos “Pesquisar contas” e “Conteúdo para pesquisa” como facilitadores da pesquisa das contas:__

  

Os campos “*Pesquisar contas*” e “*Conteúdo para pesquisa*” são um facilitador para a pesquisa das contas a serem demonstradas no campo “Contas”\.

Não existe a obrigatoriedade de sua utilização, pois a princípio o campo “Contas” já exibe todas as contas do Grupo selecionado, conforme consta na __RN06__\.

Apenas quando o usuário escolher uma das formas de pesquisa \(código ou descrição\), informar o conteúdo no campo “Conteúdo para pesquisa”, e clicar no botão “Pesquisar”, é que a lista das contas do campo “Contas” será regerada com as contas selecionadas de acordo com a pesquisa realizada \(ver __RN04__ e __RN05__\)\.

 

__RN04__

__                                                   Conteúdo para pesquisa__

Este é um campo alfanumérico no qual o usuário poderá informar uma quantidade variável de caracteres a serem utilizados como as iniciais a serem pesquisadas no código, *ou* na descrição da conta, dependendo da opção informada no campo “*Pesquisar contas*”\.

O conteúdo informado permitirá filtrar as contas por um código ou descrição específica, como também, pelas iniciais do código ou da descrição\.

__Utilização dos campos “Pesquisar contas” e “Conteúdo para pesquisa” como facilitadores da pesquisa das contas:  __

*\(ver *__*RN03*__* e *__*RN05*__*\)*

__RN05__

__                                                    Opção “Pesquisar”__

Sempre que o usuário clicar no botão “__PESQUISAR__”, a lista das contas exibidas no campo “Contas” será regerada\.

O procedimento quando o usuário clicar neste botão será o seguinte:

__Se__ o campo “*Conteúdo para pesquisa*” estiver vazio:

      Neste caso, a lista das contas será refeita considerando a regra geral descrita na __RN06__\);

__Senão__

     __Se__ campo “*Pesquisar contas*” = “*Pelas inicias do código*”

           Neste caso, a lista das contas será refeita considerando os critérios definidos na regra geral \(__RN06__\), e também, considerando

           a*penas *as contas cujo __código__ apresenta as iniciais iguais ao conteúdo informado no campo ““*Conteúdo para pesquisa*”;

     __Senão__    *\(opção “Pelas iniciais da descrição”\)* 

           Neste caso, a lista das contas será refeita considerando os critérios definidos na regra geral \(__RN06__\), e também, considerando 

           apenas as contas cuja __descrição__ apresenta as iniciais iguais ao conteúdo informado no campo ““*Conteúdo para pesquisa*”;

__RN06__

__                                                               Contas__

Assim que o Grupo e a Categoria forem selecionados pelo usuário, no campo “Contas” será exibida a lista das contas do Plano de Contas \(SAFX2002\) para que o usuário selecione aos contas a serem associados à categoria informada no campo “Categoria”\.

Serão disponibilizadas para seleção apenas as contas do grupo selecionado \(campo “Grupo Operação”\)\.

As contas aparecerão ordenadas pelo código\.

Quando no cadastro da SAFX2002 existir o mesmo código de conta em linhas repetidas, com datas de validade diferentes, será exibido na lista apenas uma ocorrência do código \(que será o de maior data de validade\)\. 

__Reformulação da lista das contas através do botão “PESQUISAR”__:

Sempre que o usuário clicar no botão “PESQUISAR”, a lista das contas será regerada, considerando os critérios para pesquisa informados nos campos “*Pesquisar contas*” e “*Conteúdo para pesquisa*”  \(ver detalhes na __RN05__\)\. 

__RN07__

__Replicar para os Estabelecimentos__

Este campo aparecerá desmarcado por default, e quando selecionado, os dados parametrizados serão replicados para os estabelecimentos selecionados pelo usuário no quadro dos Estabelecimentos\. 

= = = = = 

