# Setup

## :a: LMS Assignment ID = 25

```
https://${LMS_URL}/mod/assign/view.php?id=25
```

```json
{
  "id": 25,             // Assignment ID
  "cmid": 29,           // Rubric Definition CMID
  "name": "3.IaC"       // Assignment name
}
```

## :b: Rubric Definition for

- [ ] cmids[0]=29

- [ ] Retrieve all rubric definitions from LMS

```bash
curl -X POST "https://${LMS_URL}/webservice/rest/server.php" \
-d "wstoken=${API_SYNC_TOKEN}" \
-d "wsfunction=core_grading_get_definitions" \
-d "moodlewsrestformat=json" \
-d "cmids[0]=29" \
-d "areaname=submissions" | jq .
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2397    0  2261  100   136   3849    231 --:--:-- --:--:-- --:--:--  4076
```
<details><summary>📑</summary>

```json
{
  "areas": [
    {
      "cmid": 29,
      "contextid": 482,
      "component": "mod_assign",
      "areaname": "submissions",
      "activemethod": "rubric",
      "definitions": [
        {
          "id": 24,
          "method": "rubric",
          "name": "Présence",
          "description": "",
          "descriptionformat": 1,
          "status": 20,
          "copiedfromid": null,
          "timecreated": 1776999054,
          "usercreated": 3,
          "timemodified": 1776999054,
          "usermodified": 3,
          "timecopied": 0,
          "rubric": {
            "rubric_criteria": [
              {
                "id": 123,
                "sortorder": 1,
                "description": "README.md",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 285,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 286,
                    "score": 1,
                    "definition": "🥈",
                    "definitionformat": 1
                  },
                  {
                    "id": 287,
                    "score": 2,
                    "definition": "🥇",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 124,
                "sortorder": 2,
                "description": "images",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 288,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 289,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 125,
                "sortorder": 3,
                "description": "main.tf",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 290,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 291,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 126,
                "sortorder": 4,
                "description": "VM",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 292,
                    "score": 0,
                    "definition": "🔴",
                    "definitionformat": 1
                  },
                  {
                    "id": 293,
                    "score": 1,
                    "definition": "🟢",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 127,
                "sortorder": 5,
                "description": "SSH",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 294,
                    "score": 0,
                    "definition": "💥",
                    "definitionformat": 1
                  },
                  {
                    "id": 295,
                    "score": 1,
                    "definition": "🔗",
                    "definitionformat": 1
                  }
                ]
              }
            ]
          }
        }
      ]
    }
  ],
  "warnings": []
}
```

</details>