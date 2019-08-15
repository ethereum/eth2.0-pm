# Mocked start of Eth2 for interoperability testing

## Pubkey/privkey generation

There is a compute/storage tradeoff to be made here between calculating the required validators and reading them from a YAML file ([./keygen_10000_validators.yaml](./keygen_10000_validators.yaml)) and it is left up to implementors to choose which they prefer.

The following script is used to generated pubkey/privkeys for the first `N` validators. The `i`-th deposit/validator index uses the `validator_index_to_pubkey[i]` pubkey and associated privkey.

```python
CURVE_ORDER = 52435875175126190479447740508185965837690552500527637822603658699938581184513
validator_index_to_pubkey = {}
pubkey_to_privkey = {}
privkey_to_pubkey = {}
for index in range(N):
    privkey = int.from_bytes(
        sha256(int_to_bytes(n=index, length=32)),
        byteorder='little'
    ) % CURVE_ORDER
    pubkey = bls.privtopubkey(privkey)
    pubkey_to_privkey[pubkey] = privkey
    privkey_to_pubkey[privkey] = pubkey
    validator_index_to_pubkey[index] = pubkey
```

### Test vectors

[./keygen_test_vector.yaml](./keygen_test_vector.yaml) is a YAML file containing a list of the first 10 validators and their key pairs. The list index corresponds to the validator number. For the generation of more or fewer indices, see the script used to generate it at [./keygen.py](./keygen.py)
