# MTZ_DW_Tela_Notas_Explicativas_dos_Demonstrativos_Contabeis

> Fonte: MTZ_DW_Tela_Notas_Explicativas_dos_Demonstrativos_Contabeis.docx




THOMSON REUTERS

Módulo SPED - ECD – Escrituração Contábil Digital
Tela de Notas Explicativas dos Demonstrativos Contábeis





DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3
2.	Layout da Tela	6



























## Regras dos Campos



Módulo do Mastersaf DW: SPED >> ECD – Escrituração Contábil Digital
Menu de Localização: Manutenção >> Notas Explicativas dos Demonstrativos Contábeis

Título da tela: Notas Explicativas dos Demonstrativos Contábeis









## Layout da Tela


(Dados de preenchimento fictícios):












Ao clicar no ícone: , o sistema deverá exibir algumas opções de campos para rodar o relatório de dados dos cadastros desta parametrização:




| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15698 | João Henrique de Araujo | Criação da Tela de Notas Explicativas dos Demonstrativos Contábeis. | 11/01/2018 |
| MFS22414 | João Henrique de Araujo | Inclusão do campo “Número de Referência” na SAFX257 | 31/01/2018 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Drop Down | S | S | Default: Conforme selecionado do Manager | Na lista será demonstrado código e a razão social de cada estabelecimento centralizador*, somente da empresa que acessou o módulo.  Centralizador - XXX-XXXXXXXXXXXXXXXXX (Centralizador + cód. e razão social do estabelecimento)  Caso algum estabelecimento não tenha sido associado a uma centralização, este será demonstrado na listagem de estabelecimentos precedido da palavra “Descentralizado”:  Descentralizado - XXX-XXXXXXXXXXXXXXXXX (Descentralizado + cód. e razão social do estabelecimento)  *Entende-se Estabelecimento Centralizador aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa serão demonstrados os estabelecimentos como descentralizados. | MFS15698 |
| Indicador de Aglutinação | Drop Down | S | S | Default: Desabilitado | Na lista serão demonstradas as descrições dos Indicadores de Aglutinação. Na importação da SAFX257, o conteúdo desse campo é carregado com o código. Na tela de manutenção realizar De x Para no campo para exibir a descrição, ou seja:  B – Preencher com: “Balanço” D – Preencher com: “DRE“ L – Preencher com: “DLPA” M – Preencher com: “DMPL”  Caso não preenchido exibir a seguinte mensagem: “O campo Indicador de Aglutinação deve ser informado”. | MFS15698 |
| Número de Referência | Textbox | N | S | Default: Desabilitado | Nesse campo o usuário informa o número de referência da Nota Explicativa para cada código de aglutinação referente ao tipo de demonstração contábil.  Caractere 12 posições Não obrigatório | MFS22414 |
| Código de Aglutinação | Pasta | S | S | Sem Default: Seleção do usuário | Nesse campo o usuário poderá informar o código de aglutinação para o respectivo indicador de aglutinação selecionado.  Observação/Tratamentos: Mesma validação importação.  Os códigos de aglutinação necessariamente precisam estar carregados e/ou cadastrados na SAFX2102 - Códigos de Aglutinação Balanço/DRE/DLPA/DMPL com suas respectivas informações de empresa, estabelecimento e qual indicador de balanço pertence.  A partir da seleção do “Indicador de Aglutinação”, o sistema deverá exibir os Códigos de Aglutinação pertencentes ao indicador informado no parâmetro anterior.  Se o usuário tentar selecionar o campo “Código de Aglutinação” antes de escolher a opção de “Indicador de Aglutinação”, exibir uma mensagem de alerta: “Selecione o Indicador de Aglutinação”.  Na pesquisa do campo ser possível visualizar a descrição do código de aglutinação. Na exibição da tela, retornar apenas o código de aglutinação. | MFS15698 |
| Data da Demonstração | Data | S | S | Default: habilitado 00/00/0000 | Nesse campo o usuário poderá informar a Data da Demonstração. Esse campo indica a data em que o demonstrativo contábil foi gerado para o respectivo código de aglutinação.  Caso não preenchido exibir a seguinte mensagem: “O campo Data da Demonstração deve ser informado”. | MFS15698 |
| Nota Explicativa | Textbox | S | S | Sem Default: Campo em branco para digitação | Nesse campo o usuário poderá informar o descritivo para a Nota Explicativa do código de aglutinação.  Caso não preenchido exibir a seguinte mensagem: “O campo Código de Aglutinação deve ser informado”. | MFS15698 |
