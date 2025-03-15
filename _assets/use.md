# Style 적용 방법 

<div important>

_assets/style.css, 를 import 해주는 문장을 각 마크다운 페이지 최상단에 넣으셔야합니다.<br>
경로는 현재 파일을 기준으로 상대 경로로 표시하시는 것이 workspace 가 변경되었을 때 렌더링이 정상 적용됩니다.

</div>

<div tip>

박스 안에서 개행을 넣으려면, html 태그로 넣어주셔야합니다. <br>
<span u>&lt;br&gt;</span>을 입력하세요

</div>


```
<link rel="stylesheet" href="_assets/style.css">

<div caution>

<span u>위험</span>할 수 있는 요소가 있습니다!

</div>

<div issue>

`HIXM-3717` api) 자동모드 중 에러발생 이후 task reset post 요청 시 비정상 동작 현상 발생   

</div>

<div warning>

조심하세요! 이 부분은 <span u>주의가 필요</span>합니다.

</div>

<div tip>

<span u>유용한 팁</span>을 제공합니다!

</div>

<div note>

일반적인 노트 내용입니다.

</div>

<div important>

이 내용은 매우 <span u>중요</span>합니다!

</div>
```  

<br>

# 적용 예시

<link rel="stylesheet" href="./style.css">


<div caution>

<span u>위험</span>할 수 있는 요소가 있습니다!

</div>

<div issue>

`HIXM-3717` api) 자동모드 중 에러발생 이후 task reset post 요청 시 비정상 동작 현상 발생   

</div>

<div warning>

조심하세요! 이 부분은 <span u>주의가 필요</span>합니다.

</div>

<div tip>

<span u>유용한 팁</span>을 제공합니다!

</div>

<div note>

일반적인 노트 내용입니다.

</div>

<div important>

이 내용은 매우 <span u>중요</span>합니다!

</div>

