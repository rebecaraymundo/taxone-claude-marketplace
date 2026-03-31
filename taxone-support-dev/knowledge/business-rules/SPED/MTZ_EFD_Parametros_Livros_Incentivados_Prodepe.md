# MTZ_EFD_Parametros_Livros_Incentivados_Prodepe

> Fonte: MTZ_EFD_Parametros_Livros_Incentivados_Prodepe.docx






THOMSON REUTERS

Módulo Sped Fiscal

Parametrização dos Livros Incentivados do PRODEPE


Localização: Menu SPED, Módulo: EFD-Escrituração Fiscal Digital, item Parâmetros  Livros Incentivados (PRODEPE) x Indicador Sub-Apuração x Registro E110 (Livro Apuração ICMS Incentivado)


DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	3
3.	Funcionamento da Tela	4

























## Regras Gerais


Esta parametrização foi criada para atender à geração dos registros 1960/1970/1975/1980 (Versão 3.0 do Guia Prático) do Sped Fsical.

Estes registros contêm informações sobre os Livros de Apuração Incentivados gerados no módulo do PRODEPE. Neste módulo os livros incentivados são gerados por Série e Subsérie. A série é sempre “B”, e para a subsérie o usuário cria um sequencial.

Exemplo: B01, B02, B03, B.....

No Sped cada apuração incentivada é reconhecida por um indicador, que corresponde a tabela 4.7.1 do Sped Fiscal (Tabela de Indicadores de Sub-Apuração por Tipo de Benefício), criada pela Sefaz-PE, cuja faixa de valores vai de 02 a 50.

Esta parametrização tem por objetivo associar cada apuração incentivada do Prodepe a um indicador desta tabela.

As regras básicas da parametrização são:

- Para um mesmo estabelecimento, um livro só poderá estar associado a um indicador de sub apuração;

- Da mesma forma, para um mesmo estabelecimento, um indicador só poderá estar associado a um livro;


Com base nessas regras, os campos chave da parametrização são:

Empresa + Cód. Estabelecimento + Série do Livro + Subsérie do Livro


Para cada livro será informado um indicador, e também a data inicial da vigência desta obrigação. Assim, ao gerar Sped Fiscal, este livro de apuração será gerado a partir do período referente a data informada.


[ALTERAÇÃO-MFS64731] Alteração descrição do Parâmetro para “Livros Incentivados (PRODEPE) x Indicador Sub-Apuração x Registro E110 (Livro Apuração ICMS Incentivado)” e inclusão de nova coluna de parâmetro “E110”.

Tratamento:

- Alterar a descrição do parâmetro “Livros Incentivados (PRODEPE) x Indicador Sub-Apuração”
Para: “Livros Incentivados (PRODEPE) x Indicador Sub-Apuração x Registro E110 (Livro Apuração ICMS Incentivado)”;

- Incluir coluna de Parâmetro, “E110”, esse novo parâmetro será utilizado para o usuário selecionar o Livro (por Serie e Subsérie) que deverá compor as informações do Registro E110 (Livro de Apuração de ICMS – Incentivado gerado no módulo Prodepe). Este parâmetro deverá ser habilitado somente se o parâmetro “Recuperar informações do Livro Apuração ICMS - Incentivado – p/ o Registro E110” na tela de Dados Iniciais estiver marcado, (verificar detalhamento no Item 3 – Funcionamento da Tela, no detalhe dos campos).


Obs.: Se o Parâmetro “E110” estiver marcado, este parâmetro passará a ser utilizado na geração do Registro E110 com base nas informações da Apuração ICMS – Livro Incentivado gerado no Módulo do Prodepe, o sistema deverá permitir que seja parametrizado somente um Estabelecimento, (Série e Subsérie), o relacionamento do módulo do Sped Fiscal x Módulo Prodepe, será através dos campos:

Empresa, Cód. Estabelecimento, Série do Livro, Subsérie do Livro.

## Layout da Tela
















Livro Incentivado PRODEPE (PE) x Indicador Sub-Apuração x Registro E110 (Livro Apuração ICMS Incentivado)









## Funcionamento da Tela


Na abertura da tela, serão exibidos os dados da parametrização ordenados da seguinte forma:

- Código do Estabelecimento;
- Série/Subsérie do livro incentivado;
- Indicador da Sub-Apuração;
- Data de início da vigência;
- E110.

Sobre a inclusão, alteração e exclusão de dados na parametrização:

Para incluir uma linha na parametrização o usuário deve clicar na opção <Novo> da barra de menu, e será aberta uma linha para a seleção do estabelecimento e livro de apuração, conforme descrito abaixo nas regras específicas de cada campo;

Para excluir uma linha da parametrização o usuário deve posicionar na linha desejada e clicar na opção <Exclui> da barra de menu;

Para alteração, estarão disponíveis apenas os campos do indicador de sub apuração e da data de vigência;


Segue detalhamento de todas as opções da tela:


Botões da barra de menu:


Segue funcionamento de cada campo no detalhe:



Validações:

