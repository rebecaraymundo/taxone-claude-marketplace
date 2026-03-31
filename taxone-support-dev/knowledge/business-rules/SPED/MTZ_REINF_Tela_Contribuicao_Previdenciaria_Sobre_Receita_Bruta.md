# MTZ_REINF_Tela_Contribuicao_Previdenciaria_Sobre_Receita_Bruta

> Fonte: MTZ_REINF_Tela_Contribuicao_Previdenciaria_Sobre_Receita_Bruta.docx






THOMSON REUTERS

CPRB – Contribuição Previdenciária Sobre a Receita Bruta
EFD-REINF



DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	4


## Regras dos Campos


Localização da tela: Módulo: SPED >> REINF
Menu: CPRB >> Contribuição Previdenciária Sobre a Receita Bruta

Título da tela: CPRB – Contribuição Previdenciária Sobre a Receita Bruta


Sugestão de Tela:




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS8485 | Elenilson Coutinho | Inclusão dos campos de valores e aba ajustes para calculo CPRB, separados por obrigação “Sped Contribuições e REINF” |
| MFS14461 | Lara Aline | Inclusão de nova aba para as informações do registro infoProc (Processos relacionados a Suspensão da CPRB). |
| MFS16181 | Lara Aline | Retirada obrigatoriedade dos campos Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta e Valor Contrib. Prev. Sobre Receita Bruta |
| MFS17215 | Lara Aline | Ajuste na recuperação do campo Valor Receita Bruta – Total e ajuste na tela completa para quando usuário preencher manual os campos dessa tela. |
| MFS18794 | Lara Aline | Inclusão do código de ajuste 11 para o tipo de ajuste = Redução |
| MFS18785 | Lara Aline | Inclusão da indicação da SAFX252 na regra dos campos Valor Ajuste Adição e Valor Ajuste Exclusão |
| MFS19609 | Lara Aline | Remoção do controle de código de ajuste por tipo de ajuste. |
| MFS20401 | Lara Aline | Remoção dos códigos 12 e 13 do campo tipo de ajuste. |
| MFS-717349 | Alessandra Navatta | Documentar a regra do campo Código de receita |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Código da Receita | Lista | S | S | Código - descrição | Código Receita, valores válidos:  Este campo será recuperado da dwt_cod_receita filtrando o tributo CPRB. | MFS-717349 |
| Valor Receita Bruta - Total | Text Box | S | N |  | Este campo deve ser apresentado bloqueado para edição, tendo seu valor preenchido a partir da tela 'Receita Bruta do Estabelecimento'.  Quando o usuário efetuar o preenchimento manual dessa tela, nesse campo deve ser recuperado o valor automaticamente da tela 'Receita Bruta do Estabelecimento' de acordo com o Estabelecimento e período informado, considerando para o período o mês/ano da Data Inicial informada.  Como se trata de um campo obrigatório. Caso não houver informação para o período e estabelecimento na tela 'Receita Bruta do Estabelecimento', não permitir a gravação do cadastro na tela e exibir a seguinte mensagem: “Valor Receita Bruta – Total não encontrado, essa informação deve ser previamente cadastrada na tela 'Receita Bruta do Estabelecimento'. | MFS17215 |
| Valor Receita Bruta - Atividade | Text Box | S | S |  | Informar o Valor Receita Bruta da atividade.  Caso não preenchido exibir a seguinte mensagem: “O campo Valor Receita Bruta - Atividade deve ser informado” | MFS17215 |
| Valor Exclusões da Receita Bruta | Text Box | N | N |  | Gerar com a somatória do campo “valor de ajuste” da aba (Ajustes da Contribuição Previdenciária Apurada) quando tipo de ajuste for igual a “0” (ajuste de redução). e código de ajuste igual a 4, 5, 6, 7, 8, 9, 10 e/ou 11. | MFS8485 MFS18794 MFS19609 |
| Alíquota Contrib. Prev. Sobre Receita Bruta | Text Box | S | N |  | Informar com o valor da alíquota vinculada ao código de atividade da TACES75.   Campo desabilitado para preenchimento. | MFS17215 |
| *Valores EFD - Contribuições |  |  |  |  |  |  |
| Valor Receita demais atividades | Text Box | N | S |  | Informar o valor das demais atividades. | MFS8485 |
| Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta | Text Box | N | S |  | Informar o valor da base de cálculo.   Valor deverá ser igual a “Valor Receita Bruta - Atividade” (-) Valor Exclusões da Receita Bruta. Caso contrário, exibir a seguinte mensagem: “O Valor informado no Campo “Valor Base de Cálculo – Contrib”. Prev. Sobre Receita Bruta deve ser igual ao valor Receita Bruta – Atividade menos o valor do campo ‘Valor Exclusões da Receita Bruta’, deseja continuar?    Caso o Valor Exclusões da Receita Bruta for maior que o Valor Receita Bruta – Atividade exibir a seguinte mensagem: Valor Exclusões da Receita Bruta excede o Valor da Receita Bruta - Atividade do período. Nesse caso será gravado o valor 0 - zero.”.  E será gravado do valor zero no campo.  Obs: Caso não preenchido exibir a seguinte mensagem: “Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta não preenchida”. | MFS8485 MFS16181 MFS17215 |
| Valor Contrib. Prev. Sobre Receita Bruta | Text Box | N | S |  | Informar o valor da contribuição apurada. Valor deverá ser igual a “Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta” (*) Alíquota Contrib. Prev. Receita Bruta.   Caso contrário, exibir a seguinte mensagem: “Valor Contrib. Prev. Sobre Receita Bruta deve ser igual ao valor Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta multiplicado pelo valor do campo ‘Alíquota Contrib. Prev. sobre Receita Bruta’, deseja continuar?   Caso a multiplicação do campo Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta pelo valor do campo ‘Alíquota Contrib. Prev. sobre Receita Bruta resultar em um valor menor que zero exibir a seguinte mensagem: A multiplicação do campo Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta pelo valor do campo ‘Alíquota Contrib. Prev. sobre Receita Bruta resulta um valor negativo. Nesse caso será gravado o valor 0 - zero.”  E será gravado do valor zero no campo.   Obs: Caso não preenchido, exibir a seguinte mensagem: “Valor Valor Contrib. Prev. Sobre Receita Bruta não preenchido” | MFS8485 MFS16181 MFS17215 |
| * Valores EFD - REINF | Text Box | S | S |  |  | MFS8485 |
| Valor Ajuste Adição | Text Box | N | S | Default= Desabilitado | Informar o valor ajuste de adição. Valor deve ser igual à somatória do campo “Valor de Ajuste” quando “Tipo de Ajuste” igual a “1”. (SAFX252) | MFS8485 MFS18785 |
| Valor Ajuste Exclusão | Text Box | N | S | Default= Desabilitado | Informar o valor ajuste de redução. Valor deve ser igual à somatória do campo “Valor de Ajuste” quando tipo de ajuste for igual a “0” (ajuste de redução). e código de ajuste igual a 4, 5, 6, 7, 8, 9, 10 e/ou 11. (SAFX252) | MFS8485 MFS17215 MFS18794 MFS18785 MFS19609 |
| Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta. | Text Box | S | S |  | Informar o valor da base de cálculo.  Campo desabilitado para preenchimento. Será carregado com o “Valor Receita Bruta - Atividades” (-) “Valor Ajuste Exclusão” (+) “Valor Ajuste Adição” da Receita Bruta.   Caso o cálculo do campo “Valor Receita Bruta - Atividades” (-) “Valor Ajuste Exclusão” (+) “Valor Ajuste Adição” da Receita Bruta resultar em um valor menor que zero exibir a seguinte mensagem: O cálculo do campo “Valor Receita Bruta - Atividades” (-) “Valor Ajuste Exclusão” (+) “Valor Ajuste Adição” da Receita Bruta resulta um valor negativo. Nesse caso será gravado o valor 0 - zero.”  E será gravado do valor zero no campo. | MFS8485 MFS17215 |
| Valor Contrib. Prev. Sobre Receita Bruta | Text Box | S | S |  | Informar o valor da contribuição apurada.. Será carregado com o “Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta” (*) Alíquota Contrib. Prev. Receita Bruta.   Caso a multiplicação do campo Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta pelo valor do campo ‘Alíquota Contrib. Prev. sobre Receita Bruta resultar em um valor menor que zero exibir a seguinte mensagem: A multiplicação do campo Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta pelo valor do campo ‘Alíquota Contrib. Prev. sobre Receita Bruta resulta um valor negativo. Nesse caso será gravado o valor 0 - zero.”  E será gravado do valor zero no campo. | MFS8485 MFS17215 |
| *Aba Ajustes da Contribuição Previdenciária Apurada. | Aba |  |  |  | Os campos serão obrigatórios apenas se iniciado o processo de inclusão de informações. | MFS8485 |
| Tipo de Ajuste | Dropdown | S | S | Default = Não selecionado | Listar os valores:  Ajuste de redução; 1- Ajuste de acréscimo.  Caso não preenchido exibir a seguinte mensagem: “O campo Tipo de Ajuste deve ser informado” | MFS8485 |
| Código de Ajuste | Dropdown | S | S | Default = Não selecionado | Listar os valores:  1 - Ajuste da CPRB: Adoção do Regime de Caixa  2 - Ajuste da CPRB: Diferimento de Valores a recolher no período  3 - Adição de valores Diferidos em Período(s) Anterio-res(es).  4 - Exportações diretas  5 - Transporte internacional de cargas  6 -  Vendas canceladas e os descontos incondicionais concedidos 7 - IPI, se incluído na receita bruta  8 - ICMS, quando cobrado pelo  vendedor dos bens ou prestador dos serviços na condição de substituto tributário  9 -  Receita bruta reconhecida pela construção, recupera-ção, reforma, ampliação ou melhoramento da infraestrutu-ra, cuja contrapartida seja ativo intangível representativo de direito de exploração, no caso de contratos de conces-são de serviços públicos  10 - O valor do aporte de recursos realizado nos termos do art 6 §3 inciso III da Lei 11.079/2004  11 - Demais ajuste oriundo da Legislação Tributária  12 - Estorno   13 - Outras situações  Caso não preenchido exibir a seguinte mensagem: “O campo Código de Ajuste deve ser informado”  Obs:  Caso selecionado os códigos 11, 12, ou 13 deverá considerar sempre o código “11”, pois para EFD-REINF o código é genérico para as três situações. REINF X EFD-Contribuições  Caso selecionado o código “1” = 07  Caso selecionado o código “2” = 08  Caso selecionado o código “3” = 09 Caso selecionado o código “11” = 03  Caso selecionado “12” = 06 Caso selecionado “13” = 05  A partir deste depara deverá ser carregada a tabela de “Ajustes do EFD-Contribuições”.  Quando selecionada a opção 0 – Ajuste de Redução no campo Tipo de Ajuste serão apresentadas apenas as opções de código de ajuste igual a 4, 5, 6, 7, 8, 9, 10 e/ou 11 | MFS8485 MFS18794 MFS19609 MFS20401 |
| Valor de Ajuste | Text Box | S | S |  | Caso não preenchido exibir a seguinte mensagem: “Valor de Ajuste deve ser informado” | MFS8485 |
| Descrição do Ajuste | Text Box | S | S |  | Caso não preenchido exibir a seguinte mensagem: “Descrição do Ajuste deve ser informada” | MFS8485 |
| Data do Ajuste | Data | S | S | MM/AAAAA | Caso não preenchido exibir a seguinte mensagem: “Data do Ajuste deve ser informada” | MFS8485 |
| *Aba Processos relacionados a Suspensão da CPRB | Aba |  |  |  | Os campos serão obrigatórios apenas se iniciado o processo de inclusão de informações. | MFS14461 |
| Tipo de Processo | DropDown | S | S | Default = Não selecionado | Deverá listar as seguintes opções:  1-	Administrativo 2-	Judicial   Caso não preenchido exibir a seguinte mensagem: “Tipo de Processo deve ser informado” | MFS14461 |
| Número do Processo | Pasta | S | S | Default = Não selecionado | Deverão ser listados os processos conforme cadastro de processos na tela: (MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial (REINF) aba Informações do Processo) e filtro por tipo de processo.   Caso não preenchido exibir a seguinte mensagem: “Número de Processo deve ser informado” | MFS14461 |
| Código da Suspensão | Pasta | N | S | Default = Não selecionado | Deverão ser listados os códigos conforme cadastro de suspensão na tela: (MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial (REINF) aba Informações de Suspensão de Exigibilidade de Tributos) e filtro por número de processo e tipo de processo. | MFS8485 |
| Valor da Contribuição Previdenciária com exigibilidade suspensa | Text Box | S | S |  | Informar o valor da Contribuição Previdenciária com exigibilidade suspensa.   Caso não preenchido exibir a seguinte mensagem: “Valor da Contribuição Previdenciária com exigibilidade suspensa deve ser informado” | MFS8485 |
