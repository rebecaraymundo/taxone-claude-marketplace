# MTZ-Tela_de_Geracao_do_Meio_Magnetico

> Fonte: MTZ-Tela_de_Geracao_do_Meio_Magnetico.docx


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO















| DR | Nome | Descrição |
| --- | --- | --- |
| OS3835 | ECD – Tela de Geração do Meio Magnético. | Este documento tem por objetivo especificar as alterações para que o mastersaf possa contemplar o layout da ECD 2012. |
| OS3835-B | ECD – Tela de Geração do Meio Magnético. | Inclusão do campo: NIRE Escrituração Substituída |
| OS4518 | ECD – Tela de Geração do Meio Magnético. | Inclusão do Botão: Salvar Log de Processos Selecionados |
| OS3853 | ECD – Tela de Geração do Meio Magnético. | Ajuste na regra de exibição do campo “Estabelecimento” para geração do Tipo de Livro “Z – Razão Auxiliar” |
| OS4745 | ECD – Tela de Geração do Meio Magnético. | Alteração das informações exibidas nos campos Leiaute, Tipo de Livro e Perfil para atender à versão 3.00 da ECD. |
| MFS-2473 | ECD – Tela de Geração do Meio Magnético. | Alteração da informação exibida no campo Leiaute para atender à versão 4.00 da ECD. |
| MFS-3804 | ECD – Tela de Geração do Meio Magnético. | Ajuste na regra de exibição do campo “Estabelecimento” para geração do Tipo de Livro “Z – Razão Auxiliar”. |
| MFS-8216 | ECD – Tela de Geração do Meio Magnético. | Alteração da informação exibida no campo Leiaute para atender à versão 5.00 da ECD. |
| MFS-9689 | ECD – Tela de Geração do Meio Magnético. | Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD. De acordo com as orientações do PVA versão 4.0.0. |
| MFS17892 | ECD – Tela de Geração do Meio Magnético. | Atualização da versão do plano referencial da tela de geração do ECD. |
| MFS-23322 | ECD – Tela de Geração do Meio Magnético. | Atualização da versão do Leiaute da tela de geração do ECD. |
| MFS-23870 | ECD – Tela de Geração do Meio Magnético. | Atualização da versão do plano referencial da tela de geração do ECD. |
| MFS-29278 | ECD – Tela de Geração do Meio Magnético. | Retirar as opções de demonstrações contábeis da tela de geração do arquivo magnético. (RN13 e RN14) |
| MFS-32554 | ECD – Tela de Geração do Meio Magnético. | Atualização Leiaute 8 - Criação do Leiaute 8 na tela de Geração e Registro I010.  (Ajuste na regra RN01) |
| MFS-32555 | ECD – Tela de Geração do Meio Magnético. | Atualização Leiaute 8 - Atualização do Registro 0000: Abertura do Arquivo Digital e Identificação do Empresário ou da Sociedade Empresária (RN15) |
| MFS-32558 | ECD – Tela de Geração do Meio Magnético. | Inclusão de validação (mensagem de aviso) se existir geração de J100 (Balanço) e ou J150 (DRE) sem J800 com tipo de documento de notas explicativas. (RN14) |
| MFS32694 | ECD – Tela de Geração do Meio Magnético. | Inclusão do parâmetro ‘Qtd. Max. de logs (0 = todos)’ (RN16) |
| MFS-48442 | ECD – Tela de Geração do Meio Magnético. | Atualização Leiaute 9 - Criação do Leiaute 9 na tela de Geração e Registro I010.  (Ajuste na regra RN01) |
| MFS-60592 | ECD – Tela de Geração do Meio Magnético. | Atualização da versão do plano referencial |
| MFS-46921 | ECD – Tela de Geração do Meio Magnético. | Inclusão da regra do campo Livro Auxiliar (RN17) |
| MFS-76512 | ECD – Tela de Geração do Meio Magnético. | Atualização Leiaute 9.00 - Criação do Leiaute 9.00 na tela de Geração e Registro I010. (Ajuste na regra RN01) |
| MFS-81170 | ECD – Tela de Geração do Meio Magnético. | Atualização da versão do plano referencial da tela de geração do ECD. Inclusão da versão 8.00. |
| MFS-80610 | ECD – Tela de Geração do Meio Magnético | Permitir a escolha de uma parametrização de contas aglutinadoras. Para atender o objetivo da demanda, será disponibilizado o campo Perfil Cód. Aglutinação na tela abaixo do campo Livro Auxiliar. |
| MFS-99167 | ECD – Tela de Geração do Meio Magnético. | Continua no Leiaute 9.00 - Criação do Leiaute 9.00 na tela de Geração e Registro I010. (Ajuste na regra RN01) |


| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Alteração da tela Geração do Meio Magnético ‘Módulo: SPED/ECD Escrituração Contábil Digital,Menu: Geração  Criação dos campos: Leiaute, Finalidade Escrituração, Hash Escrituração Substituída, Obrigatoriedade de entrega no curso do ano. | OS3835 |
| RN01 | Criar nova opção na tela, para exibir o leiaute que será utilizado para gerar o arquivo txt. Opções válidas: Escrituração Contábil Digital – Versão 1.00 Escrituração Contábil Digital – Versão 2.00 Escrituração Contábil Digital – Versão 3.00 Escrituração Contábil Digital – Versão 4.00 Escrituração Contábil Digital – Versão 5.00 Escrituração Contábil Digital – Versão 6.00 Escrituração Contábil Digital – Versão 7.00 Escrituração Contábil Digital – Versão 8.00 Escrituração Contábil Digital – Versão 9.00 Escrituração Contábil Digital – Versão 9.00 Escrituração Contábil Digital – Versão 9.00 | OS3835 OS4745 MFS-2473 MFS-8216 MFS-15525 MFS-23322 MFS-32554 MFS-48442 MFS-76512 MFS-99167 |
| RN02 | Criar nova opção na tela que permite selecionar a finalidade da escrituração.  [ALTERADA MFS9689] Opções válidas até a versão de leiaute 4.00:  ‘0 – Original’ ‘1 – Substituta da Escrituração com NIRE’ ‘2 – Substituta da Escrituração sem NIRE’ ‘3 – Substituta da Escrituração com troca de NIRE’ Por default deve vir preenchido com a opção ‘0 – Original’  Quando selecionado no campo Leiaute a versão 1.00 deverá ser apresentado apenas à opção ‘0 – Original’ visto que as demais opções foram criadas apenas a partir do Leiaute versão 2.00.  Opções criadas na versão de leiaute 5.00 e válidas para todas as versões de leiaute:  Opções válidas:  ‘0 – Original’ ‘1 – Substituta’ Por default deve vir preenchido com a opção ‘0 – Original’  Ou seja, a partir na versão 5.00 deverá ser demostrados apenas as opções acima. | OS3835 MFS-8216 MFS-9689 |
| RN03 | O campo Hash Escrituração Substituída, só deve ser habilitado se a finalidade da escrituração for diferente de  ‘0 – Original’ Tipo: A Tamanho: 40 posições Campo Não Obrigatório | OS3835 |
| RN04 | Criar novo flag de Obrigatoriedade de entrega no curso do Ano. Por default deve vir desmarcado. | OS3835 |
| RN05 | Caso o cliente utilize um perfil que pelo menos um dos registros: J200, J210 ou J215 esteja selecionado e utilize na geração o layout:  Escrituração Contábil Digital – Versão 1.00, estes registros não serão gerados (já que são válidos apenas no layout: Escrituração Contábil Digital – Versão 2.00 ou superior).  Neste caso, exibir a seguinte msg no log: “Os registros J200, J210 e J215 não foram gerados, pois está sendo utilizado o layout Escrituração Contábil Digital – Versão 1.00, para a geração do arquivo”.  Caso o cliente utilize um perfil que pelo menos um dos registros: 0035, I053 ou J935 esteja selecionado  e utilize na geração o layout:  Escrituração Contábil Digital – Versão 1.00 ou Escrituração Contábil Digital – Versão 2.00, estes registros não serão gerados (já que são válidos apenas no layout: Escrituração Contábil Digital – Versão 3.00 ou superior).  Neste caso, exibir a seguinte msg no log: “Os registros 0035, I053 ou J935 não foram gerados, pois não são válidos para a versão de Leiaute indicado” | OS3835 OS4745 MFS-2473 |
| RN06 | Criação do campo: NIRE Escrituração Substituída. | OS3835-B |
| RN07 | O campo ‘NIRE Escrituração Substituída’, só deve ser habilitado se a finalidade da escrituração for igual a ‘3 – Substituta da Escrituração com troca de NIRE’, neste caso o preenchimento do campo é obrigatório. Tipo: A Tamanho: 40 posições Campo Não Obrigatório  Validação: Caso, a finalidade da escrituração for igual a ‘3’ e o campo ‘NIRE Escrituração Substituída’, não for preenchido pelo usuário, emitir a seguinte msg: “O campo ‘NIRE Escrituração Substituída’, deve ser preenchido.” | OS3835-B |
| RN08 | Botão: Salvar Log de Processos Selecionados Não obrigatório  Deverá salvar os arquivos de log dos processos assim selecionados pelo usuário, devem conter a seguinte nomenclatura: N_PROCESSO + COD_PERFIL + MM + AAAA + NOME OBRIGAÇÃO. Exemplo: 166544_003_01_2013_SPED.  Estes serão salvos no caminho assim definido pelo usuário no campo “Diretório” da aba processos da tela “Geração do Arquivo Magnético“ localizada Menu SPED à ECD – Escrituração Contábil Digital à Geração à Meio Magnético.  Obs: MM/AAAA será a “Data Inicial” do período informado para geração. | OS4518 |
| RN09 | A regra de exibição da lista de “Estabelecimentos” deve ser ajustada para o Tipo de Livro “Z – Razão Auxiliar”.  Se na tela de Geração for Selecionado no campo “Tipo de Livro” a opção “Z – Razão Auxiliar (Livro Contábil Auxiliar Leiaute conforme Regs I500 a I555)”, exibir na relação dos estabelecimentos apenas os estabelecimentos que foram associados na tela de “Impressão do Livro Razão Auxiliar” (menu Parâmetros >> Impressão do Livro Razão Auxiliar) ao Livro Auxiliar indicado na tela (campo Livro Auxiliar) OU os estabelecimentos que estejam parametrizados na tela de “Critérios de Consolidação – Razão Auxiliar das Subcontas” (menu Parâmetros >> Critérios de Consolidação – Razão Auxiliar das Subcontas) para o Livro selecionado..  Na geração do arquivo, serão geradas as informações de Estabelecimento, Livro e Período, conforme indicado pelo usuário e previamente importadas para o Mastersaf através da tela de “Livro Razão Auxiliar” (menu Manutenção >> Livro Razão Auxiliar) ou conforme indicado na tela de “Critérios de Consolidação – Razão Auxiliar das Subcontas” (menu Parâmetros >> Critérios de Consolidação – Razão Auxiliar das Subcontas).  Se o usuário indicou um Estabelecimento, Livro e Período, mas não importou dados para este Livro através da manutenção do “Livro Razão Auxiliar” OU não tem registros na SAFX179 (para situações de geração através de livro parametrizado na tela de Critérios de Consolidação – Razão Auxiliar das Subcontas), retornar no log de geração a seguinte mensagem: “Não foram encontrados dados do Estabelecimento <CÓD ESTAB>, Livro <COD LIVRO> e Período <PERIODO> importados para geração”. | OS3853 MFS-3804 |
| RN10 | Campo Tipo de Livro  Quando for selecionada a versão de Leiaute “3.00” ou superior, além dos tipos de livro já existentes (A, B, G, R e Z) demonstrar também a opção de Livro “S – Escrituração SCP Mantida pelo Sócio Ostensivo”. | OS4745 MFS-2473 |
| RN11 | Campo Perfil  Observar que em função da inclusão de um novo Tipo de Livro o campo Perfil também deve ser alterado, de modo que demonstre o perfil associado ao tipo de livro indicado pelo usuário. | OS4745 |
| RN12 | Campo Versão do Plano Referencial  Campo tipo dropdown com as opções:  1.00 2.00 3.00 4.00 5.00 6.00 7.00 8.00      Exibir como default a opção “7.00”   A versão mais atual (última versão) | OS4745 MFS17892 MFS-23870 MFS-60592 MFS-81170 |
| RN13 | Excluir as opções de Demonstrações Contábeis da tela:  Balanço Patrimonial Demonstração do Resultado Gera Relatórios das Demonstrações Contábeis (Usar Botão na barra de ferramenta) Gera Relatório de Conferência (Para consultar/alterar a definição dos registros do relatório, acionar o botão na barra de ferramentas)  Ajustar o título do agrupamento de Gerar Demonstrações Contábeis no período informado para Consistência e Arquivo RTF | MFS-29278 |
| RN14 | Botão Executar:  Ao acionar o botão Executar, e a geração for de um dos livros G, R e ou S, recuperar as demonstrações contábeis que foram geradas e que possuem o campo “Período do Arquivo da ECD” preenchido e igual ao indicado no período de geração do meio magnético.   Validações:   Se existir geração de J100(Balanço) e ou DRE (J150) com pelo menos um registro com o campo NOTA_EXP_REF preenchido, verificar se há pelo menos um J800 (Outras Informações), gerado com tipo de documento igual a “010 – Notas Explicativas”, “011 – Relatório da Administração”, “012 – Parecer dos Auditores” ou “999 – Outros”. Caso não seja encontrado, exibir a mensagem de aviso no log: “Existindo demonstrações de Balanço (J100) e ou DRE (J150), com o campo NOTA_EXP_REF preenchido, deve ter um registro J800 (Outras Informações) com tipo de documento igual a Notas Explicativas.” | MFS-29278 MFS-32558 |
| RN15 | Inclusão do parâmetro ‘Houve Mudança no Plano de Contas’, este parâmetro só deve ser habilitado a partir da versão do leiaute 8.00 (opção Escrituração Contábil Digital – Versão 8.00). | MFS-32555 |
| RN16 | Inclusão do parâmetro ‘Qtd. Max. de logs (0 = todos)’, este parâmetro por default deve ser valor ‘0’.  Formato do campo: Numérico 4 posições  Obs. Considerando o valor indicado, vamos limitar as linhas de erro exibidas no log. Caso o parâmetro esteja preenchido com ‘zero’, será demonstrado o log completo. | MFS-32694 |
| RN17 | Campo Livro Auxiliar  Apresentar os livros auxiliares criados referentes ao livro indicado no campo Tipo de Livro.   Livros que habilitam esse campo: ‘R - Diário com Escrituração Resumida (vinculado a livro auxiliar)’ou  ‘B - Livro de Balancetes Diários e Balanços’ | MFS46921 |
| RN18 | Campo Perfil Cód. Aglutinação  Disponibilizar o campo Perfil Cód. Aglutinação na tela, abaixo do campo Livro Auxiliar.  Este campo recuperará as parametrizações criadas na tela Códigos de Aglutinação (Balanço Patrimonial/Demonstração Resultado/ DLPA / DMPL), no menu Manutenção do módulo Sped ECD – Escrituração Contábil Digital  Formatação: Cod – Descrição | MFS-80610 |
