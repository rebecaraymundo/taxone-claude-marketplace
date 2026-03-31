# MTZ_EFD_Pre_Geracao_Registro_E115_Geral

> Fonte: MTZ_EFD_Pre_Geracao_Registro_E115_Geral.docx





THOMSON REUTERS

Módulo EFD-Escrituração Fiscal Digital

Pré-Geração do Registro E115 (Geral)



Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração à Registro E115 (Geral)


DOCUMENTO DE REQUISITO





Sumário

1.	Introdução:	3
2.	Parâmetros da Tela	7
3.	Recuperação dos Dados e Processamento	10
4.	Gravação dos Dados na Tabela dos Registros E115/1925 (Valores Declaratórios)	16
5.	Geração de Críticas no Log da Geração:	18
6.	Relatório de Conferência:	18


## Introdução:


Objetivo: fazer a geração dos dados do Registro E115 para todas as UF’s. outras UF’s diferentes do Rio Grande do Sul (RS).

Esta funcionalidade calcula os valores dos benefícios de isenção, imunidade, não incidência, redução de base de cálculo concedidos em por cada legislação estadual para serem demonstrados no registro E115 do Sped Fiscal.

O registro E115 do Sped Fiscal não é obrigatório, fica a critério de cada Unidade Federativa solicitar sua apresentação.
Cada Unidade Federativa que solicita o E115, publica uma lista de códigos de benefício (tabela 5.2 – Informações Adicionais da Apuração – Valores Declaratórios).

A base regra obter os valores dos benefícios de isenção, imunidade, não incidência, redução de base de cálculo deve ser baseada no Livro de Apuração do ICMS (P9), onde essas informações são apresentadas no Resumo por CFOP.

Como solução no DW para atendimento ao E115, criamos duas pré-gerações: a do E115 para o Rio Grande do Sul (opção de menu Registro E115 (Específico RS)) e a do E115 para todos os estados (opção Registro E115 (Geral)), sendo esta última a foco dessa documentação.

O resultado da pré-geração do E115 pode ser consultado no menu Geração à Manutenção à Registro E115/1925 (Valores Declaratórios).

Considerações quanto a tabela 5.2 – Informações Adicionais da Apuração – Valores Declaratórios:

- A lista de códigos de benefício (tabela 5.2 – Informações Adicionais da Apuração – Valores Declaratórios), que deve ser cadastrada no menu Parâmetro à Registros E115/1925à Informações Adicionais da Apuração (Registros E115/1925). Essa tabela não é carregada por TACES/TFIX. A ideia é o usuário cadastrar os códigos que tem necessidade de declarar.

- No momento da criação desta funcionalidade tomamos como base o estado do Paraná, cuja tabela 5.2 possui mais de 50 códigos. Veja:


- Regra de formação dos códigos da tabela 5.2 do Paraná:

httpps://www.sped.fazenda.pr.gov.br/modules/conteudo/conteudo.php?conteudo=146

- Futuramente outros estados podem lançar suas tabelas 5.2. E com isso pode haver necessidade de algumas modificações na forma de geração valores dos benefícios para o E115.

Considerações Gerais:

Esse processamento só atende a Geração Normal do Sped Fiscal, não atendendo ao PIM.
- [MFS30407] Especificamente o Rio Grande do Sul é atendido por uma geração apartada, no menu “Pré-Geração à Registro E115 (Específico RS)”, mas também poderá ser gerado pela opção Geral.  Quando o Código da Informação Adicional estiver parametrizado para as duas pré-gerações (geral e específica), o código só será gerado pela pré-geração específica.  Na opção de pré-geração geral, ele será desconsiderado.
- Esta geração só contempla o Registro E115. O registro 1925 não é gerado automaticamente, já que trabalha com sub-apurações do ICMS.
- Considerando uma determinada UF, o produto só pode estar parametrizado para um Código de Informação Adicional.
- [MFS32389] A chave da tabela da parametrização dos produtos (X272_PAR_PROD_E115) foi alterada para permitir que o mesmo produto, seja parametrizado para diferentes Códigos de Informação Adicional. Para isso o COD_INF_ADIC foi incluído na chave (esta tabela é específica da pré-geração do E115 da opção “Geral”, assim, não terá impacto em nenhuma outra geração);
- Ao parametrizar um CFOP para determinado Código de Informação Adicional, liberamos uma lista de valores que serão considerados para gerar o valor do benefício, por exemplo Valor da Base Isenta. Os valores disponíveis foram definidos com base no Livro de Apuração do ICMS – Resumo por CFOP.
- Apesar de nos basearmos na regra do Paraná, vamos deixar a rotina de Pré-Geração aberta para todas as UFs <> RS, pois há uma tendência de outros estados seguirem na mesma linha de solicitação;
- Vale a pena frisar que nos baseamos em regras do Livro de Apuração do ICMS, especificamente o Resumo por CFOP. Sendo assim os critérios de recuperação dos documentos fiscais e valores foram definidos conforme o livro P9.

