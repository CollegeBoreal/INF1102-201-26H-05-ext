# Setup

## :a: Class - INF1102-201-26H-05 - Programmation de systèmes

```
https://${LMS_URL}/course/view.php?id=4
```

## :b: Assignments for:

- [ ] courseids[0]=4

```json
{
  "id": 8,               // Assignment ID
  "cmid": 12,            // Rubric Definition CMID
  "name": "4.CRON-TASK"  // Assignment name
}
```

- [ ] Retrieve all assignments from LMS

```bash
curl -X POST "https://${LMS_URL}/webservice/rest/server.php" \
-d "wstoken=${API_SYNC_TOKEN}" \
-d "wsfunction=mod_assign_get_assignments" \
-d "moodlewsrestformat=json" \
-d "courseids[0]=4" | jq '.courses[].assignments[] | {id, cmid, name}'
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1704    0  1587  100   117   2463    181 --:--:-- --:--:-- --:--:--  2645
```
<details><summary>📑</summary>

```json
{
  "id": 25,
  "cmid": 29,
  "name": "3.IaC"
}
{
  "id": 26,
  "cmid": 30,
  "name": "4.CRON-TASK"
}
{
  "id": 27,
  "cmid": 31,
  "name": "5.BATCH"
}
{
  "id": 28,
  "cmid": 32,
  "name": "6.PWSH"
}
{
  "id": 29,
  "cmid": 33,
  "name": "7.REGEX"
}
{
  "id": 30,
  "cmid": 34,
  "name": "8.Project"
}
{
  "id": 31,
  "cmid": 35,
  "name": "9.Ansible"
}
```

</details>
