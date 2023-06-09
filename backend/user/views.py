import json
import os
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from information.models import Comment,Follow,Favorite
from video.models import Video
from watching.models import Complain
from information.models import Message
from short_video_backend.settings import BASE_DIR
import paramiko
app_name = 'user'

def test(request):
    return JsonResponse({'name': 'Darker', 'age': '18'})
@csrf_exempt
def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = User.objects.get(username=username)
                return JsonResponse({'message': "用户已存在"}, status=401)
            except User.DoesNotExist:
                newUser = User(username=username, password=password, createdTime=timezone.now())
                newUser.save()
                return JsonResponse({'message': "注册成功"}, status=200)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=402)



@csrf_exempt
def login(request):
    try:
        if request.method == 'GET':
            # data = json.loads(request.body)
            # username = data.get('username')
            # password = data.get('password')
            username = request.GET.get('username')
            password = request.GET.get('password')
            print(password)
            try:
                user = User.objects.get(username=username)
                if password != user.password:
                    return JsonResponse({'msg': '密码错误'}, status=402)

                userData = {
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
                    'sign': user.sign
                }

                return JsonResponse({'message': '登录成功', 'userData': userData}, status=200)
            except User.DoesNotExist:
                return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=402)


@csrf_exempt  # 跨域设置
def getlike(request):
    try:
        if request.method == 'GET':
            #data = json.loads(request.body)
            #id = data.get('id')
            id = request.GET.get('id')
            user = User.objects.get(id=id)
            likes = Favorite.objects.filter(userID=id).values_list('videoID', flat=True)
            videos = Video.objects.filter(id__in=likes)
            videoDetails = []
            for video in videos:
                user = User.objects.get(id=video.userID_id)
                username = user.username
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
                    'username':username
                })
            return JsonResponse({'videoDetails': videoDetails, 'message': '成功返回'}, status=200,safe=False)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def getfollow(request):
    try:
        if request.method == 'GET':
            #data = json.loads(request.body)
            #userId = data.get('id')
            userID = request.GET.get('id')
            print(userID)
            user = User.objects.get(id=userID)
            followings = user.following.all()
            followingsDetails = []
            for following in followings:
                followingUser = User.objects.get(id=following.followingId_id)
                followingsDetails.append({
                    'username': followingUser.username,
                    'avatarUrl': followingUser.avatarUrl,
                    'id':followingUser.id,
                    'sign': followingUser.sign,
                    'isFollow':True
                })
            return JsonResponse({'followings': followingsDetails, 'message': '成功返回'}, status=200)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

#视频评论信息表中的createtime和content
@csrf_exempt
def getwords(request):
    try:
        if(request.method == 'GET'):
            id=request.GET.get('id')
            user = User.objects.get(id=id)
            comments = user.comment.all()
            commentsDetails = []
            for comment in comments:
                commentsDetails.append({
                    'id' : comment.id,
                    'userID': comment.userID_id,
                    'content' :comment.content,
                    'createdTime': comment.createdTime,
                    'videoID': comment.videoID_id
                })
            return JsonResponse({'commentsDetails':commentsDetails,'message':'成功返回'}, status=200,safe=False)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def message(request):
    try:
        if(request.method == 'POST'):
            content = request.POST.get('content')
            fromName = '管理员'
            userID = request.POST.get('userID')
            message = Message(content = content,fromName =  fromName, userID_id = userID,createdTime = timezone.now )
            message.save()
            return JsonResponse({'message':'成功返回'}, status=200)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)


