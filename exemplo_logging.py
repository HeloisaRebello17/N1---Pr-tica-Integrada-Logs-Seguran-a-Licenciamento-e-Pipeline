import logging
import sys
from pythonjsonlogger import jsonlogger

# Configuração do logger
logger = logging.getLogger("exemplo")
logger.setLevel(logging.INFO)

# Formatter JSON
formatter = jsonlogger.JsonFormatter(
    fmt='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Handler para console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Handler para arquivo
file_handler = logging.FileHandler("exemplo.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Exemplos de logs
def exemplo_logs():
    print("=== Exemplos de Logging com JSON Logger ===\n")
    
    # Log simples
    logger.info("Aplicação iniciada")
    
    # Log com dados estruturados
    logger.info({
        "event": "usuario_login",
        "user_id": "12345",
        "ip": "192.168.1.100",
        "status": "success"
    })
    
    # Log de erro
    logger.error({
        "event": "erro_operacao",
        "error_code": "E001",
        "message": "Falha na conexão com banco de dados",
        "severity": "high"
    })
    
    # Log de operação
    logger.info({
        "event": "operacao_executada",
        "operacao": "soma",
        "parametros": {"a": 10, "b": 20},
        "resultado": 30,
        "tempo_execucao_ms": 15.5
    })
    
    # Log de warning
    logger.warning({
        "event": "configuracao_deprecated",
        "feature": "old_api",
        "recomendacao": "Usar nova API v2"
    })

if __name__ == "__main__":
    exemplo_logs()
    print("\n=== Logs salvos em 'exemplo.log' ===")