[MFS28993]
- A parametrização do CST somente será considerada para a geração, se houver ao menos um CST parametrizado.  Se não houver CST’s parametrizados, somente serão consideradas as parametrizações de produto e CFOP/Natureza de Operação para a geração.

[ALTERAÇÃO-MFS-67999] Tratamento p/ Geração por Inscrição Estadual Única.

Tratamento:

Foi disponibilizado o Parâmetro “Geração p/Inscrição Estadual Única” na tela de Pré-Geração do Registro E115 – Geral, para tratamento de Geração para Estabelecimentos por Inscrição Estadual Única, sendo assim deverá seguir a seguinte regra:

Se a opção selecionada for “Sim”: Serão consideradas as Notas Fiscais de todos os estabelecimentos envolvidos, o centralizador (estabelecimento selecionado em tela), e os centralizados (conforme parametrização do módulo de controle das obrigações estaduais, menu  “Obrigações >  Empresas/Estabelecimentos com Ins. Estadual Única”), onde:

Selecionar todas as Notas Fiscais dos Estabelecimentos envolvidos na centralização, identificados a partir do campo “COD_ESTAB” da tabela “ICP_INSC_EST_CENTR”, do Estabelecimento Centralizador.

Tabela ICP_INSC_EST_CENTR:

Campo COD_ESTAB: Estabelecimentos Centralizados;
Campo COD_ESTAB_CENTR: Estabelecimento Centralizador.

Se a opção selecionada for “Não”:  Será considerado somente as Notas Fiscais do estabelecimento selecionado em tela.




## Parâmetros da Tela







Funcionamento dos campos:





[MFS571174] Alteração da geração para verificar o parâmetro relativo à utilização da parametrização de produto, incluído na tela de Dados Iniciais

## Recuperação dos Dados e Processamento


Origem dos dados:  - Manutenção das Informações Adicionais da Apuração (Registros E115/1925);
- Parametrização do Produto para Informação Adicional da Apuração (opção do menu Registro E115 (Geral)); **
- Parametrização de CFOP para Informação Adicional da Apuração (opção do menu Registro E115 (Geral));
- Parametrização de CFOP / Natureza de Operação para Informações Adicionais da Apuração (menu Registro E115 (Geral));
- Parametrização de CST para Informação Adicional da Apuração (opção do menu Registro E115 (Geral)); [MFS28993]
- SAFX07 / SAFX08 - Tabelas dos Documentos Fiscais;

** Verificar o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” na tela de Dados Iniciais do SPED-EFD.

Critérios da recuperação das Notas Fiscais (SAFX07 / SAFX08):

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data Fiscal – data enquadrada no período informado em tela;

- Somente notas não canceladas;

- Somente notas com itens de mercadoria;


Alteração MFS-58897: Criado o parâmetro “Considerar campo de Código do Benefício - SAFX08 (campo 255)” na tela dos Dados Iniciais do Sped Fiscal:

- Parâmetro desmarcado – A geração do Registro E115 permanecerá conforme regra original, desconsiderando a regra do Campo 255 – Código do Benefício.

- Parâmetro marcado – A geração do Registro E115 passará a considerar o Campo 255 – Código do Benefício da tabela SAFX08, conforme regra abaixo:

- Campo Código do Benefício (SAFX08, Campo 255 – COD_BENEFICIO):

