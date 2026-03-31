# MTZ-EFD_PIS-COFINS-Tela_Cadastro_Conta_Contabil_(M400M800)

> Fonte: MTZ-EFD_PIS-COFINS-Tela_Cadastro_Conta_Contabil_(M400M800).docx



THOMSON REUTERS

Módulo SPED - EFD – Contribuições
Tela de Cadastro de Conta Contábil (M400/M800)



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos:	3
2.	Layout da Tela:	6

## Regras dos Campos:



Módulo do Mastersaf DW: SPED > EFD – Escrituração Fiscal Digital das Contribuições
Menu de Localização: Parâmetros > Cadastro de Conta Contábil (M400/M800)

Título da tela: Cadastro de Conta Contábil (M400/M800)








## Layout da Tela:




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-15817 | João Henrique | Este documento tem como objetivo criar a tela de Cadastro de Conta Contábil (M400/M800) no Módulo do SPED Contribuições. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Texto | S | N | Formato: Combo Box  Default: Estabelecimento informado no manager | Informar o Estabelecimento que corresponde a parametrização (aparecerá automaticamente quando informado no login).  Tratamento: Campo desabilitado quando informado estabelecimento na tela inicial. Se o estabelecimento não for informado na tela inicial, será demonstrado o combo box em branco. Se não for selecionado um estabelecimento apresentar uma mensagem de aviso: “Estabelecimento deve ser informado”. | MFS15817 |
| Data Cadastro da Conta | Data | S | N | Formato: Text Input DD/MM/AAAA  Default: Habilitado: 00/00/0000 | Informar a Data Cadastro da Conta na parametrização para armazenamento de histórico.   Tratamento: Após salvar o registro não permitir a edição. Se o campo não for preenchido, apresentar uma mensagem de aviso:  “A Data Cadastro Conta deve ser preenchida”. Se o usuário cadastrar uma conta com as mesmas informações (CST, Conta Contábil e Data Cadastro da Conta para o mesmo REGISTRO M400 OU M800), apresentar uma mensagem de aviso: “Conta Contábil cadastrada, por favor verificar”. Observação sobre Data Cadastro + Conta Contábil: O usuário poderá cadastrar a mesma conta, com o mesmo CST para datas diferentes.  Na geração do arquivo magnético será considerada a conta contábil mais atual. | MFS15817 |
| CST PIS/CONFIS | Texto | S | N | Formato: Seleção TACES65  Default: Desabilitado | Informar de acordo com a Tabela de CST (TACES65), seguindo a regra:  Tratamento: Após salvar o registro não permitir a edição; O sistema deverá exibir apenas os seguintes CSTs para seleção: ’4’,‘5’,’6’,’7’,’8’,’9’, a descrição deverá ser exibida ao lado do código CST. Se o campo não for preenchido, apresentar uma mensagem de aviso: “O CST PIS/CONFINS deve ser informado”. | MFS15817 |
| Conta | Numérico | S | S | Formato: Seleção SAFX2002  Default: Habilitado | Deverá ser informada a conta contábil referente ao Imposto, utilizada para Contabilização, de acordo com a Tabela de Plano de Contas (SAFX2002).  Tratamento: Ao lado da “pasta” do campo conta, o sistema deverá apresentar o Grupo da Conta Contábil com maior validade. Ao lado do código da conta Contábil deverá apresentar a descrição. Após salvar o cadastro o usuário poderá alterar a conta e salvar novamente. Se o campo não for preenchido, apresentar uma mensagem de aviso: “A Conta deve ser informada”. | MFS15817 |
| M400/M800 | Texto | S | N | Formato: CheckBox  Default: Desabilitado | Informar se deseja gerar a conta contábil para o registro M400 ou M800.  Tratamento: Após salvar o registro não permitir a edição; O usuário deverá selecionar ao menos um Checkbox: M400 OU M800. O campo é de preenchimento obrigatório. Se o usuário não marcar uma opção apresentar uma mensagem de aviso:  “Por favor marcar uma opção para Geração dos Registros: “M400 ou M800”. Ao selecionar um dos checkbox (Ex:M400), automaticamente o outro ficará bloqueado para seleção. O usuário poderá cadastrar em seguida a mesma conta contábil e dados para o outro checkbox (Ex:M800). Quando selecionar a opção e salvar o cadastro, o sistema deverá gerar a conta contábil e o CST parametrizados no arquivo magnético da EFD Contribuições para o registro marcado. | MFS15817 |
