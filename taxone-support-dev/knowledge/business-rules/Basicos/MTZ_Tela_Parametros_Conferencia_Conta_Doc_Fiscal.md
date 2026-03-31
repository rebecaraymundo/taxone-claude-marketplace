# MTZ_Tela_Parametros Conferência Conta Doc Fiscal

> Fonte: MTZ_Tela_Parametros Conferência Conta Doc Fiscal.docx






THOMSON REUTERS

Tela Parâmetros da Conferência Conta Doc Fiscal


DOCUMENTO DE REQUISITO

Sumário

1.	Tela	3
2.	Regras dos Campos	4


## Tela







## Regras dos Campos


Localização da tela: Módulo: Básicos >> Report Fiscal
Menu: Operacionais >> Conferência Conta Doc Fiscal >> Parâmetros

Título da tela: Parâmetros de Conferência Conta Doc Fiscal

Opções da barra de menu:
Grupo

NOVO – Limpa todos os campos da tela, com exceção do estabelecimento, permitindo a inclusão de um novo registro.

ABRE – Ao clicar nesta opção, serão exibidos para seleção do usuário todos os dados já parametrizados.

EXCLUI – Permite a exclusão dos dados.

CONFIRMA – Salva os dados incluídos ou alterados.

FECHA – Fecha a janela da parametrização.


Objetivo da Tela: Permitir armazenar perfis de parametrização para o relatório de Conferência Conta Doc Fiscal.

Na abertura da tela, apresentar os campos citados abaixo:







| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| 534766 | Luiz Aguiar | Criação da tela |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Aba Dados Básicos | Aba Dados Básicos | Aba Dados Básicos | Aba Dados Básicos | Aba Dados Básicos | Aba Dados Básicos | Aba Dados Básicos |
| Perfil | Texto | S | S |  | Informa o nome do Perfil de parametrização. | 534766 |
| Estabelecimentos | Texto | S | S | (Cód. - razão social do estabelecimento) | Serão demonstrados o Cod Estab e a Razão Social do estabelecimento logado.  Os dados têm origem na SAFX2064. | 534766 |
| Aba Código de CFOP | Aba Código de CFOP | Aba Código de CFOP | Aba Código de CFOP | Aba Código de CFOP | Aba Código de CFOP | Aba Código de CFOP |
| Códigos de CFOP Devolução | Pasta | S | S | Código - Descrição | Os dados têm origem na SAFX2012. | 534766 |
| Aba Código de Conta | Aba Código de Conta | Aba Código de Conta | Aba Código de Conta | Aba Código de Conta | Aba Código de Conta | Aba Código de Conta |
| Código de Conta | Pasta | S | S | Código - Descrição | Os dados têm origem na SAFX2002. | 534766 |
| Imposto | Texto | S | S |  | Informa o nome do Imposto corresponde a conta.  No caso, o usuário deve preencher o campo com um dos textos abaixo: ICMS IPI ICMS-ST PIS COFINS ICMS-FCP ICMS-DESTINO ICMS-ORIGEM | 534766 |
| Confirma | Botão | - | - |  | Ao tentar gravar um registro:  Os campos de preenchimento obrigatório devem estar preenchidos, caso contrário exibir a mensagem: ‘<Nome funcional> deve ser preenchido’ Não deve ser permitido salvar dois perfis com o mesmo nome. | 534766 |
