# Formatos de Relatório do Semgrep

## Relatórios Gerados

O Semgrep gerou automaticamente os seguintes relatórios em diferentes formatos:

## 1. JSON Padrão (semgrep_relatorio.json)
**Formato:** JSON nativo do Semgrep  
**Uso:** Integração com ferramentas, APIs, processamento automatizado  
**Comando:** `semgrep scan --config auto app.py -o semgrep_relatorio.json --json`

**Características:**
- Estrutura JSON simples
- Dados técnicos completos
- Fácil processamento por scripts
- Compatível com ferramentas de CI/CD

## 2. JSON Detalhado (semgrep_detalhado.json)
**Formato:** JSON com regras customizadas  
**Uso:** Análise detalhada com regras específicas  
**Comando:** `semgrep scan --config .semgrep.yml app.py -o semgrep_detalhado.json --json`

**Características:**
- Regras customizadas aplicadas
- 4 vulnerabilidades detectadas
- Informações de timing e performance
- Metadados completos

**Vulnerabilidades Encontradas:**
1. python.security.audit.env-var-default (3 ocorrências)
   - Linhas 7, 8, 9
   - Severidade: INFO
2. python.security.audit.log-injection (1 ocorrência)
   - Linhas 29-33
   - Severidade: WARNING

## 3. SARIF (semgrep_sarif.json)
**Formato:** SARIF 2.1.0 (Static Analysis Results Interchange Format)  
**Uso:** Padrão da indústria, integração com IDEs, ferramentas de segurança  
**Comando:** `semgrep scan --config .semgrep.yml app.py -o semgrep_sarif.json --sarif`

**Características:**
- Padrão OASIS reconhecido
- Compatível com GitHub, GitLab, Azure DevOps
- Estrutura padronizada
- Metadados ricos das regras

**Estrutura SARIF:**
```json
{
  "version": "2.1.0",
  "runs": [{
    "results": [
      {
        "ruleId": "python.security.audit.log-injection",
        "message": {"text": "Possível injeção de log..."},
        "locations": [{
          "physicalLocation": {
            "artifactLocation": {"uri": "app.py"},
            "region": {
              "startLine": 29,
              "endLine": 33,
              "snippet": {"text": "logger.info({..."}
            }
          }
        }]
      }
    ]
  }]
}
```

## 4. JUnit XML (semgrep_junit.xml)
**Formato:** JUnit XML para testes  
**Uso:** Integração com sistemas de CI/CD, Jenkins, GitLab CI  
**Comando:** `semgrep scan --config .semgrep.yml app.py -o semgrep_junit.xml --junit-xml`

**Características:**
- Formato padrão para testes
- Compatível com Jenkins, GitLab CI, GitHub Actions
- Estrutura de testes/suites
- Relatórios de falhas estruturados

## Comparação dos Formatos

| Formato | Extensão | Uso Principal | Estrutura | Integração |
|---------|----------|---------------|-----------|------------|
| JSON | .json | APIs, Scripts | Simples | Alta |
| SARIF | .json | IDEs, Ferramentas | Padrão | Muito Alta |
| JUnit XML | .xml | CI/CD | Testes | Alta |

## Como Usar os Relatórios

### Para Desenvolvedores:
```bash
# Relatório JSON para análise rápida
cat semgrep_detalhado.json | jq '.results[] | {rule: .check_id, severity: .extra.severity, line: .start.line}'
```

### Para CI/CD:
```yaml
# GitHub Actions
- name: Semgrep Scan
  run: semgrep scan --config auto . -o semgrep_results.json --json
- name: Upload Results
  uses: actions/upload-artifact@v2
  with:
    name: semgrep-results
    path: semgrep_results.json
```

### Para IDEs:
- VS Code: Instalar extensão SARIF Viewer
- IntelliJ: Importar arquivo SARIF
- Eclipse: Plugin SARIF Support

## Vantagens dos Relatórios Nativos

**Vantagens:**
- Formatos padronizados da indústria
- Integração automática com ferramentas
- Estrutura consistente entre execuções
- Metadados ricos (timing, performance, etc.)
- Compatibilidade com ecossistema de segurança

**Limitações:**
- Sem mapeamento OWASP automático
- Sem contexto em português
- Sem recomendações de correção
- Formato técnico (não executivo)

## Recomendação de Uso

### Para Desenvolvimento:
- JSON Detalhado para análise técnica
- SARIF para integração com IDEs

### Para CI/CD:
- JUnit XML para pipelines de teste
- JSON para processamento automatizado

### Para Relatórios Executivos:
- Relatórios customizados (como os que criamos)
- SARIF + processamento para dashboards

---

*Relatórios gerados pelo Semgrep v1.134.0* 