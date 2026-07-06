<link rel="stylesheet" href="../_assets/style.css">

# 1. release note 

This document summarizes new API additions, changes, and fixes based on the controller COM version.

{% hint style="warning" %}
**Update and Usage Guidelines**
* Each release document only describes changes made in that specific version.
* To use APIs from a higher version, the controller version must be upgraded.
* Before upgrading, check the release notes to review the impact on the existing system.
{% endhint %}
 
<div style="width: fit-content;">

|COM Version|Release Date|Link|
|:--:|:--:|:--:|
|v70-00.00|2026.03|[🔗](../1-release-note/70-00.md)|
|v60-32.00|2025.11|[🔗](../1-release-note/60-32.md)|
|v60-30.00|2025.03|[🔗](../1-release-note/60-30.md)|
|v60-28.00|2024.08|[🔗](../1-release-note/60-28.md)|

</div>

<div style="max-width:fit-content;">

<h4 style="font-size:15px; font-weight:bold;">Release Note Classification</h4>

|Classification|Description|
|:--|:--|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid rgb(255, 140, 0); white-space: nowrap;">Added</span>|When a new API, field, or option is added.|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #3F51B5; white-space: nowrap;">Changed</span>|When an existing API behavior, specification, or default value is changed.|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #2E7D32; white-space: nowrap;">Fixed</span>|When API-related bugs are fixed or abnormal behaviors are resolved.|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #B71C1C; white-space: nowrap;">Deprecated</span>|When an API is scheduled for future removal or its use is discouraged.|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #9E9E9E; white-space: nowrap;">Caution</span>|Crucial precautions that must be acknowledged when using the API of this version.|


<h4 style="font-size:15px; font-weight:bold;">API Method Classification</h4>

| Method | Description |
| :--- | :--- |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #E1F5FE; color: #0288D1; border: 1px solid #B3E5FC; white-space: nowrap;">GET</span> | API to retrieve data and controller status (Safe, no data changes). |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #E8F5E9; color: #2E7D32; border: 1px solid #C8E6C9; white-space: nowrap;">POST</span> | API to execute robot control commands, create new resources, and request tasks. |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #FFF3E0; color: #E65100; border: 1px solid #FFE0B2; white-space: nowrap;">PUT</span> | API to completely replace or batch update existing settings or data. |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #FFEBEE; color: #C62828; border: 1px solid #FFCDD2; white-space: nowrap;">DELETE</span> | API to permanently delete created tasks, resources, or data. |

</div>
