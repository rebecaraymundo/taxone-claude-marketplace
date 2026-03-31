# MTZ_REINF_Tela_Geracao_Previa_Evento_R2055

> Fonte: MTZ_REINF_Tela_Geracao_Previa_Evento_R2055.docx






THOMSON REUTERS

Tela de Geração Prévia do Evento R-2055
REINF



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-REINF
Menu: REINF >> Geração Prévia>> Evento R-2055

Título da tela: Geração Prévia do Evento R-2055






* Descrição não disponível em tela

| OS/CH/MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-58346 | Alessandra Cristina Navatta | Criação da tela de geração prévia do Evento R-2055 (a especificação foi baseada na documentação da tela já existente do evento S-1250 no produto e-Social) |
| MFS-63539 | Alessandra Cristina Navatta | Inclusão de data de validade para a versão 1.5.1 (ambiente produção) |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Executar | Botão | - | - | - | Quando acionado o sistema irá iniciar o processo de pré geração dos eventos.   Ao executar, se o estabelecimento estiver configurado em Dados Iniciais com o campo Tipo de Ambiente = Produção, a data da geração (sysdate) for inferior a 21/05/2021 e a versão igual a 1.5.1, não permitir a geração do arquivo e exibir a mensagem: “Em fatos geradores até 20/05/2021, não é permitido utilizar a versão 1.5.1, para o ambiente de produção” | MFS-63539 |
| Período (MM/AAAA) | Data | S | S | Formato: MM/AAAA | Mês e ano para a geração dos movimentos.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Informe a Período” | MFS-58346 |
| Versão | Alfanumérico | S | N | Listbox | Este campo é uma lista, que a princípio terá apenas uma opção: [1.5.1] | MFS-58346 |
| Geração Multiempresa | Checkbox | N | S | Default: não selecionado | Quando selecionado pelo usuário, a geração será multiempresa.  Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Relação de Estabelecimentos”. | MFS-58346 |
| Geração através de Estabelecimento Centralizador | Checkbox | N | S | Default: não selecionado | Quando selecionado pelo usuário, a geração será por estabelecimento centralizador.  Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Relação de Estabelecimentos”.  Ele marcado irá gerar todos os estabelecimentos centralizados dele.   Mensagem no log:  Erro: 'Estabelecimento - xxx com erro na geração do evento R-2055.'  Não achar o estabelecimento: ' Estabelecimento - xxx não existem dados para geração do evento R-2055.'  Finalizado o estabelecimento com sucesso: ' Estabelecimento - xxx com geração do evento R-2055 finalizada com sucesso.' | MFS-58346 |
| Empresa/Estabelecimento | Empresa/Estabelecimento | Empresa/Estabelecimento | Empresa/Estabelecimento | Empresa/Estabelecimento | Empresa/Estabelecimento | Empresa/Estabelecimento |
| Selecionar | Pasta de Seleção | N | S |  | Pasta padrão que permite seleção de um estabelecimento específico. | MFS-58346 |
| Marcar Todos | Checkbox | N | S | Default: não selecionado | Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”. | MFS-58346 |
| Relação de estabelecimentos* | Checkbox | N | S | Default: não selecionado | Se parâmetro “Geração Multiempresa” e “Geração através de Estabelecimento Centralizador” estiverem desmarcados:  Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo E somente os estabelecimentos centralizados** ou centralizadores*, ou seja, o estabelecimento precisa estar centralizado em algum centralizador ou ser um estabelecimento centralizador. Não iremos demonstrar estabelecimento Descentralizados:  XXX / XXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento  Se parâmetro “Geração Multiempresa” estiver marcado e o parâmetro “Geração através de Estabelecimento Centralizador” estiver desmarcado:  Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento (Centralizados** e Centralizadores*), mas neste caso serão demonstradas todas as empresas:  XXX / XXX-XXXXXXXXXXXXXXXXX (cód. empresa + cód. e razão social do estabelecimento)  Se parâmetro “Geração Multiempresa” estiver desmarcado e o parâmetro “Geração através de Estabelecimento Centralizador” estiver marcado:  Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento centralizador*, somente da empresa que acessou o módulo, sendo que, o código do estabelecimento deve ser precedido pela palavra “Centralizador”:  XXX / Centralizador - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Centralizador + cód. e razão social do estabelecimento)  Se parâmetro “Geração Multiempresa” e o parâmetro “Geração através de Estabelecimento Centralizador” estiverem marcados:  Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento centralizador*, mas neste caso serão demonstradas todas as empresas, sendo que, o código do estabelecimento deve ser precedido pela palavra “Centralizador”:  XXX / Centralizador - XXX-XXXXXXXXXXXXXXXXX (cód. empresa + Centralizador + cód. e razão social do estabelecimento)  Obs: No caso da geração multiempresa, as regras da geração do arquivo não se modificam. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do arquivo existirão estabelecimentos de empresas distintas.  * Entende-se Estabelecimento Centralizador aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa (ou empresas, no caso de geração multiempresa), não serão demonstrados nenhum estabelecimento.  ** Entende-se Estabelecimento Centralizado aquele que foi associado a um estabelecimento centralizador na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizado ou centralizador nesta tela para a empresa (ou empresas, no caso de geração multiempresa), não serão demonstrados nenhum estabelecimento. | MFS-58346 |
