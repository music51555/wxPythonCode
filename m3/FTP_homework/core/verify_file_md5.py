from setting import set_md5

def verify_file_md5(put_file_dict,puted_file):
    print('开始验证')
    print(put_file_dict)
    print(puted_file)
    print(put_file_dict['file_md5'])
    get_file_md5 = set_md5.set_file_md5(puted_file)
    print(get_file_md5)
    if get_file_md5 == put_file_dict['file_md5']:
        print('文件上传完成，校验MD5一致')