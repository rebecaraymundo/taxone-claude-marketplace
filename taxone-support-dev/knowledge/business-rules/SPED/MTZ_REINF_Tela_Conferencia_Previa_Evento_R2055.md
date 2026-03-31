# MTZ_REINF_Tela_Conferencia_Previa_Evento_R2055

> Fonte: MTZ_REINF_Tela_Conferencia_Previa_Evento_R2055.docx






THOMSON REUTERS

Conferência Prévia Evento R-2055
SPED – Reinf



DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: REINF >> Conferência Prévia >> Evento R-2055

Título da tela: Conferência Prévia do Evento R-2055

Obs: Ao abrir a tela de conferência deverá abrir uma subtela para seleção do período de geração.
Atenção: Para recuperar a apuração, se faz necessário ter sido executada a geração prévia do evento R-2055 (Menu: REINF >> Geração Prévia >> Evento R-2055).








| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-58348 | Alessandra Cristina Navatta | Criação da Tela |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N |  | Irá demonstrar o estabelecimento selecionado na chamada da subtela de seleção. | MFS-58348 |
| Período (MM/AAAA) | Texto | S | N |  | Irá demonstrar o período de apuração. | MFS-58348 |
| Versão | Texto | S | N |  | Irá demostrar a versão de Leiaute da EFD-REINF | MFS-58348 |
| Evento | Texto | S | N |  | Fixo R-2055 –Aquisição de Produção Rural | MFS-58348 |


| R-2055 – Aquisição de Produção Rural |
| --- |
| Identificação do Estabelecimento Adquirente da Produção |


| Tipo de Inscrição | Textbox | S | N |  | Irá demonstrar o tipo de inscrição do estabelecimento.  1-CNPJ | MFS-58348 |
| --- | --- | --- | --- | --- | --- | --- |
| Número de Inscrição | Textbox | S | N |  | Irá demonstrar o número de inscrição do estabelecimento. | MFS-58348 |
| Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência | Ocorrência |
| Data da Ocorrência | Texto | S | N |  | Irá demonstrar a data da ocorrência do R-2055 em questão. | MFS-58348 |
| Operação | Texto | S | N |  | Irá demonstrar   - Original - Retificadora | MFS-58348 |
| Situação | Texto | S | N |  | Irá demonstrar a situação do R-2055 em questão. | MFS-58348 |
| Retificação S-1250 | Texto | S | N |  | Por definição do Fisco, neste momento, não será validado este campo. | MFS-58348 |


| Identificação do Produtor Rural |
| --- |


| Tipo de Inscrição | Texto | S | N | 1 – CNPJ  ou  2 - CPF | Conteúdo do campo 20-tpInscProd do R-2055 em questão. | MFS-58348 |
| --- | --- | --- | --- | --- | --- | --- |
| Número de Inscrição | Texto | S | N |  | Conteúdo do campo 21- nrInscProd do R-2055 em questão. | MFS-58348 |
| Indicador OpcCP | Texto | S | N |  | Conteúdo do campo 22 – indOpcCP do R-2055 em questão. | MFS-58348 |
| Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural | Detalhamento da Aquisição de Produção Rural |
| Indicador de Aquisição | Texto | S | N |  | Irá demonstrar:  1 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral;  2 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade executora do Programa de Aquisição de Alimentos - PAA;  3 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA;  4 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral - Produção isenta (Lei 13.606/2018); 5 - Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade executora do PAA - Produção isenta (Lei 13.606/2018); 6 - Aquisição de produção de produtor rural pessoa jurídica por entidade executora do PAA - Produção isenta (Lei 13.606/2018); 7 - Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação | MFS-58348 |
| Valor da Receita Bruta Total | Texto | S | N |  | Conteúdo do campo “25-vlrBruto” referente ao R-2055 em questão. | MFS-58348 |
| Valor da Contribuição Previdenciária | Texto | S | N |  | Conteúdo do campo “26- vlrCPDescPR” referente ao R-2055 em questão. | MFS-58348 |
| Valor da Contribuição Previdenciária GILRAT | Texto | S | N |  | Conteúdo do campo “27- vlrRatDescPR” referente ao R-2055 em questão. | MFS-58348 |
| Valor da Contribuição Previdenciária SENAR | Texto | S | N |  | Conteúdo do campo “28- vlrSenarDesc” referente ao R-2055 em questão. | MFS-58348 |
| Totais R-5001  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. | Totais R-5001  Nesta aba são exibidos os totais calculados pelo Fisco por Código de Receita (pode existir mais de uma ocorrência). Trata-se dos campos da tag “RAquis” do evento R-5001, enviado pelo Fisco no ato do recebimento do evento R-2055. Estas informações só existirão no caso dos eventos já recepcionados pelo Fisco com sucesso (ou advertência), e são obtidas no XML de retorno enviado pelo integrador do Onesource. |
| Código de Receita | Alfanumérico | N | N | Formato: 9999-99 | Conteúdo do campo “56-CRAquis” do evento R-5001 referente ao R-2055 em questão. | MFS-58348 |
| Valor Contribuição Previdenciária | Numérico | N | N |  | Conteúdo do campo “57-vlrCRAquis” do evento R-5001 referente ao R-2055 em questão. | MFS-58348 |
| Valor Contribuição Previdenciária Exigibilidade Suspensa | Numérico | N | N |  | Conteúdo do campo “58-vlrCRAquisSusp” do evento R-5001 referente ao R-2055 em questão. | MFS-58348 |
| Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural | Informação do Processo Judicial do Produtor Rural |
| Número do Processo Judicial | Texto | S | N |  | Conteúdo do campo 30 – nrProcJud referente ao R-2055 em questão. | MFS-58348 |
| Código da Suspensão | Texto | S | N |  | Conteúdo do campo 31 – CodSusp referente ao R-2055 em questão. | MFS-58348 |
| Valor da Contribuição Previdenciária | Texto | S | N |  | Conteúdo do campo 32 – vlrCPNRet referente ao R-2055 em questão. | MFS-58348 |
| Valor da Contribuição Previdenciária GILRAT | Texto | S | N |  | Conteúdo do campo 33 – vlrRatNRet referente ao R-2055 em questão. | MFS-58348 |
| Valor da Contribuição Previdenciária SENAR | Texto | S | N |  | Conteúdo do campo 34 – vlrSenarNRet referente ao R-2055 em questão. | MFS-58348 |
