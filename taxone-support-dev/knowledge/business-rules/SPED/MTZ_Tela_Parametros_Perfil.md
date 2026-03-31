# MTZ_Tela_Parâmetros_Perfil

> Fonte: MTZ_Tela_Parâmetros_Perfil.docx



## EFD - PIS/PASEP - COFINS - Tela Perfil



DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO






| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3169-GE | Criação do documento | Tela - Perfil | 14/03/2012 |
| OS3169-GE25 | Alteração do Documento | Adequação da tela para atendimento ao Lucro Presumido | 14/03/2012 |
| OS3584-DW1 | Alteração do Documento | Adequação da tela para atendimento ao Bloco P |  |
| OS3169-25CDW | Alteração do Documento | Alteração do nome da tela de Perfil |  |
| OS3845 | Inclusão de novo registro | Incluído o registro 0120 – Identificação dos meses de dispensa | 11/12/2012 |
| OS4762 | Exclusão de registros e alteração de descrição | Exclusão dos Registros C800, C810 e C820 e alteração de descrição nos registros C400 e C490. | 27/03/2015 |
| MFS-20225 | Inclusão de Leiaute | Essa MFS tem como objetivo incluir nova versão de leiaute em atendimento a Nota de Documentação Evolutiva da EFD-Contribuições – 001/2018. | 10/12/2018 |
| MFS29843 | Inclusão de Leiaute | Essa MFS tem como objetivo incluir nova versão de leiaute em atendimento ao Guia Prático da EFD-Contribuições versão 1.32. | 24/01/2020 |


