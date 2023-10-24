Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> K={1,2,3,4}
>>> print(K)
{1, 2, 3, 4}
>>> K=set('sad342')
>>> print(K)
{'4', 's', 'd', '2', '3', 'a'}
>>> type(K)
<class 'set'>
>>> k1={1,2,3,4,5}
>>> k2={1,3,6,8,9}
>>> k1|k2
{1, 2, 3, 4, 5, 6, 8, 9}
>>> k1
{1, 2, 3, 4, 5}
>>> k2
{1, 3, 6, 8, 9}
>>> k1&k2
{1, 3}
>>> k2§k1
SyntaxError: invalid character '§' (U+00A7)
>>> k2&k1
{1, 3}
>>> k1-k2
{2, 4, 5}
>>> k2-k1
{8, 9, 6}
