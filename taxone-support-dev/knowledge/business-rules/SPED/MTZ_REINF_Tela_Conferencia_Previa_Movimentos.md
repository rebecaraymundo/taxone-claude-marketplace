# MTZ_REINF_Tela_Conferencia_Previa_Movimentos

> Fonte: MTZ_REINF_Tela_Conferencia_Previa_Movimentos.docx






THOMSON REUTERS

Conferência Prévia dos Movimentos
SPED – Reinf



DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	4

## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: REINF >> Conferência Prévia >> Movimentos

Título da tela: Conferência Prévia dos Eventos

Obs: Ao abrir a tela de conferência deverá abrir uma subtela para seleção do período de geração.





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS8958 | Elenilson Coutinho | Inclusão na Tela de Conferência Prévia s Evento (R-2010) do EFD – Reinf |
| MFS8959 | Elenilson Coutinho | Inclusão na Tela de Conferência Prévia s Evento (R-2020) do EFD – Reinf |
| MFS9074 | Elenilson Coutinho | Inclusão na Tela de Conferência Prévia s Evento (R-2060) do EFD – Reinf |
| MFS9901 | Elenilson Coutinho | Inclusão na Tela de Conferência Prévia s Evento (R-2070) do EFD – Reinf |
| MFS10357 | Elenilson Coutinho | Alteração na Tela de Conferência Prévia dos Eventos (R-2010) do EFD – Reinf |
| MFS10414 | Elenilson Coutinho | Alteração na Tela de Conferência Prévia dos Eventos (R-2020) do EFD – Reinf |
| MFS10589 | Elenilson Coutinho | Inclusão de Campo na Tela de Conferência Prévia dos Eventos (R-2020) do EFD – Reinf |
| MFS10415 | Elenilson Coutinho | Inclusão de Campo na Tela de Conferência Prévia dos Eventos (R-2070) do EFD – Reinf |
| MFS9073 | Elenilson Coutinho | Inclusão na Tela de Conferência Prévia s Evento (R-2050) do EFD – Reinf |
| MFS11487 | Elenilson Coutinho | Inclusão da aba “Ocorrencia” evento (R-2010) do EFD Reinf |
| MFS11398 | Elenilson Coutinho | Inclusão da aba “Ocorrencia” evento (R-2020) do EFD Reinf |
| MFS11400 | Elenilson Coutinho | Inclusão da aba “Ocorrencia” evento (R-2060) do EFD Reinf |
| MFS11399 | Elenilson Coutinho | Inclusão da aba “Ocorrencia” evento (R-2070) do EFD Reinf |
| MFS11670 | Elenilson Coutinho | Inclusão na Tela de Conferência Prévia s Evento (R-2040) do EFD – Reinf |
| MFS11892 | Elenilson Coutinho | Alteração evento R-2070 – Layout V 1.1 |
| MFS13362 | Lara Aline | Alteração na posição dos quadros: O quadro “Identificador do Prestador de Serviços” passou para o segundo nível com somente a informação do CNPJ do Prestador. Todos os valores foram passados para o quadro de “Ocorrências”. (R-2010). E exclusão dos campos. |
| MFS13631 | Lara Aline | Alteração na posição dos quadros: O quadro “Identificador doTomador de Serviços” passou para o segundo nível com somente a informação do tipo, numero de inscrição. Todos os valores foram passados para o quadro de “Ocorrências”. (R-2020). E exclusão dos campos |
| MFS13861 | Lara Aline | Alteração evento R-2040 – Layout V 1.2 |
| MFS13897 | Lara Aline | Alteração evento R-2050 – Layout V 1.2 |
| MFS14002 | Lara Aline | Alteração evento R-2060 – Layout V 1.2 |
| MFS14462 | Lara Aline | Inclusão do campo Versão |
| MFS17628 | Vânia Mattos | Inclusão de novas abas (“Totais R-5001”) para exibir os valores calculados pelo Fisco (informações enviadas pelo Fisco através do evento R-5001) |
| MFS20732 | Lara Aline | Inclusão do campo “Data Fiscal” na aba Notas Fiscais de Serviços |
| MFS20930 | Lara Aline | Exclusão do evento R-2070 e ajuste na numeração dos campos do R-5001 – Conforme Layout 1.4 |
| MFS-58345 | Alessandra Cristina Navatta | Reestruturação do Menu |
| MFS-58348 | Alessandra Cristina Navatta | Inclusão do Evento R-2055 |
| MFS-69588 | Alessandra Cristina Navatta | Mudança do nome do quadro de estabelecimento do evento R-2060 de ‘Identificação do Estabelecimento de Comercialização da Produção’ para ‘Identificação do Estabelecimento que Auferiu a Receita Bruta’ |
| MFS-79878 | Alessandra Cristina Navatta | Exclusão do campo Retificação S-1250, a partir da versão 2.1 do REINF. |
| MFS-79885 | Alessandra Cristina Navatta | Inclusão do evento R-4010 para atendimento à versão 2.1. do REINF. |
| MFS-79893 | Alessandra Cristina Navatta | Inclusão do evento R-4040 para atendimento à versão 2.1. do REINF. |
| MFS-79907 | Alessandra Cristina Navatta | Inclusão do evento R-4080 para atendimento à versão 2.1. do REINF. |
| MFS-90863 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1.   Não há regras a serem ajustada neste arquivo. |
| MFS-79890 | Alessandra Cristina Navatta | Inclusão do evento R-4020 para atendimento à versão 2.1.1 do REINF. |
| MFS-79960 | Alessandra Cristina Navatta | Exclusão das abas (“Totais R-5001”) para exibir os valores calculados pelo Fisco (informações enviadas pelo Fisco através do evento R-5001), a partir da versão 2.1.1, para a família 2000 (Eventos R-2010, R-2020, R-2040, R-2050, R-2055 e R-2060). Não faz sentido ter essas informações na conferência prévia, uma vez que se referem ao retorno do fisco (informação gerada posteriormente). Essas informações serão disponibilizadas em relatório. |
| MFS-535745 | Alessandra Cristina Navatta | Inclusão dos campos ideEvtAdic (no agrupamento Ocorrência/Identificação do Beneficiário), e dos campos dtEscrCont, observ no agrupamento (Informações Relativas ao Rendimento) no evento R-4010, a partir da versão 2.1.2. |
| MFS-537195 | Alessandra Cristina Navatta | Inclusão dos campos ideEvtAdic (no agrupamento Ocorrência/Identificação do Beneficiário do Rendimento), e dos campos dtEscrCont, observ no agrupamento (Informações Relativas ao Pagamento), no evento R-4020, a partir da versão 2.1.2. |
| MFS-549365 | Alessandra Cristina Navatta | Mudança de domínio no campo Tipo de Isenção.  Atendimento ao layout 2.1.2 |
| MFS-537211 | Alessandra Cristina Navatta | Inclusão dos campos ideEvtAdic (no agrupamento Ocorrência/Identificação do Estabelecimento), e do campo dtEscrCont, no agrupamento (Informações do Pagamento a Beneficiários não Identificados) no evento R-4040, a partir da versão 2.1.2. |
| MFS-537238 | Alessandra Cristina Navatta | Inclusão do campo Observ (no agrupamento Informações Relativas ao Recebimento do Rendimento), no evento R-4080, a partir da versão 2.1.2 |
| MFS-566870 | Alessandra Cristina Navatta | Ajustes referente a nota técnica 03/2023, conforme INFOLEGIS 1740/23 - Z - 084 - EFD REINF_NT 03/2023 - DW/T1  Alterações nos campos do evento R-4010: Tipo Dedução - inclusão do tipo de dedução “8 – Desconto simplificado mensal” nos agrupamentos ‘Informações Relativas às Deduções do Rendimento Tributável’ (tag detDed) e ’Detalhamento das Deduções Suspensas’ (tag dedSusp). |
| MFS-805178 | Alessandra Cristina Navatta | Ajustes referente a nota técnica 01/2025, conforme INFOLEGIS 1740/25 - Z - 104 - EFD REINF_NT 01/2025 - DW/T1 Inclusão da opção 3 – Sem Processo no campo Tipo de Processo (tag infoRRA), do evento  R-4010 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | TextBox | S | N |  | Irá demonstrar o estabelecimento selecionado na chamada da subtela de seleção. | MFS-8958 |
| Período (MM/AAAA) | Texto | S | N |  |  | MFS-8958 |
| Versão | TextBox | S | N |  | Irá demostrar a versão de Leiaute da EFD-REINF | MFS-14462 |
| Eventos-Reinf | Pasta |  |  |  |  | MFS-8958 |
| R-2010 – Retenção Contribuição Previdenciária – Prestadores Serviços | R-2010 – Retenção Contribuição Previdenciária – Prestadores Serviços | R-2010 – Retenção Contribuição Previdenciária – Prestadores Serviços | R-2010 – Retenção Contribuição Previdenciária – Prestadores Serviços | R-2010 – Retenção Contribuição Previdenciária – Prestadores Serviços | R-2010 – Retenção Contribuição Previdenciária – Prestadores Serviços | R-2010 – Retenção Contribuição Previdenciária – Prestadores Serviços |
| Identificação do Estabelecimento / Obra Contratante de Serviços | Identificação do Estabelecimento / Obra Contratante de Serviços | Identificação do Estabelecimento / Obra Contratante de Serviços | Identificação do Estabelecimento / Obra Contratante de Serviços | Identificação do Estabelecimento / Obra Contratante de Serviços | Identificação do Estabelecimento / Obra Contratante de Serviços | Identificação do Estabelecimento / Obra Contratante de Serviços |
| Tipo de Inscrição | Textbox | S | N |  | Irá demonstrar o tipo de inscrição do estabelecimento tomador de serviços.  1-CNPJ 4-CNO | MFS-8958 |
| Número de Inscrição | Textbox | S | N |  | Irá demonstrar o número de inscrição do estabelecimento tomador de serviços, CNPJ ou CNO. | MFS-8958 |
| Identificação do Prestador dos Serviços | Identificação do Prestador dos Serviços | Identificação do Prestador dos Serviços | Identificação do Prestador dos Serviços | Identificação do Prestador dos Serviços | Identificação do Prestador dos Serviços | Identificação do Prestador dos Serviços |
| CNPJ do Prestador de Serviços | Textbox | S | N |  | . | MFS-8958 |
| Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências | Ocorrências |
| Data Ocorrência | Textbox | S | N |  |  | MFS-11487 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-11487 |
| Indicador de Obra | Textbox | S | N |  | Irá demonstrar o indicador de preatação de serviço em obra  Não é obra de construção civil ou não está sujeita a matrícula  Obrad de construção civil empreitada Total   Obra de construção civil Empreitada Parcial | MFS-11487 |
| Situação | Textbox | S | N |  |  | MFS-11487 |
| Valor Total Bruto | Textbox | S | N |  |  | MFS-8958 |
| Valor Total da Base de Cálculo da Retenção do INSS | Textbox | S | N |  |  | MFS-8958 |
| Valor Total da Retenção Principal | Textbox | S | N |  |  | MFS-8958 |
| Valor Total da Retenção Adicional | Textbox | S | N |  |  | MFS-8958 |
| Valor Total da Retenção Principal Não Efetuada ou Depositada em Juízo da Decisão Judicial | Textbox | S | N |  |  | MFS-8958 |
| Valor Total da Retenção Adicional Não Efetuada ou Depositada em Juízo da Decisão Judicial | Textbox | S | N |  |  | MFS-8958 |
| Código da Conta Analítica | Textbox | S | N |  |  | MFS-8958 MFS13362 |
| Indicador CPRB | Textbox | S | N |  | Irá demonstrar o indicador do prestador de serviço quanto a incidência da CPRB.  0 - Não é serviço ou CNAE sujeito a incidência da Contribuição Previdenciária sobre a Receita Bruta(CPRB) - Retenção 11%;  1 – Serviço ou CNAE sujeito a incidência da Contribuição Previdenciária sobre a Receita Bruta(CPRB) - Retenção 3,5%; | MFS10357 |
| Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços |
| Número Documento | Textbox | S | N |  |  | MFS-8958 |
| Série | Textbox | S | N |  |  | MFS-8958 |
| Data Emissão da Nota Fiscal | Textbox | S | N |  |  | MFS-8958 |
| Data Fiscal | Textbox | S | N |  |  | MFS20732 |
| Valor Bruto | Textbox | S | N |  |  | MFS-8958 |
| Observação | Textbox | S | N |  |  | MFS-8958 |
| Informações de Tipo de Serviços | Informações de Tipo de Serviços | Informações de Tipo de Serviços | Informações de Tipo de Serviços | Informações de Tipo de Serviços | Informações de Tipo de Serviços | Informações de Tipo de Serviços |
| Tipo de Serviço | Textbox | S | N |  |  | MFS10357 |
| Código da Atividade Econômica | Textbox | S | N |  |  | MFS10357 MFS13362 |
| Valor Material ou Equipamento | Textbox | S | N |  |  | MFS-8958 MFS13362 |
| Valor Dedução Alimentação | Textbox | S | N |  |  | MFS-8958 MFS13362 |
| Valor Dedução Transporte | Textbox | S | N |  |  | MFS-8958 MFS13362 |
| Valor Base de Cálculo da Retenção do INSS | Textbox | S | N |  |  | MFS-8958 |
| Valor da Retenção do INSS | Textbox | S | N |  |  | MFS-8958 |
| Valor da Retenção da Subcontratada | Textbox | S | N |  |  | MFS-8958 |
| Valor da Retenção Principal Não Efetuada ou Depositada em Juízo da Decisão Judicial/Administrativa | Textbox | S | N |  |  | MFS-8958 |
| Valor dos Serviços/Aposentadoria Especial - 15 anos | Textbox | S | N |  |  | MFS-8958 |
| Valor dos Serviços/Aposentadoria Especial - 20 anos | Textbox | S | N |  |  | MFS-8958 |
| Valor dos Serviços/Aposentadoria Especial - 25 anos | Textbox | S | N |  |  | MFS-8958 |
| Valor da Retenção Adicional | Textbox | S | N |  |  | MFS-8958 |
| Valor da Retenção Adicional Não Efetuada ou Depositada em Juízo da Decisão Judicial/Administrativa | Textbox | S | N |  |  | MFS-8958 |
| Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal |
| Tipo do Processo Retenção Principal | Textbox | S | N |  | Irá demonstrar o tipo do processo retenção principal.  Administrativo do Tomador Judicial do Tomador Judicial do Prestador | MFS10357 |
| Número do Processo Retenção Principal | Textbox | S | N |  |  | MFS10357 |
| Código da Suspensão Principal | Textbox | S | N |  |  | MFS10357 |
| Valor Retenção Principal | Textbox | S | N |  |  | MFS10357 |
| Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional |
| Tipo do Processo Retenção Adicional | Textbox | S | N |  | Irá demonstrar o tipo do processo retenção adicional.  Administrativo do Tomador Judicial do Tomador Judicial do Prestador | MFS10357 |
| Número do Processo Retenção Adicional | Textbox | S | N |  |  | MFS10357 |
| Código da Suspensão Adicional | Textbox | S | N |  |  | MFS10357 |
| Valor Retenção Adicional | Textbox | S | N |  |  | MFS10357 |
| Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidas informações geradas pelo Fisco via evento R-5001 (evento enviado pelo Fisco no ato do recebimento do evento R-2010). Estas informações só existirão no caso dos eventos R-2010 já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  Informações exibidas:  1-Valor total da base de cálculo da retenção do evento (ocorrência única). Trata-se do campo “32-vlrTotalBaseRet” do evento R-5001;  2-Valores calculados por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “infoCRTom” do R-5001; | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidas informações geradas pelo Fisco via evento R-5001 (evento enviado pelo Fisco no ato do recebimento do evento R-2010). Estas informações só existirão no caso dos eventos R-2010 já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  Informações exibidas:  1-Valor total da base de cálculo da retenção do evento (ocorrência única). Trata-se do campo “32-vlrTotalBaseRet” do evento R-5001;  2-Valores calculados por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “infoCRTom” do R-5001; | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidas informações geradas pelo Fisco via evento R-5001 (evento enviado pelo Fisco no ato do recebimento do evento R-2010). Estas informações só existirão no caso dos eventos R-2010 já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  Informações exibidas:  1-Valor total da base de cálculo da retenção do evento (ocorrência única). Trata-se do campo “32-vlrTotalBaseRet” do evento R-5001;  2-Valores calculados por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “infoCRTom” do R-5001; | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidas informações geradas pelo Fisco via evento R-5001 (evento enviado pelo Fisco no ato do recebimento do evento R-2010). Estas informações só existirão no caso dos eventos R-2010 já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  Informações exibidas:  1-Valor total da base de cálculo da retenção do evento (ocorrência única). Trata-se do campo “32-vlrTotalBaseRet” do evento R-5001;  2-Valores calculados por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “infoCRTom” do R-5001; | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidas informações geradas pelo Fisco via evento R-5001 (evento enviado pelo Fisco no ato do recebimento do evento R-2010). Estas informações só existirão no caso dos eventos R-2010 já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  Informações exibidas:  1-Valor total da base de cálculo da retenção do evento (ocorrência única). Trata-se do campo “32-vlrTotalBaseRet” do evento R-5001;  2-Valores calculados por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “infoCRTom” do R-5001; | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidas informações geradas pelo Fisco via evento R-5001 (evento enviado pelo Fisco no ato do recebimento do evento R-2010). Estas informações só existirão no caso dos eventos R-2010 já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  Informações exibidas:  1-Valor total da base de cálculo da retenção do evento (ocorrência única). Trata-se do campo “32-vlrTotalBaseRet” do evento R-5001;  2-Valores calculados por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “infoCRTom” do R-5001; | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidas informações geradas pelo Fisco via evento R-5001 (evento enviado pelo Fisco no ato do recebimento do evento R-2010). Estas informações só existirão no caso dos eventos R-2010 já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource.  Informações exibidas:  1-Valor total da base de cálculo da retenção do evento (ocorrência única). Trata-se do campo “32-vlrTotalBaseRet” do evento R-5001;  2-Valores calculados por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “infoCRTom” do R-5001; |
| Total Base de Cálculo da Retenção | Numérico | N | N |  | Conteúdo campo “32-vlrTotalBaseRet” do evento R-5001 referente ao R-2010 em questão | MFS17628 MFS20930 |
| Código de Receita | Alfanumérico | N | N | Formato: 9999-99 | Conteúdo do campo “34-CRTom” do evento R-5001 referente ao R-2010 em questão. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária | Numérico | N | N |  | Conteúdo do campo “35-vlrCRTom” do evento R-5001 referente ao R-2010 em questão. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária Exigibilidade Suspensa | Numérico | N | N |  | Conteúdo campo “36-vlrCRTomSusp” do evento R-5001 referente ao R-2010 em questão. | MFS17628 MFS20930 |