SE o Campo 255 – COD_BENEFICIO da tabela DWT_ITENS_MERC estiver preenchido;

E o código do benefício estiver cadastrado no módulo EFD-Escrituração Fiscal Digital >> Informações Adicionais da Apuração (Registro E115/1925).
(Tabela/Campo do Parâmetro: Tabela EFD_INF_ADIC_APUR, Campo COD_INF_ADIC);
(Relacionamento entre as tabelas:  DWT_ITENS_MERC.COD_BENEFICIO = EFD_INF_ADIC_APUR.COD_INF_ADIC);
Então seguir com a sequência das próximas regras;
Senão desconsiderar o item na geração do Registro E115.
845
- Situação Especial (SAFX07, item 125 -  IND_SITUACAO_ESP) – caso esteja preenchido, deve ser diferente de:
1 - Nota Fiscal de Venda Globalizada de acordo com o Protocolo ICMS 52/2000 (Cláusula Quarta);
2 - Nota Fiscal de Acompanhamento de ECF;
8 - NF de Remessa por Conta e Ordem;
(critério baseado no P9)

- Classificação do Documento Fiscal (SAFX07, item 12 - COD_CLASS_DOC_FIS):
Se a nota é de saída (SAFX07, item 03 -  MOVTO_E_S = ‘9’), então
Considerar COD_CLASS_DOC_FIS = ‘1’, ‘3’ ou ‘4’;
Se a nota é de entrada (SAFX07, item 03 -  MOVTO_E_S <> ‘9’), então:
Considerar COD_CLASS_DOC_FIS =  ‘1’ ou ‘3’;
(critério baseado no P9)

- Nota Fiscal Transferência de Crédito/Débito (SAFX07, item 74 - IND_TRANSF_CRED) – caso esteja preenchido, deve ser = 0 – “NF que não seja de Transferência’;
(critério baseado no P9)

Se o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” estiver marcado
Não será verificada a parametrização de produto, ou seja, serão considerados todos os produtos
Senão
O produto do item deve constar na parametrização do menu “Parâmetros à Registro E115/1925 à Registro E115 (Geral) à Produtos”.
Fazer uma consulta na Parametrização do Produto (SAFX272), com os critérios:
- Empresa de login
- Estabelecimento selecionado na Tela de geração
- Produto (Grupo, Indicador e Código) = referenciado no item de mercadoria
- Data Início Validade <= Data Fiscal da nota
- Data Fim Validade quando preenchida, deve ser >= Data Fiscal da nota
Obs: se o critério acima atender a mais de uma Parametrização, recuperar a de maior Data Início Validade dentre essas.
Recuperar o Código da Informação Adicional e a Descrição Complementar.

MFS-32568: Alteração na regra de aplicação do parâmetro “Considerar campo de Código do Benefício - SAFX08 (campo 255)” na tela dos Dados Iniciais do Sped Fiscal:
Se o parâmetro “Considerar campo de Código do Benefício - SAFX08 (campo 255)” estiver marcado, o produto do item de mercadoria pode ou não constar na Parametrização do Produto (SAFX272).
Caso o produto esteja parametrizado, manter a recuperação do Código da Informação Adicional e a Descrição Complementar da Parametrização do Produto (SAFX272).
Caso o produto não esteja parametrizado, considerar:
- Código da Informação Adicional do item de mercadoria (campo 255)
- Descrição Complementar : descrição do próprio Código da Informação Adicional (Tabela EFD_INF_ADIC_APUR - Manutenção das Informações Adicionais da Apuração
(Registros E115/1925)).
Se o parâmetro “Considerar campo de Código do Benefício - SAFX08 (campo 255)” estiver desmarcado, obrigatoriamente o produto do item de mercadoria deve pertencer a Parametrização do Produto (SAFX272), se o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” estiver desmarcado.