Quando o usuário clicar na opção <CONFIRMA>, será realizada a seguinte validação:

Para cada linha a ser incluída ou alterada, será verificado se o indicador de sub apuração informado já foi parametrizado para outro livro (Série/Subsérie) da mesma Empresa e Estabelecimento.

Caso sim, será exibida a seguinte mensagem: “Indicador de Sub Apuração já informado para outro Livro do mesmo Estabelecimento”

Exemplo:

Empresa   Estabelecimento     Série/Subsérie        Indicador
001               XYZ                        B01                      05
001               XYZ                        B02                      05          (nova linha)

(Neste caso a nova linha estaria inválida, pois o indicador “05” já está parametrizado para o livro “B01”)




= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS20380 | Nova parametrização | Criação de uma nova parametrização dos livros incentivados do Prodepe x Indicador das Sub-Apurações do Sped Fiscal (tabela 4.7.1). | 10/10/2018 |
| MFS64731 | Alteração descrição do parâmetro e inclusão coluna de parâmetro E110. | Alteração da descrição do parâmetro e incluir de nova coluna de parâmetro (E110), este parâmetro passará a ser utilizado na geração do Registro E110 com base nas informações da Apuração ICMS – Livro Incentivado gerado no Módulo do Prodepe. | 04/06/2021 |
|  |  |  |  |


| NOVO | Esta opção permite a inclusão de dados, abrindo uma nova linha e disponibilizando para o usuário a janela de seleção do estabelecimento e livro de apuração, conforme descrito abaixo nas regras específicas de cada campo; |
| --- | --- |
| EXCLUI | Esta opção permite a exclusão de linhas da parametrização; |
| CONFIRMA | Opção para salvar as operações realizadas (incluídas / excluídas). Após salvar as informações, as linhas da parametrização serão reexibidas na ordem pré-estabelecida; |
| ORDENA | Ordena os dados da parametrização na ordem pré-estabelecida; |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Estabelecimento / Livro Incentivado | Alfanumérico | S | N |  | Este campo trabalha com janela de pesquisa da tabela de cadastro das obrigações fiscais por Série/Subsérie (ICT_OBRIGACAO_INCE), utilizada pelos contribuintes de PE que são beneficiários do PRODEPE.  Filtro das obrigações a serem exibidas para seleção do usuário:  - Empresa = empresa do login; - Estabelecimento = somente os estabelecimentos do estado de PE; (*) - Código do Livro Fiscal = “142” (Livros de Apuração Incentivados);  (*) Estes livros incentivados são utilizados apenas por PE, mas por segurança, será verificada a UF dos estabelecimentos, para que não apareçam dados incorretos que possam existir por alguma situação de erro ou teste.  Após a escolha da obrigação, será exibido em tela o código e a razão social do estabelecimento, e depois, a série e subsérie do livro (“Bnn”), conforme layout.  Exemplo: XXXXXX - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   B01 |
| Indicador Sub-Apuração EFD | Alfanumérico | S | S |  | Este campo é uma lista que apresenta os códigos da tabela 4.7.1 do Sped Fiscal, disponibilizada pela Sefaz-PE, com os seguintes valores:  02 03 04 ... ... ... 50  Trata-se da “Tabela de Indicadores de Sub-Apuração por Tipo de Benefício”, criada pela Sefaz-PE, cuja faixa de valores vai de 02 a 50.  Antes de salvar os dados parametrizados, será feita a crítica do indicador informado, conforme consta abaixo no item “Validações”. |
| Início Vigência | Data | S | S | DD/MM/AAAA | Neste campo será informada a data inicial da vigência do livro.  Deve ser uma data válida.  Obs.: Na geração do Sped Fiscal, este livro de apuração será gerado a partir do período referente a data informada. |
| E110 | Radio Button | N | N | Default: Desmarcado | Este campo deverá estar habilitado somente se o parâmetro ”Recuperar informações do Livro Apuração ICMS - Incentivado – p/ o Registro E110” na tela de Dados Iniciais estiver marcado (Por Estabelecimento).  Então, será utilizado para o usuário selecionar o Livro (por Serie e Subsérie) que irá compor as informações do Registro E110 (Livro de Apuração de ICMS – Incentivado gerado no módulo Prodepe).  Obs.: Como regra o sistema deverá permitir que somente um “parâmetro” (por Série e Subsérie) esteja marcado, por Estabelecimento, caso já exista 1 outra “opção” marcado, ao selecionar o mesmo Estabelecimento, o anterior será desmarcado, mantendo sempre o último Estabelecimento marcado.   Permitir que TODOS estejam desmarcados. |


| Observação sobre o indicador “02”: Conforme orientação do manual, o indicador “02” só pode ser utilizado para o incentivo do tipo Central de Distribuição. Esta regra não será validada nesta manutenção, pois seria complexo. No Prodepe a informação da Série/Subsérie do livro fica na tabela das regras do incentivo, que além de trabalhar com data de validade, também pode ter faixas de incentivo diferenciadas. Assim, esta orientação constará apenas no help. |
| --- |