| R-2020 – Retenção Contribuição Previdenciária – Tomadores de Serviços | R-2020 – Retenção Contribuição Previdenciária – Tomadores de Serviços | R-2020 – Retenção Contribuição Previdenciária – Tomadores de Serviços | R-2020 – Retenção Contribuição Previdenciária – Tomadores de Serviços | R-2020 – Retenção Contribuição Previdenciária – Tomadores de Serviços | R-2020 – Retenção Contribuição Previdenciária – Tomadores de Serviços | R-2020 – Retenção Contribuição Previdenciária – Tomadores de Serviços |
| --- | --- | --- | --- | --- | --- | --- |
| Identificação do Estabelecimento / Prestador de Serviços | Identificação do Estabelecimento / Prestador de Serviços | Identificação do Estabelecimento / Prestador de Serviços | Identificação do Estabelecimento / Prestador de Serviços | Identificação do Estabelecimento / Prestador de Serviços | Identificação do Estabelecimento / Prestador de Serviços | Identificação do Estabelecimento / Prestador de Serviços |
| Tipo de Inscrição | Textbox | S | N |  | Irá demonstrar o tipo de inscrição do estabelecimento prestador de serviços.  1-CNPJ | MFS-8959 |
| Número de Inscrição | Textbox | S | N |  |  | MFS-8959 |
| Identificação do Tomador de Serviço | Identificação do Tomador de Serviço | Identificação do Tomador de Serviço | Identificação do Tomador de Serviço | Identificação do Tomador de Serviço | Identificação do Tomador de Serviço | Identificação do Tomador de Serviço |
| Tipo Inscrição do Tomador | Textbox | S | N |  |  | MFS-8959 |
| Número Inscrição Tomador | Textbox | S | N |  |  | MFS-8959 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data Ocorrência | Textbox | S | N |  |  | MFS-11398 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-11398 |
| Situação | Textbox | S | N |  |  | MFS-11398 |
| Indicador de Obra | Textbox | S | N |  |  | MFS-8959 |


