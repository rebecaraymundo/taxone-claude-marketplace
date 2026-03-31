# Layout Importação de Serviços Contratados

> Fonte: Layout Importação de Serviços Contratados.docx


Importação de Serviços Contratados
É possível importar declarações de serviços contratados realizadas a partir de outro sistema. Para isto, o arquivo a ser importado deve possuir a extensão '.txt'. Neste arquivo deve constar um cabeçalho com as seguintes informações separadas por ponto e vírgula (;):

- Inscrição Municipal;
- Mês da competência;
- Ano da competência;
- Hora da geração, data da geração e nome / razão social do tomador de serviços;
- Código referente ao serviço contratado;
- A última informação do cabeçalho condiz à frase: "EXPORTACAO DECLARACAO ELETRONICA-ONLINE-NOTA CONTROL" (é necessário que seja escrito exatamente desta forma).

É necessário verificar a compatibilidade das informações do arquivo com relação ao layout descrito abaixo:


Para mais detalhes, consulte um exemplo neste modelo de arquivo. Para salvar este exemplo, clique com o botão direito sobre o link do modelo e utilize a opção "Salvar Como...".

Os códigos dos modelos de documentos variam de acordo com o município. Para maiores informações, entre em contato com a Central de ISSQN.

A inscrição municipal do arquivo a ser importado deve conferir com a inscrição municipal do usuário logado no sistema.

No final do campo 'Código de Área' deve conter também um ponto e vírgula (;).

Para realizar a importação, siga as instruções abaixo:

- Informe o caminho de origem (clique em procurar, localize o arquivo e selecione-o);
- Informe se há dígito verificador para tomador de serviços (sim ou não. Dependendo do município, a opção estará desativada);
- Informe se o ponto (.) será o separador decimal (sim ou não. Caso a opção escolhida seja 'não', será usada a vírgula (,) como separador decimal);
- Clique em ''Importar''. O sistema indicará possíveis erros. Se o arquivo estiver de acordo com o layout requerido e as configurações estiverem corretas, o arquivo será importado e uma mensagem de êxito na operação será exibida.




| Descrição | Tipo de Dado | Observações |
| --- | --- | --- |
| Modelo | Numérico | Código do modelo do documento declarado. Máximo de 3 (três) caracteres. Acesse o Menu Principal do Sistema->Ajuda->Tipos Documentos Fiscais, para ver a tabela de documentos. |
| Número Documento | Numérico | Número sequencial do documento. Máximo de 9 (nove) caracteres. |
| Valor Tributável | Decimal | Valor sobre o qual incidirá o imposto. Máximo de 10 (dez) caracteres. |
| Valor do documento | Decimal | Valor do documento fiscal declarado. Máximo de 10 (dez) caracteres. |
| Alíquota | Decimal | Valor da alíquota. Máximo de 3 (três) caracteres. |
| Data de Emissão | Data "ddmmaaaa" | Data de emissão do documento fiscal. A data não deve conter separadores, apenas números. |
| Data de Pagamento | Data "ddmmaaaa" | Data de pagamento. A data não deve conter separadores, apenas números. |
| CPF / CNPJ | Numérico | CPF / CNPJ do prestador declarado. Máximo de 14 (quatorze) caracteres. |
| Razão Social | Alfanumérico | Razão Social do prestador declarado. Máximo de 150 (cento e cinquenta) caracteres. |
| Inscrição Municipal | Alfanumérico | Inscrição Municipal do prestador declarado. Máximo de 15 (quinze) caracteres. |
| Imposto Retido | Booleano 0 (não) ou 1 (sim) | Carácter que indica a retenção de imposto, representando "1" para imposto retido "SIM" e "0" para imposto retido "NÃO". Máximo de 1 (um) carácter. |
| CEP | Numérico | CEP relacionado ao endereço do prestador de serviços. Máximo de 8 (oito) caracteres e não deve conter separadores. |
| Endereço | Alfanumérico | Endereço do prestador de serviços (nome da rua, avenida, travessa). Máximo de 200 (duzentos) caracteres. |
| Número | Numérico | Número do endereço do prestador de serviços. Máximo de 6 (seis) caracteres. |
| Bairro | Alfanumérico | Bairro do prestador de serviços. Máximo de 50 (cinquenta) caracteres. |
| Cidade | Alfanumérico | Cidade do prestador de serviços. Máximo de 50 (cinquenta) caracteres. |
| Estado | Alfanumérico | Estado do prestador de serviços. Máximo de 2 (dois) caracteres. |
| Código de Área | Numérico | Código DDD de área do prestador de serviços. Máximo de 2 (dois) caracteres. |
| Tributado no município | Booleano 0 (não) ou 1 (sim) | Carácter que indica se o imposto foi tributado no município ou não, representando "1" para tributado no município "SIM" e "0" para tributado no município "NÃO". Máximo de 1 (um) carácter. |
| Item LC | Numérico | Código do Item LC a ser declarado. Máximo de 4(quatro) caracteres. |
