# MTZ-Pepsico_Parametrizacao_dos_Perfis

- **Fonte:** MTZ-Pepsico_Parametrizacao_dos_Perfis.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

__Módulo Pepsico – Parametrização dos Perfis__

__Localização__: Menu Específicos, Módulo: Pepsico, item Parâmetros 🡪 Perfis do Sintegra

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4666

Altera geração do MM p/a Pepsico 

Alterações na geração do meio magnético do Sintegra para atendimento ao cliente Pepsico

27/11/2014

\(criação do docto\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Manutenção criada na OS4666 para possibilitar a geração do meio magnético do Sintegra apenas com notas fiscais *não* escrituradas, para atendimento ao regime especial do cliente\.

O objetivo é o usuário informar quais os perfis do meio magnético que deverão ser gerados apenas com as notas fiscais *não* escrituradas\.

A informação dos perfis parametrizados fica registrada na própria tabela dos perfis do Sintegra \(ICT\_PAR\_MEIO\_MAG\), através de uma coluna cuja 

manutenção é feita apenas no Módulo Pepsico, da seguinte forma:

     \- A coluna terá valor “S” para os perfis parametrizados nesta manutenção;

     \- A coluna ficará sem preenchimento \(nulo\) para os perfis *não* parametrizados nesta manutenção;

__*\(\*\)*__* A parametrização dos perfis no Módulo Meio Magnético fica no menu “Parâmetros 🡪 Convênio ICMS 57/95 e Alterações 🡪 Perfil” *

Na abertura da tela serão demonstrados todos os perfis já parametrizados anteriormente, ordenados pelo código\.

\(se necessário, a tela trabalhará com barra de rolagem para que o usuário possa visualizar todos os perfis parametrizados\) 

__RN01__

__                                                       Inclusão de um novo perfil__

Opções da barra de menu:

__NOVO__ – Abre uma nova linha para inclusão de um novo perfil;

__EXCLUI__ – Permite a exclusão de um perfil da parametrização;

__CONFIRMA__ – Salva os dados incluídos;

__RELATÓRIO__ – No relatório serão listados todos os perfis parametrizados, com seus respectivos códigos e descrições, e apresentados em ordem de código \(ver RN04\);

__FECHA__ – Fecha a janela da parametrização;

__RN02__

__                                                       Inclusão de um novo perfil__

Funcionamento da tela na inclusão de um perfil:

Para incluir um perfil na parametrização, o usuário deve clicar na opção <NOVO>\. Esta opção abrirá uma linha para inclusão de um novo perfil\. 

Em seguida, o usuário deve clicar na pastinha de seleção\.

Será aberta uma janela de pesquisa da tabela dos perfis do meio magnético \(tabela ICT\_PAR\_MEIO\_MAG\), e o usuário poderá selecionar um perfil\. Ao confirmar o perfil escolhido, a janela de pesquisa se fecha, e serão exibidos em tela o código e a descrição do perfil escolhido\.

__*\(\*\)*__* A parametrização dos perfis no Módulo Meio Magnético fica no menu “Parâmetros 🡪 Convênio ICMS 57/95 e Alterações 🡪 Perfil” *

__* *__

O usuário poderá parametrizar quantos perfis desejar, e se necessário, a tela trabalhará com barra de rolagem para que o usuário possa visualizar todos os perfis parametrizados\. 

Para os perfis parametrizados, a coluna citada na __RN00__ será atualizada com “S”\.

__RN03__

__                                                          Exclusão de um novo perfil__

Funcionamento da tela na exclusão de um perfil parametrizado:

Para excluir um perfil da parametrização o usuário deve clicar em dos campos da linha a ser excluída e clicar na opção <EXCLUI> da barra de menu\.

Será exibida uma mensagem de confirmação padrão \(Ex: “*Confirma exclusão deste registro*?”\) e quando confirmado, o procedimento será:

      \- Limpar a linha do perfil excluído da parametrização;

      \- Atualizar o registro do perfil excluído, limpando o conteúdo da coluna citada na __RN00, __que ficará com conteúdo = nulo;

__RN04__

__                                                               Relatório __

Conforme padrão das telas de manutenção, a opção <Relatório> da barra de menu gera uma listagem com todos os dados desta manutenção, que na verdade, consta apenas do código e descrição de cada um dos perfis parametrizados:

Os dados serão apresentados ordenados pelo código do perfil:

__                 Perfis do Sintegra p/ geração do arquivo apenas com as NFs não escrituradas __

                            __Código do Perfil__                                          __Descrição__

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

                                       999            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 

= = = = = 

