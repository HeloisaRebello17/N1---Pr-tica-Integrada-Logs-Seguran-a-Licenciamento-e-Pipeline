# Análise de Segurança - Semgrep

## Arquivos do Projeto

### Código
- `app.py` - Código original
- `app_corrigido.py` - Versão corrigida

### Relatórios
- `relatorio_owasp_vulnerabilidades.md` - Relatório completo
- `RESUMO_EXECUTIVO.md` - Resumo

### Relatórios Técnicos
- `semgrep_detalhado.json` - Resultados JSON
- `semgrep_sarif.json` - Formato SARIF
- `semgrep_junit.xml` - Formato JUnit

### Configuração
- `.semgrep.yml` - Configuração do Semgrep
- `FORMATOS_RELATORIO_SEMGREP.md` - Documentação

## Resultados

- 4 vulnerabilidades encontradas
- 2 categorias OWASP Top 10 relacionadas
- Score: 85/100

### Vulnerabilidades
1. OWASP A03:2021 - Injection (Log Injection)
2. OWASP A05:2021 - Security Misconfiguration

## Como Usar

Ver relatório principal:
```
cat relatorio_owasp_vulnerabilidades.md
```

Executar Semgrep:
```
semgrep scan --config .semgrep.yml app.py
```