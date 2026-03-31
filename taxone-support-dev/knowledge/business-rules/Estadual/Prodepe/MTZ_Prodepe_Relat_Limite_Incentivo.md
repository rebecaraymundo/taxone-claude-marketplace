# MTZ_Prodepe_Relat_Limite_Incentivo

- **Fonte:** MTZ_Prodepe_Relat_Limite_Incentivo.docx
- **Modificado:** 2024-07-16
- **Tamanho:** 67 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__Relatório de Limites de Incentivo__

__Localização__: Menu Estadual, Módulo Prodepe, item Relatórios 🡪 Limites de Incentivo

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS655692

Andréa Rocha

Criação do documento

16/07/2024

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

O objetivo deste relatório é o acompanhamento dos grupos / percentuais de incentivo, obtendo informações relativas a cada grupo 

de incentivo e seu posicionamento dentro do seu limite de incentivo\.

Para a emissão do relatório, é necessário que a rotina de incentivo das notas fiscais já tenha sido executada\.	

__RN01__

__                                                        Parâmetros de Tela__

Campo “__Estabelecimento__”:

- lista com a relação de todos os Estabelecimentos que sejam de Pernambuco e que tenham sido parametrizados no módulo Prodepe \(que constem na parametrização “Parâmetros 🡪 Dados Gerais”\);
-  Opção “Todos”;

Campo “__Grupo de Incentivo__”:

- lista com a relação de todos grupos de incentivo cadastrados para o estabelecimento selecionado;  
- quando a opção do Estabelecimento for  =  “Todos”,  mostrar todos os grupos da Empresa;
- a lista exibirá o código e a descrição dos grupos identificados;
- Opção “Todos”; 

Campo “__Data de Referência__”:

- o usuário deverá informar uma data de referência para gerar o relatório\.

__RN02__

__                                     Recuperação e Processamento dos Dados__

__Origem dos dados:__

     \- Tabela dos grupos de incentivos \(ICT\_GRP\_INCENT\)

     \- Tabela das regras de incentivos \(ICT\_REGRA\_INCENT\)

     \- Tabela das faixas de incentivos \(ICT\_FAIXA\_INCENT\)

     \- Tabela de histórico diário das saídas incentivadas \(ICT\_HIST\_INCENT\)

Conceito original: o objetivo deste gráfico é demonstrar o ponto exato onde se encontram as vendas de um determinado grupo de incentivo em relação à regra em vigor\. Esta regra é sempre a do ano correspondente à data informada em tela \(campo “Data Incentivo”\)\. 

Exemplo:  faixa limite de 1 a  500 unidades com 300 unidades já comercializadas

                        Min Regra                                                                                   Max Regra

       Min | \-\-\-\-\-\-\-\-\-\-\-\- | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- Max

                              1                                                        300                                    500

Considerando que desde o início do ano até a data do incentivo informada, já foram comercializadas 300 unidades deste grupo de incentivo, a seta deve estar posicionada no ponto equivalente ao 300\. O controle das quantidades comercializadas em relação às faixas de incentivo é feito sempre anualmente\.

Este é o conceito original, já que a regra era obrigatoriamente anual e para cada regra, existia apenas uma faixa limite de comercialização\. 

Novo conceito:

🡪 A regra deixou de ser obrigatoriamente anual, tendo agora uma data de validade inicial e final; 

🡪 Para cada regra poderão existir “n” faixas de comercialização que ficam na tabela das faixas de incentivos; 

🡪 Será utilizado o parâmetro “Controle das Faixas de Incentivo” que será informado na regra de incentivo, para definir como será feito o controle das quantidades comercializadas em relação às faixas de incentivo, da seguinte forma:

    Por período de apuração 🡪 o controle das quantidades comercializadas se inicia na data inicial do período de apuração, e prossegue  

    até o último dia do período; para um novo período a contagem seráreiniciada\.

    Por período de validade da regra 🡪 o controle das quantidades comercializadas se inicia na data inicial de validade da regra, e 

    prossegue até a data de validade final; a cada novo período de apuração a contagem NÃO é reiniciada\.

