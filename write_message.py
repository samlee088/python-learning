from pathlib import Path

path = Path('write_expression.txt')

content = "Hello world! \n"
content += "Hello Seto! \n"
content+= "Hello Blue Eyes White Dragon! \n"

path.write_text(content)
