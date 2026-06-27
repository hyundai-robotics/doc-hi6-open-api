### `mechinfo`

#### Description

机制信息  
使用位字段庆祝使用哪些活动。

- bit 0 : M0
- bit 1 : M1
- bit 2 : M2
- bit 3 : M3
- bit 4 : M4
- bit 5 : M5
- bit 6 : M6
- bit 7 : M7

#### Example

```python
0x13 = 0b00010011 = M4 | M1 | M0
# 指定机制 M0, M1 和 M4。
```