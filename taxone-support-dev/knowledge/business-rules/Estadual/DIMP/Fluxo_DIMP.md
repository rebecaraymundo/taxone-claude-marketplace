# Fluxo_DIMP

- **Fonte:** Fluxo_DIMP.docx
- **Modificado:** 2025-03-18
- **Tamanho:** 27 KB

---

1. __Início do Arquivo Digital__
	- __Registro 0000:__ Abertura do arquivo digital e identificação da instituição\. Este é o ponto de partida e obrigatório para todos os arquivos\.
2. __Bloco 0 \- Abertura e Identificação__
	- __Registro 0001:__ Abertura do Bloco 0\.
	- __Registro 0002:__ Identificação de liquidantes diversos \(opcional, dependendo do CNPJ informado no Registro 1110\)\.
	- __Registro 0005:__ Dados complementares do autor do arquivo\.
	- __Registro 0006:__ Dados complementares do técnico responsável \(opcional\)\.
	- __Registro 0100:__ Tabela de Cadastro do Cliente\.
	- __Registro 0105:__ Tabela de VAN do Cliente \(opcional, se aplicável\)\.
	- __Registro 0200:__ Tabela de Cadastro do Meio de Captura\.
	- __Registro 0201:__ Identificação de Titulares de Conta Conjunta \(opcional, se aplicável\)\.
	- __Registro 0300:__ Dados da Instituição Parceira \(opcional\)\.
	- __Registro 0600:__ Autorização Para Instituição Parceira \(apenas para arquivos com finalidade de autorização\)\.
	- __Registro 0700:__ Identificação da Intimação para Informações Específicas \(apenas para arquivos com finalidade de intimação\)\.
	- __Registro 0990:__ Encerramento do Bloco 0\.
3. __Bloco 1 \- Operações de Pagamentos e Demais Transações__
	- __Registro 1001:__ Abertura do Bloco 1\.
	- __Registro 1100:__ Resumo Mensal das Operações\.
		- __Registro 1110:__ Operações Diárias por Meio de Captura\.
			- __Registro 1115:__ Operações por Comprovante de Transação\.
				- __Registro 1120:__ Intermediador de Serviços e Negócios \(opcional\)\.
		- __Registro 1200:__ Cancelamento Extemporâneo \(opcional\)\.
		- __Registro 1220:__ Cancelamento Transação de Intermediador \(opcional\)\.
	- __Registro 1500:__ Resumo Mensal das Operações Financeiras\.
	- __Registro 1600:__ Cancelamento Extemporâneo Consolidado \(opcional\)\.
	- __Registro 1990:__ Encerramento do Bloco 1\.
4. __Bloco 9 \- Controle e Encerramento do Arquivo Digital__
	- __Registro 9001:__ Abertura do Bloco 9\.
	- __Registro 9900:__ Registros do Arquivo\.
	- __Registro 9990:__ Encerramento do Bloco 9\.
	- __Registro 9999:__ Encerramento do Arquivo Digital\.

__Fluxograma Visual:__

- Inicie com o __Registro 0000__\.
- Siga para o __Bloco 0__, começando com __Registro 0001__\.
- Dentro do Bloco 0, siga a hierarquia dos registros, adicionando bifurcações para registros opcionais como 0002, 0006, 0105, etc\.
- Termine o Bloco 0 com __Registro 0990__\.
- Prossiga para o __Bloco 1__ com __Registro 1001__\.
- Dentro do Bloco 1, siga a hierarquia dos registros, com ramificações para registros como 1120, 1200, 1220, etc\.
- Termine o Bloco 1 com __Registro 1990__\.
- Inicie o __Bloco 9__ com __Registro 9001__ e siga até o encerramento com __Registro 9999__\.

