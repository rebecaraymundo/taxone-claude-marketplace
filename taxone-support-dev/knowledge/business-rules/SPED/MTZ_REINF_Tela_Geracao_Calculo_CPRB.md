# MTZ_REINF_Tela_Geracao_Calculo_CPRB

> Fonte: MTZ_REINF_Tela_Geracao_Calculo_CPRB.docx






THOMSON REUTERS

Geração do Cálculo CPRB – EFD- Reinf
SPED – Reinf



DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: Cálculo da CPRB >> Geração do Cálculo

Título da tela: Geração do Cálculo da CPRB





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS17215 | Lara Aline | Inclusão da Tela de Geração do Cálculo da CPRB do EFD – Reinf |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Execução | Radio Button | N | S | Default Selecionado: Imediata | Este Campo permite ao usuário programar a importação do arquivo de retorno. Programação que pode ser:  Imediata - Processo de importação realizado naquele exato momento.   Programada – Processo de importação automático programado para a data e hora desejada pelo usuário. | MFS17215 |
| Data/Hora de Execução | Texto | N | S | Default: Desabilitado | Este campo permite ao usuário informar a data e hora desejada para importação do arquivo (Processo automático).  Campo será habilitado apenas quanto o campo Tipo de Execução na opção “Programada” for selecionado. | MFS17215 |
| Executar | Botão | N | N |  | Quando acionado o sistema irá iniciar o processo de pré geração dos eventos. | MFS17215 |
| Data Inicial | Data | S | S | Formato: DD/MM/AAAA | Caso não preenchido exibir a seguinte mensagem: “O campo Data Inicial deve ser informado”. | MFS17215 |
| Data Final | Data | S | S | Formato: DD/MM/AAAA | Caso não preenchido exibir a seguinte mensagem: “O campo Data Final deve ser informado”. | MFS17215 |
| Geração Multiempresa | Checkbox | N | S | Default: Não selecionado | Quando selecionado pelo usuário, a geração será multiempresa.  Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Empresa/ Estabelecimento”. | MFS17215 |
| Selecionar | Pasta de Seleção | N | S |  | Pasta padrão que permite seleção de um estabelecimento específico. | MFS17215 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”. | MFS17215 |
| Empresa/Estabelecimento | Checkbox | S | S | Default: não selecionado | Nesse campo deverá apresentar todos os estabelecimentos da empresa do login que possuam o cadastro das Informações do Contribuinte preenchido e devido à inclusão do campo Geração Multiempresa, seguir a seguinte regra:  Se parâmetro “Geração Multiempresa” estiver marcado  Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão demonstradas todas as empresas:  XXX / XXX-XXXXXXXXXXXXXXXXX (cód.empresa + cód. e razão social do estabelecimento)  Se parâmetro “Geração Multiempresa” estiver desmarcado  Na lista será demonstrado apenas o código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo.  XXX-XXXXXXXXXXXXXXXXX (cód. e razão social do estabelecimento)  Ao menos uma Empresa/Estabelecimento deverá ser selecionada, caso contrário exibir a seguinte mensagem: Ao menos uma Empresa/Estabelecimento deve ser selecionada. | MFS17215 |