[MFS30407]
- O CFOP ou CFOP/Natureza do item deve constar na parametrização do menu “Parâmetros à Registro E115/1925 à Registro E115 (Geral) à CFOP ou CFOP/Natureza de Operação” e NÃO deve constar na parametrização do menu “Parâmetros à Registro E115/1925 à Registro E115 (Específico RS) à CFOP ou CFOP/Natureza de Operação”, para qualquer código de anexo da GIA-RS informado nas telas.
Fazer uma consulta na Parametrização do CFOP/Natureza da Operação, com os critérios:
- Empresa de login
- Estabelecimento selecionado na Tela de geração
- CFOP referenciado no item de mercadoria
- Natureza da Operação referenciado no item de mercadoria
- Código da Informação Adicional = Código da Informação Adicional relacionado ao Produto (se o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” estiver desmarcado) do item de mercadoria via Parametrização
Recuperar o campo “Recuperação de Valores” da parametrização.

Caso o item de mercadoria não possua Natureza da Operação, ou a relação do CFOP/Natureza do item não estejam parametrizados, fazer a consulta na Parametrização do CFOP:

Fazer uma consulta na Parametrização do CFOP, com os critérios:
- Empresa de login
- Estabelecimento selecionado na Tela de geração
- CFOP = referenciado no item de mercadoria
- Código da Informação Adicional = Código da Informação Adicional relacionado ao Produto (se o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” estiver desmarcado) do item de mercadoria via Parametrização
Recuperar o campo “Recuperação de Valores” da parametrização.

[MFS28993]

- O CST do item deve constar na parametrização do menu “Parâmetros à Registro E115/1925 à Registro E115 (Geral) à CST”.
Fazer uma consulta na Parametrização do CST, com os critérios:
- Empresa de login
- Estabelecimento selecionado na Tela de geração
- CST (Situação Tributária Estadual – B) = referenciado no item de mercadoria
- Código da Informação Adicional = Código da Informação Adicional relacionado ao Produto (se o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” estiver desmarcado)  do item de mercadoria via Parametrização

Obs.: A Parametrização do CST somente será considerada para a geração, se houver ao menos um CST parametrizado.  Se não houver CST’s parametrizados, serão considerados todos os CST’s.


Consolidação:

Os itens de documento fiscal que atendam os critérios acima são consolidados por:
- Código da Informação Adicional
- Produto (Grupo, Indicador e Código) (ver OBS abaixo sobre a Descrição Complementar)

[MFS32389] Com a alteração na chave da parametrização dos produtos, a geração foi ajustada para prever a situação de um mesmo produto, parametrizado para diferentes Códigos de Informação Adicional.

Exemplo: O produto ABC poderá ser parametrizado para o código PR810057 e também para o PR820043.

A lógica da geração não se altera, e os itens recuperados das notas fiscais continuarão a ser consolidados por Código da Informação Adicional e Produto, conforme o funcionamento original.



[MFS32389] Com a alteração na chave da parametrização dos produtos, para permitir que um produto seja parametrizado para diferentes Códigos de Informação Adicional, a geração foi ajustada para prever esta situação.

Exemplo: O Produto 01 poderá ser parametrizado para o código PR810057 e também para o PR820043.

Recuperação de Valores:
[MFS26565]- Inclusão de novos valores
Os valores dos itens de documento fiscal são recuperados de acordo o campo “Recuperação de Valores” da Parametrização do CFOP ou CFOP/Natureza da Operação:








## Gravação dos Dados na Tabela dos Registros E115/1925 (Valores Declaratórios)


Os documentos fiscais recuperados da SAX07 / SAFX08 serão gravados na tabela de forma consolidada (vide tópico Consolidação), com as seguintes informações:

Obs: Os documentos fiscais são consolidados (vide tópico Consolidação) de forma a permitir que N registros E115 sejam gerados para um mesmo Código da Informação Adicional (pode haver variação de produtos). Esses registros poderão ser diferenciados pela Descrição Complementar.



## Geração de Críticas no Log da Geração:


[MFS571174] Alteração da geração para verificar o parâmetro relativo à utilização da parametrização de produto, incluído na tela de Dados Iniciais

Vamos gerar críticas para notas fiscais que não atendam às parametrizações de Produto, Cfop e Cfop/Natureza da Operação.

Se o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” estiver marcado
Não serão dadas as mensagens de erro abaixo porque não vai ter produto parametrizado
Senão
Serão dadas as mensagens de erro porque vai ter produto parametrizado:

