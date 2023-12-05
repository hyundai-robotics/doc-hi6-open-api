## mechinfo

### 설명

메커니즘 정보(mechanism info)입니다.
어떤 메커니즘들이 사용되는 지를 bit-field로 지정합니다.  

- bit 0 : M0
- bit 1 : M1
- bit 2 : M2
- bit 3 : M3
- bit 4 : M4
- bit 5 : M5
- bit 6 : M6
- bit 7 : M7

### 사용 예

```python
0x13 = 0b00010011 = M4 | M1 | M0
# 메커니즘 M0, M1, M4를 지정합니다.
```
