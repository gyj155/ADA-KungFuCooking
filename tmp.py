import markdown

# 读取 index.md 文件
with open("index.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# 转换为 HTML
html_content = markdown.markdown(md_content)

# 写入到 index.html
with open("index.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("HTML 文件已生成！")
