Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> decimal to binary conversion
SyntaxError: invalid syntax
>>> bin(47)
'0b101111'
>>> bin(256)
'0b100000000'
>>> bin(15)
'0b1111'
>>> 
>>> octal to decimal conversion
SyntaxError: invalid syntax
>>> x=0o111
>>> print(x)
73
>>> a=0o10110
>>> print(a)
4168
>>> 0o1234
668
>>> 0o98764
SyntaxError: invalid digit '9' in octal literal
>>> 0o123456787654321
SyntaxError: invalid digit '8' in octal literal
>>> 0o123456765432123
5744381801555
>>> 
>>> hexadecimal to decimal conversion
SyntaxError: invalid syntax
>>> h=0x56ab
>>> print(h)
22187
>>> f=0x34532fe
>>> print(f)
54866686
>>> 0x453211234eeef
1217301411327727
