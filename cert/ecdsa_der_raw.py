"""Utilities to convert ECDSA signatures between ASN.1/DER (r,s) and raw (r||s) formats.

Functions:
 - der_to_raw(der_sig, field_size): convert DER-encoded ECDSA signature to raw bytes (r||s)
 - raw_to_der(raw_sig): convert raw bytes (r||s) to ASN.1/DER-encoded signature

field_size is the size in bytes of each coordinate (for P-256 = 32, P-384 = 48, P-521 = 66).
"""
from __future__ import annotations

import math
from typing import Tuple


def _int_to_fixed_bytes(value: int, length: int) -> bytes:
    b = value.to_bytes(length, byteorder="big")
    return b


def _fixed_bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b, byteorder="big")


def der_to_raw(der_sig: bytes, field_size: int) -> bytes:
    """Convert a DER-encoded ECDSA signature to raw format (r||s).

    Args:
        der_sig: ASN.1/DER encoded ECDSA signature (sequence of two INTEGERs).
        field_size: size in bytes of each coordinate (e.g. 32 for P-256).

    Returns:
        raw signature bytes of length 2*field_size.

    Raises:
        ValueError on parse errors or if integers are too large.
    """
    if not der_sig:
        raise ValueError("Empty DER signature")

    pos = 0
    if der_sig[pos] != 0x30:
        raise ValueError("Expected SEQUENCE (0x30)")
    pos += 1

    # read length
    length = der_sig[pos]
    pos += 1
    if length & 0x80:
        num_len_bytes = length & 0x7F
        if num_len_bytes == 0 or num_len_bytes > 2:
            raise ValueError("Unsupported length encoding in DER sequence")
        if pos + num_len_bytes > len(der_sig):
            raise ValueError("Truncated DER length")
        length = int.from_bytes(der_sig[pos:pos+num_len_bytes], "big")
        pos += num_len_bytes

    if pos + length != len(der_sig):
        # allow extra trailing but warn
        # We'll require exact match to avoid ambiguity
        raise ValueError("DER sequence length mismatch")

    def _read_integer() -> int:
        nonlocal pos
        if der_sig[pos] != 0x02:
            raise ValueError("Expected INTEGER (0x02)")
        pos += 1
        ilen = der_sig[pos]
        pos += 1
        if ilen & 0x80:
            num_len_bytes = ilen & 0x7F
            if num_len_bytes == 0 or num_len_bytes > 2:
                raise ValueError("Unsupported integer length encoding")
            if pos + num_len_bytes > len(der_sig):
                raise ValueError("Truncated integer length")
            ilen = int.from_bytes(der_sig[pos:pos+num_len_bytes], "big")
            pos += num_len_bytes
        if pos + ilen > len(der_sig):
            raise ValueError("Truncated INTEGER content")
        ib = der_sig[pos:pos+ilen]
        pos += ilen
        # INTEGER is signed; if there's a leading 0x00 it's used to prevent negative
        if len(ib) > 0 and ib[0] == 0:
            # strip one leading zero
            ib = ib[1:]
        return int.from_bytes(ib, byteorder="big")

    r = _read_integer()
    s = _read_integer()

    # ensure r and s fit into field_size
    max_int = 1 << (field_size * 8)
    if r >= max_int or s >= max_int:
        raise ValueError("Integer too large for field size")

    print('r=', r)
    print('s=', s)
    rb = _int_to_fixed_bytes(r, field_size)
    sb = _int_to_fixed_bytes(s, field_size)
    return rb + sb


def raw_to_der(raw_sig: bytes) -> bytes:
    """Convert raw (r||s) signature to ASN.1/DER encoded signature.

    Args:
        raw_sig: raw signature bytes (r concatenated with s). Must be even length.

    Returns:
        DER-encoded signature bytes.
    """
    if len(raw_sig) % 2 != 0:
        raise ValueError("Raw signature must have even length")
    half = len(raw_sig) // 2
    r = int.from_bytes(raw_sig[:half], "big")
    s = int.from_bytes(raw_sig[half:], "big")

    def _encode_integer(x: int) -> bytes:
        if x == 0:
            return b"\x02\x01\x00"
        xb = x.to_bytes((x.bit_length() + 7) // 8, "big")
        # if highest bit is 1, prefix 0x00 to indicate positive integer
        if xb[0] & 0x80:
            xb = b"\x00" + xb
        return b"\x02" + len(xb).to_bytes(1, "big") + xb

    r_enc = _encode_integer(r)
    s_enc = _encode_integer(s)
    seq = r_enc + s_enc
    # encode sequence
    if len(seq) < 0x80:
        length = len(seq).to_bytes(1, "big")
    else:
        # use two length bytes if needed
        length_bytes = len(seq).to_bytes(2, "big")
        length = (0x80 | len(length_bytes)).to_bytes(1, "big") + length_bytes
    return b"\x30" + length + seq


__all__ = ["der_to_raw", "raw_to_der"]
