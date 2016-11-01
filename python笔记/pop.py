import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return charset

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg, indent=0):
    if indent:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' '*indent, header, value))

    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%s part %s' % (' '*indent, n))
            print('%s----------------' % ' '*indent)
            print_info(part, indent +1)
    else:
        content_type = msg.get_content_type()
        if content_type in ['text/plain', 'text/html']:
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content =  content.decode(charset)
            print('%sText: %s' % (' '*indent, content))
        else:
            print('%sAttachment: %s' % (' '*indent, content_type))

email = '18064519110@163.com'
password = 'd1s1rt23xsx'
ip = 'pop3.163.com'

server = poplib.POP3(ip)
# server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))
server.user(email)
server.pass_(password)

print('message: %s, Size %s' % server.stat())

resp, mails, octets = server.list()
print(mails)

# 获取最后一封邮件
index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
print(type(msg))
print_info(msg)
server.quit()