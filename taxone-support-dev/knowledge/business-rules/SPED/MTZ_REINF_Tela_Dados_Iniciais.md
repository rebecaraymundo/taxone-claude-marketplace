# MTZ_REINF_Tela_Dados_Iniciais

> Fonte: MTZ_REINF_Tela_Dados_Iniciais.docx






THOMSON REUTERS

Tela de Dados Iniciais
SPED – Reinf



DOCUMENTO DE REQUISITO




Sumário

1.	Tela	4
2.	Regras dos Campos	5


## Tela


## Regras dos Campos



Localização da tela: Módulo: SPED >> EFD – Reinf
Menu: Parâmetros >> Dados Iniciais (Primeira tela do módulo)

Título da tela: Dados Iniciais

Opções da barra de menu:

[MFS17933]
NOVO – Limpa todos os campos da tela, com exceção do estabelecimento, permitindo a inclusão de um novo registro.

ABRE – Ao clicar nesta opção, serão exibidos para seleção do usuário todos os dados já parametrizados.

EXCLUI – Permite a exclusão dos dados.

CONFIRMA – Salva os dados incluídos ou alterados.

RELATÓRIO – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado.

FECHA – Fecha a janela da parametrização.





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-12777 | Elenilson Coutinho | Tela de Dados Iniciais |
| MFS14222 | Lara Aline | Inclusão do campo ‘Desconsiderar NFs sem Valor de Retenção informado’ |
| MFS14404 | Lara Aline | Ajuste no campo ‘Desconsiderar NFs sem Valor de Retenção informado’ para tratar o evento R-2020. |
| MFS14821 | Lara Aline | Inclusão dos campos Tipo de Ambiente e Proc. Emissão Evento. |
| MFS16067 | Lara Aline | Inclusão do campo ‘Desconsiderar sem Valor de Retenção informado’ para evento R-2040 |
| MFS17269 | Lara Aline | Ajuste no campo Tipo de Ambiente conforme nova versão 1.3.02. |
| MFS17933 | Lara Aline | Inclusão da opção excluir o cadastro dos Dados Iniciais |
| MFS21078 | Lara Aline | Inclusão do parâmetro ‘Considerar para composição da Receita Bruta’ para o evento R-2050. |
| MFS-58342 | Alessandra Cristina Navatta | Inclusão do parâmetro “Gerar evento R-2055 a partir da SAFX63 – Arquivo de Contribuição Rural - INSS” |
| MFS-67713 | Alessandra Cristina Navatta | Inclusão do parâmetro “Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)”. Ajuste no label do parâmetro “Gerar evento R-2055 a partir da SAFX63 – Arquivo de Contribuição Rural – INSS” para “Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS” |
| MFS90387 | Rogério Ohashi | Inclusão do parâmetro ‘Considerar para composição da Receita Bruta’ para o evento R-2055. |
| MFS-98132 | Rogério Ohashi | Alteração do parâmetro ‘Considerar para composição da Receita Bruta’ para o evento R-2055, alterar o Label De: “3 – Base de Cálculo do INSS” Para: “3 – Base de Cálculo do INSS RURAL”. |
| MFS-565337 | Alessandra Cristina Navatta | Inclusão do parâmetro “Consolida o Valor Bruto dos Registros da SAFX53 com Mesmo Número de Nota e Operações Distintas”, para o evento R-4020 |
| MFS-581948 | Alessandra Cristina Navatta | Inclusão do Parâmetro ‘Recuperação dos registros da SAFX53 com base na data de’ para os eventos R-4010 e R-4020 |
| MFS-607389 | Alessandra Cristina Navatta | Inclusão do Parâmetro ‘Considerar Valor Base igual ao Valor Bruto’ nos eventos R-4020 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | TextBox | S | S |  | Campo será carregado com o estabelecimento logado no sistema. Caso nenhum estabelecimento tenha sido selecionado no log, serão listados todos os estabelecimentos da empresa logada e que usuário tenha permissão de acesso. | MFS-12777 |
| Tipo de Ambiente | DropDown | N | N | Default: Produção | Deverão ser listadas as seguintes opções:   1 - Produção 2 - Produção Restrita – Dados Reais 3 - Produção Restrita – Dados Fictícios | MFS14821 MFS17269 |
| Proc. Emissão Evento | DropDown | N | N | Default: Aplicativo do Contribuinte | Deverão ser listadas as seguintes opções:   1 - Aplicativo do Contribuinte 2 - Aplicativo Governamental | MFS14821 |
| Evento R-2010/R-2020 – Retenção Contribuição Previdenciária – Serviços Tomados/Prestados | Evento R-2010/R-2020 – Retenção Contribuição Previdenciária – Serviços Tomados/Prestados | Evento R-2010/R-2020 – Retenção Contribuição Previdenciária – Serviços Tomados/Prestados | Evento R-2010/R-2020 – Retenção Contribuição Previdenciária – Serviços Tomados/Prestados | Evento R-2010/R-2020 – Retenção Contribuição Previdenciária – Serviços Tomados/Prestados | Evento R-2010/R-2020 – Retenção Contribuição Previdenciária – Serviços Tomados/Prestados | Evento R-2010/R-2020 – Retenção Contribuição Previdenciária – Serviços Tomados/Prestados |
| Desconsiderar NFs sem Valor de Retenção informado | Checkbox | N | S | Default: Não selecionado | Quando selecionado deverá desconsiderar todas as NFs que não tiverem valor de retenção informado na geração do R-2010 e R-2020. | MFS-14222 MFS-14404 |
| Evento R-2040 – Recursos Repassados a Associação Desportiva | Evento R-2040 – Recursos Repassados a Associação Desportiva | Evento R-2040 – Recursos Repassados a Associação Desportiva | Evento R-2040 – Recursos Repassados a Associação Desportiva | Evento R-2040 – Recursos Repassados a Associação Desportiva | Evento R-2040 – Recursos Repassados a Associação Desportiva | Evento R-2040 – Recursos Repassados a Associação Desportiva |
| Geração com base nas informações | Radio Button | N | S | Default Selecionado: Documento Fiscal de Serviço | Este parâmetro define a base das informações para geração do evento R-2040.  Documento Fiscal de Serviço: Quando selecionada esta opção as informações serão geradas com base na SAFX09.  Contas a Pagar: Quando selecionada esta opção as informações serão geradas com base na SAFX03. | MFS-12777 |
| Desconsiderar sem Valor de Retenção informado | Checkbox | N | S | Default: Não selecionado | Quando selecionado deverá desconsiderar todas as NFs ou Arquivo de Fornecedores (Contas a Pagar) que não tiverem valor de retenção informado na geração do R-2040. | MFS-16067 |
| Evento R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria | Evento R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria | Evento R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria | Evento R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria | Evento R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria | Evento R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria | Evento R-2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria |
| Considerar para composição da Receita Bruta | Checkbox | N | S | Default: Valor Contábil | Este parâmetro define a qual a composição do valor da receita bruta na geração do evento R-2050.  Deverão ser listadas as seguintes opções:   1 – Valor Contábil 2 – Valor Total 3 – Base de Cálculo do INSS. | MFS-21078 |
| Replicar para os Estabelecimentos | Checkbox | N | S | Default: Não selecionado | Quando selecionado deverá permitir replicar a parametrização para outros estabelecimentos. | MFS-12777 |
| Evento R-2055 – Aquisição de Produção Rural: | Evento R-2055 – Aquisição de Produção Rural: | Evento R-2055 – Aquisição de Produção Rural: | Evento R-2055 – Aquisição de Produção Rural: | Evento R-2055 – Aquisição de Produção Rural: | Evento R-2055 – Aquisição de Produção Rural: | Evento R-2055 – Aquisição de Produção Rural: |
| Geração a partir da SAFX63 – Arquivo de Contribuição Rural - INSS | Checkbox | N | S | Default: Não selecionado | Nesse campo o usuário poderá selecionar se deseja gerar o evento R-2055 a partir da SAFX63. | MFS-58342 MFS-67713 |
| Geração por Data de Emissão (SAFX07 – Arquivos de Notas Fiscais | Checkbox | N | S | Default: desabilitado e Não selecionado | Esse parâmetro só ficará habilitado e possível de marcação se o parâmetro “Geração a partir da SAFX63 – Arquivo de Contribuição Rural - INSS”, estiver desmarcado.  Nesse campo o usuário poderá selecionar se deseja gerar o evento R-2055 com base na data de emissão quando a origem for documento fiscal (SAFX07). | MFS-67713 |
| Considerar para composição da Receita Bruta | Checkbox | N | S | Default: Valor Contábil | Este parâmetro define a qual a composição do valor da receita bruta na geração do evento R-2055 no quadro “Evento R-2055 – Aquisição de Produtor Rural”.  Deverão ser listadas as seguintes opções:   1 – Valor Contábil 2 – Valor Total 3 – Base de Cálculo do INSS RURAL. 3 – Base de Cálculo do INSS. | MFS-90387 MFS-98132 |
| Evento R-4010/R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Física e Pessoa Jurídica | Evento R-4010/R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Física e Pessoa Jurídica | Evento R-4010/R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Física e Pessoa Jurídica | Evento R-4010/R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Física e Pessoa Jurídica | Evento R-4010/R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Física e Pessoa Jurídica | Evento R-4010/R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Física e Pessoa Jurídica | Evento R-4010/R-4020 – Pagamentos/Créditos a Beneficiário Pessoa Física e Pessoa Jurídica |
| Recuperação dos registros da SAFX53 com base na data de | Radio Button | N | S | Default Selecionado: Movimento | Este parâmetro define a data que será considerada para recuperar os registros na geração dos eventos R-4010 e/ou R-4020  Movimento: Quando selecionada esta opção a recuperação dos registros serão com base no campo 03 – DATA_MOVTO da SAFX53.  Fato Gerador: Quando selecionada esta opção a recuperação dos registros serão com base no campo 26 – DATA_FATO_GERADOR da SAFX53. | MFS-581948 |
| Evento R-4020 – Pagamentos /Créditos a Beneficiário Pessoa Jurídica | Evento R-4020 – Pagamentos /Créditos a Beneficiário Pessoa Jurídica | Evento R-4020 – Pagamentos /Créditos a Beneficiário Pessoa Jurídica | Evento R-4020 – Pagamentos /Créditos a Beneficiário Pessoa Jurídica | Evento R-4020 – Pagamentos /Créditos a Beneficiário Pessoa Jurídica | Evento R-4020 – Pagamentos /Créditos a Beneficiário Pessoa Jurídica | Evento R-4020 – Pagamentos /Créditos a Beneficiário Pessoa Jurídica |
| Consolida o Valor Bruto dos Registros da SAFX53 com Mesmo Número de Nota e Operações Distintas | Checkbox | N | S | Default: Não selecionado | Quando selecionado este parâmetro, será consolidado o valor bruto dos registros da SAFX53 com mesmo número de nota e com operações distintas | MFS-565337 |
| Considerar Valor Base igual ao Valor Bruto | Checkbox | N | S | Default: Selecionado | Quando selecionado este parâmetro, na geração do evento R-4020, o valor da base será igual ao valor do campo valor bruto (independente se o campo Valor Base na tabela de arquivo de controle de tributo estiver preenchido ou não).  Caso o parâmetro esteja desmarcado, o valor base será de acordo com a informação do campo Valor Base, criado na tabela de arquivo de controle de tributo, nesta demanda. Obs. Visando não impactar os clientes que possuem o cenário do valor base igual ao valor bruto, criamos este parâmetro, mantendo a definição anterior (valor base igual ao valor do campo valor bruto), quando este parâmetro estiver selecionado. Lembrando que o campo valor base, não existia na X53 (foi criado nesta demanda e definido como não obrigatório). | MFS-607389 |
