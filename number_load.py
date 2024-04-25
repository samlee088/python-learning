from pathlib import Path
import json
numbers = [0, 1, 2, 3, 4, 5,]

path = Path("number_paste.json")
content = json.dumps(numbers)
path.write_text(content)


content = path.read_text()
updated_content = json.loads(content)
print(updated_content)
