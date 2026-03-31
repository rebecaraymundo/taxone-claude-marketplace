# MTZ_Geracao_Registros

> Fonte: MTZ_Geracao_Registros.docx



## EFD - PIS/PASEP - COFINS – Dados Iniciais



DOCUMENTO DE REQUISITO



### REGRAS DE NEGÓCIO










| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3169-GE25 | Alteração do Documento | Geração do Meio Magnético para as empresas enquadradas no Lucro Presumido | 05/04/2012 |
| OS3583 | Alteração do Documento | Na tela de Geração dos Registros incluir no parâmetro ‘’Gerar Relatórios Demonstrativos da Apuração no Período Informado”, a opção Demonstrativo da Apuração por Tipo de Natureza da Receita | 11/05/2012 |
| OS3169-25CDW | Alteração do Documento | -Alteração no nome da tela para Geração dos Registros – EFD – Escrituração Fiscal Digital das Contribuições	 -Inclusão de novo leiaute - EPC201 - EFD – Escrituração Fiscal Digital das Contribuicoes – Versao 2.0.1 |  |
| OS3169-GE13D | Alteração do Documento | Criação da geração dos dados para os Relatórios de Demonstrativo da Apuração “Por Tipo de Crédito’’ e ‘’Por Tipo de Contribuição’’ |  |
| OS3169-GE25A | Alteração do Documento | Novas mensagens de log |  |
| OS3732 | Alteração do Documento | Inclusão da opção de Geração Multiempresa | 28/12/2012 |
| CH22520/2014 | Alteração do Documento | Inclusão de regra para definição da Data Final da Geração dos Registros. | 18/11/2014 |
| MFS29843 | Alteração do Documento | Inclusão de regra para definição do layout de acordo com o período informado. | 04/02/2020 |
| MFS47099 | Alteração do Documento | Inclusão de parâmetro na tela: “Serviços não parametrizados na tela Identificador da Nat. Base do Crédito.”  Inclusão de validação, se o parâmetro acima estiver marcado.  (RN15) | 09/12/2020 |
| MFS-573500 | Alessandra Navatta | Excluir o agrupamento Performance da tela. Retirando inclusive o parâmetro "Preparação dos Dados de Documentos Fiscal (EPCDF/EPCNE) Expressa". (RN16)  Obs. Apenas documentação da exclusão do agrupamento/parâmetro, já que o campo inicialmente, não foi documentado em regra. | 05/10/2023 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | As regras abaixo são válidas se na tela de Dados Iniciais, o usuário marcar a opção de ‘2 -Lucro Presumido’ no parâmetro ‘Regime de Tributação’. | OS3169-GE25 |
| RN01 | Quando o usuário escolher a apuração ‘2 -Lucro Presumido’ com o Tipo ‘1 – Regime de Caixa – Escrituração consolidada (Registro F500)’,apenas os registros abaixo citados poderão ser gerados:  Bloco 0:   Bloco F: | OS3169-GE25 |
| RN01 | Bloco M: | OS3169-GE25 |
| RN01 | Bloco 1:     Bloco 9:   Vale ressaltar que dentre os registros acima apenas os registros marcados na tela PERFIL serão gerados no arquivo txt. Caso exista algum conflito de parametrização entre as telas de Dados Iniciais e Perfil, a parametrização feita em Dados Iniciais será mandatória. | OS3169-GE25 |
| RN02 | Quando o usuário escolher a apuração  ‘2 -Lucro Presumido’ com o Tipo ‘2 – Regime de Competência – Escrituração consolidada (Registro F550)’ ,apenas os registros abaixo citados poderão ser gerados: Bloco 0:  Bloco F: | OS3169-GE25 |
| RN02 | Bloco M:   Bloco 1: | OS3169-GE25 |
| RN02 | Bloco 9:  Vale ressaltar que dentre os registros acima apenas os registros marcados na tela PERFIL serão gerados no arquivo txt. Caso exista algum conflito de parametrização entre as telas de Dados Iniciais e Perfil, a parametrização feita em Dados Iniciais será mandatória. | OS3169-GE25 |
| RN03 | Quando o usuário escolher a apuração  ‘2 -Lucro Presumido’ com o Tipo ‘9 – Regime de Competência – Escrituração detalhada, com base nos registros dos Blocos “A”, “C”, “D” e “F”’ ,apenas os registros abaixo citados poderão ser gerados:  Bloco 0:  Bloco A: | OS3169-GE25 |
| RN03 | Bloco C: | OS3169-GE25 |
| RN03 |  | OS3169-GE25 |
| RN03 | Bloco D:  Bloco F: | OS3169-GE25 |
| RN03 | Bloco M:   Bloco 1: | OS3169-GE25 |
| RN03 | Bloco 9:   Vale ressaltar que dentre os registros acima apenas os registros marcados na tela PERFIL serão gerados no arquivo txt. Caso exista algum conflito de parametrização entre as telas de Dados Iniciais e Perfil, a parametrização feita em Dados Iniciais será mandatória. | OS3169-GE25 |
| RN04 | Deverá ser criado na tela de Geração dos Registros EFD PIS/COFINS o novo parâmetro “Gerar Relatórios Demonstrativos da Apuração no Período Informado com as seguintes opções: Demonstrativo da Apuração por Tipo de Crédito Demonstrativo da Apuração por Tipo de Contribuição | OS3169-GE13D |
| RN04 | Deverá ser incluído na tela de Geração dos Registros no  parâmetro “Gerar Relatórios Demonstrativos da Apuração no Período Informado a seguinte opção: Demonstrativo da Apuração por Tipo de Natureza da Receita  Caso seja marcada esta opção, com base nas regras “RNG – M400_M410_M800_M810_v7.doc”, será gerado o relatório (Demonstrativo da Apuração por Tipo de Natureza da Receita), que será emitido seguindo layout citado nas  regras (RN84 a RN94)  da “MTZ -Relatorio de Demonstrativo da Apuracao EFD PISPASEP-COFINS.docx.”, através da tela ‘Emissão do Relatório de Demonstrativo da Apuração à Por Tipo de Natureza da Receita’, localizada no Módulo: SPEDà EFD – Escrituração Fiscal Digital das Contribuições , Menu: Obrigações à Demonstrativos | OS3583 |
| RN05 | Alteração do nome da tela de Geracao dos Registros.Localização Obrigações  Dê: Geracao dos Registros – EFD PIS/COFINS Para: Geração dos Registros – EFD – Escrituração Fiscal Digital das Contribuições | OS3169-25CDW |
| RN06 | Inclusão de um novo leiaute que contempla os registros do Lucro Presumido na geração do arquivo da EFD – Escrituração Fiscal Digital das Contribuições  	 Nome do Leiaute: EPC201 – EFD – Escrituração Fiscal Digital das Contribuicoes – Versao 2.0.1 | OS3169-25CDW |
| RN07 | Este leiaute considera as informações do Lucro Presumido (registros F500/F550). | OS3169-25CDW |
| RN08 | Este leiaute deve ser utilizado a partir da competência de  julho/2012. | OS3169-25CDW |
| RN09 | Com base na data informada nos campos Data Inicial e Data Final deve ser habilitado o leiaute compatível com o período, conforme informado abaixo: - Se a data Inicial e final estiver compreendida até 30/06/2012 (deverá ser visualizado na tela, apenas o leiaute: EPC100 – Escrituracao Fiscal Digital da Contribuicao para o PIS/PAEP e da COFINS – Versao 1.0.0 - Se a data inicial e a final for a partir de julho/2012 (deverá ser visualizado na tela, apenas o leiaute: EPC201 – EFD – Escrituração Fiscal Digital das Contribuicoes – Versao 2.0.1 - Se a data inicial e a final for a partir de janeiro/2019 (deverá ser visualizado na tela, apenas o leiaute: EPC310 – EFD – Escrituração Fiscal Digital das Contribuicoes –  A partir da Versão 1.28  [MFS-29843] Inclusão do leiaute 2020 - Se a data inicial e a final for a partir de janeiro/2020 (deverá ser visualizado na tela, apenas o leiaute: EPC320 – EFD – Escrituração Fiscal Digital das Contribuições – A partir da Versão 1.32 - Se a data informada for inválida (Período compreendido em meses diferentes/ data inválida) a msg de período inválido será mostrada no log conforme abaixo: O período da geração está inválido. - Se o cliente informar a data Inicial e Final, em meses distintos e no período informado, os dois leiautes estiverem vigentes, mostrar os dois leiautes e no log mostrar a msg de período inválido: “O período da geração está inválido.” | OS3169-25CDW MFS-29843 |
| RN10 | Neste leiaute (EPC201 – EFD – Escrituração Fiscal Digital das Contribuicoes – Versao 2.0.1), além de gerar todos os registros da versão 1.0.0 deve ser contemplado os registros F500/F509/F510/F519/F525/F550/F559/F560/F569/1900, incluir o 5º campo do registro 0110 e o campo 02 do registro 0000, deve ser ‘003’. | OS3169-25CDW |
| RN11 | Incluir as seguintes msgs no log:  1 – Se existir alguma receita (documentos de saída), que foi recuperada para a geração dos registros F500/F550 e que não possua os CST (tanto de PIS quanto COFINS) dentre os listados : 01,02,04,05,06,07,08,09,49 e 99 exibir a seguinte msg no log: ‘O documento XXX foi considerado na geração, mas não possui um CST válido.’ 2- Se existir alguma receita (documentos de saída), que foi recuperada para a geração dos registros F510/F560 e que não possua os CST (tanto de PIS quanto COFINS) dentre os listados : 03,05,06,07,08,09,49 e 99 exibir a seguinte msg no log: ‘O documento XXX foi considerado na geração, mas não possui um CST válido.’ | OS3169-GE25A |
| RN12 | 1. Inclusão da Opção ‘Geração Multiempresa’: 1.1 Este campo deve ser desmarcado por default; 1.2 Quando a opção ‘Geração Multiempresa’ estiver marcada, serão exibidas todas as empresas que o usuário possui acesso e que possuam estabelecimentos com parametrização em Dados Iniciais. Se não tiver marcado, serão listados apenas os estabelecimentos da empresa que o usuário estiver logado (considerando o perfil de acesso do usuário e os estabelecimentos  que possuam parametrização em Dados Iniciais). | OS3732 |
| RN13 | Funcionamento da Geração Multiempresa:  Quando o parâmetro Geração Multiempresa estiver marcado, no campo Empresa/Estabelecimento, serão exibidas todas as empresas que o usuário logado possui acesso (e que possuam estabelecimentos com parametrização em Dados Iniciais). Para as empresas selecionadas será gerado um arquivo (processo) para cada estabelecimento centralizador, com os dados dos respectivos estabelecimentos centralizados (de acordo com a parametrização realizada no Módulo: Mastersaf DW/ Básicos / Parâmetros, Menu: Preliminares >> Centralização da Escrituração das Obrigações Federais) e caso existam estabelecimentos descentralizados para esta empresa, será gerado um arquivo (processo) para cada estabelecimento descentralizado. Se o parâmetro estiver desmarcado, serão apresentados no campo Empresa/Estabelecimento os estabelecimentos centralizados e descentralizados (considerando o perfil de acesso do usuário e os estabelecimentos que possuam parametrização em Dados Iniciais), para o usuário selecionar para qual estabelecimento serão gerados os arquivos . | OS3732 |
| RN14 | Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições / Menu: Obrigações >> Geração dos Registros  Campo Data Final  O conteúdo do campo “Data Final” deve estar no mesmo período (MM/AAAA) da data informada no campo Data Inicial. Caso seja de período diferente, retornar não permitir a geração dos registros e retornar a mensagem ao usuário: “Data Final informada deve ser do mesmo período da Data Inicial”. | CH22520/2014 |
| RN15 | Incluir o parâmetro “serviços não parametrizados na tela Identificador da Nat. Base do Crédito” na tela.   Tratamento para a Validação:  Se o parâmetro “Serviços não parametrizados na tela Identificador da Nat. Base do Crédito” estiver marcado e se em dados iniciais a opção “Considerar a Natureza da Base do Crédito a partir de Documentos Fiscais“ estiver desmarcada:  Verificar em todas as notas recuperadas na geração dos registros A170, que possuem item de serviço,  Se o serviço está parametrizado em alguma das parametrizações da tela de Identificador da Nat. Base de Crédito (por CFOP, por extensões de CFOP e ou por Código de Serviço)”, Caso não esteja em nenhuma das parametrizações (por CFOP, por extensões de CFOP e ou por Código de Serviço), exibir a mensagem de aviso por serviço: “O serviço ‘XXXX’, não foi parametrizado para identificarmos a Nat. Base de Crédito (por CFOP, por extensões de CFOP e ou por Código de Serviço). Favor rever a parametrização (Parâmetros / Identificador da Nat. Base de Crédito).”  Se o parâmetro “Serviços não parametrizados na tela Identificador da Nat. Base do Crédito” estiver marcado e se em dados iniciais a opção “Considerar a Natureza da Base do Crédito a partir de Documentos Fiscais” estiver marcada, exibir a mensagem de aviso: “Atenção! A validação da parametrização dos Serviços não será realizada, pois, a identificação da natureza da base do crédito não considera parametrização e sim a informação existente no documento fiscal, conforme parametrização feita em Dados Iniciais."  Se o parâmetro “Serviços não parametrizados na tela Identificador da Nat. Base do Crédito” estiver desmarcado, a validação não deve ser realizada. | MFS47099 |
| RN16 | Excluir o agrupamento ‘Performance’ da tela. Retirando inclusive o parâmetro "Preparação dos Dados de Documentos Fiscal (EPCDF/EPCNE) Expressa". | MFS-573500 |
