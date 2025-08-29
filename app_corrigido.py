import os, time, logging, sys, re
from pythonjsonlogger import jsonlogger
from ddtrace import tracer, patch
from datadog import statsd


# Configuração segura de variáveis de ambiente
# Correção para OWASP A05:2021 - Security Misconfiguration
os.environ.setdefault("DD_SERVICE", os.environ.get("SERVICE_NAME", "unknown-service"))
os.environ.setdefault("DD_ENV", os.environ.get("ENVIRONMENT", "development"))
os.environ.setdefault("DD_VERSION", os.environ.get("VERSION", "0.0.0"))


patch(logging=True)

logger = logging.getLogger("soma")
logger.setLevel(logging.INFO)
formatter = jsonlogger.JsonFormatter("%(asctime)s %(message)s")

sh = logging.StreamHandler(sys.stdout); sh.setFormatter(formatter); logger.addHandler(sh)

# Configuração segura de caminho de log
log_path = os.environ.get("LOG_PATH", "./logs/soma.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)
fh = logging.FileHandler(log_path, encoding="utf-8"); fh.setFormatter(formatter); logger.addHandler(fh)
logger.propagate = False

def sanitize_log_data(data):
    """
    Sanitiza dados para logging seguro
    Correção para OWASP A03:2021 - Injection (Log Injection)
    """
    if isinstance(data, str):
        # Remove caracteres especiais que podem afetar logs
        return re.sub(r'[^\w\s\-\.]', '', data)
    return str(data)

def validate_input(a, b):
    """
    Valida entrada da função soma
    Boa prática de segurança
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Parâmetros devem ser números")
    return True

def soma(a: int, b: int) -> int:
    # Validação de entrada
    validate_input(a, b)
    
    start = time.perf_counter()
    with tracer.trace("soma.operacao", resource="soma"):
        r = a + b
        dur_ms = (time.perf_counter() - start) * 1000
        statsd.increment("soma.requests", tags=["op:soma"])
        statsd.distribution("soma.latency_ms", dur_ms, tags=["op:soma"])
        
        # Logging seguro com dados sanitizados
        logger.info({
            "event": "soma_executada",
            "a": sanitize_log_data(a),
            "b": sanitize_log_data(b),
            "resultado": sanitize_log_data(r),
            "latency_ms": round(dur_ms, 2)
        })
        return r

if __name__ == "__main__":
    try:
        print(soma(2, 3))
        print(soma(40, 2))
    except Exception as e:
        logger.error(f"Erro na execução: {sanitize_log_data(str(e))}")
        sys.exit(1) 