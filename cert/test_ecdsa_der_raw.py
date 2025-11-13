import os
import binascii
from ecdsa_der_raw import der_to_raw, raw_to_der


def test_known_der_to_raw_and_back():
    # Example DER signature (r and s are small test values)
    # This DER encodes r=0x01..01 (32 bytes) and s=0x02..02 (32 bytes) with leading zeroes omitted.
    # We'll craft a DER using raw_to_der and then parse it.
    r = bytes([1] * 32)
    s = bytes([2] * 32)
    raw = r + s
    der = raw_to_der(raw)

    parsed = der_to_raw(der, 32)
    assert parsed == raw


def test_roundtrip_random():
    import secrets

    for size in (32, 48, 66):
        for _ in range(10):
            r = secrets.randbits(size * 8 - 1).to_bytes(size, "big")
            s = secrets.randbits(size * 8 - 1).to_bytes(size, "big")
            raw = r + s
            der = raw_to_der(raw)
            parsed = der_to_raw(der, size)
            assert parsed == raw


if __name__ == "__main__":
    test_known_der_to_raw_and_back()
    test_roundtrip_random()
    print("OK")
