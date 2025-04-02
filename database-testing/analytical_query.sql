SELECT
    registro_ans,
    razao_social,
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS despesa_total
FROM financial_statements
JOIN active_health_plan_operators ON REG_ANS = registro_ans
WHERE DESCRICAO LIKE '%EVENTOS/%SINISTROS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND DATA_REGISTRO BETWEEN '2024-10-01' AND '2024-12-31'
AND (VL_SALDO_FINAL - VL_SALDO_INICIAL) < 0
GROUP BY registro_ans, razao_social
ORDER BY despesa_total ASC
LIMIT 10;

SELECT registro_ans, razao_social, SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS despesa_anual
FROM financial_statements
JOIN active_health_plan_operators ON REG_ANS = registro_ans
WHERE DESCRICAO LIKE '%EVENTOS/%SINISTROS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND DATA_REGISTRO BETWEEN '2024-01-01' AND '2024-12-31'
    AND (VL_SALDO_FINAL - VL_SALDO_INICIAL) < 0
GROUP BY registro_ans, razao_social
ORDER BY despesa_anual ASC
LIMIT 10;
