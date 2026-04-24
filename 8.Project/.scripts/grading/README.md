# Setup

## :a: LMS Assignment ID = 30

```
https://${LMS_URL}/mod/assign/view.php?id=30
```

```json
{
  "id": 30,
  "cmid": 34,
  "name": "8.Project"
}
```

## :b: Rubric Definition for

- [ ] cmids[0]=34

- [ ] Retrieve all rubric definitions from LMS


```bash
curl -X POST "https://${LMS_URL}/webservice/rest/server.php" \
-d "wstoken=${API_SYNC_TOKEN}" \
-d "wsfunction=core_grading_get_definitions" \
-d "moodlewsrestformat=json" \
-d "cmids[0]=34" \
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
      "cmid": 34,
      "contextid": 487,
      "component": "mod_assign",
      "areaname": "submissions",
      "activemethod": "rubric",
      "definitions": [
        {
          "id": 29,
          "method": "rubric",
          "name": "🅰️ Présence",
          "description": "",
          "descriptionformat": 1,
          "status": 20,
          "copiedfromid": null,
          "timecreated": 1776999055,
          "usercreated": 3,
          "timemodified": 1776999055,
          "usermodified": 3,
          "timecopied": 0,
          "rubric": {
            "rubric_criteria": [
              {
                "id": 145,
                "sortorder": 1,
                "description": "README.md",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 334,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 335,
                    "score": 1,
                    "definition": "🥈",
                    "definitionformat": 1
                  },
                  {
                    "id": 336,
                    "score": 2,
                    "definition": "🥇",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 146,
                "sortorder": 2,
                "description": "images",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 337,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 338,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 147,
                "sortorder": 3,
                "description": "🚀 analyse.py",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 339,
                    "score": 0,
                    "definition": "❔",
                    "definitionformat": 1
                  },
                  {
                    "id": 340,
                    "score": 1,
                    "definition": "‼️",
                    "definitionformat": 1
                  },
                  {
                    "id": 341,
                    "score": 2,
                    "definition": "🚀",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 149,
                "sortorder": 4,
                "description": "🧾 RAPPORT",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 344,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 345,
                    "score": 1,
                    "definition": "🧾",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 148,
                "sortorder": 5,
                "description": "✍️ Sgn",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 342,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 343,
                    "score": 1,
                    "definition": "✍️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 150,
                "sortorder": 6,
                "description": "🖼️ Figures",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 346,
                    "score": 0,
                    "definition": "0️⃣",
                    "definitionformat": 1
                  },
                  {
                    "id": 347,
                    "score": 1,
                    "definition": "1️⃣",
                    "definitionformat": 1
                  },
                  {
                    "id": 348,
                    "score": 2,
                    "definition": "*️⃣",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 151,
                "sortorder": 7,
                "description": "analyse.ps1",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 349,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 350,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 152,
                "sortorder": 8,
                "description": "rapport.txt",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 351,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 352,
                    "score": 1,
                    "definition": "✔️",
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
