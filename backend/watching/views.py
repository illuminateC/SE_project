import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from information.models import Favorite, Message, Comment, Follow
from user.models import User
from video.models import Video
from watching.models import Like, Complain, LikeComment


# Create your views here.
@csrf_exempt
def like(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #id = data.get('id')
            #userID = data.get('userID')
            #videoID = data.get('videoID')
            id = request.POST.get('id')
            userID = request.POST.get('userID')
            videoID = request.POST.get('videoID')
            print(userID)
            try:
                like = Like.objects.get(userID_id=userID, videoID_id=videoID)
                return JsonResponse({'message': "已点赞"}, status=402)
            except Like.DoesNotExist:
                newLike = Like(id=id, userID_id=userID, videoID_id=videoID)
                newLike.save()
                likeNum_video = Video.objects.get(id=videoID).likeNum
                likeNum_user = User.objects.get(
                    id=Video.objects.get(id=videoID).userID_id).likeNum
                bl_video = Video.objects.filter(id=videoID).update(likeNum=likeNum_video + 1)
                bl_user = User.objects.filter(id=Video.objects.get(id=videoID).userID_id).update(likeNum=likeNum_user + 1)
                if bl_video == 1 and bl_user == 1:
                    return JsonResponse({'message': "点赞成功"}, status=200)
                else:
                    return JsonResponse({'message': "未知错误"}, status=401)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def save(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #id = data.get('id')
            #userID = data.get('userID')
            #videoID = data.get('videoID')
            id = request.POST.get('id')
            userID = request.POST.get('userID')
            videoID = request.POST.get('videoID')

            try:
                favorite = Favorite.objects.get(userID_id=userID, videoID_id=videoID)
                return JsonResponse({'message': "收藏已存在"}, status=402)
            except Favorite.DoesNotExist:
                newFavorite = Favorite(id=id, userID_id=userID, videoID_id=videoID)
                newFavorite.save()
                collectNum_video = Video.objects.get(id=videoID).collectNum
                collectNum_user = User.objects.get(
                    id=Video.objects.get(id=videoID).userID_id).collectNum
                bl_video = Video.objects.filter(id=videoID).update(
                    collectNum=collectNum_video + 1)
                bl_user = User.objects.filter(id=Video.objects.get(id=videoID).userID_id).update(
                    collectNum=collectNum_user + 1)
                if bl_video == 1 and bl_user == 1:
                    return JsonResponse({'message': "收藏成功"}, status=200)
                else:
                    return JsonResponse({'message': "未知错误"}, status=401)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def dislike(request):
    # try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #id = data.get('id')
            #userID = data.get('userID')
            #videoID = data.get('videoID')
            id = request.POST.get('id')
            userID = request.POST.get('userID')
            videoID = request.POST.get('videoID')

            try:
                like = Like.objects.get(userID_id=userID, videoID_id=videoID)
                likeNum_video = Video.objects.get(id=videoID).likeNum
                likeNum_user = User.objects.get(
                    id=Video.objects.get(id=videoID).userID_id).likeNum
                bl_video = Video.objects.filter(
                    id=videoID).update(likeNum=likeNum_video - 1)
                bl_user = User.objects.filter(id=Video.objects.get(
                    id=videoID).userID_id).update(likeNum=likeNum_user - 1)
                Like.objects.get(id=id).delete()
                if bl_video == 1 and bl_user == 1:
                    return JsonResponse({'message': "取消点赞成功"}, status=200)
                else:
                    return JsonResponse({'message': "未知错误"}, status=401)

            except Like.DoesNotExist:
                return JsonResponse({'message': "点赞不存在"}, status=402)
    # except Exception as e:
    #     return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def dissave(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #id = data.get('id')
            #userID = data.get('userID')
            #videoID = data.get('videoID')
            id = request.POST.get('id')
            userID = request.POST.get('userID')
            videoID = request.POST.get('videoID')
            try:
                favorite = Favorite.objects.get(userID_id=userID, videoID_id=videoID)
                collectNum_video = Video.objects.get(id=videoID).collectNum
                collectNum_user = User.objects.get(id=Video.objects.get(id=videoID).userID_id).collectNum
                bl_video = Video.objects.filter(id=videoID).update(collectNum=collectNum_video - 1)
                bl_user = User.objects.filter(id=Video.objects.get(id=videoID).userID_id).update(collectNum=collectNum_user - 1)
                Favorite.objects.get(id=id).delete()
                if bl_video == 1 and bl_user == 1:
                    return JsonResponse({'message': "取消收藏成功"}, status=200)
                else:
                    return JsonResponse({'message': "未知错误"}, status=401)
            except Favorite.DoesNotExist:
                return  JsonResponse({'message': "收藏不存在"}, status=402)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def likecomment(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #id = data.get('id')
            #userID = data.get('userID')
            id = request.POST.get('id')
            userID = request.POST.get('userID')

            try:
                likecomment = LikeComment.objects.get(userID_id=userID, commentID_id=id)
                return JsonResponse({'message': "已点赞"}, status=402)
            except LikeComment.DoesNotExist:
                newlike = LikeComment(userID_id=userID, commentID_id=id)
                newlike.save()
            try:
                comments = Comment.objects.filter(videoID_id=Comment.objects.get(id=id).videoID_id)
            except Comment.DoesNotExist:
                return JsonResponse({'message': "视频不存在"}, status=402)
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
                        'isOwn': str(comment.userID_id) == userID
                    })
            return JsonResponse({'message': "点赞成功", 'commentList': commentList}, status=200)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def dislikecomment(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #id = data.get('id')
            #userID = data.get('userID')
            id = request.POST.get('id')
            userID = request.POST.get('userID')

            try:
                LikeComment.objects.get(userID_id=userID, commentID_id=id).delete()
                comments = Comment.objects.filter(videoID_id=Comment.objects.get(id=id).videoID_id)
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
                            'isOwn': str(comment.userID_id) == userID
                        })

                return JsonResponse({'message': "取消点赞成功", 'commentList': commentList}, status=200)
            except LikeComment.DoesNotExist:
                return JsonResponse({'message': "未点赞"}, status=402)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)