| Valor Total Bruto | Textbox | S | N |  |  | MFS-8959 |
| --- | --- | --- | --- | --- | --- | --- |
| Valor Total da Base de Cálculo da Retenção do INSS | Textbox | S | N |  |  | MFS-8959 |
| Valor Total da Retenção Principal | Textbox | S | N |  |  | MFS-8959 |
| Valor Total da Retenção Adicional | Textbox | S | N |  |  | MFS-8959 |
| Valor Total da Retenção Principal Não Efetuada ou Depositada em Juízo da Decisão Judicial | Textbox | S | N |  |  | MFS-8959 |
| Valor Total da Retenção Adicional Não Efetuada ou Depositada em Juízo da Decisão Judicial | Textbox | S | N |  |  | MFS-8959 |
| Código da Conta Analítica | Textbox | S | N |  |  | MFS-8959 MFS13631 |
| Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços | Notas Fiscais de Serviços |
| Série | Textbox | S | N |  |  | MFS-8959 |
| Número Documento | Textbox | S | N |  |  | MFS-8959 |
| Data Emissão da Nota Fiscal | Textbox | S | N |  |  | MFS-8959 |
| Data Fiscal | Textbox | S | N |  |  | MFS20732 |
| Valor Bruto | Textbox | S | N |  |  | MFS-8959 |
| Observação | Textbox | S | N |  |  | MFS-8959 |
| Informação do Tipo de Serviço | Informação do Tipo de Serviço | Informação do Tipo de Serviço | Informação do Tipo de Serviço | Informação do Tipo de Serviço | Informação do Tipo de Serviço | Informação do Tipo de Serviço |
| Tipo de Serviço | Textbox | S | N |  |  | MFS10414 |
| Código da Atividade Econômica | Textbox | S | N |  |  | MFS10414 MFS13631 |
| Valor Material ou Equipamento | Textbox | S | N |  |  | MFS10414 MFS13631 |
| Valor Dedução Alimentação | Textbox | S | N |  |  | MFS10414 MFS13631 |
| Valor Dedução Transporte | Textbox | S | N |  |  | MFS10414 MFS13631 |
| Valor Base de Cálculo da Retenção do INSS | Textbox | S | N |  |  | MFS10414 |
| Valor da Retenção do INSS | Textbox | S | N |  |  | MFS10414 |
| Valor da Retenção da Subcontratada | Textbox | S | N |  |  | MFS10414 |
| Valor da Retenção Principal Não Efetuada ou Depositada em Juízo da Decisão Judicial/Administrativa | Textbox | S | N |  |  | MFS10414 |
| Valor dos Serviços/Aposentadoria Especial - 15 anos | Textbox | S | N |  |  | MFS10414 |
| Valor dos Serviços/Aposentadoria Especial - 20 anos | Textbox | S | N |  |  | MFS10414 |
| Valor dos Serviços/Aposentadoria Especial - 25 anos | Textbox | S | N |  |  | MFS10414 |
| Valor Adicional | Textbox | S | N |  |  | MFS10414 |
| Valor da Retenção Adicional Não Efetuada ou Depositada em Juízo da Decisão Judicial/Administrativa | Textbox | S | N |  |  | MFS10414 |
| Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal | Informações de Processo Retenção Principal |
| Tipo do Processo Retenção Principal | Textbox | S | N |  |  | MFS10414 |
| Número do Processo Retenção Principal | Textbox | S | N |  |  | MFS10414 |
| Código da Suspensão Principal | Textbox | S | N |  |  | MFS10414 |
| Valor Retenção Principal | Textbox | S | N |  |  | MFS10414 |
| Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional | Informações de Processo Retenção Adicional |
| Tipo do Processo Retenção Adicional | Textbox | S | N |  | Irá demonstrar o tipo do processo retenção adicional.  Administrativo do Tomador Judicial do Tomador | MFS10414 |
| Número do Processo Retenção Adicional | Textbox | S | N |  |  | MFS10414 |
| Código da Suspensão Adicional | Textbox | S | N |  |  | MFS10414 |
| Valor Retenção Adicional | Textbox | S | N |  |  | MFS10414 |
| Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais das bases e retenções calculados pelo Fisco. Trata-se dos campos da tag “RPrest” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2020. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais das bases e retenções calculados pelo Fisco. Trata-se dos campos da tag “RPrest” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2020. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais das bases e retenções calculados pelo Fisco. Trata-se dos campos da tag “RPrest” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2020. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais das bases e retenções calculados pelo Fisco. Trata-se dos campos da tag “RPrest” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2020. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais das bases e retenções calculados pelo Fisco. Trata-se dos campos da tag “RPrest” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2020. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais das bases e retenções calculados pelo Fisco. Trata-se dos campos da tag “RPrest” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2020. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais das bases e retenções calculados pelo Fisco. Trata-se dos campos da tag “RPrest” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2020. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. |
| Total Base de Cálculo da Retenção | Numérico | N | N |  | Conteúdo do campo “40-vlrTotalBaseRet” do evento R-5001 referente ao R-2020 em questão. | MFS17628 MFS20930 |
| Total Valor Retenção | Numérico | N | N |  | Conteúdo do campo “41-vlrTotalRetPrinc” do evento R-5001 referente ao R-2020 em questão. | MFS17628 MFS20930 |
| Total Valor Retenção Adicional | Numérico | N | N |  | Conteúdo do campo “42-vlrTotalRetAdic” do evento R-5001 referente ao R-2020 em questão. | MFS17628 MFS20930 |
| Total Valor Retenção não efetuada | Numérico | N | N |  | Conteúdo do campo “43-vlrTotalNRetPrinc” do evento R-5001 referente ao R-2020 em questão. | MFS17628 MFS20930 |
| Total Valor Retenção Adicional não efetuada | Numérico | N | N |  | Conteúdo do campo “44-vlrTotalNRetAdic” do evento R-5001 referente ao R-2020 em questão. | MFS17628 MFS20930 |
| R-2040 – Recursos Repassados para Associação Desportiva | R-2040 – Recursos Repassados para Associação Desportiva | R-2040 – Recursos Repassados para Associação Desportiva | R-2040 – Recursos Repassados para Associação Desportiva | R-2040 – Recursos Repassados para Associação Desportiva | R-2040 – Recursos Repassados para Associação Desportiva | R-2040 – Recursos Repassados para Associação Desportiva |
| Identificação do Estabelecimento de Repasse dos Recursos | Identificação do Estabelecimento de Repasse dos Recursos | Identificação do Estabelecimento de Repasse dos Recursos | Identificação do Estabelecimento de Repasse dos Recursos | Identificação do Estabelecimento de Repasse dos Recursos | Identificação do Estabelecimento de Repasse dos Recursos | Identificação do Estabelecimento de Repasse dos Recursos |
| Tipo de Inscrição | Textbox | S | N |  | Irá demonstrar o tipo de inscrição do estabelecimento.  1-CNPJ | MFS-11670 |
| Número de Inscrição | Textbox | S | N |  |  | MFS-11670 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data Ocorrência | Textbox | S | N |  |  | MFS-11670 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-11670 |
| Situação | Textbox | S | N |  |  | MFS-11670 |
| Informação dos Repasses Efetuados a Associação Desportiva | Informação dos Repasses Efetuados a Associação Desportiva | Informação dos Repasses Efetuados a Associação Desportiva | Informação dos Repasses Efetuados a Associação Desportiva | Informação dos Repasses Efetuados a Associação Desportiva | Informação dos Repasses Efetuados a Associação Desportiva | Informação dos Repasses Efetuados a Associação Desportiva |
| CNPJ da Associação Desportiva | Textbox | S | N |  |  | MFS-11670 |
| Valor Total do Repasse | Textbox | S | N |  |  | MFS-11670 |
| Valor Total da Retenção | Textbox | S | N |  |  | MFS-11670 |
| Valor Total da Retenção não Efetuada | Textbox | S | N |  |  | MFS-11670 |
| Tipo do Processo | Textbox | S | N |  |  | MFS-11670 MFS13861 |
| Número do Processo | Textbox | S | N |  |  | MFS-11670 MFS13861 |
| Código de Suspensão | Textbox | S | N |  |  | MFS-11670 MFS13861 |
| Código da Conta Analítica | Textbox | S | N |  |  | MFS-11670 MFS13861 |
| Detalhamento dos Recursos Repassados a Associação Desportiva | Detalhamento dos Recursos Repassados a Associação Desportiva | Detalhamento dos Recursos Repassados a Associação Desportiva | Detalhamento dos Recursos Repassados a Associação Desportiva | Detalhamento dos Recursos Repassados a Associação Desportiva | Detalhamento dos Recursos Repassados a Associação Desportiva | Detalhamento dos Recursos Repassados a Associação Desportiva |
| Tipo do Repasse | Textbox | S | N |  |  | MFS-11670 |
| Valor Bruto | Textbox | S | N |  |  | MFS-11670 |
| Valor da Apuração da Retenção | Textbox | S | N |  |  | MFS-11670 |
| Descrição do Recurso Repassado | Textbox | S | N |  |  | MFS13861 |
| Valor da Retenção não Efetuada | Textbox | S | N |  |  | MFS-11670 MFS13861 |
| Informações de Processos relacionados a não Retenção de Contribuição Previdenciária | Informações de Processos relacionados a não Retenção de Contribuição Previdenciária | Informações de Processos relacionados a não Retenção de Contribuição Previdenciária | Informações de Processos relacionados a não Retenção de Contribuição Previdenciária | Informações de Processos relacionados a não Retenção de Contribuição Previdenciária | Informações de Processos relacionados a não Retenção de Contribuição Previdenciária | Informações de Processos relacionados a não Retenção de Contribuição Previdenciária |
| Tipo do Processo | Textbox | S | N |  |  | MFS13861 |
| Número do Processo | Textbox | S | N |  |  | MFS13861 |
| Código de Suspensão | Textbox | S | N |  |  | MFS13861 |
| Valor da Retenção não Efetuada | Textbox | S | N |  |  | MFS13861 |
| Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais de cada associação desportiva (cada CNPJ) calculados pelo Fisco. Trata-se dos campos da tag “RRecRepAD” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2040. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais de cada associação desportiva (cada CNPJ) calculados pelo Fisco. Trata-se dos campos da tag “RRecRepAD” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2040. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais de cada associação desportiva (cada CNPJ) calculados pelo Fisco. Trata-se dos campos da tag “RRecRepAD” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2040. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais de cada associação desportiva (cada CNPJ) calculados pelo Fisco. Trata-se dos campos da tag “RRecRepAD” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2040. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais de cada associação desportiva (cada CNPJ) calculados pelo Fisco. Trata-se dos campos da tag “RRecRepAD” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2040. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais de cada associação desportiva (cada CNPJ) calculados pelo Fisco. Trata-se dos campos da tag “RRecRepAD” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2040. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais de cada associação desportiva (cada CNPJ) calculados pelo Fisco. Trata-se dos campos da tag “RRecRepAD” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2040. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. |
| Valor Total do Repasse | Numérico | N | N |  | Conteúdo do campo “47-vlrTotalRep” do evento R-5001 referente ao R-2040 em questão, e para o CNPJ da associação em foco. | MFS17628 MFS20930 |
| Código de Receita | Alfanumérico | N | N | Formato: 9999-99 | Conteúdo do campo “48-CRRecRepAD” do evento R-5001 referente ao R-2040 em questão, e para o CNPJ da associação em foco. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária | Numérico | N | N |  | Conteúdo do campo “49-vlrCRRecRepAD” do evento R-5001 referente ao R-2040 em questão, e para o CNPJ da associação em foco. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária não efetuada | Numérico | N | N |  | Conteúdo do campo “50-vlrCRRecRepADSusp” do evento R-5001 referente ao R-2040 em questão, e para o CNPJ da associação em foco. | MFS17628 MFS20930 |


| R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria |
| --- |
| Informação da Comercialização da Produção |


| Tipo de Inscrição | Textbox | S | N |  | Irá demonstrar o tipo de inscrição do estabelecimento.  1-CNPJ | MFS-9073 |
| --- | --- | --- | --- | --- | --- | --- |
| Número de Inscrição | Textbox | S | N |  |  | MFS-9073 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data da Ocorrência | Textbox | S | N |  |  | MFS13897 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS13897 |
| Situação | Textbox | S | N |  |  | MFS13897 | MFS13897 |
| Valor Receita Bruta Total | Textbox | S | N |  |  | MFS-9073 |
| Valor da Contribuição Previdenciária | Textbox | S | N |  |  | MFS-9073 |
| Valor da Contribuição Previdenciária GILRAT | Textbox | S | N |  |  | MFS-9073 |
| Valor da Contribuição Previdenciária SENAR | Textbox | S | N |  |  | MFS-9073 |
| Valor da Contribuição Exigibilidade Suspensa | Textbox | S | N |  |  | MFS13897 |
| Valor da Contribuição Previdenciária GILRAT Exigibilidade Suspensa | Textbox | S | N |  |  | MFS13897 |
| Valor da Contribuição Previdenciária SENAR Exigibilidade Suspensa | Textbox | S | N |  |  | MFS13897 |