| Cód. |  | DR |
| --- | --- | --- |
| RN01 | Campo “Leiaute”  O objetivo deste campo é informar o leiaute a ser considerado para a criação do perfil possibilitando ao usuário criar um Perfil específico para geração do “EFD – Escrituração Fiscal Digital - PIS/PASEP-COFINS”.  [ALTERADA – MFS-20225] Conteúdo do campo: Escrituração Fiscal Digital da Contribuição para o PIS/Pasep e da Cofins – Versão 1.0.0 EFD – Escrituração Fiscal Digital das Contribuições – Até Versão 1.27 EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1.28 EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1.32  A partir da MFS-20225 foi necessário separar os layouts por conta da alteração que os registros M210 e M610 tiveram, pois foram acrescentados campos nesses registros que valerão a partir de 2019, porém, como a entrega da EFD precisará ocorrer ainda em novembro e dezembro de 2018, a sua estrutura deverá ser sem o acréscimo desses campos.  Campo “Perfil”  Neste campo o usuário deverá digitar o código e uma descrição livres, para a criação de um novo perfil. | OS3169-GE MFS-20225 MFS29843 |
| RN02 | Quadro “Definição dos Blocos”  Neste quadro aparecerão os blocos referentes ao leiaute informado.  Ao clicar num determinado bloco, os registros correspondentes aparecerão no quadro “Definição dos Registros”. | OS3169-GE |
| RN03 | No Perfil para atendimento do “EFD – Escrituração Fiscal Digital - PIS/PASEP-COFINS” serão considerados os seguintes blocos: | OS3169-GE |
| RN04 | Quadro “Definição dos Registros”  Neste quadro aparecerão os registros correspondentes ao Bloco escolhido. A informação dos registros deverá ser recuperada das TFIX 67,68,69,70, considerando o layout escolhido. Inicialmente só existe uma opção de layout (“EFD100”), mas deve ser disponibilizado um novo ato legal com novo layout. Obs.: As TFIX’s  serão alterada para conter os dados do novo layout. | OS3169-GE |
| RN05 | Para cada registro são demonstradas as seguintes informações:   Reg.:           Número do registro                   (campo “Registro” da TFIX) Nível:         Nível do registro na hierarquia  (campo “Nivel” da TFIX) Descrição: Nome do registro                      (campo “Descrição” da TFIX)                           (usar endentação de acordo com o nível do registro) Obrigatoriedade: Obrigatoriedade de geração dos registros. Nesta coluna aparecerá a informação se o registro é obrigatório ou não. Esta coluna é apenas informativa. Para os registros de movimento (campo “Registro de Movimento” da TFIX = “S”) será exibido o formato “X/X”, mostrando a obrigatoriedade dos movimentos na entrada e na saída, separadamente. Para os registros normais (campo “Registro de Movimento” da TFIX = “N”), aparecerá apenas o formato  “X”.   Ao recuperar a obrigatoriedade da TFIX, deve-se considerar o perfil informado pelo usuário (no campo “Perfil de Apresentação”), já que há variações na obrigatoriedade de apresentação dos registros entre os dois perfis. Contribuição Social: Indicador S/N para a incidência da contribuição (campo “Contribuição Social” da TFIX) Crédito: Indicador S/N para a incidência da contribuição (campo “Contribuição Social” da TFIX) | OS3169-GE |
| RN06 | Funcionamento da tela:  Inclusão de um novo perfil:  Para criar um perfil, o usuário deve informar o layout, o perfil de apresentação e o código/descrição do perfil a ser criado. Após a informação destes dados, o procedimento será:  Mostrar os blocos no quadro “Definição dos Blocos” conforme a relação dos blocos já descrita acima. O primeiro bloco da lista deve aparecer em foco (Bloco 0);  O quadro “Definição dos Registros” deve apresentar os registros do Bloco escolhido, que serão recuperados da TFIX. Como o Bloco 0 aparecerá sempre selecionado por default, este quadro também mostrará inicialmente os registros do Bloco 0;  Sempre que o usuário selecionar outro bloco no quadro “Definição dos Blocos”, o quadro “Definição dos Registros” deve ser exibido com os registros referentes ao bloco escolhido.   Na criação de um novo perfil, no quadro dos registros deverão aparecer “marcados” APENAS os registros obrigatórios. | OS3169-GE |
| RN07 | Entende-se por registro obrigatório:              Registros comuns com obrigatoriedade = O         Registros de movimento com obrigatoriedade = O para as entradas  OU  para as saídas         (ou seja, sempre que existir uma opção “O”, seja ela referente à operação de entrada ou de saída)          Exemplo:                               =  O/O (obrigatório para as entradas e para as saídas)                               =  O/N (obrigatório p/as entradas e não gerar p/as saídas)                                =  N/O (obrigatório p/as saídas e não gerar p/as entradas)  Os registros que não devem ser gerados, que são os registros com obrigatoriedade = “N”, não deverão ser habilitados para alteração do usuário, e permanecerão sempre desmarcados.  O perfil de apresentação não poderá ser alterado (mesmo que internamente esta informação não faça parte da chave da tabela). Este procedimento evitará problemas na inicialização dos registros. Caso o usuário precise alterar o perfil de apresentação, ele deverá criar um novo perfil. | OS3169-GE |
| RN08 | Entende-se por registro que NÃO deve ser gerado:              Registros comuns com obrigatoriedade  =  N         Registros de movimento com obrigatoriedade  = N para as entradas  E  para as saídas   O usuário poderá efetuar alterações marcando / desmarcando o campo de seleção de cada registro. A alteração na seleção dos registros deve obedecer  as seguintes regras gerais: | OS3169-GE |
| RN09 | Regras Gerais:  Os registros obrigatórios não serão habilitados para alteração (seguindo o mesmo conceito de registro obrigatório descrito acima);                  Ao desmarcar um registro PAI, deve-se automaticamente desmarcar todos os FILHOS, e demais registros dos níveis inferiores associados a ele;;  Ao marcar um registro FILHO cujo PAI esteja desmarcado, deve-se marcar automaticamente o PAI, e demais registros dos níveis anteriores a ele;  A relação de dependência entre os registros deve ser observada através da informação do nível (consultar documento Hierarquia.doc”); | OS3169-GE |
| RN10 | Alterações de perfis já existentes:  Através do botão ABRE o usuário poderá selecionar o perfil desejado. Na janela de seleção do botão ABRE, deverão aparecer somente os perfis criados para geração do Sped Fiscal. Não deverão aparecer perfis de geração de outros meios magnéticos (outros módulos).  No caso da consulta / alteração de um perfil já existente, os registros devem ser exibidos conforme tenham sido atualizados anteriormente, com a seleção feita pelo usuário. | OS3169-GE |
| RN11 | Incluir no bloco F, na definição dos Registros, logo abaixo do registro F211, as seguintes informações:   ATENÇÃO: Os registros F500/F509/510/F519/F525 devem ficar desabilitados até a implementação da OS 3169-GE25C que trata a geração do Lucro Presumido – Regime Caixa. | OS3169-GE25 |
| RN12 | Incluir no bloco 1 , na definição dos Registros, logo abaixo do registro 1809, a seguinte informação:   Se o usuário marcar um dos registros F500/F510/F550/F560 o registro 1900 deve ser marcado automaticamente (sem ser possível desabilitar a geração do registro). Se o usuário marcar um dos registros F500/F510 ele não pode marcar os registros /F550/F560 e vice-versa. | OS3169-GE25 |
| RN13 | Incluir na definição dos blocos a linha do bloco P e  na definição dos Registros, as seguintes informações:  Bloco P:   IMPORTANTE: Não será tratado o registro P110 nesta OS. | OS3584-DW1 |
| RN14 | Incluir no bloco 0 , na definição dos Registros, logo abaixo do registro 0140, a seguinte informação:  Bloco 0: | OS3584-DW1 |
| RN15 | Alteração do nome da tela de Perfil. Localização Parâmetros  Dê: Perfil de Geração – EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS (Inclusão de um novo perfil)	 Para: Perfil de Geração – EFD – Escrituração Fiscal Digital das Contribuições (Inclusão de um novo perfil) | OS3169-25CDW |
| RN16 | Habilitar os registros F500/F509/510/F519/F525 que tratam a geração do Lucro Presumido – Regime Caixa, conforme mencionado na RN11. | OS3169-25C |
| RN17 | Incluir no bloco 0 , a identificação do registro abaixo, posicionar logo abaixo do registro 0111 a partir do leiaute versão 2.0.1  Bloco 0: | OS3845 |
| RN18 | Excluir do bloco C , a identificação dos registros abaixo, a partir do leiaute versão 2.0.1 | OS4762 |
| RN19 | Alteração do bloco C, a descrição dos registros abaixo, a partir do leiaute versão 2.0.1 | OS4762 |
| RN20 | Incluir os registros:  Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1.28: | MFS-20225 |
| RN21 | Alterar o registro M210:  Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1.28:  Considerar os campos:   Caso contrário, manter a estrutura antiga antes da versão 1.28. | MFS-20225 |
| RN22 | Alterar o registro M610:  Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1.28:  Considerar os campos:   Caso contrário, manter a estrutura antiga antes da versão 1.28. | MFS-20225 |
| RN23 | Incluir os registros:  Se campo leiaute = EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1.32: | MFS-29843 |