🡺 De acordo com os novos conceitos, este demonstrativo deve ser alterado para trabalhar da seguinte forma:

\- A regra a ser considerada deve ser a linha da tabela ICT\_REGRA\_INCENT na qual a data do incentivo informada em tela se encaixe entre a data de validade inicial e final da regra\. Considerar que a validade final pode estar nula, pois não é campo obrigatório\.

\- No quadro que mostra os dados do grupo de incentivo, mostrar as datas de validade inicial e final da regra\. 

\- Neste mesmo quadro, o campo “Faixa do Incentivo” vai demonstrar todas as faixas existentes na tabela ICT\_FAIXA\_INCENT, com os seus respectivos percentuais\.

Exemplo do relatório:

Grupo de Incentivo:   xxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Validade da regra em vigor:   99/99/9999  a  99/99/9999

Medida:  xxx – xxxxxxxxxxxxxxxxxxxxxxxxxxx

Faixas de Incentivo:  xxxxxxx  a  xxxxxxxxx   99,9999%

                                  xxxxxxx  a  xxxxxxxxx   99,9999%

                                  xxxxxxx  a  xxxxxxxxx   99,9999%

Quantidade/Peso Comercializado até a data: xxxxxxxxxxxxxxxxx 

\- Para montar o gráfico, no caso de existir mais de uma faixa, considerar a menor faixa inicial para a marca “Min Regra” e a maior faixa final para a marca “Max Regra”; considerar que a faixa final não é obrigatória, e por isso, esta “marca” poderá não existir\.

\- Para totalizar as quantidades comercializadas até a data do incentivo informada, o que é feito totalizando\-se as linhas da tabela de  Histórico diário das saídas incentivadas, considerar o parâmetro da regra, o IND\_CONTROLE\_FAIXA:

Se IND\_CONTROLE\_FAIXA = “1” \-> iniciar a totalização dos valores da ICT\_HIST\_INCENT a partir da data inicial do período de apuração referente à data de incentivo informada \(\*\*\), até a data de incentivo informada em tela \(inclusive\)\. 

Se IND\_CONTROLE\_FAIXA = “2” 🡪 iniciar a totalização dos valores da ICT\_HIST\_INCENT a partir da data de validade inicial da regra e totalizar até a data de incentivo informada em tela \(inclusive\)\. 

\(\*\*\) No caso do IND\_CONTROLE\_FAIXA = “1”, o que significa controle por período de apuração, será necessário verificar qual a data inicial do período\. Para isso, utilizar como parâmetro a data de incentivo informada em tela e a periodicidade da obrigação fiscal “142” do Estabelecimento em questão, da seguinte forma:

1. Recuperar da tabela ICT\_OBRIGACAO\_INCE a linha correspondente a obrigação fiscal “142” da Empresa e Estabelecimento em questão\. Existindo mais de uma linha, o que poderá acontecer para quem trabalhar com mais de um grupo de incentivo \(e portanto existirão diferentes série/subséries\), não tem problema, basta utilizar distinct na coluna IND\_PERIODICIDADE obedecendo aos critérios de Empresa/Estabelecimento/Código do Livro = “142”\. 
2. Comparar a data de incentivo informada com a periodicidade da apuração \(coluna IND\_PERIODICIDADE\):

Se periodicidade = “DE”

    		Se dia da data de referência < 11

         		     data inicial do período =  01 \+ mês/ano da data de referência 

    		Senão

     Se dia da data de referência  < 21

                                data inicial do período =  11 \+ mês/ano da data de referência 

                          Senão

                               data inicial do período =  21 \+ mês/ano da data de referência 

 

Se periodicidade = “QZ”

                Se dia da data de referência < 16

                     data inicial do período =  01 \+ mês/ano da data de referência 

                Senão

                    data inicial do período =  16 \+ mês/ano da data de referência 

Se periodicidade = “ME”

                data inicial do período =  01 \+ mês/ano da data de referência 

        = = = = =

