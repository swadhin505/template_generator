import sys, os, subprocess

def HTML_CSS_JS():
        t = input("Enter the title of the template: ")
        t = t.strip()
        pwd = os.getcwd()
        with open(f"{pwd}\Batch.bat", 'w') as f:
            f.write(f"""
@echo off
md "{pwd}\{t}"
cd "{pwd}\{t}"
echo "Hello" > "{pwd}\{t}\index.html"
echo "Hello" > "{pwd}\{t}\style.css"
echo "Hello" > "{pwd}\{t}\script.js"
            """)
        subprocess.call(f"{pwd}\Batch.bat")

        with open(f"{pwd}\{t}\index.html", 'w') as f:
            f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>{t}</title>
</head>
<body>
    Hello World !!!
    <script src="script.js"></script>
</body>
</html>
            """)

        
        with open(f"{pwd}\{t}\style.css", 'w') as f:
            f.write("""* {
    box-sizing: border-box;
    margin: 0px;
    padding: 0px;
}
            """)
        
        with open(f"{pwd}\{t}\script.js", 'w') as f:
            f.write("""// Write your script here""")
        
        os.remove(f"{pwd}\Batch.bat")
    

        