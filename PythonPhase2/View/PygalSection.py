import pygal
view=pygal.Line()
view.add('sin(x)',[21,34])
view.add('cos(x)',[34,56])
view.title = 'sin(x)'
view.render_to_file('file.svg')
