from typing import Any, Literal

def groebner(seq, ring, method=...) -> list[Any]:
    ...

def spoly(p1, p2, ring):
    ...

def Sign(f):
    ...

def Polyn(f):
    ...

def Num(f):
    ...

def sig(monomial, index) -> tuple[Any, Any]:
    ...

def lbp(signature, polynomial, number) -> tuple[Any, Any, Any]:
    ...

def sig_cmp(u, v, order) -> Literal[-1, 1]:
    ...

def sig_key(s, order) -> tuple[Any, Any]:
    ...

def sig_mult(s, m) -> tuple[Any, Any]:
    ...

def lbp_sub(f, g) -> tuple[Any, Any, Any]:
    ...

def lbp_mul_term(f, cx) -> tuple[Any, Any, Any]:
    ...

def lbp_cmp(f, g) -> Literal[-1, 1]:
    ...

def lbp_key(f) -> tuple[tuple[Any, Any], Any]:
    ...

def critical_pair(f, g, ring) -> tuple[Any, tuple[tuple[Any, ...], Any] | None, Any, Any, tuple[tuple[Any, ...], Any] | None, Any]:
    ...

def cp_cmp(c, d) -> Literal[-1, 1]:
    ...

def cp_key(c, ring) -> tuple[tuple[tuple[Any, Any], Any], tuple[tuple[Any, Any], Any]]:
    ...

def s_poly(cp) -> tuple[Any, Any, Any]:
    ...

def is_rewritable_or_comparable(sign, num, B) -> bool:
    ...

def f5_reduce(f, B) -> tuple[Any, Any, Any]:
    ...

def red_groebner(G, ring) -> list[Any]:
    ...

def is_groebner(G, ring) -> bool:
    ...

def is_minimal(G, ring) -> bool:
    ...

def is_reduced(G, ring) -> bool:
    ...

def groebner_lcm(f, g):
    ...

def groebner_gcd(f, g):
    ...