- Gerar crítica para Nota fiscal atenda aos oito primeiros critérios definidos no tópico 3, cujo CFOP ou CFOP/Natureza de Operação esteja parametrizado para algum Código de Informação Adicional da UF do Estabelecimento, mas que o produto não exista na Parametrização de Produto para o Estabelecimento foco.
- Mensagem: Item do documento fiscal não foi considerado na pré-geração do E115, pois o Produto não foi parametrizado.
- Solução: Criar parametrização na opção de menu Parâmetros à Registro E115/1925 à Registro E115 (Geral) à Produtos
- Chave de Identificação: Num Doc.Fis xxxx + Serie xxxx + Subsérie xx + Data Fiscal + Pessoa Fis/Jur (gr/ind/cod): xx/x/xxxx + Item xxx + Produto (gr/ind/cod): xx/x/xxxx

- Gerar crítica para Nota fiscal atenda aos oito primeiros critérios definidos no tópico 3, cujo produto exista na Parametrização de Produto para o Estabelecimento foco, mas o CFOP (ou CFOP/Natureza Operação) do item, não esteja parametrizada para o Código da Informação Adicional relacionada ao produto.

- Mensagem: Item do documento fiscal não foi considerado na pré-geração do E115, pois o CFOP (ou CFOP/Natureza Operação) não foi parametrizado.
- Solução: Criar parametrização em uma das opções de menu Parâmetros à Registro E115/1925 à Registro E115 (Geral) à CFOP ou CFOP/Natureza de Operação
- Chave de Identificação: Num Doc.Fis xxxx + Serie xxxx + Subsérie xx + Data Fiscal + Pessoa Fis/Jur (gr/ind/cod): xx/x/xxxx + Item xxx + CFOP: xxxx + Natureza da Operação(gr/cod): xx/xxxx



## Relatório de Conferência:



