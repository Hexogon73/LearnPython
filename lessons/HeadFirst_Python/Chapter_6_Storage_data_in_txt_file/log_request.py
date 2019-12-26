"""page 285"""


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        log.write(f'{req} -> {res}\n')


log_request('req1', 'res1')
log_request('req2', 'res2')
log_request('req3', 'res3')