@csrf_exempt
def getmessage(request):
    try:
        if(request.method == 'GET'):
            id = request.GET.get('id')
            user=User.objects.get(id=id)
            messages = user.message.all()
            messagesDetails = []
            for message in messages:
                messagesDetails.append({
                    'id': message.id,
                    'content': message.content,
                    'createdTime': message.createdTime,
                    'fromName' : message.fromName
                })
            return JsonResponse({'messagesDetails':messagesDetails,'message':'成功返回'}, status=200,safe=False)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def avatar(request):
    if request.method == 'POST':
        #try:
            userID = request.POST.get('id')
            avatar = request.FILES.get('avatar')

            user = User.objects.get(id=userID)

            dir_avatar_url = '/home/ubuntu/data/avatars/'

            transport = paramiko.Transport(('43.143.140.26', 22))
            transport.connect(username='ubuntu', password='Wlp123456789')
            sftp = paramiko.SFTPClient.from_transport(transport)

            dir_avatar = os.path.join(os.path.join(BASE_DIR, 'static'), 'avatars')

            if not os.path.exists(dir_avatar):
                os.makedirs(dir_avatar)

            dir_avatar = os.path.join(dir_avatar, avatar.name)
            dir_avatar_url = dir_avatar_url + str(userID) + '.' + avatar.name.split('.')[-1]

            dest = open(dir_avatar, 'wb+')
            for chunk in avatar.chunks():
                dest.write(chunk)
            dest.close()

            sftp.put(dir_avatar, dir_avatar_url)
            transport.close()

            avatarUrl = 'http://43.143.140.26' + '/avatars/' + str(userID) + '.' + avatar.name.split('.')[-1]
            user.avatarUrl = avatarUrl
            user.save()
            return JsonResponse({'message': '成功返回'}, status=200)
        #except Exception as e:
            #return JsonResponse({'message': '未知错误'}, status=401)
    #else:
        #return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def sign(request):
    if request.method == 'POST':
        try:
            #data = json.loads(request.body)
            #user_id = data.get('id')
            #signature = data.get('sign')
            user_id = request.POST.get('id')
            signature = request.POST.get('sign')
            user = User.objects.get(id=user_id)
            user.sign = signature
            user.save()
            return JsonResponse({'message': '个性签名更新成功'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)
@csrf_exempt
def deletecontent(request):
    if request.method == 'POST':
        try:
            #data = json.loads(request.body)
            #commentId = data.get('id')
            commentId = request.POST.get('id')
            comment = Comment.objects.get(id=commentId)
            comment.delete()
            return JsonResponse({'message': '评论删除成功'}, status=200)
        except Comment.DoesNotExist:
            return JsonResponse({'message': '评论不存在'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
# def getVideo(request):
#     if request.method == 'GET':
#         #data = json.loads(request.body)
#         #userId = data.get('id')
#         userID= request.GET.get('id')
#         try:
#             videos = Video.objects.filter(userID=userID)
#             if(videos.exists()):
#                 videoDetails = []
#                 for video in videos:
#                     videoDetails.append({
#                         'videoID':video.id,
#                         'title' : video.title,
#                         'description' : video.description,
#                         'coverUrl' : video.coverUrl,
#                         'videoUrl' : video.videoUrl,
#                         'avatarUrl' : video.avatarUrl,
#                         'likeNum' : video.likeNum,
#                         'collectNum' : video.collectNum,
#                         'viewNum' :video.viewNum,
#                         'zone' : video.zone,
#                         'tag' : video.tag,
#                         'userID' : video.userID_id,
#                         'createdTime' : video.createdTime,
#                         'needAudit' : video.needAudit
#                     })
#                 return JsonResponse({'videos': videoDetails}, status=200,safe=False)
#             else:
#                 return JsonResponse({'message': '无相关视频'}, status=401)
#         except Exception as e:
#             return JsonResponse({'message': '未知错误'}, status=401)
#     else:
#         return JsonResponse({'message': '请求方法不允许'}, status=401)
def getVideo(request):
    if request.method == 'GET':
        #data = json.loads(request.body)
        #userId = data.get('id')
        userID= request.GET.get('id')
        try:
            videos = Video.objects.filter(userID=userID)
            if(videos.exists()):
                videoDetails = []
                for video in videos:
                    user = User.objects.get(id=video.userID_id)
                    username = user.username
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
                return JsonResponse({'videos': videoDetails}, status=200,safe=False)
            else:
                videoDetails = []
                return JsonResponse({'message': '无相关视频','videoList':videoDetails}, status=200)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)
@csrf_exempt
def follow(request):
    # try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #userid = data.get('userId')
            #followid = data.get('fanId')
            userID = request.POST.get('userID')
            followid = request.POST.get('fanId')
            try:
                user = User.objects.get(id=userID)
                user.followNum += 1
                user.save()
                follow = User.objects.get(id=followid)
                follow.fanNum += 1
                follow.save()
                following = Follow.objects.create(followingId_id= followid, followerId_id=userID)
                return JsonResponse({'message': '成功返回',}, status=200,safe=False)
            except User.DoesNotExist:
                return JsonResponse({'message': '用户不存在'}, status=401)
    # except Exception as e:
    #     return JsonResponse({'message': '未知错误'}, status=402)
@csrf_exempt
def disfollow(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #userid = data.get('userId')
            #followid = data.get('fanId')
            userID = request.POST.get('userID')
            followid = request.POST.get('fanId')
            try:
                user = User.objects.get(id=userID)
                user.followNum -= 1
                user.save()
                follow = User.objects.get(id=followid)
                follow.fanNum -= 1
                follow.save()
                Follow.objects.filter(followingId= followid, followerId=userID).delete()
                return JsonResponse({'message': '成功返回',}, status=200,safe=False)
            except User.DoesNotExist:
                return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=402)



@csrf_exempt
def getcomplain(request):
    if request.method == 'GET':
        #try:
            complaints = Complain.objects.values('description', 'userID', 'videoID')
            complaint_list = []
            for complaint in complaints:
                video_id = complaint['videoID']
                video = Video.objects.get(id=video_id)
                video_url = video.videoUrl
                video_title = video.title
                user_id = complaint['userID']
                user = User.objects.get(id = user_id)
                user_name = user.username
                complaint_data = {
                    'content': complaint['description'],
                    'username': user_name,
                    'title': video_title,
                    'videoUrl': video_url,
                    'videoID': video_id
                }
                complaint_list.append(complaint_data)


            return JsonResponse({'complaintList':complaint_list,'message':'成功返回'}, status=200, safe=False)
        #except:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def userprofile(request):
    try:
        if request.method == 'GET':
            #data = json.loads(request.body)
            #id = data.get('id')
            id = request.GET.get('id')
            try:
                user = User.objects.get(id=id)
                userData = {
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
                    'sign': user.sign
                }
                return JsonResponse({'message': '成功返回', 'userData': userData}, status=200, safe=False)
            except User.DoesNotExist:
                return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=402)