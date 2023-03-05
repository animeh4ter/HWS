from jinja2 import FileSystemLoader, Environment

dicto = {
    "h1": "Page with HWs",
    "p": "HW done"
}

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
tm = env.get_template('main.html')
msg = tm.render(items=dicto, title='Homework')
print(msg)
