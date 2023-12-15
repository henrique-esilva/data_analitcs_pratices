-- Mostrar nome do professor e nome das atividades que ele é habilitado
-- Mostrar nome do aluno, telefone, data e horário da aula de todas as aulas marcadas
-- Mostrar nome do aluno, telefone e endereço completo
-- Mostrar nome dos produtos, valor e nome de sua categoria
-- Mostrar nome do produto, quantidade vendida e preço vendido de todos os produtos da venda 14

USE academia;

SELECT funcionario.nome AS 'professor', atv.nomeatividade AS 'atividade' FROM funcionario INNER JOIN professor prof ON funcionario.cpffuncionario=prof.cpffuncionario INNER JOIN habilitaprofessor rel ON rel.idprofessor=prof.idprofessor INNER JOIN atividade atv ON atv.idatividade=rel.idatividade;
SELECT aula.dataaula, aula.horario, aluno.nome AS Aluno, aluno.telefone AS 'contato do aluno' FROM aula INNER JOIN aulaaluno ON aulaaluno.idaula=aula.idaula INNER JOIN aluno ON aluno.matricula=aulaaluno.matricula;
SELECT
  a.nome AS NomeAluno,
  a.telefone AS Telefone,
  CONCAT(e.rua, ', ', e.bairro, ', ', e.cidade, ' - ', e.uf, ' ', e.cep) AS EnderecoCompleto
FROM
  aluno a
JOIN
  endereco e ON a.cep = e.cep;