| Receita por Tipo de Comercialização |
| --- |


| Indicativo de Comercialização | Textbox | S | N |  | Irá demonstrar o Indicativo de Comercialização:  1 - Comercialização da Produção por Prod. Rural PJ/Agroindústria, exceto para entidades executoras do PAA;  7 - Comercialização da Produção com Isenção de Contribuição Previdenciária, de acordo com a Lei n° 13.606/2018; 8 - Comercialização da Produção para Entidade do Programa de Aquisição de Alimentos - PAA;  9 - Comercialização da Produção no Mercado Externo. | MFS-9073 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Valor Receita Bruta por Indicativo de Comercialização | Textbox | S | N |  |  | MFS-9073 |
| Conta Analítica | Textbox | S | N |  |  | MFS-9073 MFS13897 |


| Detalhamento da Receita Bruta por Nota Fiscal |
| --- |


| Nota Fiscal | Textbox | S | N |  |  | MFS-9073 MFS13897 |
| --- | --- | --- | --- | --- | --- | --- |
| Data Emissão | Textbox | S | N |  |  | MFS-9073 MFS13897 |
| Valor Bruto Nota Fiscal | Textbox | S | N |  |  | MFS-9073 MFS13897 |
| Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RComl” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2050. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RComl” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2050. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RComl” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2050. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RComl” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2050. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RComl” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2050. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RComl” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2050. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1   Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RComl” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2050. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. |
| Código de Receita | Alfanumérico | N | N | Formato: 9999-99 | Conteúdo do campo “52-CRComl” do evento R-5001 referente ao R-2050 em questão. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária | Numérico | N | N |  | Conteúdo do campo “53-vlrCRComl” do evento R-5001 referente ao R-2050 em questão. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária Exigibilidade Suspensa | Numérico | N | N |  | Conteúdo do campo “54-vlrCRComlSusp” do evento R-5001 referente ao R-2050 em questão. | MFS17628 MFS20930 |
| Informações de Processos Administrativos/Judiciais | Informações de Processos Administrativos/Judiciais | Informações de Processos Administrativos/Judiciais | Informações de Processos Administrativos/Judiciais | Informações de Processos Administrativos/Judiciais | Informações de Processos Administrativos/Judiciais | Informações de Processos Administrativos/Judiciais |
| Tipo do Processo | Textbox | S | N |  |  | MFS13897 | MFS13897 |
| Número do Processo | Textbox | S | N |  |  | MFS13897 | MFS13897 |
| Código de Suspensão | Textbox | S | N |  |  | MFS13897 | MFS13897 |
| R-2055 – Aquisição de Produção Rural | R-2055 – Aquisição de Produção Rural | R-2055 – Aquisição de Produção Rural | R-2055 – Aquisição de Produção Rural | R-2055 – Aquisição de Produção Rural | R-2055 – Aquisição de Produção Rural | R-2055 – Aquisição de Produção Rural | R-2055 – Aquisição de Produção Rural |
| Identificação do Estabelecimento Adquirente da Produção | Identificação do Estabelecimento Adquirente da Produção | Identificação do Estabelecimento Adquirente da Produção | Identificação do Estabelecimento Adquirente da Produção | Identificação do Estabelecimento Adquirente da Produção | Identificação do Estabelecimento Adquirente da Produção | Identificação do Estabelecimento Adquirente da Produção | Identificação do Estabelecimento Adquirente da Produção |
| Tipo de Inscrição | Textbox | S | N |  | Irá demonstrar o tipo de inscrição do estabelecimento.  1-CNPJ | MFS-58348 | MFS-58348 |
| Número de Inscrição | Textbox | S | N |  | Irá demonstrar o número de inscrição do estabelecimento. | MFS-58348 | MFS-58348 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data da Ocorrência | Texto | S | N |  | Irá demonstrar a data da ocorrência do R-2055 em questão. | MFS-58348 | MFS-58348 |
| Operação | Texto | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-58348 | MFS-58348 |
| Situação | Texto | S | N |  | Irá demonstrar a situação do R-2055 em questão. | MFS-58348 | MFS-58348 |
| Retificação S-1250 | Texto | S | N |  | Por definição do Fisco, neste momento, não será validado este campo.  [ALTERAÇÃO MFS-79878] -  Este campo não deve ser gerado a partir da versão 2.1 do REINF | MFS-58348  MFS-79878 | MFS-58348  MFS-79878 |
| Identificação do Produtor Rural | Identificação do Produtor Rural | Identificação do Produtor Rural | Identificação do Produtor Rural | Identificação do Produtor Rural | Identificação do Produtor Rural | Identificação do Produtor Rural | Identificação do Produtor Rural |
| Tipo de Inscrição | Texto | S | N | 1 – CNPJ  ou  2 - CPF | Conteúdo do campo 20-tpInscProd do R-2055 em questão. | MFS-58348 | MFS-58348 |
| Número de Inscrição | Texto | S | N |  | Conteúdo do campo 21- nrInscProd do R-2055 em questão. | MFS-58348 | MFS-58348 |
| Indicador OpcCP | Texto | S | N |  | Conteúdo do campo 22 – indOpcCP do R-2055 em questão. | MFS-58348 | MFS-58348 |
| Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural |
| Indicador de Aquisição | Texto | S | N |  | Irá demonstrar:  1 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral;  2 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade executora do Programa de Aquisição de Alimentos - PAA;  3 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA;  4 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral - Produção isenta (Lei 13.606/2018); 5 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade executora do PAA - Produção isenta (Lei 13.606/2018); 6 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA - Produção isenta (Lei 13.606/2018); 7 - Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação | MFS-58348 | MFS-58348 |
| Valor da Receita Bruta Total | Texto | S | N |  | Conteúdo do campo “25-vlrBruto” referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor da Contribuição Previdenciária | Texto | S | N |  | Conteúdo do campo “26- vlrCPDescPR” referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor da Contribuição Previdenciária GILRAT | Texto | S | N |  | Conteúdo do campo “27- vlrRatDescPR” referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor da Contribuição Previdenciária SENAR | Texto | S | N |  | Conteúdo do campo “28- vlrSenarDesc” referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001 [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. |
| Código de Receita | Alfanumérico | N | N | Formato: 9999-99 | Conteúdo do campo “56-CRAquis” do evento R-5001 referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor Contribuição Previdenciária | Numérico | N | N |  | Conteúdo do campo “57-vlrCRAquis” do evento R-5001 referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor Contribuição Previdenciária Exigibilidade Suspensa | Numérico | N | N |  | Conteúdo do campo “58-vlrCRAquisSusp” do evento R-5001 referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural |
| Número do Processo Judicial | Texto | S | N |  | Conteúdo do campo 30 – nrProcJud referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Código da Suspensão | Texto | S | N |  | Conteúdo do campo 31 – CodSusp referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor da Contribuição Previdenciária | Texto | S | N |  | Conteúdo do campo 32 – vlrCPNRet referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor da Contribuição Previdenciária GILRAT | Texto | S | N |  | Conteúdo do campo 33 – vlrRatNRet referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |
| Valor da Contribuição Previdenciária SENAR | Texto | S | N |  | Conteúdo do campo 34 – vlrSenarNRet referente ao R-2055 em questão. | MFS-58348 | MFS-58348 |


| R-2060 – Contribuição Previdenciária Sobre a Receita Bruta |
| --- |
| Identificação do Estabelecimento que Auferiu a Receita Bruta |


| Tipo de Inscrição | Textbox | S | N |  | Irá demonstrar o tipo de inscrição do estabelecimento tomador de serviços.  1-CNPJ 4-CNO | MFS-9074 |
| --- | --- | --- | --- | --- | --- | --- |
| Número de Inscrição | Textbox | S | N |  |  | MFS-9074 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data Ocorrência | Textbox | S | N |  |  | MFS-11400 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-11400 |
| Valor Receita Bruta | Textbox | S | N |  |  | MFS-11400 |
| Valor da Contribuição Previdenciária | Textbox | S | N |  |  | MFS-11400 |
| Valor da Contribuição Previdenciária com exigibilidade Suspensa | Textbox | S | N |  |  | MFS14002 |
| Tipo do Processo | Textbox | S | N |  |  | MFS-11400 MFS14002 |
| Número do Processo | Textbox | S | N |  |  | MFS-11400 MFS14002 |
| Código Suspensão | Textbox | S | N |  |  | MFS-11400 MFS14002 |
| Situação | Textbox | S | N |  |  | MFS-11400 |


| Identificação do Valor Total da Receita por Tipo de Código de Atividade |
| --- |


| Código de Atividade Econômica | Textbox | S | N |  |  | MFS-9074 |
| --- | --- | --- | --- | --- | --- | --- |
| Valor Receita Bruta Atividade | Textbox | S | N |  |  | MFS-9074 |
| Valor Exclusão da Receita Bruta | Textbox | S | N |  |  | MFS-9074 |
| Valor Adição Receita Bruta | Textbox | S | N |  |  | MFS-9074 |
| Valor da Base de Cálculo da Contribuição Previdenciária | Textbox | S | N |  |  | MFS9074 |
| Valor Contribuição Previdenciária | Textbox | S | N |  |  | MFS9074 |
| Código da Conta Analítica | Textbox | S | N |  |  | MFS9074 MFS14002 |


| Identificação do Detalhamento da Receita Bruta |
| --- |


| Série | Textbox | S | N |  |  | MFS9074 MFS14002 |
| --- | --- | --- | --- | --- | --- | --- |
| Número Documento | Textbox | S | N |  |  | MFS9074 MFS14002 |
| Data Emissão Nota Fiscal | Textbox | S | N |  |  | MFS9074 MFS14002 |
| Valor Bruto do Documento Fiscal | Textbox | S | N |  |  | MFS9074 MFS14002 |
| Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RCPRB” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2060. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RCPRB” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2060. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RCPRB” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2060. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RCPRB” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2060. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RCPRB” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2060. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RCPRB” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2060. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001   [ALTERAÇÃO MFS-79960] – Não gerar essa aba a partir da versão 2.1.1  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RCPRB” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2060. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. |
| Código de Receita | Alfanumérico | N | N | Formato: 9999-99 | Conteúdo do campo “56-CRCPRB” do evento R-5001 referente ao R-2060 em questão. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária | Numérico | N | N |  | Conteúdo do campo “57-vlrCRCPRB” do evento R-5001 referente ao R-2060 em questão. | MFS17628 MFS20930 |
| Valor Contribuição Previdenciária Exigibilidade Suspensa | Numérico | N | N |  | Conteúdo do campo “58-vlrCRCPRBSusp” do evento R-5001 referente ao R-2060 em questão. | MFS17628 MFS20930 |
| Informações de Processos relacionados à Suspenção de CPRB | Informações de Processos relacionados à Suspenção de CPRB | Informações de Processos relacionados à Suspenção de CPRB | Informações de Processos relacionados à Suspenção de CPRB | Informações de Processos relacionados à Suspenção de CPRB | Informações de Processos relacionados à Suspenção de CPRB | Informações de Processos relacionados à Suspenção de CPRB |
| Tipo do Processo | Textbox | S | N |  |  | MFS14002 | MFS14002 |
| Número do Processo | Textbox | S | N |  |  | MFS14002 | MFS14002 |
| Código de Suspensão | Textbox | S | N |  |  | MFS14002 | MFS14002 |


| Ajuste da Contribuição Apurada |
| --- |


| Tipo de Ajuste | Textbox | S | N |  |  | MFS9074 |
| --- | --- | --- | --- | --- | --- | --- |
| Código do Ajuste | Textbox | S | N |  |  | MFS9074 |
| Valor de Ajuste | Textbox | S | N |  |  | MFS9074 |
| Descrição do Ajuste | Textbox | S | N |  |  | MFS9074 |
| Data Ajuste | Textbox | S | N |  |  | MFS9074 |


| R-2070 – Retenções na Fonte – IR, CSLL, Cofins, PIS/PASEP – Pagamentos Diversos |
| --- |
| Identificação Beneficiário Pessoa Física |


| Código do Pagamento | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Insc. do Beneficiário | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Número de Insc. do Beneficiário | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data Ocorrência | Textbox | S | N |  |  | MFS-11399 MFS20930 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-11399 MFS20930 |
| Nome do Beneficiário | Textbox | S | N |  |  | MFS11399 MFS20930 |
| Data do Laudo Moléstia Grave | Textbox | N | N |  |  | MFS11399 MFS20930 |
| Situação | Textbox | S | N |  |  | MFS11399 MFS20930 |
| Estabelecimentos | Estabelecimentos | Estabelecimentos | Estabelecimentos | Estabelecimentos | Estabelecimentos | Estabelecimentos |
| Tipo de Inscrição | Textbox | S | N |  |  | MFS11892 MFS20930 |
| Número de Inscrição | Textbox | S | N |  |  | MFS11892 MFS20930 |


| Informações de Pagamento Residente ou Domiciliado no Brasil |
| --- |


| Data de Pagamento | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Indicador de Exig. Suspensa | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Indicador de 13° Salário | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor do Rendimento Tributável | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor do IRRF | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor Comp. Judicial Ano Calendário | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Valor Comp. Judicial Ano Anteriores | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Valor Depósito Judicial | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Detalhamento das Deduções |
| --- |


| Indicador do Tipo de Dedução | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Valor da Dedução | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Rendimentos Isentos/Não Tributáveis |
| --- |


| Tipo de Isenção | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Valor Isenção | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Desc. Do Rendimento Isento | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Detalhamento das Competências |
| --- |


| Ind. De Período de Referência | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Período de referência do Pag. | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor do Rendimento Tributável | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Informações RRA |
| --- |


| Tipo de Processo | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Número do Processo | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Código Suspensão | Textbox | N | N |  |  | MFS10415 MFS20930 |
| Natureza RRA | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Quantidade de Meses | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Valor da Desp. Com Custas Judiciais | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Despesa com Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Identificação do Advogado |
| --- |


| Tipo de Inscrição do advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Número de Insc. Do Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Despesa com Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Informação Processo Judicial |
| --- |


| Número do Processo Judicial | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Código Suspensão | Textbox | N | N |  |  | MFS10415 MFS20930 |
| Indicador da Origem dos Recursos | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Desp. Com Custas Judiciais | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Despesa com Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Identificação Origem dos Recursos | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Identificação do Advogado |
| --- |


| Tipo de Inscrição do advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Número de Insc. Do Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Despesa com Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Identificação do Beneficiário Pessoa Jurídica |
| --- |


| Código do Pagamento | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Insc. do Beneficiário | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Número de Insc. do Beneficiário | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data Ocorrência | Textbox | S | N |  |  | MFS-11399 MFS20930 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-11399 MFS20930 |
| Nome do Beneficiário | Textbox | S | N |  |  | MFS11399 MFS20930 |
| Data Moléstia | Textbox | S | N |  |  | MFS11892 MFS20930 |
| Situação | Textbox | S | N |  |  | MFS11399 MFS20930 |


| Informações de Pagamento Residente ou Domiciliado no Brasil |
| --- |


| Data de Pagamento | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Valor do Rendimento Tributável | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Retenção na Fonte | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Informação Processo Judicial |
| --- |


| Número do Processo Judicial | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Indicador da Origem dos Recursos | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Desp. Com Custas Judiciais | Textbox | S | N |  |  | MFS9074 MFS20930 |
| Valor da Despesa com Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Identificação Origem dos Recursos | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Código Suspensão | Textbox | S | N |  |  | MFS11892 MFS20930 |


| Identificação do Advogado |
| --- |


| Tipo de Inscrição do advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Número de Insc. Do Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Valor da Despesa com Advogado | Textbox | S | N |  |  | MFS9901 MFS20930 |


| Identificação do Beneficiário Exterior |
| --- |


| Código do Pagamento | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Insc. Do Beneficiário | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Número de Insc. Do Beneficiário | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data Ocorrência | Textbox | S | N |  |  | MFS-11399 MFS20930 |
| Operação | Textbox | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-11399 MFS20930 |
| Nome/Razão Social do Beneficiário | Textbox | S | N |  |  | MFS-11399 MFS20930 |
| Data do Laudo Moléstia Grave | Textbox | S | N |  |  | MFS-11399 MFS20930 |
| Situação | Textbox | S | N |  |  | MFS-11399 MFS20930 |


| Informações de Beneficiário Residente ou Domiciliado no Exterior |
| --- |


| Código do País | Textbox | S | N |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- |
| Descrição do Logradouro | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Número do Logradouro | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Complemento do Logradouro | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Nome do Bairro/Distrito | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Nome da Cidade | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Código de End. Postal | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Ind. Do Número de Ident. Fiscal | Textbox | S | N |  |  | MFS9901 MFS20930 |
| Número de Ident. Fiscal | Textbox | N | N |  |  | MFS9901 MFS20930 |
| Relação Fonte pagadora PJ e BPJ | Textbox | N | N |  |  | MFS9901 MFS20930 |


| Informações de Pagamentos Residente ou Domiciliado no Exterior |
| --- |


| Data de Pagamento | Data de Pagamento | Textbox | S | N |  |  |  | MFS9901 MFS20930 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo de Rendimento | Tipo de Rendimento | Textbox | S | N |  |  |  | MFS9901 MFS20930 |
| Forma de Tributação | Forma de Tributação | Textbox | S | N |  |  |  | MFS9901 MFS20930 |
| Valor Pago | Valor Pago | Textbox | S | N |  |  |  | MFS9901 MFS20930 |
| Valor da Retenção na Fonte | Valor da Retenção na Fonte | Textbox | S | N |  |  |  | MFS9901 MFS20930 |
| R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física | R-4010 - Pagamentos/Créditos a Beneficiário Pessoa Física |
| Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento |
| Tipo de Inscrição | Tipo de Inscrição | Texto | S | N |  |  | Irá demonstrar o tipo de inscrição do estabelecimento   1-CNPJ | MFS-79885 |
| Número de Inscrição | Número de Inscrição | Texto | S | N |  |  |  | MFS-79885 |
| Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário | Ocorrência/Identificação do Beneficiário |
| Data da Ocorrência | Data da Ocorrência | Texto | S | N |  |  | Irá demonstrar a data da ocorrência do R-4010 em questão. | MFS-79885 |
| Operação | Operação | Texto | S | N |  |  | Irá demonstrar   - Original - Retificadora | MFS-79885 |
| Situação | Situação | Texto | S | N |  |  | Irá demonstrar a situação do R-4010 em questão. | MFS-79885 |
| CPF | CPF | Texto | S | N | XXX.XXX.XXX-XX | XXX.XXX.XXX-XX | CPF do Beneficiário | MFS-79885 |
| Nome | Nome | Texto | S | N |  |  | Nome do Beneficiário | MFS-79885 |
| ideEvtAdic | ideEvtAdic | Texto | S | N |  |  | Identificador de evento adicional por beneficiário, a critério do declarante.  Apresentar este campo a partir da versão 2.1.2 | MFS-535745 |
| Identificação dos Dependentes | Identificação dos Dependentes | Identificação dos Dependentes | Identificação dos Dependentes | Identificação dos Dependentes | Identificação dos Dependentes | Identificação dos Dependentes | Identificação dos Dependentes | Identificação dos Dependentes |
| CPF | CPF | Texto | S | N | XXX.XXX.XXX-XX | XXX.XXX.XXX-XX | Neste campo deve ser considerado o somatório do valor bruto do rendimento R-4010, independente da data do recebimento e sim do período de apuração. | MFS-79885 |
| Relação de Dependência | Relação de Dependência | Texto | S | N | Código - Descrição | Código - Descrição | Informar a Relação de Dependência | MFS-79885 |
| Descrição | Descrição | Texto | S | N | Descrição | Descrição | Descrição da Dependência, quando o tipo de relação de dependência for igual a ‘99 – Outros’ | MFS-79885 |
| Identificação dos Rendimentos | Identificação dos Rendimentos | Identificação dos Rendimentos | Identificação dos Rendimentos | Identificação dos Rendimentos | Identificação dos Rendimentos | Identificação dos Rendimentos | Identificação dos Rendimentos | Identificação dos Rendimentos |
| Natureza do Rendimento | Natureza do Rendimento | Texto | S | N |  |  | Natureza de Rendimento | MFS-79885 |
| Observação | Observação | Texto | S | N | Descrição | Descrição | Observação | MFS-79885 |
| Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento | Informações Relativas ao Rendimento |
| Fato Gerador | Fato Gerador | Texto | S | N | DD/MM/AAAA | DD/MM/AAAA | Data do Fato Gerador | MFS-79885 |
| Comp. | Comp. | Texto | S | N | MM/AAAA | MM/AAAA | Mês e Ano da Competência | MFS-79885 |
| 13º | 13º | Texto | S | N | Código | Código | Indicador de 13º  Lista de Valor Válido: S | MFS-79885 |
| Rend. Bruto | Rend. Bruto | Texto | S | N | 0,00 | 0,00 | Valor do rendimento bruto | MFS-79885 |
| Rend. Tributável | Rend. Tributável | Texto | S | N | 0,00 | 0,00 | Valor tributável | MFS-79885 |
| Valor IR | Valor IR | Texto | S | N | 0,00 | 0,00 | Valor do IR | MFS-79885 |
| RRA | RRA | Texto | S | N | Código | Código | Indicador de Rendimento Recebido Acumuladamente.  Lista de Valor Válido: S | MFS-79885 |
| FCI_SCP | FCI_SCP | Texto | S | N | Código - Descrição | Código - Descrição | Indicador de FCI e SCP  Lista de Valores Válidos: 1-FCI;  2-SCP | MFS-79885 |
| Núm. Insc. FCI_SCP | Núm. Insc. FCI_SCP | Texto | S | N | XX.XXX.XXX/XXXX-XX | XX.XXX.XXX/XXXX-XX | Número da Inscrição de FCI/SCP | MFS-79885 |
| % SCP | % SCP | Texto | S | N | 999 | 999 | Percentual de SCP | MFS-79885 |
| IndJud | IndJud | Texto | S | N | Código | Código | Informar o Indicativo exclusivo de rendimento de natureza diversa de RRA e que seja oriundo de decisão judicial  Lista de Valores Válidos: S; N | MFS-79885 |
| País Resid. Exterior | País Resid. Exterior | Texto | S | N | 999 | 999 | Informar o código do país de destino da remessa do pagamento a residente ou domiciliado no exterior. | MFS-79885 |
| dtEscrCont | dtEscrCont | Texto | S | N | DD/MM/AAAA | DD/MM/AAAA | Data da escrituração contábil.  Apresentar este campo a partir da versão 2.1.2 | MFS-535745 |
| observ | observ | Texto | S | N |  |  | Observações  Apresentar este campo a partir da versão 2.1.2 | MFS-535745 |
| Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável | Informações Relativas às Deduções do Rendimento Tributável |
| Tipo Dedução | Tipo Dedução | Texto | S | N | Código - Descrição | Código - Descrição | Informar o indicativo do tipo de dedução  [ALTERAÇÃO  MFS-566870] Inclusão da opção 8  Lista de valores válidos:  1 - Previdência oficial; 2 - Previdência privada; 3 - Fundo de aposentadoria programada individual - Fapi;  4 - Fundação de previdência complementar do servidor público - Funpresp; 5 - Pensão alimentícia; 7 – Dependentes; 8 – Desconto simplificado mensal. | MFS-79885 MFS-566870 |
| Valor Dedução | Valor Dedução | Texto | S | N | 0,00 | 0,00 | Valor da Dedução | MFS-79885 |
| Inform. Entidade | Inform. Entidade | Texto | S | N | Código | Código | Informar se há informações da entidade de previdência complementar  Lista de valores válidos: S - Sim;  N - Não. | MFS-79885 |
| Núm. Inscr. Previdencia Compl. | Núm. Inscr. Previdencia Compl. | Texto | S | N |  |  | Número da inscrição da entidade da previdência complementar | MFS-79885 |
| Valor Patroc. FUNPRESP | Valor Patroc. FUNPRESP | Texto | S | N | 0,00 | 0,00 | Valor da contribuição do ente público patrocinador da Fundação de Previdência do Servidor Público (Funpresp). | MFS-79885 |
| Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia | Dependentes e Beneficiários da Pensão Alimentícia |
| CPF | CPF | Texto | S | N | XXX.XXX.XXX-XX | XXX.XXX.XXX-XX | CPF do dependente ou beneficiário da pensão alimentícia. | MFS-79885 |
| Valor Dedução | Valor Dedução | Texto | S | N | 0,00 | 0,00 | Valor da dedução referente ao dependente ou do beneficiário da pensão alimentícia. | MFS-79885 |
| Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis | Rendimentos Isentos ou não Tributáveis |
| Tipo Isenção | Tipo Isenção | Texto | S | N | Código - Descrição | Código - Descrição | Infomar o Tipo de Isenção:  Lista de valores válidos:  1 - Parcela isenta 65 anos; 2 - Diária de viagem;  3 - Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho;  4 - Abono pecuniário;  5 - Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore, aluguéis e serviços prestados;  6 - Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço;  7 - Complementação de aposentadoria, correspondente às contribuições efetuadas no período de 01/01/1989 a 31/12/1995;  8 - Ajuda de custo; [EXCLUSÃO MFS-549365] 9 - Rendimentos pagos sem retenção do IR na fonte - Lei 10.833/2003;  [INCLUSÃO MFS-549365] – 10 - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função;  [INCLUSÃO MFS-549365] – 11- Resgate de previdência complementar por portador de moléstia grave;   99 - Outros (especificar). | MFS-79885 MFS-549365 |
| Valor Isento | Valor Isento | Texto | S | N | 0,00 | 0,00 | Valor da parcela isenta. | MFS-79885 |
| Descrição do Rendimento | Descrição do Rendimento | Texto | S | N |  |  | Descrição do rendimento isento/não tributável. | MFS-79885 |
| Data Laudo | Data Laudo | Texto | S | N | DD/MM/AAAA | DD/MM/AAAA | Data da moléstia grave atribuída pelo laudo. | MFS-79885 |
| Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos | Processos Relacionados a não Retenção de Tributos |
| Tipo Processo | Tipo Processo | Texto | S | N | Código - Descrição | Código - Descrição | Preencher com o código correspondente ao tipo de processo  Lista de Valores Válidos: 1 - Administrativo;  2 - Judicial. | MFS-79885 |
| Núm. Processo | Núm. Processo | Texto | S | N |  |  | Informar o número do processo administrativo/judicial. | MFS-79885 |
| Cód. Suspensão | Cód. Suspensão | Texto | S | N |  |  | Informar o código indicativo da suspensão | MFS-79885 |
| Valor Retenção que Deixou de ser Efetuada | Valor Retenção que Deixou de ser Efetuada | Texto | S | N | 0,00 | 0,00 | Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial. | MFS-79885 |
| Valor Depósito Judicial | Valor Depósito Judicial | Texto | S | N | 0,00 | 0,00 | Valor do depósito judicial em função de processo administrativo ou judicial. | MFS-79885 |
| Valor Comp. Ano Calendário | Valor Comp. Ano Calendário | Texto | S | N | 0,00 | 0,00 | Valor da compensação relativa ao ano calendário em função de processo judicial. | MFS-79885 |
| Valor Comp. Anos Anteriores | Valor Comp. Anos Anteriores | Texto | S | N | 0,00 | 0,00 | Valor da compensação relativa a anos anteriores, em função de processo judicial. | MFS-79885 |
| Valor Rend. Exigibilidade Suspensa | Valor Rend. Exigibilidade Suspensa | Texto | S | N | 0,00 | 0,00 | Valor do rendimento com exigibilidade suspensa. | MFS-79885 |
| Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas | Detalhamento das Deduções Suspensas |
| Tipo Dedução | Tipo Dedução | Texto | S | N | Código - Descrição | Código - Descrição | Informar o indicativo do tipo de dedução:   [ALTERAÇÃO  MFS-566870] Inclusão da opção 8  Lista de Valores Válidos:  1 - Previdência oficial;  2 - Previdência privada;  3 - Fundo de aposentadoria programada individual - Fapi;  4 - Fundação de previdência complementar do servidor público - Funpresp;  5 - Pensão alimentícia;  7 – Dependentes; 8 – Desconto simplificado mensal. | MFS-79885 MFS-566870 |
| Valor Dedução Suspensa | Valor Dedução Suspensa | Texto | S | N | 0,00 | 0,00 | Valor da dedução da base de cálculo do imposto de renda, com exigibilidade suspensa. | MFS-79885 |
| Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia | Deduções Suspensas por Dependentes e Beneficiários da Pensão Alimentícia |
| CPF | CPF | Texto | S | N | XXX.XXX.XXX-XX | XXX.XXX.XXX-XX | CPF do dependente ou beneficiário da pensão alimentícia. | MFS-79885 |
| Valor Dedução Exigibilidade Suspensa | Valor Dedução Exigibilidade Suspensa | Texto | S | N | 0,00 | 0,00 | Valor da dedução relativa a dependentes ou a pensão alimentícia com exigibilidade suspensa | MFS-79885 |
| Informações Complementares - RRA | Informações Complementares - RRA | Informações Complementares - RRA | Informações Complementares - RRA | Informações Complementares - RRA | Informações Complementares - RRA | Informações Complementares - RRA | Informações Complementares - RRA | Informações Complementares - RRA |
| Tipo Processo | Tipo Processo | Texto | S | N | Código - Descrição | Código - Descrição | Informar o código e descrição correspondente ao tipo de processo:   Lista de Valores Válidos: 1 - Administrativo;  2 – Judicial; 3 – Sem Processo | MFS-79885 MFS-805178 |
| Núm. Processo | Núm. Processo | Texto | S | N |  |  | Informar o número do processo/requerimento administrativo/judicial. | MFS-79885 |
| Origem dos Recursos | Origem dos Recursos | Texto | S | N | Código - Descrição | Código - Descrição | Informar o indicativo da origem dos recursos.  Lista de Valores Válidos:   1-Recursos do próprio declarante;  2-Recursos de terceiros - Declarante é a instituição financeira responsável pelo repasse dos valores | MFS-79885 |
| Descrição | Descrição | Texto | S | N |  |  | Descrição dos Rendimentos Recebidos Acumuladamente - RRA. | MFS-79885 |
| Qtd Meses | Qtd Meses | Texto | S | N | 0,0 | 0,0 | Informar o número de meses relativo aos Rendimentos Recebidos Acumuladamente - RRA | MFS-79885 |
| CNPJ Origem Recursos | CNPJ Origem Recursos | Texto | S | N | XX.XXX.XXX/XXXX-XX | XX.XXX.XXX/XXXX-XX | CNPJ da empresa que repassou os recursos. | MFS-79885 |
| Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial |
| Valor Despesas Custas Judiciais | Valor Despesas Custas Judiciais | Texto | S | N | 0,00 | 0,00 | Informar o valor da despesa com custas judiciais | MFS-79885 |
| Valor Despesa Advogados | Valor Despesa Advogados | Texto | S | N | 0,00 | 0,00 | Informar o valor da despesa com advogado(s). | MFS-79885 |
| Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado |
| Tipo Inscrição | Tipo Inscrição | Texto | S | N | Código - Descrição | Código - Descrição | Tipo de inscrição do advogado.  Lista de Valores Válidos: 1-CNPJ;  2-CPF | MFS-79885 |
| Núm. Inscrição | Núm. Inscrição | Texto | S | N |  |  | Informar o número de inscrição do advogado. | MFS-79885 |
| Valor Advogado | Valor Advogado | Texto | S | N | 0,00 | 0,00 | Valor da despesa com o advogado. | MFS-79885 |
| Informações de Processo Judicial | Informações de Processo Judicial | Informações de Processo Judicial | Informações de Processo Judicial | Informações de Processo Judicial | Informações de Processo Judicial | Informações de Processo Judicial | Informações de Processo Judicial | Informações de Processo Judicial |
| Núm. Processo | Núm. Processo | Texto | S | N |  |  | Informar o número do processo judicial | MFS-79885 |
| Origem Recurso | Origem Recurso | Texto | S | N | Código - Descrição | Código - Descrição | Informar o indicativo da origem dos recursos:   Lista de Valores Válidos:  1 - Recursos do próprio declarante;  2 - Recursos de terceiros - Declarante é a instituição financeira responsável pelo repasse dos valores. | MFS-79885 |
| CNPJ Origem Recurso | CNPJ Origem Recurso | Texto | S | N |  |  | Informar o CNPJ da empresa que repassou os recursos. | MFS-79885 |
| Descrição | Descrição | Texto | S | N |  |  | Descrição | MFS-79885 |
| Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial |
| Valor Despesas Custas Judiciais | Valor Despesas Custas Judiciais | Texto | S | N | 0,00 | 0,00 | Informar o valor da despesa com custas judiciais | MFS-79885 |
| Valor Despesa Advogados | Valor Despesa Advogados | Texto | S | N | 0,00 | 0,00 | Informar o valor da despesa com advogado(s). | MFS-79885 |
| Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado |
| Tipo Inscrição | Tipo Inscrição | Texto | S | N | Código - Descrição | Código - Descrição | Tipo de inscrição do advogado.  Lista de Valores Válidos: 1-CNPJ;  2-CPF | MFS-79885 |
| Núm. Inscrição | Núm. Inscrição | Texto | S | N |  |  | Informar o número de inscrição do advogado. | MFS-79885 |
| Valor Advogado | Valor Advogado | Texto | S | N | 0,00 | 0,00 | Valor da despesa com o advogado. | MFS-79885 |
| Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior |
| Ind. Núm. Identificação Fiscal | Ind. Núm. Identificação Fiscal | Texto | S | N | Código - Descrição | Código - Descrição | Informar o indicativo do Número de Identificação Fiscal - NIF:  Lista de Valores Válidos:  1-Beneficiário com NIF; 2-Beneficiário dispensado do NIF;  3-País não exige NIF. | MFS-79885 |
| Núm. Identificação Fiscal | Núm. Identificação Fiscal | Texto | S | N |  |  | Informar o número de Identificação Fiscal - NIF. | MFS-79885 |
| Forma de Tributação | Forma de Tributação | Texto | S | N |  |  | Informar a forma de tributação. | MFS-79885 |
| Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior |
| Logradouro | Logradouro | Texto | S | N |  |  | Informar o logradouro | MFS-79885 |
| Núm. | Núm. | Texto | S | N |  |  | Informar o número do logradouro. | MFS-79885 |
| Complemento | Complemento | Texto | S | N |  |  | Informar o complemento do logradouro. | MFS-79885 |
| Bairro | Bairro | Texto | S | N |  |  | Informar o bairro | MFS-79885 |
| Cidade | Cidade | Texto | S | N |  |  | Informar a cidade | MFS-79885 |
| Estado | Estado | Texto | S | N |  |  | Informar o estado | MFS-79885 |
| Cód. Postal | Cód. Postal | Texto | S | N |  |  | Informar o código postal (CEP) | MFS-79885 |
| Telefone | Telefone | Texto | S | N |  |  | Informar o telefone. | MFS-79885 |
| Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde | Identificação da Operadora do Plano Privado Coletivo Empresarial de Assistência à Saúde |
| Núm. Inscrição | Núm. Inscrição | Texto | S | N |  |  | Informar o número do CNPJ da operadora de plano privado coletivo empresarial de assistência à saúde. | MFS-79885 |
| Registro ANS | Registro ANS | Texto | S | N |  |  | Informar o Registro na Agência Nacional de Saúde - ANS. | MFS-79885 |
| Valor Saúde | Valor Saúde | Texto | S | N | 0,00 | 0,00 | Informar o valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do titular | MFS-79885 |
| Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Titular do Plano de Saúde Coletivo Empresarial |
| Tipo Inscrição | Tipo Inscrição | Texto | S | N | Código - Descrição | Código - Descrição | Tipo de Inscrição  Lista de Valores Válidos 1 - Pessoa jurídica;  2 - Pessoa física. | MFS-79885 |
| Núm. Inscrição | Núm. Inscrição | Texto | S | N | XX.XXX.XXX/XXXX-XX ou XXX.XXX.XXX-XX | XX.XXX.XXX/XXXX-XX ou XXX.XXX.XXX-XX | Número de Inscrição | MFS-79885 |
| Valor Reembolso | Valor Reembolso | Texto | S | N | 0,00 | 0,00 | Valor do Reembolso relativo ao período da apuração | MFS-79885 |
| Valor Reembolso Anos Anteriores | Valor Reembolso Anos Anteriores | Texto | S | N | 0,00 | 0,00 | Valor do Reembolso relativo aos anos anteriores | MFS-79885 |
| Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial | Informações de Dependente do Plano de Saúde Coletivo Empresarial |
| CPF | CPF | Texto | S | N | XXX.XXX.XXX-XX | XXX.XXX.XXX-XX | CPF do dependente | MFS-79885 |
| Valor Saúde | Valor Saúde | Texto | S | N | 0,00 | 0,00 | Valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do dependente | MFS-79885 |
| Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial | Informação de Reembolso do Dependente do Plano de Saúde Coletivo Empresarial |
| Tipo Inscrição | Tipo Inscrição | Texto | S | N | Código - Descrição | Código - Descrição | Informar o tipo de inscrição do prestador de serviços  Lista de Valores Válidos 1 - Pessoa jurídica;  2 - Pessoa física. | MFS-79885 |
| Núm. Inscrição | Núm. Inscrição | Texto | S | N | XX.XXX.XXX/XXXX-XX ou XXX.XXX.XXX-XX | XX.XXX.XXX/XXXX-XX ou XXX.XXX.XXX-XX | Informar o número de inscrição do prestador de serviços de assistência médica. | MFS-79885 |
| Valor Reembolso Per. Apur, | Valor Reembolso Per. Apur, | Texto | S | N | 0,00 | 0,00 | Informar o valor do reembolso relativo ao período. | MFS-79885 |
| Valor Reembolso Anos Anteriores | Valor Reembolso Anos Anteriores | Texto | S | N | 0,00 | 0,00 | Informar o valor do reembolso relativo aos anos anteriores. | MFS-79885 |
| R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica | R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica |
| Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento |
| Tipo de Inscrição | Tipo de Inscrição | Texto | S | N |  |  | Irá demonstrar o tipo de inscrição do estabelecimento   1-CNPJ | MFS-79890 |
| Número de Inscrição | Número de Inscrição | Texto | S | N |  |  |  | MFS-79890 |
| Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento | Ocorrência/ Identificação do Beneficiário do Rendimento |
| Data da Ocorrência | Data da Ocorrência | Texto | S | N |  |  | Irá demonstrar a data da ocorrência do R-4010 em questão. | MFS-79890 |
| Operação | Operação | Texto | S | N |  |  | Irá demonstrar   - Original - Retificadora | MFS-79890 |
| Situação | Situação | Texto | S | N |  |  | Irá demonstrar a situação do R-4010 em questão. | MFS-79890 |
| CNPJ | CNPJ | Texto | S | N | XXX.XXX.XXX-XX | XXX.XXX.XXX-XX | CNPJ do Beneficiário | MFS-79890 |
| Nome | Nome | Texto | S | N |  |  | Nome do Beneficiário | MFS-79890 |
| IsenImun | IsenImun | Texto | S | N | Código-Descrição | Código-Descrição | Informações sobre isenção e imunidade: 1 - Entidade não isenta/não imune - Tributação normal; 2- Instituição de educação e de assistência social sem fins lucrativos, a que se refere o art. 12 da Lei nº 9.532, de 10 de dezembro de 1997; 3- Instituição de caráter filantrópico, recreativo, cultural, científico e às associações civis, a que se refere o art. 15 da Lei nº 9.532, de 1997. | MFS-79890 |
| ideEvtAdic | ideEvtAdic | Texto | S | N |  |  | Identificador de evento adicional por beneficiário, a critério do declarante.  Apresentar este campo a partir da versão 2.1.2 | MFS-537195 |
| Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento |
| Natureza do Rendimento | Natureza do Rendimento | Texto | S | N |  |  | Natureza de Rendimento | MFS-79890 |
| Observação | Observação | Texto | S | N | Descrição | Descrição | Observação | MFS-79890 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data da Ocorrência | Data da Ocorrência | Texto | S | N |  |  | Irá demonstrar a data da ocorrência do R-4020 em questão. | MFS-79890 |
| Operação | Operação | Texto | S | N |  |  | Irá demonstrar   - Original - Retificadora | MFS-79890 |
| Situação | Situação | Texto | S | N |  |  | Irá demonstrar a situação do R-4020 em questão. | MFS-79890 |
| Informações Relativas ao Pagamento | Informações Relativas ao Pagamento | Informações Relativas ao Pagamento | Informações Relativas ao Pagamento | Informações Relativas ao Pagamento | Informações Relativas ao Pagamento | Informações Relativas ao Pagamento | Informações Relativas ao Pagamento | Informações Relativas ao Pagamento |
| Fato Gerador | Fato Gerador | Texto | S | N | DD/MM/AAAA | DD/MM/AAAA | Data do Fato Gerador | MFS-79890 |
| Valor Bruto | Valor Bruto | Texto | S | N | 0,00 | 0,00 | Valor do rendimento bruto | MFS-79890 |
| FCI_SCP | FCI_SCP | Texto | S | N | Código - Descrição | Código - Descrição | Indicador de FCI e SCP  Lista de Valores Válidos: 1-FCI;  2-SCP | MFS-79890 |
| Núm. Insc. FCI_SCP | Núm. Insc. FCI_SCP | Texto | S | N | XX.XXX.XXX/XXXX-XX | XX.XXX.XXX/XXXX-XX | Número da Inscrição de FCI/SCP | MFS-79890 |
| % SCP | % SCP | Texto | S | N | 999 | 999 | Percentual de SCP | MFS-79890 |
| IndJud | IndJud | Texto | S | N | Código | Código | Informar o Indicativo exclusivo de rendimento de natureza diversa de RRA e que seja oriundo de decisão judicial  Lista de Valores Válidos: S; N | MFS-79890 |
| País Resid. Exterior | País Resid. Exterior | Texto | S | N | 999 | 999 | Informar o código do país de destino da remessa do pagamento a residente ou domiciliado no exterior. | MFS-79890 |
| dtEscrCont | dtEscrCont | Texto | S | N | DD/MM/AAAA | DD/MM/AAAA | Data da escrituração contábil.  Apresentar este campo a partir da versão 2.1.2 | MFS-537195 |
| observ | observ | Texto | S | N |  |  | Observações  Apresentar este campo a partir da versão 2.1.2 | MFS-537195 |
| Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte | Informações Relativas a Retenções na Fonte |
| Valor Base IR | Valor Base IR | Texto | S | N | 0,00 | 0,00 | Valor da Base de retenção do Imposto de Renda. | MFS-79890 |
| Valor IR | Valor IR | Texto | S | N | 0,00 | 0,00 | Valor da retenção do Imposto de Renda. | MFS-79890 |
| Valor Base Agreg | Valor Base Agreg | Texto | S | N | 0,00 | 0,00 | Valor da Base de retenção de tributos de forma agregada. | MFS-79890 |
| Valor Agreg | Valor Agreg | Texto | S | N | 0,00 | 0,00 | Valor da retenção em valor agregado de tributos. | MFS-79890 |
| Valor Base CSLL | Valor Base CSLL | Texto | S | N | 0,00 | 0,00 | Valor da Base de retenção de CSLL. | MFS-79890 |
| Valor CSLL | Valor CSLL | Texto | S | N | 0,00 | 0,00 | Valor da retenção da CSLL. | MFS-79890 |
| Valor Base COFINS | Valor Base COFINS | Texto | S | N | 0,00 | 0,00 | Valor da Base de retenção de COFINS | MFS-79890 |
| Valor COFINS | Valor COFINS | Texto | S | N | 0,00 | 0,00 | Valor da retenção da COFINS. | MFS-79890 |
| Valor Base PIS/PASEP | Valor Base PIS/PASEP | Texto | S | N | 0,00 | 0,00 | Valor da Base de retenção da PIS/PASEP. | MFS-79890 |
| Valor PIS/PASEP | Valor PIS/PASEP | Texto | S | N | 0,00 | 0,00 | Valor da retenção da PIS/PASEP. | MFS-79890 |
| Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais | Processos Relacionados a não Retenção de Tributos ou Depósitos Judiciais |
| Tipo Processo | Tipo Processo | Texto | S | N | Código - Descrição | Código - Descrição | Preencher com o código correspondente ao tipo de processo  Lista de Valores Válidos: 1 - Administrativo;  2 - Judicial. | MFS-79890 |
| Núm. Processo | Núm. Processo | Texto | S | N |  |  | Informar o número do processo administrativo/judicial. | MFS-79890 |
| Cód. Suspensão | Cód. Suspensão | Texto | S | N |  |  | Informar o código indicativo da suspensão | MFS-79890 |
| Valor Base Susp IR | Valor Base Susp IR | Texto | S | N | 0,00 | 0,00 | Valor da base do IR com exigibilidade suspensa. | MFS-79890 |
| Valor N IR | Valor N IR | Texto | S | N | 0,00 | 0,00 | Valor da retenção que deixou de ser efetuada relativo ao Imposto de Renda. | MFS-79890 |
| Valor Dep IR | Valor Dep IR | Texto | S | N | 0,00 | 0,00 | Valor do depósito judicial de IR. | MFS-79890 |
| Valor Base Susp CSLL | Texto | Texto | S | N | N | 0,00 | Valor da base de CSLL com exigibilidade suspensa. | MFS-79890 |
| Valor N CSLL | Valor N CSLL | Texto | S | N | 0,00 | 0,00 | Valor da retenção que deixou de ser efetuada relativo a CSLL. | MFS-79890 |
| Valor Dep CSLL | Valor Dep CSLL | Texto | S | N | 0,00 | 0,00 | Valor do depósito judicial de CSLL. | MFS-79890 |
| Valor Base Susp COFINS | Valor Base Susp COFINS | Texto | S | N | 0,00 | 0,00 | Valor da base de COFINS com exigibilidade suspensa. | MFS-79890 |
| Valor N COFINS | Valor N COFINS | Texto | S | N | 0,00 | 0,00 | Valor da retenção que deixou de ser efetuada relativo a COFINS. | MFS-79890 |
| Valor Dep COFINS | Valor Dep COFINS | Texto | S | N | 0,00 | 0,00 | Valor do depósito judicial de COFINS. | MFS-79890 |
| Valor Base Susp PIS/PASEP | Valor Base Susp PIS/PASEP | Texto | S | N | 0,00 | 0,00 | Valor da base de PIS/PASEP com exigibilidade suspensa. | MFS-79890 |
| Valor N PIS/PASEP | Valor N PIS/PASEP | Texto | S | N | 0,00 | 0,00 | Valor da retenção que deixou de ser efetuada relativo a PIS/PASEP. | MFS-79890 |
| Valor Dep PIS/PASEP | Valor Dep PIS/PASEP | Texto | S | N | 0,00 | 0,00 | Valor do depósito judicial de PIS/PASEP. | MFS-79890 |
| Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial | Informações Complementares Relativas a Rendimentos Decorrentes de Decisão Judicial |
| Núm. Processo | Núm. Processo | Texto | S | N |  |  | Informar o número do processo judicial | MFS-79890 |
| Origem Recurso | Origem Recurso | Texto | S | N | Código - Descrição | Código - Descrição | Informar o indicativo da origem dos recursos:   Lista de Valores Válidos:  1 - Recursos do próprio declarante;  2 - Recursos de terceiros - Declarante é a instituição financeira responsável pelo repasse dos valores. | MFS-79890 |
| CNPJ Origem Recurso | CNPJ Origem Recurso | Texto | S | N |  |  | Informar o CNPJ da empresa que repassou os recursos. | MFS-79890 |
| Descrição | Descrição | Texto | S | N |  |  | Descrição | MFS-79890 |
| Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial | Despesas com Processo Judicial |
| Valor Despesas Custas Judiciais | Valor Despesas Custas Judiciais | Texto | S | N | 0,00 | 0,00 | Informar o valor da despesa com custas judiciais | MFS-79890 |
| Valor Despesa Advogados | Valor Despesa Advogados | Texto | S | N | 0,00 | 0,00 | Informar o valor da despesa com advogado(s). | MFS-79890 |
| Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado | Identificação do Advogado |
| Tipo Inscrição | Tipo Inscrição | Texto | S | N | Código - Descrição | Código - Descrição | Tipo de inscrição do advogado.  Lista de Valores Válidos: 1-CNPJ;  2-CPF | MFS-79890 |
| Núm. Inscrição | Núm. Inscrição | Texto | S | N |  |  | Informar o número de inscrição do advogado. | MFS-79890 |
| Valor Advogado | Valor Advogado | Texto | S | N | 0,00 | 0,00 | Valor da despesa com o advogado. | MFS-79890 |
| Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior | Informações Complementares Relativas a Pagamentos no Exterior |
| Ind. Núm. Identificação Fiscal | Ind. Núm. Identificação Fiscal | Texto | S | N | Código - Descrição | Código - Descrição | Informar o indicativo do Número de Identificação Fiscal - NIF:  Lista de Valores Válidos:  1-Beneficiário com NIF; 2-Beneficiário dispensado do NIF;  3-País não exige NIF. | MFS-79890 |
| Núm. Identificação Fiscal | Núm. Identificação Fiscal | Texto | S | N |  |  | Informar o número de Identificação Fiscal - NIF. | MFS-79890 |
| Rel. Fonte Pagadora | Rel. Fonte Pagadora | Texto | S | N |  |  | Informar a relação da fonte pagadora do beneficiário. | MFS-79890 |
| Forma de Tributação | Forma de Tributação | Texto | S | N |  |  | Informar a forma de tributação. | MFS-79890 |
| Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior | Endereço do Beneficiário Residente ou Domiciliado no Exterior |
| Logradouro | Logradouro | Texto | S | N |  |  | Informar o logradouro | MFS-79890 |
| Núm. | Núm. | Texto | S | N |  |  | Informar o número do logradouro. | MFS-79890 |
| Complemento | Complemento | Texto | S | N |  |  | Informar o complemento do logradouro. | MFS-79890 |
| Bairro | Bairro | Texto | S | N |  |  | Informar o bairro | MFS-79890 |
| Cidade | Cidade | Texto | S | N |  |  | Informar a cidade | MFS-79890 |
| Estado | Estado | Texto | S | N |  |  | Informar o estado | MFS-79890 |
| Cód. Postal | Cód. Postal | Texto | S | N |  |  | Informar o código postal (CEP) | MFS-79890 |
| Telefone | Telefone | Texto | S | N |  |  | Informar o telefone. | MFS-79890 |
| R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados | R-4040 - Pagamentos/créditos a beneficiários não identificados |
| Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento |
| Tipo de Inscrição | Tipo de Inscrição | Texto | S | N |  |  | Irá demonstrar o tipo de inscrição do estabelecimento   1-CNPJ | MFS-79893 |
| Número de Inscrição | Número de Inscrição | Texto | S | N |  |  |  | MFS-79893 |
| ideEvtAdic | ideEvtAdic | Texto | S | N |  |  | Identificador de evento adicional por beneficiário, a critério do declarante.  Apresentar este campo a partir da versão 2.1.2 | MFS-537211 |
| Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento | Identificação da Natureza do Rendimento |
| Natureza do Rendimento | Natureza do Rendimento | Texto | S | N |  |  |  | MFS-79893 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data da Ocorrência | Data da Ocorrência | Texto | S | N |  |  | Irá demonstrar a data da ocorrência do R-4040 em questão. | MFS-79893 |
| Operação | Operação | Texto | S | N |  |  | Irá demonstrar   - Original - Retificadora | MFS-79893 |
| Situação | Situação | Texto | S | N |  |  | Irá demonstrar a situação do R-4040 em questão. | MFS-79893 |
| Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados | Informações do Pagamento a Beneficiários Não Identificados |
| Data do Movimento | Data do Movimento | Texto | S | N |  |  |  | MFS-79893 |
| Valor Líquido | Valor Líquido | Texto | S | N |  |  |  | MFS-79893 |
| Valor Reajustado | Valor Reajustado | Texto | S | N |  |  |  | MFS-79893 |
| Valor do Imposto de Renda Retido na Fonte | Valor do Imposto de Renda Retido na Fonte | Texto | S | N |  |  |  | MFS-79893 |
| dtEscrCont | dtEscrCont | Texto | S | N | DD/MM/AAAA | DD/MM/AAAA | Data da escrituração contábil.  Apresentar este campo a partir da versão 2.1.2 | MFS-537211 |
| Descrição | Descrição | Texto | S | N |  |  |  | MFS-79893 |
| Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais |
| Tipo de Processo | Tipo de Processo | Texto | S | N |  |  |  | MFS-79893 |
| Número do Processo Judicial | Número do Processo Judicial | Texto | S | N |  |  |  | MFS-79893 |
| Código de Suspensão | Código de Suspensão | Texto | S | N |  |  |  | MFS-79893 |
| Valor da Base com Exigibilidade Suspensa | Valor da Base com Exigibilidade Suspensa | Texto | S | N |  |  |  | MFS-79893 |
| Valor da Retenção que Deixou de ser Efetuada | Valor da Retenção que Deixou de ser Efetuada | Texto | S | N |  |  |  | MFS-79893 |
| Valor do Depósito Judicial | Valor do Depósito Judicial | Texto | S | N |  |  |  | MFS-79893 |
| R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento | R-4080 – Retenção no Recebimento |
| Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento | Identificação do Estabelecimento |
| Tipo de Inscrição | Tipo de Inscrição | Texto | S | N |  |  | Irá demonstrar o tipo de inscrição do estabelecimento   1-CNPJ | MFS-79907 |
| Número de Inscrição | Número de Inscrição | Texto | S | N |  |  |  | MFS-79907 |
| Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento | Identificação do Rendimento |
| Natureza do Rendimento | Natureza do Rendimento | Texto | S | N |  |  |  | MFS-79907 |
| Observações | Observações | Texto | S | N |  |  |  | MFS-79907 |
| Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento | Ocorrência/ Identificação da Fonte Pagadora do Rendimento |
| Data da Ocorrência | Data da Ocorrência | Texto | S | N |  |  | Irá demonstrar a data da ocorrência do R-4080 em questão. | MFS-79907 |
| Operação | Operação | Texto | S | N |  |  | Irá demonstrar   - Original - Retificadora | MFS-79907 |
| Situação | Situação | Texto | S | N |  |  | Irá demonstrar a situação do R-4080 em questão. | MFS-79907 |
| CNPJ da Fonte Pagadora | CNPJ da Fonte Pagadora | Texto | S | N |  |  |  | MFS-79907 |
| Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento | Informações Relativas ao Recebimento do Rendimento |
| Data do Recebimento | Data do Recebimento | Texto | S | N |  |  |  | MFS-79907 |
| Valor Bruto | Valor Bruto | Texto | S | N |  |  |  | MFS-79907 |
| Valor Base IR | Valor Base IR | Texto | S | N |  |  |  | MFS-79907 |
| Valor do Imposto de Renda Retido na Fonte | Valor do Imposto de Renda Retido na Fonte | Texto | S | N |  |  |  | MFS-79907 |
| Observ | Observ | Texto | S | N |  |  |  | MFS-537238 |
| Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais | Informações de Processos Relacionados a não Retenção de Tributos ou a Depósitos Judiciais |
| Tipo de Processo | Tipo de Processo | Texto | S | N |  |  |  | MFS-79907 |
| Número do Processo Judicial | Número do Processo Judicial | Texto | S | N |  |  |  | MFS-79907 |
| Código de Suspensão | Código de Suspensão | Texto | S | N |  |  |  | MFS-79907 |
| Valor da Base com Exigibilidade Suspensa | Valor da Base com Exigibilidade Suspensa | Texto | S | N |  |  |  | MFS-79907 |
| Valor da Retenção que Deixou de ser Efetuada | Valor da Retenção que Deixou de ser Efetuada | Texto | S | N |  |  |  | MFS-79907 |
| Valor do Depósito Judicial | Valor do Depósito Judicial | Texto | S | N |  |  |  | MFS-79907 |
