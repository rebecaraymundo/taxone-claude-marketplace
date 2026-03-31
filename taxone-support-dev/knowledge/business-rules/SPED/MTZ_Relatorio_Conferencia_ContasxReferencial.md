# MTZ_Relatorio_Conferencia_ContasxReferencial

> Fonte: MTZ_Relatorio_Conferencia_ContasxReferencial.doc

TITLE  "ECD - Livros SPED (Matriz)"  \* MERGEFORMAT ECD - Relatório Conferência Contas x Referencial


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		MFS46980	ECD – Relatório Conferência Contas x Referencial	Incluído no Tax One o relatório para conferência das contas da empresa x plano referêncial 		MFS-58039	Alessandra Cristina Navatta	Incluir a funcionalidade no DW.
Incluir no processamento as validações: 
-Contas com Naturezas Distintas nas Contas Referencial e Contas da Empresa
- Centro de Custo em mais de uma Conta do Plano Referencial.		

REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	Selecionar a x02 (definitiva) filtrando por empresa/estabelecimento selecionadas em tela, cuja a data de saldo esteja compreendida, entre data inicial e data final, deverão ser recuperados todas as contas distintamente.	MFS46980		RN02	Selecionar a x80 (definitiva) filtrando por empresa/estabelecimento selecionadas em tela, cuja a data de saldo esteja compreendida, entre data inicial e data final, deverão ser recuperados todas as contas distintamente.	MFS46980		RN03	Neste caso deverão ser recuperados os grupos válidos para empresa/estabelecimento selecionado em tela e compreendido na data inicial e final informados. Recuperar da tabela x2002 (definitiva) todas as contas pertencente ao grupo recuperado anteriormente e onde a validade da conta seja maior ou igual a data final informada.
	MFS46980		RN04	Deverão ser recuperadas as contas referenciais consultando a tabela x2101 (definitiva) pela versão selecionada em tela, essas recuperadas deverão ser verificadas as contas existentes na recuperação anterior, referenciadas por conta ou mais centro de custo.
	MFS46980		RN05	
Deverá conter as seguintes informações:


[ALTERAÇÃO MFS-58039] Quando não existir informações a ser exibida no relatório:
-Se não existir dados na base (de acordo com a parametrização realizada na geração do relatório), exibir a mensagem: ‘Não há dados na base, de acordo com as informações indicadas na geração do relatório’.
-Se existir dados na base (de acordo com a parametrização realizada na geração do relatório), porém, não existir nenhuma divergência de informação, exibir a mensagem: ‘Não foi identificado nenhuma conta contábil que foi movimentada no período sem estar associada a uma conta referencial'.
Nomenclatura do arquivo: ConfReferencial_MOVIMENTO.xls
	MFS46980
MFS-58039		RN06	Se a opção ‘Contas com Naturezas Distintas nas Contas Referencial e Contas da Empresa’, estiver marcada, o sistema deverá varrer as parametrizações existentes na tela Plano de Contas Referencial X Plano de Contas da Empresa (X2101), considerando as contas que foram movimentadas no período indicado em tela (geração do relatório) e apresentar no relatório as contas da empresa que possuem natureza diferente da natureza da conta referencial.

Considerar a tabela abaixo para identificar se as naturezas são compatíveis:

Plano de Conta Referencial
Plano de Contas da Empresa

Patrimonial
0. Compensação
1. Ativo
2. Passivo
5. Mutações Ativas ("Variações Patrimoniais" anuais)
6. Mutações  Passivas ("Variações Patrimoniais" anuais)                                                                                                                                                                                                           
7. Patrimônio Líquido                                                                                                                                                                                      
          9. Outros

Resultado
3. Despesa
4. Receita
8. Custo


O relatório deve conter as seguintes informações (arquivo de saída em formato excel):

Entidade, Código Empresa, Código do Estabelecimento, Código e Descrição Conta Referencial, Natureza da Conta Referencial, Código e Descrição Conta Empresa, Natureza da Conta Empresa, Código e Descrição Centro de Custo.
Ordenação:
Ordenar os registros por Entidade, Código Empresa, Código do Estabelecimento, Código e Descrição Conta Referencial, Natureza da Conta Referencial, Código e Descrição Conta Empresa, Natureza da Conta Empresa, Código e Descrição Centro de Custo.


Atenção: Esta validação deve ser realizada independente da opção indicada no parâmetro ‘Tipo de Origem’, porém, esse parâmetro é importante, para verificar se a origem a ser considerada será a X02, X80 e ou ambas. Quando não for considerada a X80, as informações de centro de custo deverão sair em branco no relatório.

Quando não existir informações a ser exibida no relatório:

-Se não existir dados na base (de acordo com a parametrização realizada na geração do relatório), exibir a mensagem: ‘Não há dados na base, de acordo com as informações indicadas na geração do relatório’.

-Se existir dados na base (de acordo com a parametrização realizada na geração do relatório), porém, não existir nenhuma divergência de informação, exibir a mensagem: ‘Não foi identificado nenhuma Natureza de Conta Referencial, divergente da Natureza da Conta da Empresa, de acordo com as informações indicadas na geração do relatório’.

Nomenclatura do arquivo: ConfReferencial_NAT_CTAS.xls

	MFS-58039		RN07	
Se a opção ‘Centro de Custo em mais de uma Conta do Plano Referencial’ estiver marcada, o sistema deverá varrer as parametrizações existentes na tela Plano de Contas Referencial X Plano de Contas da Empresa (X2101), considerando as contas e centro de custo movimentados no período indicado em tela (geração do relatório) e apresentar no relatório as contas referenciais que estão associadas com o mesmo centro de custo.

Atenção: Esta validação deve apenas ser realizada se as opções ‘Saldos por Centro de Custo’ e ‘Todas as Contas’ no parâmetro ‘Tipo de Origem’ estiver marcado, pois a mesma só faz sentido ser feita para origem de X80. 

O relatório deve conter as seguintes informações (arquivo de saída em formato excel): 

Entidade, Código e Descrição Centro de Custo, Código Empresa, Código Estabelecimento, Código e Descrição Conta Referencial, Código e Descrição Conta Empresa.
Ordenação:
Ordenar os registros por Entidade, Código e Descrição de Centro de Custo, Código e Descrição de Conta Referencial,  Código e Descrição Conta Empresa.


Quando não existir informações a ser exibida no relatório:

-Se a opção ‘Todas as Contas’ for selecionada e não existir informações na X80 na base, exibir a mensagem no log: ‘Não foi encontrado saldos por centro de custo na base, no período indicado na geração do relatório.’

-Se não existir dados na base (de acordo com a parametrização realizada na geração do relatório), exibir a mensagem: ‘Não há dados na base, de acordo com as informações indicadas na geração do relatório’.

-Se existir dados na base (de acordo com a parametrização realizada na geração do relatório), porém, não existir nenhuma divergência de informação, exibir a mensagem: ‘Não foi identificado nenhum centro de custo que está associado a mais de uma conta referencial, de acordo com as informações indicadas na geração do relatório’.

Nomenclatura do arquivo: ConfReferencial_CCUSTO_CTAREF.xls
	MFS-58039		RN08	Esta funcionalidade deve ser disponibilizada inclusive no produto DW.
	MFS-58039