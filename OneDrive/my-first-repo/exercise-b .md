# API Reference Entry

## POST /api/v1/projects/{projectId}/tasks

### Description
Allows an authenticated user to create a new task within a specified project. The task includes scheduling details, priority settings, and assignee information.

---

### HTTP Request
POST /api/v1/projects/{projectId}/tasks

### Request Headers

| Header Name | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| Authorization | String | Yes | Bearer token format: Bearer <your_access_token> |
| Content-Type | String | Yes | Must be set to application/json. |

---

### Request Parameters

#### Path Parameters
| Parameter | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| projectId | String | Yes | The unique identifier of the project where the task will be created. |

#### Request Body Parameters (JSON)
| Parameter | Data Type | Required | Description |
| :--- | :--- | :--- | :--- |
| title | String | Yes | The headline or name of the task (1 to 255 characters). |
| description | String | No | A detailed explanation or context regarding the task work. |
| assigneeId | String | Yes | The unique user ID of the person responsible for completing the task. |
| dueDate | String | Yes | The target completion date in ISO 8601 format (YYYY-MM-DD). |
| priority | String | Yes | The importance level of the task. Allowed values: low, medium, high. |

---

### HTTP Response Status Codes

| Status Code | Status Name | Description |
| :--- | :--- | :--- |
| 201 | Created | The task was successfully created. Returns the full task object. |
| 400 | Bad Request | Missing required body fields, invalid data types, or invalid priority value. |
| 401 | Unauthorized | Missing, expired, or invalid authentication token. |
| 404 | Not Found | The specified projectId does not exist or is inaccessible. |

---

### Example Request Body

{
  "title": "Redesign Landing Page Hero Section",
  "description": "Update graphics and rewrite copy for the Q4 product launch.",
  "assigneeId": "usr_789456123",
  "dueDate": "2026-09-30",
  "priority": "high"
}

### Example Successful Response (201 Created)

{
  "id": "tsk_987654321",
  "projectId": "prj_123456789",
  "title": "Redesign Landing Page Hero Section",
  "description": "Update graphics and rewrite copy for the Q4 product launch.",
  "assigneeId": "usr_789456123",
  "dueDate": "2026-09-30",
  "priority": "high",
  "status": "todo",
  "createdAt": "2026-08-24T07:45:12Z"
}