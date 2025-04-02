SELECT
    registro_ans,
    razao_social,
    SUM(vl_saldo_final - vl_saldo_inicial) AS despesa_total
FROM financial_statements
JOIN active_health_plan_operators ON reg_ans = registro_ans
WHERE descricao LIKE '%EVENTOS/%SINISTROS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND data_registro BETWEEN '2024-10-01' AND '2024-12-31'
AND (vl_saldo_final - vl_saldo_inicial) < 0
GROUP BY registro_ans, razao_social
ORDER BY despesa_total ASC
LIMIT 10;

SELECT registro_ans, razao_social, SUM(vl_saldo_final - vl_saldo_inicial) AS despesa_anual
FROM financial_statements
JOIN active_health_plan_operators ON reg_ans = registro_ans
WHERE descricao LIKE '%EVENTOS/%SINISTROS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND data_registro BETWEEN '2024-01-01' AND '2024-12-31'
    AND (vl_saldo_final - vl_saldo_inicial) < 0
GROUP BY registro_ans, razao_social
ORDER BY despesa_anual ASC
LIMIT 10;