As notas fiscais que foram consideradas na geração devem ser apresentadas neste relatório.
As seguintes informações devem ser demonstradas:
- Data Fiscal
- Núm/Serie/Subsérie
- Entrada/Saída
- Código da Informação Adicional (código)
- Item de Mercadoria
- Produto (ind/cod)
- CFOP
- Natureza de Operação
- Indicador Recuperação dos Valores (descrição)
- Valor da Informação Adicional (resultante da aplicação do Indicador da Recuperação de Valor aos valores da SAFX08:
- Valor da Base Isenta do ICMS
- Valor da Base Outras do ICMS
- Valor da Base Reduzida do ICMS
- Valor do Tributo ICMSS



| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS23415 | Pré-Geração do E115 (Geral) | Essa MFS tem como objetivo criar a rotina de pré-geração do Registro E115 (Geral), para atender as Unidades das Federações exceto Rio Grande do Sul. | 26/02/2018 |
| MFS26565 | Andréa Rocha | Alteração da geração para tratar os novos valores do campo Recuperação de Valores. | 03/05/2019 |
| MFS28993 | Andréa Rocha | Alteração da geração para utilizar a parametrização de CST | 10/09/2019 |
| MFS30407 | Andréa Rocha | Alteração da geração para verificar se o código da informação adicional está parametrizado para a geração específica do registro E115 e retirar a validação do campo estabelecimento para o estado igual a RS | 26/09/2019 |
| MFS32389 | Vânia Mattos | Alteração da X272_PAR_PROD_E115 para inclusão do COD_INF_ADIC na PK. Este alteração permitirá que o mesmo produto seja parametrizado para diferentes COD_INF_ADIC. | 27/08/2020 |
| MFS58897 | Rogério Ohashi | Alteração na Regra para utilizar o Parâmetro “Considerar campo Código do Benefício” para considerar ou não o Campo 255 – Código do Benefício da Tabela SAFX08 na geração do Registro E115. Esse ajuste se faz necessário para os clientes que utilizaram esse campo como critério de geração, conforme informação do campo no Manual Layout. | 04/02/2021 |
| MFS59764 | Rogério Ohashi | Alteração da Regra de preenchimento do Campo 04 - DESCR_COMPL_AJ, Descrição complementar do ajuste, para os Estabelecimento do Estado do Rio de Janeiro, que conforme manual da Secretaria de Fazenda, o campo não deve ser preenchido. | 04/02/2021 |
| MFS67999 | Rogério Ohashi | Inclusão de Regra de tratamento para Geração de Estabelecimentos com Inscrição Estadual Única. | 13/07/2021 |
| MFS32568 | Liliane Assaf | Alteração na regra que utiliza o Parâmetro “Considerar campo Código do Benefício da SAFX08 (campo 255)” para desobrigar o uso da parametrização do Produto. Usando esse parâmetro, Código da Informação Adicional virá do item de mercadoria. Sendo assim não há necessidade do produto estar parametrizado para o Código da Informação Adicional. Sem o uso da parametrização do produto, a Descrição Complementar será a descrição do próprio Código da Informação Adicional. | 02/09/2021 |
| MFS87559 | Aline Melo | Inclusão de campo de pesquisa UF | 08/06/2022 |
| MFS571174 | Andréa Rocha | Alteração da geração para verificar o parâmetro incluído na tela de Dados Iniciais, para desconsiderar a parametrização de produtos. | 03/10/2023 |
| MFS693829 | Andréa Rocha | Alteração na regra de geração do registro E115, para utilizar um parâmetro que vai definir se o campo 04-DESCR_COMPL_AJ deve ser preenchido ou não. Foi feita uma alteração na regra pela MFS59764. para os Estabelecimento do Estado do Rio de Janeiro, que conforme manual da Secretaria de Fazenda, o campo não devia ser preenchido. A partir de julho 2024,  Resolução SEFAZ Nº 684, o campo deve ser preenchido para algumas situações para o RJ, por isso o parâmetro está sendo criado. | 10/10/2024 |
| MFS1019580 | Rogério Ohashi | Alteração na regra de geração do registro E115, para utilizar um parâmetro que vai definir se o campo 03-VL_INF_ADIC deve ser preenchido com zero ou não, conforme manual da Secretaria de Fazenda, o campo não deve ser preenchido com zero. A partir de julho 2024,  Resolução SEFAZ Nº 684, o campo deve ser preenchido para algumas situações para o RJ, por isso o parâmetro está sendo criado. | 13/01/2026 |


| Código | Benefício | Descrição | Dt Início | Dt Final | Ajuste - EFD |
| --- | --- | --- | --- | --- | --- |
| PR810057 | Isenção | Isenção prevista no item 57 do Anexo V do RICMS/2017 | 01/08/2018 |  | Gerar o registro E115, informando no campo 02 (COD_INF_ADIC) o código da informação; no campo 03 (VL_INF_ADIC) o valor do imposto do item destacado no documento fiscal - se não houver imposto, preencher com "0" (zero); e no campo 04 (DESCR_COMPL_AJ) a descrição do ajuste. |
| PR810058 | Isenção | Isenção prevista no item 58 do Anexo V do RICMS/2017 | 01/08/2018 |  | Gerar o registro E115, informando no campo 02 (COD_INF_ADIC) o código da informação; no campo 03 (VL_INF_ADIC) o valor do imposto do item destacado no documento fiscal - se não houver imposto, preencher com "0" (zero); e no campo 04 (DESCR_COMPL_AJ) a descrição do ajuste. |
| PR820043 | Redução de base de cálculo | Redução de base de cálculo prevista no item 36-A do Anexo VI do RICMS/2017 | 01/08/2018 |  | Gerar o registro E115, informando no campo 02 (COD_INF_ADIC) o código da informação; no campo 03 (VL_INF_ADIC) o valor do imposto do item destacado no documento fiscal - se não houver imposto, preencher com "0" (zero); e no campo 04 (DESCR_COMPL_AJ) a descrição do ajuste. |
| PR840007 | Suspensão | Suspensão prevista no inciso VII do “caput” do art. 1º do Anexo VIII do RICMS/2017 | 01/08/2018 |  | Gerar o registro E115, informando no campo 02 (COD_INF_ADIC) o código da informação; no campo 03 (VL_INF_ADIC) o valor do imposto do item destacado no documento fiscal - se não houver imposto, preencher com "0" (zero); e no campo 04 (DESCR_COMPL_AJ) a descrição do ajuste. |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Data Inicial | Data | S | S | DD/MM/AAAA | Neste campo o usuário informa a data inicial do período para a recuperação dos movimentos.  Deve ser uma data válida. |
| Data Final | Data | S | S | DD/MM/AAAA | Neste campo o usuário informa a data final do período para a recuperação dos movimentos.  Consistências: Deve ser uma data válida. Caso a Data Final informada seja menor que a Data Inicial, gravar no log a seguinte mensagem: “A Data Inicial deve ser menor ou igual a Data Final informada.” Caso a Data Inicial e a Data Final excedam o período de um mês, gravar no log a seguinte mensagem: “Data Inicial e Final deverão pertencer a um mesmo mês.” |
| Geração p/Inscrição Estadual Única | Texto | N | S | Formato: Radio Button Group  Default: Habilitado Desmarcado | Este campo apresenta duas opções:   - Sim - Não  As opções são alternativas.  A opção informada interfere no campo “Estabelecimentos”, conforme descrito na regra específica. |
| UF |  | S | S | Formato: ListBox  Default: Em branco | Neste campo é exibida a lista de todas as UF’s. O usuário deve selecionar a UF do estabelecimento que será informado para a geração. MFS87559 |
| Estabelecimentos | Alfanumérico | S | S |  | Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  O campo deve ser apresentado sem listar nenhum estabelecimento. Após selecionar a UF, devem ser listados somente os estabelecimentos que sejam da UF selecionada. MFS87559  Serão disponibilizados para seleção apenas os estabelecimentos que não estejam no Rio Grande do Sul (UF do Estabelecimento diferente de RS); |
| Selecionar |  | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:  - Somente Estabelecimentos da empresa do login;  - Somente Estabelecimentos da UF diferente de RS;  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados. |
| Marcar todos |  | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”. |


| (***) Sobre a Descrição Complementar:   Na verdade, a consolidação é feita pela Descrição Complementar parametrizada para o produto. E para cada consolidação, é gravada uma linha na tabela. Conforme teste realizados (MFS32389), a geração funciona da seguinte forma:  O campo é de preenchimento não obrigatório na parametrização dos produtos.  Quando preenchido, a geração dos dados do E115 consolida as informações por Código da Informação Adicional e Descrição Complementar, e grava um registro E115 para cada consolidação, onde os valores apurados são totalizados.  Se para cada Produto for informada uma descrição complementar diferente, o registro E115 será demonstrado separadamente por Produto, exibindo a descrição parametrizada.   Se forem informadas descrições iguais para vários Produtos, as informações destes Produtos serão consolidadas num único registro E115, para o Código da Informação Adicional.  Todos os Produtos com descrição complementar não informada, são consolidados, e no E115 será demonstrada a descrição do próprio Código da Informação Adicional. |
| --- |


| Campo “Recuperação de Valores” da  Parametrização por CFOP, CFOP/Natureza da Operação | Campo da SAFX08 |
| --- | --- |
| 1 – Base Isenta ICMS | Valor da Base Isenta do ICMS  (SAFX08, item 56 - BASE_ICMS quando item 55 - TRIB_ICMS = 2) |
| 2 – Base Outras ICMS | Valor da Base Outras do ICMS (SAFX08, item 56 - BASE_ICMS quando item 55 - TRIB_ICMS = 3) |
| 3 – Base Reduzida ICMS | Valor da Base Reduzida do ICMS (SAFX08, item 57 - BASE_REDU_ICMS) |
| 4 – Base Isenta ICMS + Base Reduzida ICMS (baseado no P9) | Soma dos campos: Valor da Base Isenta do ICMS e Valor da Base Reduzida do ICMS (SAFX08, item 56 - BASE_ICMS quando item 55 - TRIB_ICMS = 2) +  (SAFX08, item 57 - BASE_REDU_ICMS) |
| 5 - Base Outras ICMS + Valor do ICMS-S (baseado no P9) | Soma dos campos: Valor da Base Outras do ICMS e Valor do Tributo ICMSS (SAFX08, item 56 - BASE_ICMS quando item 55 - TRIB_ICMS = 3) +  (SAFX08, item 52 - VLR_SUBST_ICMS) |
| 6 - Valor Desonerado ICMS | Valor Desonerado ICMS (SAFX08, item 258 - VLR_DESONERADO_ICMS) |
| 7 - Valor Diferido ICMS | Valor Diferido ICMS (SAFX08, item 259 - VLR_DIFERIDO_ICMS) |


| PK | Campo | Regra de Preenchimento |
| --- | --- | --- |
| S | Código da empresa | Código da empresa (SAFX07) |
| S | Código do estabelecimento | Será preenchido com o estabelecimento informado na pré-geração. |
| S | Período | Será preenchido com a Data Inicial e Final informada na pré-geração. |
| S | Sequencial | Sequência única por Empresa, Estabelecimento e Período.Exemplo: Cód. Inf. Adicional.  Apuração                            Sequencial PRXXXXXX             01/01/2017 a 31/01/2017   1 PRXXXXXX             01/01/2017 a 31/01/2017   2 PRYYYYYY             01/01/2017 a 31/01/2017   3 PRYYYYYY             01/01/2017 a 31/01/2017   4   PRXXXXXX             01/02/2017 a 28/02/2017   1 PRXXXXXX             01/02/2017 a 28/02/2017   2 |
|  | Código da Informação Adicional | [MFS571174] Alteração da geração para verificar o parâmetro relativo à utilização da parametrização de produto, incluído na tela de Dados Iniciais  Se o parâmetro “Desconsiderar a parametrização de Produto para a Pré-geração” estiver desmarcado       Será preenchido com a informação do Código da Informação Adicional parametrizado para o Produto e CFOP (ou        Produto e CFOP/ Natureza de Operação) Senão       Será preenchido com a informação do Código da Informação Adicional parametrizado para o CFOP (CFOP/        Natureza de Operação). |
|  | Valor da Informação Adicional | Será preenchido com a soma dos valores dos itens de mercadoria de acordo com a Parametrização do CFOP ou CFOP/Natureza da Operação. Vide tópico Recuperação de Valores. [ALTERAÇÃO-MSS1019580] Regra geral de preenchimento do campo “Valor Informação Adicional”.  Se o parâmetro “Não Preencher Valor da Informação Adicional” do cadastro das Informações Adicionais da          Apuração - Registro E115/1925 (*) estiver marcado     NÂO preencher o Campo 03 - VL_INF_ADIC      Senão o campo deverá ser preenchido. |
|  | Descrição Complementar | Preencher este campo conforme regra:  [ALTERAÇÃO - MFS-59764] Regra Específica para o Rio de Janeiro – Não preencher o campo “Descrição Complementar. [ALTERAÇÃO – MFS693829] Regra geral de preenchimento do campo “Descrição Complementar”. Retirada da regra criada pela MFS59764.  Se o parâmetro “Não Preencher Descrição Complementar do Ajuste” do cadastro das Informações Adicionais da          Apuração - Registro E115/1925 (*) estiver marcado     NÂO preencher o Campo 04 - DESCR_COMPL_AJ Senão Se o campo Descrição Complementar da Parametrização do Produto (SAFX272) estiver preenchido, então:     Considerar a Descrição Complementar da Parametrização do Produto.            Senão    Considerar a Descrição do Código da Informação Adicional (*).   * Vide: Parâmetro à Registros E115/1925à Informações Adicionais da Apuração (Registros E115/1925).     SE o Estabelecimento for do Rio de Janeiro: Campo IDENT_ESTADO da Tabela ESTABELECIMENTO igual ao Campo IDENT_ESTADO da Tabela ESTADO, sendo o Campo COD_ESTADO = “DF”:                                      ESTABELECIMENTO.IDENT_ESTADO = ESTADO.IDENT_ESTADO                                      ESTADO.COD_ESTADO = ‘DF’                                               NÂO preencher o Campo 04 - DESCR_COMPL_AJ. |
|  | Sub-Apuração do Sped Fiscal | Não será preenchido. A pré-Geração só atende ao registro E115. Portanto não teremos a geração da informação da sub-apuração utilizada apenas no registro 1925. |
|  | Usuário | Gravar o usuário que efetuou a pré-geração desse Registro. |
|  | Data Operação | Gravar com a data que foi efetuada a pré-geração desse Registro. |
|  | Número do Processo | Gravar o número do processo da  pré-geração desse Registro. |
