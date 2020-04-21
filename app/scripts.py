def avatar_download(avatar):
    with open('/home/admin_/Desktop/'+avatar._name,'wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)