@csrf_exempt
def deletecomment(request):
    if request.method == 'POST':
        try:
            #data = json.loads(request.body)
            #commentId = data.get('id')
            commentID = request.POST.get('id')
            userID = request.POST.get('userID')
            videoID = request.POST.get('videoID')
            comment = Comment.objects.get(id=commentID)
            comment.delete()
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
                        'isOwn': str(comment.userID_id) == userID
                    })
            return JsonResponse({'message': '评论删除成功', 'commentList': commentList}, status=200)
        except Comment.DoesNotExist:
            return JsonResponse({'message': '评论不存在'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def passvideo(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #videoID = data.get('videoID')
            videoID = request.POST.get('videoID')
            Video.objects.filter(id=videoID).update(needAudit=0)
            Complain.objects.filter(videoID_id=videoID).delete()
            return JsonResponse({'message': "通过成功"}, status=200)

    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def message(request):
    try:
        if request.method == 'POST':
            #data = json.loads(request.body)
            #title = data.get('title')
            #content = data.get('content')
            #createdTime = data.get('createdTime')
            #userID = data.get('userID')
            #fromName = data.get('fromName')
            title = request.POST.get('title')
            content = request.POST.get('content')
            createdTime = request.POST.get('createdTime')
            userID = request.POST.get('userID')
            fromName = request.POST.get('fromName')
            newMessage = Message(title=title, content=content,
                                 createdTime=createdTime, userID_id=userID, fromName=fromName)
            newMessage.save()
            return JsonResponse({'message': "发送成功"}, status=200)

    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)



@csrf_exempt
def complain(request):
     try:

        if request.method == 'POST':

            #data = json.loads(request.body)
            #id = data.get('id')
            #description = data.get('description')
            #userID = data.get('userID')
            #videoID = data.get('videoID')

            id = request.POST.get('id')
            description = request.POST.get('description')
            userID = request.POST.get('userID')
            videoID = request.POST.get('videoID')

            newComplain = Complain(id=id, description=description, userID_id=userID, videoID_id=videoID)
            newComplain.save()
            Video.objects.filter(id=videoID).update(needAudit=1)
            return JsonResponse({'message': "投诉成功"}, status=200)

     except Exception as e:
         return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def getvideo(request):
    try:
        if request.method == 'GET':
            #data = json.loads(request.body)
            #videoID = data.get('videoID')
            #userID = data.get('userID')
            videoID = request.GET.get('videoID')
            userID = request.GET.get('userID')

            video = Video.objects.get(id=videoID)
            user = User.objects.get(id=userID)

            video.viewNum = video.viewNum + 1
            video.save()
            # video.update(viewNum=video.viewNum+1)
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
                        'isOwn': str(comment.userID_id) == userID
                    })
            user_video = User.objects.get(id=Video.objects.get(id=videoID).userID_id)
            user_video_user = {
                'id': user_video.id,
                'username': user_video.username,
                'videoNum': user_video.videoNum,
                'likeNum': user_video.likeNum,
                'collectNum': user_video.collectNum,
                'fanNum': user_video.fanNum,
                'followNum': user_video.followNum,
                'avatarUrl': user_video.avatarUrl,
                'sign': user_video.sign,
                'isFollowed': Follow.objects.filter(followerId_id=userID, followingId_id=user_video.id).exists()
            }
            return JsonResponse(
                {
                    'message': "观看成功",
                    'avatarUrl': user.avatarUrl,
                    'collectNum': video.collectNum,
                    'description': video.description,
                    'videoID': videoID,
                    'needAudit': video.needAudit,
                    'likeNum': video.likeNum,
                    'title': video.title,
                    'userID': userID,
                    'videoUrl': video.videoUrl,
                    'zone': video.zone,
                    'isLiked': Like.objects.filter(userID=userID, videoID=videoID).exists(),
                    'isCollectted': Favorite.objects.filter(userID=userID, videoID=videoID).exists(),
                    'commentNum': Comment.objects.filter(videoID=videoID).count(),
                    'commentList': commentList,
                    'user': user_video_user,
                    'createdTime': video.createdTime,
                    'viewNum': video.viewNum,

                },
                status=200
            )

    except Exception as e:
        return JsonResponse({'message': "视频不存在"}, status=401)
