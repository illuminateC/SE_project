import datetime
import paramiko

import json
import os
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from information.models import Comment
from short_video_backend.settings import BASE_DIR
from user.models import User
from video.models import Video
from watching.models import LikeComment


@csrf_exempt
def upload(request):  # get video and cover
    # try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #videoID = data.get('videoID')
            #title = data.get('title')
            #description = data.get('description')
            #zone = data.get('zone')
            #userID = data.get('userID')
            tmp = request.POST.get('videoID')
            title = request.POST.get('title')
            description = request.POST.get('description')
            zone = request.POST.get('zone')
            userID = request.POST.get('userID')


            dir_video_url = '/home/ubuntu/data/videos/'
            dir_cover_url = '/home/ubuntu/data/covers/'
            transport = paramiko.Transport(('43.143.140.26', 22))
            transport.connect(username='ubuntu', password='Wlp123456789')
            sftp = paramiko.SFTPClient.from_transport(transport)

            dir_video = os.path.join(
                os.path.join(BASE_DIR, 'static'), 'videos')
            dir_cover = os.path.join(os.path.join(BASE_DIR, 'static'), 'cover')

            if not os.path.exists(dir_video):
                os.makedirs(dir_video)
            if not os.path.exists(dir_cover):
                os.mkdir(dir_cover)

            video = request.FILES.get('video')
            cover = request.FILES.get('cover')

            coverUrl = ''
            videoUrl = ''

            newVideo = Video(title=title, description=description, coverUrl=coverUrl,
                             videoUrl=videoUrl, zone=zone, userID_id=userID, createdTime=datetime.datetime.now())
            newVideo.save()
            videoID = newVideo.id
            dir_video = os.path.join(dir_video, video.name)
            dir_video_url = dir_video_url + str(videoID) + '.' + video.name.split('.')[-1]

            dest = open(dir_video, 'wb+')
            for chunk in video.chunks():
                dest.write(chunk)
            dest.close()
            dir_cover = os.path.join(dir_cover, cover.name)
            dir_cover_url = dir_cover_url + str(videoID) + '.' + cover.name.split('.')[-1]
            dest = open(dir_cover, 'wb+')
            for chunk in cover.chunks():
                dest.write(chunk)
            dest.close()
            sftp.put(dir_video, dir_video_url)
            sftp.put(dir_cover, dir_cover_url)
            transport.close()

            videoUrl = 'http://43.143.140.26' + '/videos/' + str(videoID) + '.' + video.name.split('.')[-1]
            coverUrl = 'http://43.143.140.26' + '/covers/' + str(videoID) + '.' + cover.name.split('.')[-1]

            Video.objects.filter(id=videoID).update(videoUrl=videoUrl, coverUrl=coverUrl)

            User.objects.filter(id=userID).update(videoNum=User.objects.get(id=userID).videoNum+1)


            return JsonResponse({'message': "上传成功"}, status=200)
    # except Exception as e:
    #     return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def content(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #id = data.get('id')
            #username = data.get('username')
            #content = data.get('content')
            #videoID = data.get('videoID')
            id = request.POST.get('id')
            userID = request.POST.get('userID')
            content = request.POST.get('content')
            videoID = request.POST.get('videoID')
            createdTime = request.POST.get('createdTime')
            newComment = Comment(id=id, userID_id=userID, content=content, videoID_id=videoID, createdTime=createdTime)
            newComment.save()
            comments = Comment.objects.filter(videoID_id=videoID)
            commentList = []
            if comments.exists():
                for comment in comments:
                    commentList.append({
                        'id': comment.id,
                        'userID': comment.userID_id,
                        'avatarUrl': User.objects.get(id=comment.userID_id).avatarUrl,
                        'username': User.objects.get(id=comment.userID_id).username,
                        'content': comment.content,
                        'isLike': LikeComment.objects.filter(userID_id=userID, commentID_id=comment.id).exists(),
                        'likeNum': LikeComment.objects.filter(commentID_id=comment.id).count(),
                        'isOwn': str(comment.userID_id) == userID,
                        'createdTime': comment.createdTime
                    })
            return JsonResponse({'message': "上传成功", 'commentList': commentList}, status=200)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def delete(request):
    # try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #videoID = data.get('videoID')
            videoID = request.POST.get('videoID')
            dir_video = '/home/ubuntu/data/videos/'
            dir_cover = '/home/ubuntu/data/covers/'
            dir_video += Video.objects.get(id=videoID).videoUrl.split('/')[-1]
            dir_cover += Video.objects.get(id=videoID).coverUrl.split('/')[-1]

            print(dir_cover)
            print(dir_video)

            transport = paramiko.Transport(('43.143.140.26', 22))
            transport.connect(username='ubuntu', password='Wlp123456789')
            sftp = paramiko.SFTPClient.from_transport(transport)

            sftp.remove(dir_video)
            sftp.remove(dir_cover)

            # os.remove(dir_video)
            # os.remove(dir_cover)
            user = User.objects.get(id=Video.objects.get(id=videoID).userID_id)
            user.videoNum -= 1
            user.save()
            Video.objects.get(id=videoID).delete()

            return JsonResponse({'message': "删除成功"}, status=200)

    # except Exception as e:
    #     return JsonResponse({'message': "未知错误"}, status=401)