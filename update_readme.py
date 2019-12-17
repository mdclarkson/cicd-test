import re
import sys
from veracode import Application

app = Application(sys.argv[1])

with open('sca_results.txt') as f:
    lines = f.readlines()

sca_table = []
selected = [
    'Scan Date & Time', 'Vulnerable Libraries', 
    'High Risk Vulnerabilities' ,'Medium Risk Vulnerabilities',
    'Low Risk Vulnerabilities'
    ]

for line in lines:
    row = re.split(r'\s{2,}', line)
    if row[0] not in selected:
        continue
    if len(row) < 2:
        continue
    sca_table.append(row)

def sca_results():
    html = '<table>\n'
    for tr in sca_table:
        html += '\t\t<tr>'
        for td in tr:
            html += '<td>{}</td>'.format(td.strip())
        html += '</tr>\n'
    html += '\t</table>'
    return html
    

def sast_results():
    html = f'''
	<table>
		<tr><td>Scan Date</td><td>{app.info.modified_date.strftime('%b %d %Y')}</td></tr>
		<tr><td>Very High Risk Vulnerabilities</td><td>{app.build.report.flaw_status.sev_5_change}</td></tr>
		<tr><td>High Risk Vulnerabilities</td><td>{app.build.report.flaw_status.sev_4_change}</td></tr>
		<tr><td>Medium Risk Vulnerabilities</td><td>{app.build.report.flaw_status.sev_3_change}</td></tr>
		<tr><td>Low Risk Vulnerabilities</td><td>{app.build.report.flaw_status.sev_2_change}</td></tr>
	</table>
    '''
    return html

html = '''
<table>
<tr><th>Veracode SCA Results</th><th>Veracode SAST Results</th></tr>
<tr>
    <td>{}</td>
    <td>{}</td>
</tr>
</table>
'''.format(sca_results(), sast_results())

with open('README.md', 'r') as f:
    readme = f.read()
    

top = readme[:readme.index('<!-- results -->')+16]
bottom = readme[readme.index('<!-- end results -->'):]

md = top + html + bottom

with open('README.md', 'w') as f:
    f.write(md)

