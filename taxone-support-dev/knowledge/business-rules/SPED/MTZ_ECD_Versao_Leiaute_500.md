# MTZ_ECD_Versao_Leiaute_500

> Fonte: MTZ_ECD_Versao_Leiaute_500.docx






THOMSON REUTERS

ECD
Atualização da Geração do Arquivo para atender ao Leiaute 5.00



DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO




Alterações Registro 0000




Alterações Registro I010



Alterações Registro I015



Alterações Registro I051



Alterações Registro I053



Alterações Registro J800




Novo Registro J801 - Termo de Verificação para Fins de Substituição da ECD




Alterações Registro J930



Inclusão do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016)





Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:






| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-8216 | Lara Aline | Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD. |
| MFS-8620 | Lara Aline | Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD. |
| CH21396/2016 | Lara Aline | Ajuste na geração do campo 02 - COD_CTA_RES do I015 para os livros auxiliares (A e Z). |
| MFS-9689 | Lara Aline | Atualização das Informações do arquivo da ECD para atender à versão 5.00 do Leiaute da ECD. De acordo com as orientação do PVA versão 4.0.0. |
| MFS9809/ CH2989/2017 | Andrea Rocha | Atualização das informações do bloco K |
| MFS10727 | Lara Aline | Ajuste na regra do Campo 02 – COD_PLAN_REF do Registro I051. |
| MFS-10358 | Lara Aline | Atualização das Informações do arquivo da ECD para atender o Bloco K na versão 5.00 do Leiaute da ECD. |
| CH8476_2017 (MFS-10940) | Julyana Perrucini | Alteração da regra de preenchimento do campo 03 do Registro J930. |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN00 | Regra Geral  Este documento tem como objetivo demonstrar as alterações da versão 5.00 do leiaute da ECD em relação à versão 4.00. Este novo leiaute será obrigatório a partir do ano-calendário 2016.  Todos os registros deverão ser mantidos conforme layout anterior, incluindo as alterações e criação dos novos registros que estarão definidos nas regras de negócios descritas neste documento, documento de requisito e documentos matriz relacionados na alteração da versão. | MFS-8216 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RN0000-14 | Registro 0000 – Campo 14 – IND_FIN_ESC  Indicador de Finalidade de Escrituração Preencher com ‘0’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘0 – Original’; Preencher com ‘1’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘1 – Substituta’  Campo de preenchimento obrigatório. | MFS-8216 |
| RN0000-16 | [EXCLUÌDO] Registro 0000 – Campo 16 – NIRE_SUBST.  Este campo foi excluído a partir do layout da versão 5.00.   Importante: Deverá ser reposicionada a numeração dos campos posteriores. | MFS-8216 |
| RN0000-20 | Registro 0000 – Campo 20 – IND_ESC_CONS  Este campo existe a partir da versão 5.00. Inicialmente será gerado com conteúdo fixo: “N”  Será gerado conforme parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais (menu Parâmetros): Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”. Se o parâmetro estiver selecionado, será gerado com conteúdo “S”. | MFS-8216 MFS-10358 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNI010-03 | Registro I010 – Campo 03 – COD_VER_LC  Para a versão 5.00, será gerado com o código “5.00”. | MFS-8216 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNI015-02 | Registro I015 – Campo 02 – COD_CTA_RES  Para os livros auxiliares ‘A’ ou ‘Z’ nesse campo será gerada a informação da conta sintética (campo COD_CONTA_SINT da SAFX2002) associada à conta analítica movimentada encontrada, nesse caso será gerada sempre a primeira conta sintética encontrada. Exemplo:   No caso do exemplo acima para a conta analítica 1.1.1.01.0001 está associada a conta sintética 1.1.1.01, que será gerado no registro I015 para os livros ‘A’ ou ‘Z’.  Obs.: Para os outros Livros a geração desse campo continua conforme o padrão, ou seja, gerando a conta analítica movimentada encontrada. | CH21396_2016 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNI051-02 | Registro I051 – Campo 02 – COD_PLAN_REF  A partir da versão 5.00 nesse campo foi incluído um novo Código da Entidade “10- Financeiras – Lucro Presumido” e foi alterado o tamanho do campo para 2 posições.  A partir da versão 5.00 este registro será gerado apenas quando o Código da Entidade for igual a “1 - PJ em Geral”, ”2 - PJ em Geral - Lucro Presumido”, “3 – Financeiras”, “4 – Seguradoras”, “5 - Imunes e Isentas em Geral”, “6 - Financeiras - Imunes e Isentas”, “7 - Seguradoras - Imunes e Isentas”, “8 - Entidades Fechadas de Previdência Complementar”, “9 - Partidos Políticos”. ou “10- Financeiras – Lucro Presumido/ Secretaria da Receita Federal”.  Caso o usuário não tenha realizado parametrização para uma destas entidades indicadas acima em Dados Iniciais e/ou Plano de Contas Referencial X Plano de Contas Empresa e esteja gerando a versão 5.00 do Leiaute, será demonstrada uma mensagem no log: “A partir da versão 5.00 do leiaute não serão válidas as Contas Referenciais de entidade 00-SUSEP ou 20- Banco Central do Brasil (COSIF)”. | MFS8620 MFS10727 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNI053-04 | Registro I053 – Campo 04 – NAT_SUB_CNT  Será gerado com o conteúdo do campo Natureza da Subconta da tela de Subconta Correlata.  Não deverão ser considerados os códigos de Natureza da Subconta que estejam fora do período de validade na TACES90. | MFS-8216 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNJ800-02 | Registro J800 – Campo 02 – TIPO_DOC  Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.  Será gerado o código conforme opção selecionada pelo usuário no campo “Tipo de documento” na Aba Demonstrações Contábeis dos Dados Iniciais (menu Parâmetros) - quadro ‘Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)’, conforme opções a seguir:  001: Demonstração do Resultado Abrangente do Período  002: Demonstração dos Fluxos de Caixa  003: Demonstração do Valor Adicionado  010: Notas Explicativas  011: Relatório da Administração  012: Parecer dos Auditores  099: Outros | MFS-8620 MFS-9689 |
| RNJ800-03 | Registro J800 – Campo 03 – DESC_RTF  Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.  Será gerado com o conteúdo do campo Descrição (.rtf) da tela de Dados iniciais/Aba Demonstrações Contábeis - Quadro (Outras Informações das Demonstrações Contábeis (Balanço Patrimonial e Demonstração de Resultado)). | MFS-8620 MFS-9689 |
| RNJ800-04 | Registro J800 – Campo 04 – HASH_RTF  Este campo existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.  Será gerado sem informação (em branco). Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo. | MFS-8620 MFS-9689 |
|  |  |  |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNJ801-00 | Registro J801 – Regra Geral  Este registro existe a partir da versão 5.00, porém ele deve ser gerado para todas as versões.  Origem das informações: Tela de Dados Iniciais – Aba Demonstrações Contábeis (Módulo ECD / Menu Parâmetros > Dados Iniciais)  Regra de Seleção: Este registro será gerado sempre que no quadro ‘Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)’ na aba Demonstrações Contábeis da tela de Dados Iniciais existir informação de um arquivo RTF.  Campo-chave: ARQ_RTF  Registro pai / Nível hierárquico: J005 / Nível 3  Ocorrência: Um por arquivo | MFS-8620 MFS-9689 |
| RNJ801-01 | Registro J801 – Campo 01 – REG  Informação fixa “J801”. | MFS-8620 |
| RNJ801-02 | Registro J801 – Campo 02 – TIPO_DOC  Nesse registro será gerado o tipo de documento que no caso será 001: Termo de Substituição da ECD.  Valor fixo: 001.  O quadro ‘Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)’ foi criado justamente para o usuário informar o arquivo de formato RTF que corresponde apenas ao tipo de documento: Termo de Substituição da ECD. | MFS-8620 |
| RNJ801-03 | Registro J801 – Campo 03 – DESC_RTF  Será gerado com o conteúdo do campo Descrição (.rtf) da tela de Dados iniciais/Aba Demonstrações Contábeis - Quadro (Termo de Verificação para Fins de Substituição da ECD (Balanço Patrimonial e Demonstração de Resultado)). | MFS-8620 |
| RNJ801-04 | Registro J801 – Campo 04 – HASH_RTF  Será gerado sem informação (em branco). Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo. | MFS-8620 |
| RNJ801-05 | Registro J801 – Campo 05 – ARQ_RTF  Será gerada uma sequência de bytes que representem um único arquivo no formato RTF (Rich Text Format). | MFS-8620 |
| RNJ801-06 | Registro J801 – Campo 06 – IND_FIM_RTF  Informação fixa “J801FIM”. | MFS-8620 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNJ930-03 | Registro J930 – Campo 03 – IDENT_CPF_CNPJ  Consultar DE-PARA: DE-PARA _SPED Contábil_Conf.IN RFB nº 926.09.xls.  Tratamento: Se o campo NUM_CPF da tabela RESP_INFORMACAO não estiver preenchido, será verificada a existência do CNPJ no campo NUM_CPF da tabela RESP_CONTADOR, ambos localizados em Básicos > Parâmetros > Requisitos Legais > Responsável pelas informações. | CH8476_2017 (MFS-10940) |
| RNJ930-12 | Registro J930 – Campo 12 – IND_RESP_LEGAL  Este campo existe a partir da versão 5.00, porém ele dever ser gerado para todas as versões.  Será gerado conforme parâmetro “Indicação do Representante Legal Junto às Bases da RFB” na Aba Signatários dos Dados Iniciais (menu Parâmetros): Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”. Se o parâmetro estiver selecionado, será gerado com conteúdo “S”. | MFS-8216 MFS-9689 |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNK001 | Registro K001 – Abertura do Bloco K  A princípio não atenderemos a geração do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K.  Registro abertura: K001 | MFS8216 MFS-10358 |
| RNK001-01 | Registro K001 – Campo 1 – REG  Informação fixa “K001”. | MFS9809 |
| RNK001-02 | Registro K001 – Campo 2 – IND_DAD  Indicador de movimento:  Bloco com dados informados;  Bloco sem dados informados.  Gravar a informação de acordo com os dados encontrados para esse bloco se houver dados informados gravar = 0 - Bloco com dados informados, se não encontrar dados gravar = 1 - Bloco sem dados informados.  Informação fixa “1”.  Obs.: Como a princípio não atenderemos a geração do Bloco K, o conteúdo deste campo será fixo igual a “1” (Bloco sem dados informados). | MFS9809 MFS-10358 |
| RNK030-00 | Registro K030 – Regra geral  Origem da Informação: SAFX240 - Relação das Empresas Consolidadas.  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K030 será gerada conforme definida neste documento.  Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K030 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K030 – Período da Escrituração Contábil Consolidada”.   parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais (menu Parâmetros)  Campo-chave: DT_INI   Registro pai / Nível hierárquico: K030 / Nível 2  Ocorrência: Um por arquivo. | MFS-10358 |
| RNK030-01 | Registro K030 – Campo 1 – REG  Informação fixa “K030”. | MFS-10358 |
| RNK030-02 | Registro K030 – Campo 2 – DT_INI  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Inicial do período consolidado. | MFS-10358 |
| RNK030-03 | Registro K030 – Campo 3 – DT_FIN  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final do período consolidado. | MFS-10358 |
| RNK100-00 | Registro K100 – Regra geral  Origem da Informação: SAFX240 - Relação das Empresas Consolidadas.  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K100 será gerada conforme definida neste documento.   Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K100 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K100 – Relação das Empresas Consolidadas”.  Campo-chave: EMP_COD  Registro pai / Nível hierárquico: K100 / Nível 3  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK100-01 | Registro K100 – Campo 1 – REG  Informação fixa “K100”. | MFS-10358 |
| RNK100-02 | Registro K100 – Campo 2 – COD_PAIS  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código do País. | MFS-10358 |
| RNK100-03 | Registro K100 – Campo 3 – EMP_COD  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa Participante. | MFS-10358 |
| RNK100-04 | Registro K100 – Campo 4 – CNPJ  Considerando a Origem da Informação, demonstrar aqui APENAS os primeiros 8 dígitos do conteúdo informado no campo CNPJ da Empresa Participante. | MFS-10358 |
| RNK100-05 | Registro K100 – Campo 5 – NOME  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nome da Empresa Participante. | MFS-10358 |
| RNK100-06 | Registro K100 – Campo 6 – PER_PART  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Participação Total. | MFS-10358 |
| RNK100-07 | Registro K100 – Campo 7 – EVENTO  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Ocorrido no Período. | MFS-10358 |
| RNK100-08 | Registro K100 – Campo 8 – PER_CONS  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Consolidação no Final Período. | MFS-10358 |
| RNK100-09 | Registro K100 – Campo 9 – DATA_INI_EMP  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Início da Consolidação. | MFS-10358 |
| RNK100-10 | Registro K100 – Campo 10 – DATA_FIN_EMP  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final da Consolidação. | MFS-10358 |
| RNK110-00 | Registro K110 – Regra geral  Origem da Informação: SAFX241 - Relação dos Eventos Societários / Empresas Participantes do Evento.  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K110 será gerada conforme definida neste documento. Este registro é filho do K100.   Este registro é filho do K100. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado.   Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K110 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K110 – Relação dos Eventos Societários”.   Campo-chave: Nenhum   Registro pai / Nível hierárquico: K110 / Nível 4  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK110-01 | Registro K110 – Campo 1 – REG  Informação fixa “K110”. | MFS-10358 |
| RNK110-02 | Registro K110 – Campo 2 – EVENTO  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Societário ocorrido no período. | MFS-10358 |
| RNK110-03 | Registro K110 – Campo 3 – DT_EVENTO  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data do Evento Societário. | MFS-10358 |
| RNK115-00 | Registro K115 – Regra geral  Origem da Informação: SAFX241 - Relação dos Eventos Societários / Empresas Participantes do Evento.  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K115 será gerada conforme definida neste documento.  Campo-chave: Nenhum  Registro pai / Nível hierárquico: K115 / Nível 5  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK115-01 | Registro K115 – Campo 1 – REG  Informação fixa “K115”. | MFS-10358 |
| RNK115-02 | Registro K115 – Campo 2 – EMP_COD_PART  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa envolvida na operação. | MFS-10358 |
| RNK115-03 | Registro K115 – Campo 3 – COND_PART  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Condição da empresa relacionada à operação. | MFS-10358 |
| RNK115-04 | Registro K115 – Campo 4 – PER_EVT  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual da empresa participante envolvido na operação. | MFS-10358 |
| RNK200-00 | Registro K200 – Regra geral  Origem da Informação: SAFX2002 – Tabela de Plano de Contas  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K200 será gerada conforme definida neste documento.   Serão consideradas as contas contábeis utilizadas nas escriturações contábeis consolidadas (campo IND_CONTA_CONSOLID = S da SAFX2002) que possuam movimento (SAFX242) no período de consolidação do K030 (SAFX240).  Para a geração do Plano de Contas Consolidado, as informações serão recuperadas da tela de Plano de Contas (menu: Manutenção >> Códigos >> Plano de Contas) do módulo Mastersaf DW.  Para este cenário, deve ser gerado no arquivo as informações do cadastro das contas sintéticas (campo COD_CONTA_SINT da SAFX2002) associada à conta movimentada encontrada (SAFX242) e também o cadastro de todas as outras contas vinculadas, de nível superior, de forma que tenhamos o plano completo.  Exemplo: No movimento (SAFX242) temos a conta: 0001.0001.0001.0001, que no cadastro tem:   Neste exemplo, apenas a conta 0001.0001.0001.0001 foi movimentada, porém, no arquivo gerado devem ser demonstradas informações das contas "0001.0001.0001.0001", "0001.0001.0001", "0001.0001" e "0001".  Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K200 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K200 – Plano de Contas Consolidado”.  Campo-chave: COD_CTA  Registro pai / Nível hierárquico: K200 / Nível 2  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK200-01 | Registro K200 – Campo 1 – REG  Informação fixa “K200”. | MFS-10358 |
| RNK200-02 | Registro K200 – Campo 2 – COD_NAT  Considerando a Origem da Informação, demonstrar aqui o conteúdo de acordo com campo Indicador de Natureza conforme abaixo:  Indicador de Natureza:  Se informado ‘0. Compensação’, gravar ‘05’; Se informado ‘1. Ativo’, gravar ‘01’; Se informado ‘2. Passivo’, gravar ‘02’; Se informado ‘3. Despesa’, gravar ‘04’; Se informado ‘4. Receita’, gravar ‘04’; Se informado ‘5. Mutações Ativas ("Variações Patrimoniais" anuais)’, gravar ‘09’; Se informado ‘6. Mutações Passivas ("Variações Patrimoniais" anuais)’, gravar ‘09’;                                                                                                                                                                                                           Se informado ‘7. Patrimônio Líquido’, gravar ‘03’;                                                                                                                                                                                      Se informado ‘8. Custo’, gravar ‘04’; Se informado ‘9. Outros’, gravar ‘09’. | MFS-10358 |
| RNK200-03 | Registro K200 – Campo 3 – IND_CTA  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador de Conta. | MFS-10358 |
| RNK200-04 | Registro K200 – Campo 4 – NIVEL  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nível. | MFS-10358 |
| RNK200-05 | Registro K200 – Campo 5 – COD_CTA  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta. | MFS-10358 |
| RNK200-06 | Registro K200 – Campo 6 – COD_CTA_SUP  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código de Conta Sintética. | MFS-10358 |
| RNK200-07 | Registro K200 – Campo 7 – CTA  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Descrição da Conta. | MFS-10358 |
| RNK210-00 | Registro K210 – Regra geral  Origem da Informação: Manutenção - Mapeamento para Planos de Contas das Empresas Consolidadas  Localizaçao: Menu SPED,  Módulo: ECD - Escrituração Contábil Digital, item de menu Manutenção  Bloco K  Mapeamento para Planos de Contas das Empresas Consolidadas  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K210 será gerada conforme definida neste documento.   Campo-chave: COD_EMP, COD_CTA_EMP  Registro pai / Nível hierárquico: K210 / Nível 4  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK210-01 | Registro K210 – Campo 1 – REG  Informação fixa “K210”. | MFS-10358 |
| RNK210-02 | Registro K210 – Campo 2 – COD_EMP  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código/Nome da Empresa Participante. | MFS-10358 |
| RNK210-03 | Registro K210 – Campo 3 – COD_CTA_EMP  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta da Empresa Participante. | MFS-10358 |
| RNK300-00 | Registro K300 – Regra geral  Origem da Informação: SAFX242 - Saldos das Contas Consolidadas.  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K300 será gerada conforme definida neste documento.  Serão considerados apenas os saldos das contas consolidadas que pertençam ao período de consolidação informado no K030 (SAFX240).  Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K300 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K300 – Saldos das Contas Consolidadas”.   Campo-chave: COD_CTA  Registro pai / Nível hierárquico: K300 / Nível 3.  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK300-01 | Registro K300 – Campo 1 – REG  Informação fixa “K300”. | MFS-10358 |
| RNK300-02 | Registro K300 – Campo 2 – COD_CTA  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada. | MFS-10358 |
| RNK300-03 | Registro K300 – Campo 3 – VAL_AG  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto aglutinado. | MFS-10358 |
| RNK300-04 | Registro K300 – Campo 4 – IND_VAL_AG  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor aglutinado. | MFS-10358 |
| RNK300-05 | Registro K300 – Campo 5 – VAL_EL  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto das eliminações. | MFS-10358 |
| RNK300-06 | Registro K300 – Campo 6 – IND_VAL_EL  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado. | MFS-10358 |
| RNK300-07 | Registro K300 – Campo 7 – VAL_CS  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto consolidado. | MFS-10358 |
| RNK300-08 | Registro K300 – Campo 8 – IND_VAL_CS   Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor consolidado. | MFS-10358 |
| RNK310-00 | Registro K310 – Regra geral  Origem da Informação: SAFX243 - Empresas Detentoras das Parcelas do Valor Eliminado Total.  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K310 será gerada conforme definida neste documento.  Este registro é filho do K300. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado.  Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K310 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K310 – Empresas Detentoras das Parcelas do Valor Eliminado Total”.  Campo-chave: EMP_COD_PARTE   Registro pai / Nível hierárquico: K310 / Nível 4.  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK310-01 | Registro K310 – Campo 1 – REG  Informação fixa “K310”. | MFS-10358 |
| RNK310-02 | Registro K310 – Campo 2 – EMP_COD_PARTE  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa detentora do valor aglutinado que foi eliminado. | MFS-10358 |
| RNK310-03 | Registro K310 – Campo 3 – VALOR  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela do valor eliminado total. | MFS-10358 |
| RNK310-04 | Registro K310 – Campo 4 – IND_VALOR  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado. | MFS-10358 |
| RNK315-00 | Registro K315 – Regra geral  Origem da Informação: SAFX244 - Empresas Contrapartes das Parcelas do Valor Eliminado Total.  Regra de geração: Quando a empresa tem escriturações contábeis consolidadas (Parâmetro “Escriturações Contábeis Consolidadas” selecionado na tela de Dados Iniciais – menu Parâmetros) e a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5.00”, a estrutura do registro K315 será gerada conforme definida neste documento.  Como este registro é de geração facultativa, pode ocorrer do usuário não tê-lo selecionado no Perfil (menu Parâmetros >> Perfil). Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K315 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K315 – Empresas Contrapartes das Parcelas do Valor Eliminado Total”.   Campo-chave: EMP_COD_CONTRA, COD_CONTRA  Registro pai / Nível hierárquico: K315 / Nível 5.  Ocorrência: Vários por arquivo. | MFS-10358 |
| RNK315-01 | Registro K315 – Campo 1 – REG  Informação fixa “K315”. | MFS-10358 |
| RNK315-02 | Registro K315 – Campo 2 – EMP_COD_CONTRA  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa da contrapartida. | MFS-10358 |
| RNK315-03 | Registro K315 – Campo 3 – COD_CONTRA  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada da contrapartida. | MFS-10358 |
| RNK315-04 | Registro K315 – Campo 4 – VALOR  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela da contrapartida do valor eliminado total. | MFS-10358 |
| RNK315-05 | Registro K315 – Campo 5 – IND_VALOR  Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado. | MFS-10358 |
| RNK990 | Registro K990 – Encerramento do Bloco K  A princípio não atenderemos a geração do Bloco K - Conglomerados Econômicos (Facultativo para o ano-calendário 2016), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K.  Registro encerramento: K990 | MFS8216 MFS-10358 |
| RNK990-01 | Registro K990 – Campo 1 – REG  Informação fixa “K990”. | MFS9809 |
| RNK990-02 | Registro K990 – Campo 2 –QTD_LIN_K   Será preenchido com o total de linhas do bloco K. | MFS9809 |
|  |  |  |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
