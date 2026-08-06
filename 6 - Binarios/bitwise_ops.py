def decimal_para_binario(n):
  binario = bin(n)
  print(f"{n} em binario = {binario}")

def and_(a, b):
  print(f"{a} & {b} = {a & b}")
  print(f"  0b{a:08b} & 0b{b:08b} = 0b{a & b:08b}")

def or_(a, b):
  print(f"{a} | {b} = {a | b}")
  print(f"  0b{a:08b} | 0b{b:08b} = 0b{a | b:08b}")

def xor_(a, b):
  print(f"{a} ^ {b} = {a ^ b}")
  print(f"  0b{a:08b} ^ 0b{b:08b} = 0b{a ^ b:08b}")

def not_(n):
  print(f"~{n} = {~n}")
  print(f"  ~0b{n:08b} = 0b{~n & 0xFF:08b}  (em 8 bits)")

def left_shift(n, desloc):
  print(f"{n} << {desloc} = {n << desloc}")
  print(f"  0b{n:08b} << {desloc} = 0b{n << desloc:08b}")

def right_shift(n, desloc):
  print(f"{n} >> {desloc} = {n >> desloc}")
  print(f"  0b{n:08b} >> {desloc} = 0b{n >> desloc:08b}")


print("=== REPRESENTACAO BINARIA ===")
decimal_para_binario(5)
decimal_para_binario(13)

print("\n=== AND ===")
and_(5, 3)

print("\n=== OR ===")
or_(5, 3)

print("\n=== XOR ===")
xor_(5, 3)

print("\n=== NOT ===")
not_(5)

print("\n=== LEFT SHIFT ===")
left_shift(5, 1)

print("\n=== RIGHT SHIFT ===")
right_shift(5, 1)
