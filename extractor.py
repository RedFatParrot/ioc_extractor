import fitz
import iocextract
from optparse import OptionParser

parser = OptionParser(usage='usage: python extractor [-f] file.pdf')
parser.add_option('-f', '--file', 
                        dest='filename',
                        help='foo help')
(options, args) = parser.parse_args()
if not options.filename:   # if filename is not given
    parser.error('Filename not given')


doc = fitz.open(options.filename)
iocs = []

for page in range(doc.pageCount):
	pageread = doc.loadPage(page)
	text = pageread.getText("text")
	for ipv4 in iocextract.extract_ipv4s(text):
		iocs.append(ipv4)

for page in range(doc.pageCount):
	pageread = doc.loadPage(page)
	text = pageread.getText("text")
	for url in iocextract.extract_urls(text):
		iocs.append(url)

iocs = list(dict.fromkeys(iocs))
for i in iocs:
	print(i)