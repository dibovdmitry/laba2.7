#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "b", "h", "j", "l"}
    b = {"b", "c", "h", "l", "r", "u"}
    c = {"j", "k", "n", "t", "z"}
    d = {"b", "i", "k", "v", "w"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    bA = u.difference(a)
    bB = u.difference(b)

    y = (bA.intersection(bB)).difference(c.union(d))
    print(f"y = {y}")
