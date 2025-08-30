# Pipeline Integrado - Testes, SAST e Licenciamento

## Visão Geral

Este pipeline automatiza a execução de testes, análise de segurança (SAST) e auditoria de licenciamento no GitHub Actions.

## Componentes do Pipeline

### 1. Job: Testes e Logs
- **Objetivo:** Executar testes básicos com logging estruturado
- **Artefatos:** Logs de execução dos testes
- **Dependências:** Python 3.12, python-jsonlogger, ddtrace, datadog

### 2. Job: Análise SAST
- **Objetivo:** Executar análise de segurança com Semgrep
- **Configurações:**
  - Regras de segurança audit
  - Regras de secrets
  - Regras OWASP Top Ten
- **Artefatos:** Relatório SARIF
- **Falha automática:** Se vulnerabilidades críticas forem detectadas

### 3. Job: Auditoria de Licenciamento
- **Objetivo:** Verificar licenças das dependências
- **Ferramenta:** pip-licenses
- **Licenças incompatíveis:** GPL-3.0, AGPL-3.0, LGPL-3.0
- **Artefatos:** Relatório de licenças em Markdown e JSON
- **Falha automática:** Se licenças incompatíveis forem detectadas

### 4. Job: Relatório Final
- **Objetivo:** Gerar relatório consolidado
- **Funcionalidades:**
  - Status de todos os jobs
  - Resumo de vulnerabilidades
  - Resumo de licenças
  - Comentário automático em Pull Requests

## Configuração

### Triggers
- Push para branches: `main`, `segurança`
- Pull Requests para branch: `main`

### Arquivos de Configuração
- `.github/workflows/security-pipeline.yml` - Pipeline principal
- `.semgrep-pipeline.yml` - Regras customizadas do Semgrep
- `requirements.txt` - Dependências do projeto

## Execução

### Local
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar testes
python app_corrigido.py

# Executar Semgrep
semgrep scan --config .semgrep-pipeline.yml .

# Verificar licenças
pip-licenses --format=markdown
```

### GitHub Actions
O pipeline executa automaticamente em:
1. Push para branches configuradas
2. Pull Requests para main

## Resultados

### Artefatos Gerados
1. **test-logs/** - Logs de execução dos testes
2. **semgrep-results.sarif** - Resultados da análise SAST
3. **license-report.md** - Relatório de licenças
4. **security-pipeline-report.md** - Relatório consolidado

### Critérios de Falha
- Vulnerabilidades críticas/altas detectadas pelo Semgrep
- Licenças incompatíveis encontradas
- Falha na execução dos testes

### Critérios de Sucesso
- Todos os jobs executados com sucesso
- Nenhuma vulnerabilidade crítica detectada
- Nenhuma licença incompatível encontrada

## Monitoramento

### Pull Requests
- Comentário automático com relatório de segurança
- Status visual dos jobs no GitHub
- Artefatos disponíveis para download

### Notificações
- Status de sucesso/falha visível no GitHub
- Relatórios detalhados nos artefatos
- Logs completos para debugging

## Personalização

### Adicionar Novas Regras Semgrep
Editar `.semgrep-pipeline.yml`:
```yaml
- id: nova.regra
  pattern: |
    padrao_a_detectar
  message: "Descrição da vulnerabilidade"
  severity: ERROR
  languages: [python]
```

### Modificar Licenças Incompatíveis
Editar o pipeline em `.github/workflows/security-pipeline.yml`:
```bash
INCOMPATIBLE_LICENSES=("GPL-3.0" "AGPL-3.0" "LGPL-3.0" "NOVA-LICENSE")
```

### Adicionar Novos Testes
Modificar o job `test-and-logs` no pipeline para incluir novos testes.

## Troubleshooting

### Problemas Comuns
1. **Falha no Semgrep:** Verificar configuração das regras
2. **Falha na auditoria de licenças:** Verificar dependências no requirements.txt
3. **Falha nos testes:** Verificar logs de execução

### Debug
- Todos os logs estão disponíveis nos artefatos do GitHub Actions
- Relatórios detalhados são gerados automaticamente
- Status de cada job é visível na interface do GitHub
