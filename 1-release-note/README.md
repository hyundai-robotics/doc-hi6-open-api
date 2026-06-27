<link rel="stylesheet" href="../_assets/style.css">

# 1. 发布说明

本文档总结了基于控制器 COM 版本的新 API 添加、变更和修复。

{% hint style="warning" %}
**更新和使用指南**
* 每个发布文档仅描述该特定版本中所做的更改。
* 要使用较高版本的 API，必须升级控制器版本。
* 升级前，请检查发布说明以审核对现有系统的影响。
{% endhint %}
 
<div style="width: fit-content;">

|COM 版本|发布日期|链接|
|:--:|:--:|:--:|
|v70-00.00|2026.03|[🔗](../1-release-note/70-00.md)|
|v60-32.00|2025.11|[🔗](../1-release-note/60-32.md)|
|v60-30.00|2025.03|[🔗](../1-release-note/60-30.md)|
|v60-28.00|2024.08|[🔗](../1-release-note/60-28.md)|

</div>

<div style="max-width:fit-content;">

<h4 style="font-size:15px; font-weight:bold;">发布说明分类</h4>

|分类|描述|
|:--|:--|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid rgb(255, 140, 0); white-space: nowrap;">新增</span>|当添加新的 API、字段或选项时。|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #3F51B5; white-space: nowrap;">更改</span>|当现有 API 的行为、规范或默认值更改时。|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #2E7D32; white-space: nowrap;">修复</span>|当修复与 API 相关的错误或解决异常行为时。|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #B71C1C; white-space: nowrap;">弃用</span>|当某个 API 计划未来删除或不鼓励使用时。|
|<span style="padding-left: 6px; font-weight: bold; display: inline-block; border-left: 4px solid #9E9E9E; white-space: nowrap;">注意</span>|使用该版本 API 时必须承认的重要注意事项。|


<h4 style="font-size:15px; font-weight:bold;">API 方法分类</h4>

| 方法 | 描述 |
| :--- | :--- |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #E1F5FE; color: #0288D1; border: 1px solid #B3E5FC; white-space: nowrap;">GET</span> | 用于检索数据和控制器状态的 API（安全，不更改数据）。 |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #E8F5E9; color: #2E7D32; border: 1px solid #C8E6C9; white-space: nowrap;">POST</span> | 用于执行机器人控制命令、创建新资源和请求任务的 API。 |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #FFF3E0; color: #E65100; border: 1px solid #FFE0B2; white-space: nowrap;">PUT</span> | 用于完全替换或批量更新现有设置或数据的 API。 |
| <span style="padding: 0px 4px; border-radius: 4px; font-weight: bold; font-size: 12px; margin-right: 6px; display: inline-block; text-align: center; line-height: 1.5; min-width: 50px; background: #FFEBEE; color: #C62828; border: 1px solid #FFCDD2; white-space: nowrap;">DELETE</span> | 用于永久删除已创建任务、资源或数据的 API。 |

</div>