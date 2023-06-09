import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from video.models import Video
from user.models import User
from short_video_backend.settings import BASE_DIR
from information.models import Follow
@csrf_exempt
def video(request):
    if request.method == 'GET':
        try:
            search_str = request.GET.get('search_str')
            videos = Video.objects.filter(title__icontains=search_str)
            if videos.exists():
                videoDetails = []
                for video in videos:
                    videoDetails.append({
                        'videoID': video.id,
                        'title': video.title,
                        'description': video.description,
                        'coverUrl': video.coverUrl,
                        'videoUrl': video.videoUrl,
                        'avatarUrl': video.avatarUrl,
                        'likeNum': video.likeNum,
                        'collectNum': video.collectNum,
                        'viewNum': video.viewNum,
                        'zone': video.zone,
                        'tag': video.tag,
                        'userID': video.userID_id,
                        'createdTime': video.createdTime,
                        'needAudit': video.needAudit,
                        'username': User.objects.get(id=video.userID_id).username
                    })
                return JsonResponse({'videos': videoDetails}, status=200)
            else:
                return JsonResponse({'message': '视频不存在'}, status=200)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def user(request):
    if request.method == 'GET':
        search_str = request.GET.get('search_str')
        print(search_str)
        if(len(search_str)>30):
            return JsonResponse({'message': '检索信息过长'}, status=401)
        users = User.objects.filter(username__icontains=search_str)
        if users.exists():
            userInfo = []
            for user in users:
                userInfo.append({
                    'id': user.id,
                    'username': user.username,
                    'password': user.password,
                    'videoNum': user.videoNum,
                    'likeNum': user.likeNum,
                    'collectNum': user.collectNum,
                    'fanNum': user.fanNum,
                    'followNum': user.followNum,
                    'avatarUrl': user.avatarUrl,
                    'isSuperAdmin': user.isSuperAdmin,
                    'createdTime': user.createdTime,
                    'sign' : user.sign
                })
            return JsonResponse({'users': userInfo}, status=200)
        else:
            return JsonResponse({'message': '用户不存在'}, status=200)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def getzone(request):
    if request.method == 'GET':
        zone = request.GET.get('zone')
        if zone:
            videos = Video.objects.filter(zone=zone).order_by('-viewNum', '-likeNum')
            if videos.exists():
                superVideos = []
                videoDetails = []
                for video in videos:
                    user = User.objects.get(id = video.userID_id)
                    username = user.username
                    videoDetails.append({
                        'videoID': video.id,
                        'title': video.title,
                        'description': video.description,
                        'coverUrl': video.coverUrl,
                        'videoUrl': video.videoUrl,
                        'avatarUrl': video.avatarUrl,
                        'likeNum': video.likeNum,
                        'collectNum': video.collectNum,
                        'viewNum': video.viewNum,
                        'zone': video.zone,
                        'tag': video.tag,
                        'userID': video.userID_id,
                        'createdTime': video.createdTime,
                        'needAudit': video.needAudit,
                        'username' : username
                    })
                return JsonResponse({'videos': videoDetails, 'superVideos': superVideos}, status=200,safe=False)
            else:
                return JsonResponse({'message': '视频不存在'}, status=401)
        elif zone is None:
            videos = Video.objects.all().order_by('-viewNum', '-likeNum')
            if videos.exists():
                superVideos = []
                videoDetails = []
                for video in videos:
                    user = User.objects.get(id=video.userID_id)
                    username = user.username
                    if video == videos[1] or video == videos[2] or video == videos[0]:
                        superVideos.append({
                            'videoID': video.id,
                            'title': video.title,
                            'description': video.description,
                            'coverUrl': video.coverUrl,
                            'videoUrl': video.videoUrl,
                            'avatarUrl': video.avatarUrl,
                            'likeNum': video.likeNum,
                            'collectNum': video.collectNum,
                            'viewNum': video.viewNum,
                            'zone': video.zone,
                            'tag': video.tag,
                            'userID': video.userID_id,
                            'createdTime': video.createdTime,
                            'needAudit': video.needAudit,
                            'username': username
                        })
                    else:
                        videoDetails.append({
                            'videoID':video.id,
                            'title' : video.title,
                            'description' : video.description,
                            'coverUrl' : video.coverUrl,
                            'videoUrl' : video.videoUrl,
                            'avatarUrl' : video.avatarUrl,
                            'likeNum' : video.likeNum,
                            'collectNum' : video.collectNum,
                            'viewNum' :video.viewNum,
                            'zone' : video.zone,
                            'tag' : video.tag,
                            'userID' : video.userID_id,
                            'createdTime' : video.createdTime,
                            'needAudit' : video.needAudit,
                            'username': username

                        })
                return JsonResponse({'videos': videoDetails,'superVideos':superVideos}, status=200,safe=False)
            else:
                return JsonResponse({'message': '视频不存在'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def getrecommand(request):
    if request.method == 'GET':
        zone = request.GET.get('zone')
        videoid = request.GET.get('videoID')
        videos = Video.objects.filter(zone=zone).order_by('-viewNum', '-likeNum')
        if videos.exists():
            videoDetails = []
            for video in videos:
                if str(video.id) == videoid :
                    continue
                else :
                    user = User.objects.get(id = video.userID_id)
                    username = user.username
                    videoDetails.append({
                        'videoID': video.id,
                        'title': video.title,
                        'description': video.description,
                        'coverUrl': video.coverUrl,
                        'videoUrl': video.videoUrl,
                        'avatarUrl': video.avatarUrl,
                        'likeNum': video.likeNum,
                        'collectNum': video.collectNum,
                        'viewNum': video.viewNum,
                        'zone': video.zone,
                        'tag': video.tag,
                        'userID': video.userID_id,
                        'createdTime': video.createdTime,
                        'needAudit': video.needAudit,
                        'username' : username
                        })
            return JsonResponse({'videos': videoDetails}, status=200,safe=False)
        else:
            return JsonResponse({'message': '视频不存在'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)


@csrf_exempt
def getfollow(request):
    if request.method == 'GET':
        userID = request.GET.get('id')
        try:
            user = User.objects.get(id = userID)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=401)
        try:
            followings = Follow.objects.filter(followerId=userID)
            videos = Video.objects.filter(userID__in=[following.followingId for following in followings])
            video_list = []
            for video in videos:
                newuser = User.objects.get(id = video.userID_id)
                username = newuser.username
                video_list.append({
                    'videoID':video.id,
                    'title' : video.title,
                    'description' : video.description,
                    'coverUrl' : video.coverUrl,
                    'videoUrl' : video.videoUrl,
                    'avatarUrl' : video.avatarUrl,
                    'likeNum' : video.likeNum,
                    'collectNum' : video.collectNum,
                    'viewNum' :video.viewNum,
                    'zone' : video.zone,
                    'tag' : video.tag,
                    'userID' : video.userID_id,
                    'createdTime' : video.createdTime,
                    'needAudit' : video.needAudit,
                    'username' : username
                    })
            isFollow = True
            return JsonResponse({'videos': video_list, 'message': '成功返回','isFollow':isFollow}, status=200,safe=False)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def id2name(request):
    if request.method == 'GET':
        userID = request.GET.get('userID')
        try:
            user = User.objects.get(id=userID)
            username = user.username
            return JsonResponse({'username': username}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=401)
    else:
        return JsonResponse({'message': '请求方式错误'}, status=401)

@csrf_exempt
def isfollowed(request):
    if request.method == 'GET':
        userID = request.GET.get('userID')
        queryID = request.GET.get('queryID')
        return JsonResponse({
            'isFollowed': Follow.objects.filter(followerId_id=userID, followingId_id=queryID).exists()
        }, status=200)
    else:
        return  JsonResponse({'message': '请求方式错误'}, status=401)