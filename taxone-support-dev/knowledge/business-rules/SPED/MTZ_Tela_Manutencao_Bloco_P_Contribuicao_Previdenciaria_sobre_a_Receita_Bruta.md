# MTZ_Tela_Manutenção_Bloco P_Contribuicao_Previdenciaria_sobre_a_Receita_Bruta

> Fonte: MTZ_Tela_Manutenção_Bloco P_Contribuicao_Previdenciaria_sobre_a_Receita_Bruta.docx



## EFD - Contribuições - Tela Contribuição Previdenciária sobre a Receita Bruta P100 (SAFX185)




Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Manutenção >> Registro do Bloco P >> Contribuição Previdenciária sobre a Receita Bruta (P100)


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO






| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3584-DW1 | Criação do documento | Tela – Contribuição Previdenciária sobre a Receita Bruta | 13/04/2012 |
| OS4316 | Inclusão de campo | Incluir o campo Código e Descrição da SCP |  |
| CH21166_2014 | Alteração da validação do campo 13 | Este documento tem como objetivo alterar a validação do preenchimento do campo 13 - Valor da Base de Cálculo da Contribuição Previdenciária  sobre a Receita Bruta |  |


| Cód. |  | DR |
| --- | --- | --- |
| RN01 | Criar a tela Contribuição Previdenciária Sobre a Receita Bruta (P100), para receber informações que serão informadas no bloco P , registro P100. A tela receberá dados por estabelecimento.  Localização: Sped → EFD – Contribuições → Manutenções Registro Bloco P | OS3584-DW1 |
| RN02 | Esta nova tela deverá conter os botões (Novo, Abre, Exclui, Confirme, P199, Relatório, Fecha.) | OS3584-DW1 |
| RN03 | Campos Obrigatórios: Estabelecimento, Data Inicial, Data Final, Ind_Cod_Ativ_Econ, , Código Receita, Valor Receita Bruta – Total, Valor Receita Bruta – Atividade, Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta, Alíquota Contrib. Prev. Sobre Receita Bruta e Valor Contrib. Prev. Sobre Receita Bruta | OS3584-DW1 |
| RN04 | Campos Chaves: Empresa, Estabelecimento, Data Inicial, Ind_Cod_Ativ_Econ, Código Receita,  Cod_Cta | OS3584-DW1 |
| RN05 | A conta contábil deve estar cadastrada na tabela de plano de contas (SAFX2002). | OS3584-DW1 |
| RN06 | O código de centro de custo deve estar registrado na Tabela Centro de Custos (SAFX2003). | OS3584-DW1 |
| RN07 | O Indicador do Código da Atividade Econômica deve constar na tabela 5.1.1 (TACES75), caso contrário exibir msg ao usuário. | OS3584-DW1 |
| RN08 | Se o indicador da Atividade Econômica for 99999999 permitir qualquer valor de alíquota, mesmo que não esteja cadastrada na TACES75 | OS3584-DW1 |
| RN09 | Se o indicador da Atividade Econômica for diferente de 99999999 , só permitir as alíquotas que estão informada na tabela 5.1.1  (TACES 75), caso contrário exibir a msg ao usuário. | OS3584-DW1 |
| RN10 | As datas Inicial e Final devem estar dentro do mesmo período, senão, exibir a msg ao usuário. | OS3584-DW1 |
| RN11 | Código Receita, valores válidos: 298501 – Empresas Prestadoras de Serviço de Tecnologia da Informação – TI e Tecnologia da Informação e Comunicação – TCI 298502 – Contribuicao Previdenciaria Sobre Receita Bruta - Empresas Prestadoras de Servicos TI e TIC  - 13º Salario  299101 - Contribuição Previdenciária sobre a Receita Bruta – Demais 299102 - Contribuição Previdenciária sobre Receita Bruta – Demais 13º Salario  Este campo será recuperado da dwt_cod_receita filtrando o tributo CPRB. | OS3584-DW1 |
| RN12 | Deverá ser criado o campo Código da SCP, acompanhado da pasta de seleção da informação e o campo de texto para demonstração da descrição vinculada ao código.  Quando acionada a pasta, serão demonstrados os registros da tabela SAFX2057 – Cadastro da SCP. Para o código selecionado, será demonstrada também a descrição da SCP.  Nome do campo em tela: “Código da SCP:”  Caso o usuário informe um código que não tenha cadastro correspondente na SAFX2057, retornar a mensagem de erro: “Cadastro da SCP não encontrado”. | OS4316 |
| RN13 | Campo 13 – Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta  [ALTERADA – CH21166_2014] Tabela: SAFX185 Item: 13 Nome do Campo: Será definido pelo A&D Descrição: Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta Tipo: N Tamanho: 015V002 Comentário: Valor da Base de Cálculo da Contribuição Previdenciária sobre a Receita Bruta   (Campo 13 = Campo 10 – Campo 12) Obrigatório Validação:  O valor informado neste campo deve ser maior ou igual a zero, então fazer a verificação da seguinte forma: Se o valor do Campo 10 e o valor do Campo 12 for igual permitir preencher com zeros (0,00); Se o valor do Campo 10 for maior que o Campo 12 permitir preencher com zeros (0,00) ou a diferença (a informação correta será de responsabilidade do usuário); Se o valor do Campo 10 for menor que o Campo 12 e o campo 13 receber valor maior que zero exibir a seguinte msg ao usuário: “O valor informado no campo “XXXXX(13)” deve ser maior que zero.”  Observação: A mensagem é para entender que não haverá valor negativo, pois o valor do campo 12 nunca poderá ser maior que o campo 10, mas ele pode ser zero quando os valores forem iguais. | OS3584-DW CH21166_2014 |
| RN14 | Exibir msgs de alerta quando o usuário acionar o botão salvar e :  1 – O campo ‘Valor Receita Bruta – Atividade’ maior que o campo  ‘Valor Receita Bruta Total’ Msg: O valor do campo ‘Valor Receita Bruta – Atividade’ deve ser menor ou igual ao valor do campo  ‘Valor Receita Bruta Total’, deseja continuar?  Se selecionar sim, o registro é gravado, se não, o registro não é salvo, mas as informações digitadas na tela  não serão perdidas.  2 –Valor do campo “Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta” não for a  diferença entre os campos “Valor Receita Bruta – Atividade ”  e  “Valor Exclusões da Receita Bruta” Msg: o Valor informado no campo  “Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta”  deve ser  igual ao “Valor Receita Bruta – Atividade”  menos o valor do campo “Valor Exclusões da Receita Bruta”  3- OS campos Valor Receita Bruta – Total, Valor Receita Bruta – Atividade, Valor Base Cálculo – Contrib. Prev. Sobre Receita Bruta, Alíquota Contrib. Prev. Sobre Receita Bruta e Valor Contrib. Prev. Sobre Receita Bruta, devem ser maiores que zero.  Msg: O valor informado no campo “XXXXX” deve ser maior que zero. | OS3584-DW1 |
