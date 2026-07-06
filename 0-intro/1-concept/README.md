## 0.1 About ${cont_model} Open API

In this document, HD Hyundai Robotics publishes an API for application developers to easily monitor and remotely control the robot controller (hereafter referred to as ${cont_model}).<br>
This enables developers to read and write ${cont_model} data without requiring a thorough comprehension of the source code used in ${cont_model} development.<br>
The image below will help you better grasp the role of Open API.

<img src="../../_assets/05_open_api_flow.png" style="max-height: 22vh;">

The parts marked in orange in the picture above show the role of Open API.

|Arrow sign|Description|
|:---|:---|
|`Solid line`|This means that the `developer` (`client`) `requests` information to `${cont_model}` (`server`) using one of four methods (GET, POST, PUT, DELETE).|
|`Dotted line`|This means that the `controller` that `received` the `request` `sends back` the appropriate `response` in json or text format.|

In this way, developers can use the Open API in the document to remotely control or monitor their desktops, laptops, tablet PCs, etc. connected via ${cont_model} and Ethernet based on http and REST API.


<br><br>


#### Be sure to check before you start!

* The current document is written based on ${cont_model} Open API schema version `5`. You can check it through [API](../../1-version/1-get/1-api_ver.md).

* For developers who are familiar with developing HTTP REST API client functions, you can skip from [0.2 Required prior knowledge](../2-prerequisite/README.md) to [0.4 Simple API call without coding](../4-api-test/README.md).


{% hint style="warning" %}

The APIs described in this document are supported starting from `${cont_model} V60.24-00` unless otherwise specified.

Please note that URLs and properties not specified in this document may change without notice in the same API version.

{% endhint %}
