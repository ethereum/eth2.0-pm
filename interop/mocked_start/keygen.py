from py_ecc.bls.api import privtopub
from hashlib import sha256 as _sha256
from typing import List, Dict
from yaml import dump, Dumper

CURVE_ORDER = 52435875175126190479447740508185965837690552500527637822603658699938581184513


def sha256(x):
    return _sha256(x).digest()


def generate_validator_keypairs(N: int) -> List[Dict]:
    keypairs = []
    for index in range(N):
        privkey = int.from_bytes(
            sha256(index.to_bytes(length=32, byteorder='little')),
            byteorder='little'
        ) % CURVE_ORDER
        pubkey = privtopub(privkey)
        keypairs.append({'privkey': privkey, 'pubkey': pubkey})
    return keypairs


if __name__ == '__main__':
    keypairs = generate_validator_keypairs(100)
    keypairs_yaml = dump(keypairs, Dumper=Dumper)
    with open('keygen_test.yaml', 'w') as f:
        f.write(keypairs_yaml)
