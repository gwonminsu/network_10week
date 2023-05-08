

FTP_SERVER_URL = 'ftp.kernel.org'
from ftplib import FTP
def test_ftp_connection(path, username, email):
    ftp = FTP(path, username, email)

    ftp.cwd("/pub")
    print("File list at %s:" %path)
    files = ftp.dir()
    print(files)

    ftp.quit()

if __name__ == '__main__':
    test_ftp_connection(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com')