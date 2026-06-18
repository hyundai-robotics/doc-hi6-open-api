<link rel="stylesheet" href="../_assets/style.css">

# 1. release note 

제어기 COM 버전을 기준으로 API 신규 추가, 변경 및 수정 사항을 정리한 문서입니다.

{% hint style="warning" %}
**업데이트 및 사용 유의 사항**
* 각 릴리즈 문서에는 해당 버전에서 변경된 내용만 기술됩니다.
* 상위 버전의 API를 사용하려면 반드시 제어기 버전을 업그레이드해야 합니다.
* 버전 업데이트 전, 기존 시스템에 미칠 영향을 릴리즈 노트에서 미리 확인하십시오.
{% endhint %}
 
<div style="width: fit-content;">

|COM 버전|배포 일정|링크|
|:--:|:--:|:--:|
|v70-00.00|2026.03|[🔗](70-00.md)|
|v60-32.00|2025.11|[🔗](60-32.md)|
|v60-30.00|2025.03|[🔗](60-30.md)|
|v60-28.00|2024.08|[🔗](60-28.md)|

</div>

<div style="max-width:fit-content;">

<h4 style="font-size:15px; font-weight:bold;">릴리즈 노트 분류 기준</h4>

|구분|설명|
|:--|:--|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid rgb(255, 140, 0);">Added</span>|신규 API, 필드 또는 옵션이 추가된 경우|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #3F51B5;">Changed</span>|기존 API 동작 방식, 사양, 기본값이 변경된 경우|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #2E7D32;">Fixed</span>|API 관련 오류 수정, 비정상 동작 보완|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #B71C1C;">Deprecated</span>|향후 제거 예정이거나 사용이 권장되지 않는 API|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #9E9E9E;">Caution</span>|해당 버전 API 사용 시 반드시 인지해야 할 주의 사항|


<h4 style="font-size:15px; font-weight:bold;">API Method 분류</h4>


| Method | 설명 |
| :--- | :--- |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #E1F5FE; color: #0288D1; border: 1px solid #B3E5FC;">GET</span> | 데이터 및 제어기 상태 조회 API (안전함, 데이터 변경 없음) |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #E8F5E9; color: #2E7D32; border: 1px solid #C8E6C9;">POST</span> | 로봇 제어 명령 실행, 새로운 리소스 생성 및 작업 요청 API |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #FFF3E0; color: #E65100; border: 1px solid #FFE0B2;">PUT</span> | 기존 설정이나 데이터의 전체 교체 및 일괄 업데이트 API |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #FFEBEE; color: #C62828; border: 1px solid #FFCDD2;">DELETE</span> | 생성된 작업, 태스크, 리소스 또는 데이터를 영구 삭제하는 API |

</div>
