'''
Created on Jan 1, 2016

@author: zpq
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_datas(self, data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('outputer.html', 'w')
        fout.write("<html><head><meta charset=\"UTF-8\"></head><body>")
        fout.write("<table border=1>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body></html>")
        fout.close()
    
    
    
    



