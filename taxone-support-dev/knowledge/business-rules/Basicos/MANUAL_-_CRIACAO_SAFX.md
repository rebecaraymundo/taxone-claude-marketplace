# MANUAL - CRIAÇAO SAFX

> Fonte: MANUAL - CRIAÇAO SAFX.docx


Manual Passo a Passo para a Criação de uma SAFX
- Analisar a User Story requerida, preencher conforme contexto da SAFX a ser criada, indicar prazo de entrega (em qual sprint e data), colocar horas estimadas, mudar status para Active, alocar a demanda para o B.A que irá desenvolvê-la e indicar tags (exemplo: no início da demanda, inserir a tag com o nome do projeto e BA)
- Exemplo de demanda para B.A desenvolver o documento de requisitos

- Desenvolver o documento de requisitos (MTZ) – explicar o contexto (para que serve, quais campos serão necessários, quais as informações referentes aos campos que serão criados ou estarão na SAFX, qual a localização das telas e qual a localização da tela após o sucesso da carga da SAFX feita pelo usuário, quais as regras de negócio, criar uma tabela que mostre detalhes sobre os campos (nome do campo, descrição, índice, obrigatoriedade, chave primária etc.), como serão feitas as cargas e importações etc.
- Incluir número da demanda do ADO no MTZ
- Incluir mensagens de erro que os campos devem exibir, caso o usuário não preencha (normalmente, todos os campos sinalizados como OBRIGATÓRIOS devem receber mensagens de erro)
- Exemplo de documento MTZ
- Pasta com documentos MTZ: SharePoint
- Após desenvolver o documento MTZ da SAFX, fazer a reserva do número da SAFX desejado (exemplo: normalmente, os campos 3000 são para Reforma Tributária, 2000 para Cadastro)
- Para fazer a reserva, vá para a pasta Reservas_Controle TXT > Reservas_Tabelas_SAFX_BASICAS_TACES_TFIX, nesse arquivo é possível fazer a reserva de números para SAFX, TFIX, TACES e BASICAS

- Preencher conforme imagem abaixo:

- Após a reserva do número da SAFX, é necessário preencher a TFIX 11 (com base na SAFX criada, é necessário identificar o grupo correspondente ao tipo de SAFX que será criada (verificar com DEV ou B.A)):
- Exemplo de preenchimento da TFIX 11

- É necessário preencher também o arquivo da SAFX 22 (mensagens de erro que aparecerão, caso o usuário não preencha campos que forem obrigatórios), é possível criar novas mensagens ou reutilizar outras já criadas

- Preencher também a TFIX96 (aqui, todos os campos que sairão na nova SAFX criada devem ser inseridos e preenchidos, mostrando a qual SAFX pertencem, índice, obrigatoriedade, descrição, nome do campo, tamanho, tipo, número da demanda, quais campos recebem mensagem de erro e qual o número da mensagem de erro/campo reservado na TFIX22, comentário)

- Link para Reserva de Códigos TFIX


- Quando uma SAFX estiver em produção ou estiver disponibilizada por DEV e QA, preencher o documento de Manual Layout MastersafDW, que possui todos os novos campos que serão publicados no próximo patch pelo time de documentação (localizado na pasta Manuais de Layout)



- NÃO ESQUECER DE INCLUIR NÚMERO DA DEMANDA E CRÍTICA DE ERROS (Mensagens da TFIX 22 -> exemplo: campo COD_TIPO_LIVRO, MFS-768407,  crítica de erro 913307
- Incluir os campos em ordem crescente (exemplo: a nova SAFX 343 será publicada e na documentação de Manual de Layout de SAFX deve ficar após a SAFX 342)
- Quando terminar de inserir os novos campos, lembrar de posicionar a aba de Índice e Tabelas SAFX na primeira linha (no caso, SAFX01 que fica no topo/início da página)

- SEMPRE deixar na primeira aba também (Versão Manual) e com o número do Patch já atualizado (o número é baseado em quando os novos campos serão disponibilizados no Patch -> perguntar para o QA)

- É necessário também, preencher o arquivo Alteracoes_Tabelas, que consta quais campos de SAFX novos serão disponibilizados (similar ao manual de layout de SAFX)
- Inserir campos na ordem correta

- C/S = Criação de novos campos (normalmente usada no meu caso)
- Ao finalizar os preenchimentos na tabela do manual de layout e no arquivo ALTERACOES_TABELAS_SAFX, lembre-se de retornar ao primeiro campo de ambos os arquivos (ir ao topo da página) e salvar o arquivo estando na capa/versao_manual de cada arquivo usado)


- Após fazer o preenchimento do Manual de Layout SAFX e dar check-in no documento, é necessário criar uma demanda no board do time de documentação, para abrir uma MDOC de publicação desse manual layout (avisar também no grupo de REQUISITOS sobre a atualização do novo manual de layout)
- Exemplo: Demanda MDOC - SAFX 342
