# MTZ-EFD_PIS-COFINS-Manutencao_Registro_0120

> Fonte: MTZ-EFD_PIS-COFINS-Manutencao_Registro_0120.docx





THOMSON REUTERS

Módulo EFD Contribuições

Manutenção Registro 0120 (Identificação dos Periodos Dispensados)


Localização: Menu SPED, Módulo Escrituração Fiscal Digital das Contribuições, item Manutenção  Registros do Bloco 0  Identificação dos Períodos Dispensados (0120)

DOCUMENTO DE REQUISITO



Sumário

1.	Tela	3
2.	Regras dos Campos	3




## Tela







## Regras dos Campos



Tabela epc_per_dispensados




| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS12767 | Atualização das alterações do GP vrs. 1.22 | Atualização das alterações do GP vrs. 1.22 | 17/08/2017  (criação do documento) |
| MFS28409 | Liliane Assaf | Alteração na permitir a inclusão de mais de um registro no mesmo ano calendário. | 30/07/2019 |


| Campo | PK |  | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ano Calendário | X |  | N | S | S | AAAA |  |
| Mês de Apresentação do Registro | X |  | A | S | S |  | Lista contendo todos os meses: Janeiro, Fevereiro, ..., Dezembro  [MFS-28409] Inclusão da regra: O mês de Apresentação do Registro passa a fazer parte da chave de identificação, permitindo a inclusão de vários registros de distintos meses de apresentação para o mesmo ano calendário. |
| Mês de Dispensa | X |  | A | S | S |  | Pelo menos um mês de dispensa deve estar selecionado.  [MFS-28409] Exclusão da Restrição: O mês de Apresentação do Registro obrigatoriamente deve ser selecinado com Mês de Dispensa. Caso contrário, o registro não será salvo e será exibita a seguinte mensagem: “O Mês de apresentação escolhido precisa ser selecionado em “Mês de dispensa”. Segundo o Guia Prático existem duas formas de apresentação do 0120: - mês a mês: neste caso o Mês de Dispensa seria igual ao Mês de apresentação; - em dezembro: neste caso os Meses de Dispensa seriam: Janeiro, fevereiro,  até Novembro.  Dezembro não estari serlecionado. Excluímos essa regra de controle da tela, para evitar que uma nova mudança da regra do Guia Prático, afete o funcionamento da tela.  Cabe ao cliente selecionar corretamente os meses de dispensa conforme a forma de apresentação do registro 0120 que ele estiver adotando. |
| Informação Complementar |  |  | A | N | S | Listbox | [MFS12767]: Alterado o tratamento do campo “Informação Complementar”.  Este campo é uma lista com as opções  abaixo, mas também pode ser digitado com qualquer informação que o usuário queira inserir.  01-Pessoa jurídica imune ou isenta do IRPJ (Indicador "02" do Campo 13 do registro "0000") 02-Órgãos públicos, autarquias e fundações públicas 03-Pessoa jurídica inativa 04-Pessoa jurídica em geral, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos 05-Sociedade em Conta de Participação - SCP, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos 06-Sociedade Cooperativa, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos 07-Escrituração decorrente de incorporação, fusão ou cisão, sem operações geradoras de receitas (tributáveis ou não) ou de créditos 99-Demais hipóteses de dispensa de escrituração, relacionadas no art. 5º, da IN RFB nº 1.252, de 2012   O preenchimento do campo é obrigatório a partir de Ago/2017, e nesse caso deve ser utilizado um dos valores da lista.  Assim, antes de salvar a operação, será feita a seguinte crítica:   Se  (Ano Calendário > 2017)  ou        (Ano Calendário = 2017 e mês selecionado =            Ago / Set / Out / Nov ou Dez)  Nesses casos, quando o campo não for preenchido, a operação não será salva e será exibida a seguinte mensagem de erro:  “A partir de Agosto de 2017, utilizar somente o conteúdo disponibilizado na lista” |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
