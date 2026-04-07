# Auto-fix gerado pelo MAS-Ops
# Problema: Timeout sem retry

import time

def call_gateway(payload, retries=3):
    for attempt in range(retries):
        try:
            return _do_request(payload)
        except TimeoutError:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
